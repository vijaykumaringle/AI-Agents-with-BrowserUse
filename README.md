# AI Agents with BrowserUse

A sophisticated AI-powered agent system that analyzes AI trends in India using Google's Gemini AI model and browser automation.

## Features

- Multi-agent system for comprehensive analysis
- Automated news gathering and analysis
- Industry impact assessment
- HTML and JSON report generation
- Modern, responsive UI for results
- Error handling and logging

## Agent Architecture

The system consists of four specialized agents:

1. **News Agent**
   - Task: Gather latest AI news from reliable sources
   - Focus: Major news websites and tech publications
   - Extracts: Article titles, dates, and key points

2. **Analysis Agent**
   - Task: Analyze news content for trends and insights
   - Identifies: Common themes and emerging technologies
   - Provides: Structured analysis with supporting evidence

3. **Industry Impact Agent**
   - Task: Analyze AI's impact on Indian industries
   - Focus: Key sectors like manufacturing, healthcare, finance
   - Identifies: Opportunities and challenges

4. **Summarization Agent**
   - Task: Create concise summaries
   - Constraints: 500-word limit
   - Includes: Actionable insights for stakeholders

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Google Cloud credentials:
   - Create a Google Cloud Project
   - Enable Generative AI API
   - Create service account credentials
   - Set GOOGLE_APPLICATION_CREDENTIALS environment variable

3. Run the script:
```bash
python Dev1-Browseruse/agent.py
```

## Output

The script generates:
- HTML report in `news/` directory (e.g., `ai_analysis_YYYY-MM-DD_HH-MM-SS.html`)
- JSON data file in `news/` directory (e.g., `ai_analysis_YYYY-MM-DD_HH-MM-SS.json`)
- Terminal output with detailed analysis

## Requirements

- Python 3.13+
- Google Cloud Project with Generative AI API enabled
- Valid Google Cloud credentials
- Browser automation capabilities

## Error Handling

The system includes:
- Custom exception classes for different error types
- Robust logging
- Graceful error recovery
- Resource cleanup

## License

MIT License
