import json
import shutil
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile

from fasthtml.common import *
from loguru import logger

from whatsapp_analyzer import WhatsAppGroupAnalysis, chat_to_df

# Configure logger
logger.add("whatsapp_analyzer.log", rotation="1 MB")

# Initialize FastHTML app with debug mode
app, rt = fast_app(debug=True)

# Create temp directory if it doesn't exist
TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

# Maximum file size (10MB)
MAX_FILE_SIZE = 10 * 1024 * 1024

@rt("/")
def get():
    """Render the main page with file upload form."""
    return Container(
        H1("WhatsApp Chat Analyzer"),
        P("Upload your WhatsApp chat export file (.txt) to analyze inactive users and participation patterns."),
        Form(
            Div(
                Label("Upload WhatsApp Chat Export (txt file)"),
                Input(type="file", name="chat_file", accept=".txt", required=True),
                class_="form-group"
            ),
            Div(
                Label("Analysis Type"),
                Select(
                    Option("single", "Single Group Analysis"),
                    Option("multiple", "Multiple Groups Analysis"),
                    Option("score", "Score Inactive Users"),
                    name="analysis_type",
                    required=True
                ),
                class_="form-group"
            ),
            Div(
                Label("Window Days"),
                Input(
                    type="number",
                    name="window_days",
                    value="60",
                    min="1",
                    required=True
                ),
                class_="form-group"
            ),
            Div(
                Label("Exclude Contacts"),
                Input(
                    type="checkbox",
                    name="exclude_contacts",
                    value="true"
                ),
                class_="form-group"
            ),
            Div(
                Label("Decay Days (for scoring)"),
                Input(
                    type="number",
                    name="decay_days",
                    value="90",
                    min="1"
                ),
                class_="form-group"
            ),
            Div(
                Label("Reference Messages (for scoring)"),
                Input(
                    type="number",
                    name="reference_messages",
                    value="5",
                    min="1"
                ),
                class_="form-group"
            ),
            Button("Analyze Chat", type="submit", class_="button-primary"),
            action="/analyze",
            method="POST",
            enctype="multipart/form-data"
        ),
        class_="container"
    )

def create_table_rows(results):
    """Create table rows from results DataFrame."""
    # Create header row
    header_row = Tr(*[Th(col) for col in results.columns])
    
    # Create data rows
    data_rows = []
    for _, row in results.iterrows():
        data_rows.append(
            Tr(*[Td(str(cell)) for cell in row])
        )
    
    return header_row, data_rows

@rt("/analyze", methods=["POST"])
async def analyze(req):
    """Handle file upload and analysis."""
    try:
        form = await req.form()
        
        # Get form data
        chat_file = form.get("chat_file")
        if not chat_file:
            return error_response("No file uploaded")
        
        # Validate file size
        file_size = 0
        temp_file = NamedTemporaryFile(delete=False, dir=TEMP_DIR, suffix=".txt")
        
        try:
            # Save uploaded file
            with open(temp_file.name, "wb") as f:
                while chunk := await chat_file.read(8192):
                    file_size += len(chunk)
                    if file_size > MAX_FILE_SIZE:
                        return error_response("File too large (max 10MB)")
                    f.write(chunk)
            
            # Get analysis parameters
            analysis_type = form.get("analysis_type", "single")
            window_days = int(form.get("window_days", 60))
            exclude_contacts = form.get("exclude_contacts") == "true"
            decay_days = int(form.get("decay_days", 90))
            reference_messages = int(form.get("reference_messages", 5))
            
            # Process the chat file
            df = chat_to_df(temp_file.name)
            analysis = WhatsAppGroupAnalysis(df)
            
            # Get results based on analysis type
            if analysis_type == "score":
                inactive_users = analysis.get_inactive_users(exclude_contacts=exclude_contacts)
                results = analysis.calculate_activity_score(
                    inactive_users,
                    decay_days=decay_days,
                    reference_messages=reference_messages
                )
            else:
                results = analysis.get_inactive_users(exclude_contacts=exclude_contacts)
            
            # Save results to a temporary CSV file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_filename = f"whatsapp_analysis_{timestamp}.csv"
            csv_path = TEMP_DIR / csv_filename
            results.to_csv(csv_path, index=False)
            
            # Create table using FastHTML components
            header_row, data_rows = create_table_rows(results)
            
            return Container(
                H2("Analysis Results"),
                P(f"Found {len(results)} users to analyze."),
                Div(
                    A(
                        "⬇️ Download CSV",
                        href=f"/download/{csv_filename}",
                        class_="button-secondary"
                    ),
                    A(
                        "⬅️ Back to Upload",
                        href="/",
                        class_="button-secondary"
                    ),
                    class_="button-group"
                ),
                Div(
                    Table(
                        Thead(header_row),
                        Tbody(*data_rows),
                        class_="table"
                    ),
                    class_="table-container"
                ),
                class_="container"
            )
            
        finally:
            # Clean up temporary file
            Path(temp_file.name).unlink(missing_ok=True)
            
    except Exception as e:
        logger.exception("Error processing file")
        return error_response(f"Error processing file: {str(e)}")

