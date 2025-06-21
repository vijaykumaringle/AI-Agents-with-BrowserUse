# Dev1-Browseruse - AI Agents Implementation

This directory contains the implementation of the AI Agents system that analyzes AI trends in India using Google's Gemini AI model and browser automation.

## File Structure

- `agent.py`: Main implementation file containing the agent system
- `news/`: Directory for generated analysis reports
  - HTML files: Formatted analysis reports
  - JSON files: Raw data for each analysis

## Implementation Details

### Core Components

1. **Agent Creation Functions**
   ```python
   async def create_news_agent(llm):
       """Create an agent specialized in finding news articles"""
       return Agent(
           task="Find the latest news articles about AI in India from reliable sources...",
           llm=llm
       )
   ```

2. **Error Handling**
   - Custom exception classes for different error types
   - Robust error logging
   - Graceful error recovery

3. **Output Generation**
   - HTML file generation with modern styling
   - JSON data structure for analysis results
   - Timestamp-based file naming

### Configuration

```python
# Configuration constants
NEWS_DIR = "news"
OUTPUT_FILE_PREFIX = "ai_analysis_"
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds
```

### Key Features

1. **Error Handling**
   - Browser errors
   - File operation errors
   - Analysis errors
   - Unexpected errors

2. **Logging**
   - Configured with INFO level
   - Detailed logging for each step
   - Error tracking and debugging

3. **File Management**
   - Automatic directory creation
   - Timestamp-based file naming
   - Proper error handling for file operations

### Running the Code

1. **Prerequisites**
   - Python 3.13+
   - Google Cloud credentials
   - Browser automation capabilities
   - Required Python packages (install using `pip install -r requirements.txt`)

2. **Environment Setup**
   ```bash
   # Set Google Cloud credentials
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
   
   # Create virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Basic Execution**
   ```bash
   # Run from parent directory
   python Dev1-Browseruse/agent.py
   ```

4. **Advanced Execution Options**
   - Run with debug logging:
     ```bash
     export LOG_LEVEL=DEBUG
     python Dev1-Browseruse/agent.py
     ```
   
   - Run with custom output directory:
     ```bash
     export OUTPUT_DIR=/custom/path
     python Dev1-Browseruse/agent.py
     ```

### Output Format

The script generates multiple output files with a timestamp-based naming convention:

1. **HTML Report**
   - **File Name**: `ai_analysis_YYYY-MM-DD_HH-MM-SS.html`
   - **Location**: `news/` directory
   - **Structure**:
     ```html
     <div class="header">
         <h1>AI in India - Comprehensive Analysis</h1>
         <p class="timestamp">Generated on: YYYY-MM-DD HH:MM:SS</p>
     </div>
     
     <div class="section">
         <h2>Latest News</h2>
         <div class="analysis">News content here</div>
     </div>
     
     <div class="section">
         <h2>Key Analysis</h2>
         <div class="analysis">Analysis content here</div>
     </div>
     
     <div class="section">
         <h2>Industry Impact</h2>
         <div class="analysis">Impact analysis here</div>
     </div>
     
     <div class="section">
         <h2>Summary</h2>
         <div class="analysis">Summary content here</div>
     </div>
     ```
   - **Features**:
     - Responsive layout for all devices
     - Clean typography and spacing
     - Clear section separation
     - Footer with generation information

2. **JSON Data**
   - **File Name**: `ai_analysis_YYYY-MM-DD_HH-MM-SS.json`
   - **Location**: `news/` directory
   - **Structure**:
     ```json
     {
         "news": "Latest news content",
         "analysis": "Detailed analysis",
         "impact": "Industry impact analysis",
         "summary": "Concise summary",
         "timestamp": "YYYY-MM-DD HH:MM:SS"
     }
     ```
   - **Usage**:
     - Data source for visualization tools
     - Input for further analysis
     - Backup of analysis results

3. **Terminal Output**
   - Progress indicators with emojis
   - Detailed step-by-step logs
   - Final results displayed in terminal
   - Error messages with context

### Output Directory Structure
```
news/
├── ai_analysis_YYYY-MM-DD_HH-MM-SS.html
├── ai_analysis_YYYY-MM-DD_HH-MM-SS.json
├── ai_analysis_YYYY-MM-DD_HH-MM-SS.html
├── ai_analysis_YYYY-MM-DD_HH-MM-SS.json
└── ...
```

### Output File Naming Convention
- **Pattern**: `ai_analysis_YYYY-MM-DD_HH-MM-SS`
- **Components**:
  - `YYYY-MM-DD`: Date of analysis
  - `HH-MM-SS`: Time of analysis
  - `ai_analysis`: Fixed prefix
- **Example**: `ai_analysis_2025-06-21_23-40-47.html`

### Error Handling Flow

```python
try:
    # Initialize model and create agents
    # Execute analysis steps
    # Generate output files
except BrowserError as e:
    logger.error(f"Browser error occurred: {e}")
except FileError as e:
    logger.error(f"File operation error: {e}")
except AnalysisError as e:
    logger.error(f"Analysis error occurred: {e}")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
```

### Best Practices

1. Always check for directory existence before writing files
2. Use proper error handling for all operations
3. Maintain consistent logging
4. Keep code modular and maintainable
5. Use async/await for non-blocking operations

## Troubleshooting

1. **Browser Errors**
   - Check if browser is properly installed
   - Verify network connectivity
   - Check for browser process timeouts

2. **File Errors**
   - Verify write permissions
   - Check disk space
   - Ensure proper directory structure

3. **Analysis Errors**
   - Validate input data
   - Check for API rate limits
   - Verify model responses
