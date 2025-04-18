# WhatsApp Analyzer

A tool for analyzing WhatsApp group chat exports. It supports both single group and multiple group analysis, with features for identifying inactive users and analyzing message patterns.

## Features

- Parse WhatsApp chat exports into structured data
- Analyze single or multiple group chats
- Identify inactive users based on configurable criteria
- Track user joining dates and message counts
- Support for excluding contacts (users with names starting with '~')
- Comprehensive logging and progress tracking
- Activity scoring with exponential decay to identify formerly active members

## Installation

1. Install `uv` if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository and install dependencies:
```bash
git clone <repository-url>
cd whatsapp-analyzer
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
uv pip install -e .
```

## Usage

### Single Group Analysis

```bash
python whatsapp_analyzer.py analyze-single path/to/chat.txt --output results.csv
```

Options:
- `--output`, `-o`: Save results to a CSV file
- `--window-days`, `-w`: Number of days to consider for inactivity (default: 60)
- `--exclude-contacts`: Exclude contacts (users with names starting with '~')

### Multiple Group Analysis

```bash
python whatsapp_analyzer.py analyze-multiple path/to/groups/ --output combined_results.csv
```

The script will process all `.txt` files in the specified directory as WhatsApp chat exports.

### Activity Scoring for Inactive Users

```bash
python whatsapp_analyzer.py score-inactive path/to/chat.txt --output scored_users.csv
```

This command calculates an exponential decay activity score for inactive users, helping you identify formerly active members who might be worth re-activating.

Options:
- `--output`, `-o`: Save results to a CSV file
- `--window-days`, `-w`: Number of days to consider for inactivity (default: 60)
- `--exclude-contacts`: Exclude contacts (users with names starting with '~')
- `--decay-days`, `-d`: Number of days for score to decay to zero (default: 90)
- `--reference-messages`, `-r`: Number of messages that would give a score of 1.0 (default: 5)

The output CSV includes all the standard columns plus:
- `Days_Since_Last_Message`: Number of days since the user's last message
- `Base_Score`: Raw score based on total messages sent
- `Activity_Score`: Final score with exponential decay applied

The results are sorted by `Activity_Score` in ascending order (lowest to highest), so the least promising users to re-activate appear at the top of the list.

## Development

- Format code: `ruff format .`
- Lint code: `ruff check .`
- Fix linting issues: `ruff check . --fix`

## TODO

- [ ] Add support for more WhatsApp export formats
- [ ] Implement message content analysis
- [ ] Add visualization capabilities
- [ ] Add export to different formats (JSON, Excel)
- [ ] Add support for message reactions analysis
- [ ] Implement user activity patterns
- [ ] Add support for media message analysis