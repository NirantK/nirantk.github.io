import os
from typing import Any, Optional

from dotenv import load_dotenv
from linkup import LinkupClient
from loguru import logger

load_dotenv()

api_key: Optional[str] = os.getenv("LINKUP_API_KEY")
if not api_key:
    logger.error("LINKUP_API_KEY environment variable is not set")
    raise ValueError("LINKUP_API_KEY environment variable is not set")

client = LinkupClient(api_key=api_key)

company_names = [
    "Airbnb",
    "Uber",
    "Pinterest",
    "Netflix",
    "Spotify",
    "Youtube",
    # "Linkedin",
    "Stripe",
    "Doordash",
    "Shopify",
    # "Reddit",
    "Tiktok",
    "Bytedance",
    "Glean",
    "Ramp",
    "Retool",
]

for company_name in company_names:
    try:
        response: Any = client.search(
            query=f"What has {company_name} Engineering written about LLMs and Foundation Models?",
            depth="standard",
            output_type="searchResults",
            include_images=False,
        )
        logger.info(f"Successfully retrieved search results for {company_name}")
        with open(f"{company_name}-llm-research.md", "w") as f:
            for result in response.results:
                f.write(f"## {result.name}\n\n")
                f.write(f"Source: {result.url}\n\n") 
                f.write(f"{result.content}\n\n")
                f.write("---\n\n")
    except Exception as e:
        logger.exception(f"Error during API search: {str(e)}")
