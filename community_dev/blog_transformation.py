from pathlib import Path
from typing import Any, Dict

import click
import toml
import yaml
from loguru import logger
from tqdm import tqdm


def convert_frontmatter(input_str: str) -> str:
    """Convert TOML frontmatter to YAML frontmatter with additional fields.
    
    Args:
        input_str: The TOML frontmatter string
        
    Returns:
        str: The converted YAML frontmatter string
    """
    # Remove the +++ from the start and end
    trimmed_str = input_str.strip().strip("+++").strip()

    # Parse the TOML frontmatter
    parsed_toml: Dict[str, Any] = toml.loads(trimmed_str)

    # Add additional fields
    parsed_toml["excerpt"] = parsed_toml.get("description", "")
    parsed_toml["date"] = str(parsed_toml.get("date", "2021-04-27T00:00:00+00:00"))
    parsed_toml["lastmod"] = parsed_toml["date"]
    parsed_toml["images"] = []
    parsed_toml["draft"] = False
    parsed_toml["contributors"] = ["Nirant Kasliwal"]
    parsed_toml["weight"] = 50

    # Convert to YAML frontmatter
    yaml_frontmatter = yaml.safe_dump(parsed_toml, default_flow_style=False)

    # Add the --- at the start and end
    return "---\n" + yaml_frontmatter + "---"


@click.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, dir_okay=True))
def process_directory(directory: str) -> None:
    """Process all markdown files in the given directory to convert their frontmatter.
    
    Args:
        directory: Path to the directory containing markdown files
    """
    logger.info(f"Processing markdown files in {directory}")
    
    # Get a list of all markdown files in the directory
    markdown_files = list(Path(directory).glob("*.md"))
    logger.info(f"Found {len(markdown_files)} markdown files")

    # Process each markdown file
    for markdown_file in tqdm(markdown_files, desc="Converting frontmatter"):
        try:
            contents = markdown_file.read_text()

            # Find the frontmatter section
            start_index = contents.find("+++")
            end_index = contents.find("+++", start_index + 1)

            if start_index == -1 or end_index == -1:
                logger.warning(f"No frontmatter found in {markdown_file}")
                continue

            # Extract and convert the frontmatter
            frontmatter = contents[start_index : end_index + 3]
            new_frontmatter = convert_frontmatter(frontmatter)

            # Replace the frontmatter in the file contents
            new_contents = contents.replace(frontmatter, new_frontmatter)

            # Write the new contents back to the file
            markdown_file.write_text(new_contents)
            logger.debug(f"Successfully processed {markdown_file}")
            
        except Exception as e:
            logger.error(f"Error processing {markdown_file}: {str(e)}")


if __name__ == "__main__":
    logger.add("blog_transformation.log", rotation="1 day")
    process_directory()