@rt("/download/{filename}")
async def download(filename: str):
    """Handle CSV file download."""
    try:
        file_path = TEMP_DIR / filename
        if not file_path.exists():
            return error_response("File not found")
        
        with open(file_path, "r") as f:
            content = f.read()
            
        # Clean up the file after reading
        file_path.unlink()
        
        return Response(
            content,
            headers={
                "Content-Type": "text/csv",
                "Content-Disposition": f"attachment; filename={filename}"
            }
        )
    except Exception as e:
        logger.exception("Error downloading file")
        return error_response(f"Error downloading file: {str(e)}")

def error_response(message: str):
    """Return an error page."""
    return Container(
        H2("Error"),
        P(message, class_="error"),
        A("⬅️ Back to Upload", href="/"),
        class_="container"
    )

# Add some basic CSS styling
app.css = """
.container { 
    max-width: 1200px; 
    margin: 0 auto; 
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.form-group { 
    margin-bottom: 1.5rem; 
}
.form-group label { 
    display: block; 
    margin-bottom: 0.5rem;
    font-weight: 600;
}
.form-group input[type="file"],
.form-group input[type="number"],
.form-group select { 
    display: block;
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #fff;
}
.form-group input[type="checkbox"] {
    margin-top: 0.5rem;
}
.error { 
    color: #dc3545;
    padding: 1rem;
    border: 1px solid #dc3545;
    border-radius: 4px;
    margin-bottom: 1rem;
}
.table-container {
    overflow-x: auto;
    margin: 1rem 0;
    border: 1px solid #dee2e6;
    border-radius: 4px;
}
.table { 
    width: 100%; 
    border-collapse: collapse; 
    margin: 0;
    background-color: #fff;
}
.table th, .table td { 
    padding: 0.75rem; 
    border: 1px solid #dee2e6;
    text-align: left;
    font-size: 0.9rem;
}
.table th { 
    background: #f8f9fa;
    font-weight: 600;
    position: sticky;
    top: 0;
    z-index: 1;
    white-space: nowrap;
}
.table td {
    white-space: nowrap;
}
.table tbody tr:nth-child(even) {
    background-color: #f8f9fa;
}
.table tbody tr:hover {
    background-color: #f2f2f2;
}
.button-primary { 
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
.button-secondary {
    display: inline-block;
    padding: 0.5rem 1rem;
    margin: 0.5rem;
    background-color: #6c757d;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    cursor: pointer;
}
.button-primary:hover,
.button-secondary:hover {
    background-color: #0056b3;
    text-decoration: none;
    color: white;
}
.button-group {
    margin: 1rem 0;
    display: flex;
    gap: 1rem;
}
body {
    background-color: #f8f9fa;
    padding: 2rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
"""

if __name__ == "__main__":
    serve() 