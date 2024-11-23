import datetime
from pathlib import Path

import yaml


def convert_front_matter(content: str) -> str:
    """Convert old front matter format to new format."""
    # Split content into front matter and body
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return content
    
    # Parse the existing front matter
    try:
        front_matter = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return content
    
    # Create new front matter
    new_front_matter = {}
    
    # Convert date
    if 'date' in front_matter:
        # Handle string dates with timezone
        if isinstance(front_matter['date'], str):
            try:
                date_obj = datetime.datetime.strptime(
                    front_matter['date'].split('+')[0].strip(), 
                    '%Y-%m-%d %H:%M:%S'
                )
                new_front_matter['date'] = date_obj.date().isoformat()
            except ValueError:
                new_front_matter['date'] = front_matter['date']
    
    # Convert authors from contributors
    if 'contributors' in front_matter:
        new_front_matter['authors'] = []
        for contributor in front_matter['contributors']:
            # Convert 'Nirant Kasliwal' to 'nirant'
            if contributor.lower().startswith('nirant'):
                new_front_matter['authors'].append('nirant')
            else:
                # Convert other names to lowercase, remove spaces
                author_id = contributor.lower().replace(' ', '')
                new_front_matter['authors'].append(author_id)
    
    # Copy over tags as categories
    if 'tags' in front_matter:
        new_front_matter['categories'] = front_matter['tags']
    
    # Copy title
    if 'title' in front_matter:
        new_front_matter['title'] = front_matter['title']
    
    # Generate new front matter YAML
    new_front_matter_str = yaml.dump(new_front_matter, allow_unicode=True, sort_keys=False)
    
    # Combine everything back
    return f"---\n{new_front_matter_str}---\n{parts[2]}"

def process_file(file_path: Path) -> None:
    """Process a single markdown file."""
    content = file_path.read_text(encoding='utf-8')
    new_content = convert_front_matter(content)
    file_path.write_text(new_content, encoding='utf-8')

def main():
    # Process all markdown files in the writing directory
    docs_dir = Path('docs/writing')
    for md_file in docs_dir.glob('**/*.md'):
        if md_file.is_file() and 'posts' not in md_file.parts:
            print(f"Processing {md_file}")
            process_file(md_file)
if __name__ == "__main__":
    main()
