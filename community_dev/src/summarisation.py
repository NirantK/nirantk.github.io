import datetime
import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import fire
import pandas as pd
import pytz
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from loguru import logger
from tqdm import tqdm

from formatting_utils import human_date
from prompts import PROMPT_TEMPLATES

text_splitter = CharacterTextSplitter.from_tiktoken_encoder()


def make_docs(plain_text: str) -> List[Document]:
    """Split text into documents for summarization.

    Args:
        plain_text: Text to split into documents

    Returns:
        List of Document objects
    """
    texts = text_splitter.split_text(plain_text)
    docs = [Document(page_content=t) for t in texts]
    return docs


@lru_cache
def summarize_docs(
    docs: List[Document],
    prompt_template: str,
    model: Any,
    chain_type: str = "stuff",
) -> str:
    """Summarize a list of documents using a language model.

    Args:
        docs: List of Document objects to summarize
        prompt_template: Template for the summarization prompt
        model: Language model to use for summarization
        chain_type: Type of summarization chain to use, defaults to "stuff"

    Returns:
        Summarized text
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

    # We should abstract chain logic when more chain type experiments are added
    if chain_type == "map_reduce":
        chain = load_summarize_chain(
            model, chain_type=chain_type, map_prompt=prompt, combine_prompt=prompt
        )
    else:
        chain = load_summarize_chain(model, chain_type=chain_type, prompt=prompt)
    chain_output = chain({"input_documents": docs}, return_only_outputs=True)
    return chain_output["output_text"]


def summarize(message: str, prompt_template: str, chain_type: str = "stuff") -> str:
    """Summarize a message using a language model.

    Args:
        message: Text to summarize
        prompt_template: Template for the summarization prompt
        chain_type: Type of summarization chain to use, defaults to "stuff"

    Returns:
        Summarized text
    """
    docs = make_docs(message)
    summary_text = summarize_docs(
        docs,
        prompt_template,
        chain_type="stuff",
        model=ChatOpenAI(temperature=0),
    )
    return summary_text


def extract_urls_context(text: str, window_size: int = 1) -> List[str]:
    """Extract URLs and their context from text.

    Args:
        text: Text to extract URLs from
        window_size: Number of lines of context to include before and after the URL, defaults to 1

    Returns:
        List of strings containing URLs and their context
    """
    lines = text.split("\n")
    url_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )
    urls_context = []

    for idx, line in enumerate(lines):
        for match in url_pattern.finditer(line):
            start, end = match.span()
            prev_line = lines[idx - window_size] if idx > 0 else ""
            next_line = lines[idx + window_size] if idx < len(lines) - 1 else ""
            context = f"{prev_line}\n{line}\n{next_line}".strip()
            # Dropping match.group() from append as we are not using it
            urls_context.append(context)
    return urls_context


def get_page_header_date(date_object: datetime.date) -> str:
    """Format a date object for use in a page header.

    Args:
        date_object: Date to format

    Returns:
        Formatted date string with timezone information
    """
    # Combine the date object with a time object and set the desired timezone
    dt = datetime.datetime.combine(date_object, datetime.time())
    desired_timezone = pytz.timezone("Asia/Kolkata")
    localized_dt = desired_timezone.localize(dt)

    # Format the datetime object using strftime
    formatted_datetime = localized_dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    formatted_datetime = formatted_datetime[:-2] + ":" + formatted_datetime[-2:]

    return formatted_datetime


def make_page_header(row: pd.Series) -> str:
    """Create a page header from a DataFrame row.

    Args:
        row: DataFrame row containing date and title/description information

    Returns:
        Formatted page header
    """
    date, summary_text = row["Date"], row["title_desc"]
    dt = get_page_header_date(date)
    fields = json.loads(summary_text)  # This is expensive!
    summary_title, summary_description = fields["title"], fields["description"]

    page_header = f"""+++
                    title =  "{summary_title}"
                    date = {dt}
                    tags = ["daily_summary"]
                    featured_image = ""
                    description = "{summary_description}"
                    toc = true
                    +++
                    """
    return page_header


def make_page(row: pd.Series) -> tuple[str, str]:
    """Create a complete page from a DataFrame row.

    Args:
        row: DataFrame row containing page content

    Returns:
        Tuple of (page content, file name)
    """
    page = (
        row["page_headers"]
        + "\n"
        + row["Summary"]
        + "\n"
        + "\n## Links\nThe description and link can be mismatched because of extraction errors.\n\n"
        + row["EndNote"]
    )
    file_name = f"{human_date(row['Date'])}.md"
    return page, file_name


def generate_daily_df(csv_path: Union[str, Path]) -> pd.DataFrame:
    """Generate a DataFrame with daily message data.

    Args:
        csv_path: Path to the CSV file containing message data

    Returns:
        DataFrame with daily message data
    """
    df = pd.read_csv(csv_path)
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df["Date"] = df["Datetime"].dt.date
    daily_df = df.groupby("Date").agg({"Message": " \n ".join}).reset_index()
    daily_df["wc"] = daily_df["Message"].apply(lambda x: len(x.split()))
    return daily_df


def generate_daily_summary(csv_path: Union[str, Path]) -> None:
    """Generate daily summaries from a CSV file containing message data.

    Args:
        csv_path: Path to the CSV file containing message data
    """
    readpath = Path(csv_path).resolve()
    assert readpath.exists(), f"CSV file does not exist: {readpath}"
    write_dir = Path("../../content/ai/").resolve()
    
    logger.info(f"Processing CSV file: {readpath}")
    daily_df = generate_daily_df(readpath)
    
    # Generating the summary column
    logger.info("Generating summaries")
    daily_df["Summary"] = daily_df["Message"].apply(
        summarize, args=(PROMPT_TEMPLATES["summary_template"],)
    )

    # Generating the EndNote column
    logger.info("Extracting URLs and context")
    daily_df["Endnote"] = (
        daily_df["Message"]
        .apply(extract_urls_context)
        .apply(
            lambda urls_context: "\n".join(
                [
                    summarize(message, PROMPT_TEMPLATES["link_context_template"])
                    for message in urls_context
                ]
            )
        )
    )

    # Generating Title and Description Columns that can be passed to header method
    logger.info("Generating titles and descriptions")
    # We are avoiding the for loop with this intermediate column
    daily_df["title_desc"] = daily_df["Summary"].apply(
        summarize,
        args=(
            PROMPT_TEMPLATES["title_description_template"],
            "map_reduce",
        ),
    )
    
    # Generating page headers
    logger.info("Generating page headers")
    page_headers = []
    for idx in tqdm(range(len(daily_df)), desc="Creating page headers"):
        page_headers.append(make_page_header(daily_df.iloc[idx]))

    # Dumping all the updates
    daily_df["page_headers"] = page_headers
    backup_path = Path("daily_backup.json")
    daily_df.to_json(backup_path)  # This is always in the current directory
    logger.info(f"Saved backup to {backup_path}")

    # Using page headers to make pages
    logger.info("Writing pages to files")
    for idx in tqdm(range(len(daily_df)), desc="Writing pages"):
        page, file_name = make_page(daily_df.iloc[idx])
        file_path = write_dir / file_name
        with file_path.open("w") as f:
            f.write(page)
    
    logger.info(f"Completed processing. Files written to {write_dir}")


if __name__ == "__main__":
    fire.Fire(generate_daily_summary)
