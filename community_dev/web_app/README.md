# WhatsApp Chat Analyzer Web App

A web application for analyzing WhatsApp chat exports to identify inactive users and participation patterns.

## Features

- Upload WhatsApp chat export files (.txt)
- Multiple analysis types:
  - Single Group Analysis
  - Multiple Groups Analysis
  - Score Inactive Users
- Configurable parameters:
  - Window days for inactivity
  - Exclude/Include contacts
  - Decay days for scoring
  - Reference messages for scoring
- Results displayed in a clean table format
- Secure file handling with automatic cleanup

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Open your browser and navigate to:
```
http://localhost:5001
```

## Usage

1. Export your WhatsApp chat:
   - Open WhatsApp group
   - Click group info
   - Scroll down and click "Export chat"
   - Choose "Without Media"
   - Save the .txt file

2. Upload and Analyze:
   - Visit the web app
   - Upload the exported .txt file
   - Choose analysis type
   - Configure analysis parameters
   - Click "Analyze Chat"

3. View Results:
   - Results will be displayed in a table
   - Use browser's save functionality to save as HTML if needed

## Security Notes

- Maximum file size: 10MB
- Files are processed in a temporary directory
- Automatic file cleanup after processing
- Input validation and sanitization

## Development

See [TODO.md](TODO.md) for development roadmap and planned features.

## License

MIT License 