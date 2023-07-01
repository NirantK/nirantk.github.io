import click
import toml
import yaml
import glob
import os

def convert_frontmatter(input_str):
    # Remove the +++ from the start and end
    trimmed_str = input_str.strip().strip('+++').strip()

    # Parse the TOML frontmatter
    parsed_toml = toml.loads(trimmed_str)

    # Add additional fields
    parsed_toml['excerpt'] = parsed_toml.get('description', '')
    parsed_toml['date'] = str(parsed_toml.get('date', '2021-04-27T00:00:00+00:00'))
    parsed_toml['lastmod'] = parsed_toml['date']
    parsed_toml['images'] = []
    parsed_toml['draft'] = False
    parsed_toml['contributors'] = ["Nirant Kasliwal"]
    parsed_toml['weight'] = 50

    # Convert to YAML frontmatter
    yaml_frontmatter = yaml.safe_dump(parsed_toml, default_flow_style=False)

    # Add the --- at the start and end
    return '---\n' + yaml_frontmatter + '---'

@click.command()
@click.argument('directory')
def process_directory(directory):
    # Get a list of all markdown files in the directory
    markdown_files = glob.glob(os.path.join(directory, '*.md'))

    # Process each markdown file
    for markdown_file in markdown_files:
        with open(markdown_file, 'r+') as file:
            contents = file.read()

            # Find the frontmatter section
            start_index = contents.find('+++')
            end_index = contents.find('+++', start_index + 1)

            if start_index == -1 or end_index == -1:
                continue

            # Extract and convert the frontmatter
            frontmatter = contents[start_index:end_index + 3]
            new_frontmatter = convert_frontmatter(frontmatter)

            # Replace the frontmatter in the file contents
            new_contents = contents.replace(frontmatter, new_frontmatter)

            # Write the new contents back to the file
            file.seek(0)
            file.write(new_contents)
            file.truncate()

if __name__ == '__main__':
    process_directory()
