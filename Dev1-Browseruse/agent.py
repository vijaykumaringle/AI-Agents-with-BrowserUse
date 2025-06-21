import asyncio
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import logging
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
NEWS_DIR = "news"
OUTPUT_FILE_PREFIX = "ai_analysis_"
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Error handling classes
class BrowserError(Exception):
    """Custom exception for browser-related errors"""
    pass

class FileError(Exception):
    """Custom exception for file operation errors"""
    pass

class AnalysisError(Exception):
    """Custom exception for analysis errors"""
    pass

async def create_news_agent(llm):
    """Create an agent specialized in finding news articles"""
    return Agent(
        task="Find the latest news articles about AI in India from reliable sources.",
        llm=llm
    )

async def create_analysis_agent(llm):
    """Create an agent specialized in analyzing news content"""
    return Agent(
        task="Analyze the news articles and extract key insights and trends about AI in India.",
        llm=llm
    )

async def create_summarization_agent(llm):
    """Create an agent specialized in summarizing information"""
    return Agent(
        task="Create a concise and engaging summary of the AI trends in India, highlighting key points and implications.",
        llm=llm
    )

async def create_industry_impact_agent(llm):
    """Create an agent specialized in analyzing industry impact"""
    return Agent(
        task="Analyze the impact of AI developments on different industries in India and identify key sectors being transformed.",
        llm=llm
    )

async def create_news_agent(llm):
    """Create an agent specialized in finding news articles"""
    return Agent(
        task="Find the latest news articles about AI in India from reliable sources. Focus on major news websites and tech publications. Extract key information including article titles, dates, and main points.",
        llm=llm
    )

async def create_analysis_agent(llm):
    """Create an agent specialized in analyzing news content"""
    return Agent(
        task="Analyze the news articles and extract key insights and trends about AI in India. Identify common themes, emerging technologies, and industry impacts. Provide a structured analysis with supporting evidence from the articles.",
        llm=llm
    )

async def create_summarization_agent(llm):
    """Create an agent specialized in summarizing information"""
    return Agent(
        task="Create a concise and engaging summary of the AI trends in India, highlighting key points and implications. The summary should be no more than 500 words and should include actionable insights for stakeholders.",
        llm=llm
    )

async def create_industry_impact_agent(llm):
    """Create an agent specialized in analyzing industry impact"""
    return Agent(
        task="Analyze the impact of AI developments on different industries in India and identify key sectors being transformed. Provide specific examples and potential opportunities for growth.",
        llm=llm
    )

async def main():
    try:
        # Load credentials from environment variable
        load_dotenv()
        
        # Initialize the model with credentials
        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-exp'
        )
        
        # Create news directory with proper error handling
        news_dir = Path(NEWS_DIR)
        try:
            news_dir.mkdir(exist_ok=True)
        except OSError as e:
            raise FileError(f"Failed to create news directory: {e}")
        
        # Create specialized agents
        news_agent = await create_news_agent(llm)
        analysis_agent = await create_analysis_agent(llm)
        summarization_agent = await create_summarization_agent(llm)
        industry_impact_agent = await create_industry_impact_agent(llm)
        
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logger.info(f"Starting AI analysis at {timestamp}")
        
        # Step 1: Gather news
        logger.info("Gathering latest AI news in India...")
        news_result = await news_agent.run()
        logger.info("News collection complete")
        
        # Step 2: Analyze news
        logger.info("Analyzing news content...")
        analysis_result = await analysis_agent.run()
        logger.info("Analysis complete")
        
        # Step 3: Analyze industry impact
        logger.info("Analyzing industry impact...")
        impact_result = await industry_impact_agent.run()
        logger.info("Industry impact analysis complete")
        
        # Step 4: Create final summary
        logger.info("Creating comprehensive summary...")
        final_result = await summarization_agent.run()
        logger.info("Summary creation complete")
        
        # Prepare output data
        output_data = {
            'news': news_result.final_result(),
            'analysis': analysis_result.final_result(),
            'impact': impact_result.final_result(),
            'summary': final_result.final_result(),
            'timestamp': timestamp
        }
        
        # Generate HTML and JSON files
        logger.info("Generating output files...")
        html_path, json_path = await generate_html(output_data, timestamp)
        logger.info(f"Files created: {html_path}, {json_path}")
        
        # Print formatted results
        print("\n🌟 AI in India - Comprehensive Analysis 🌟")
        print("\n=== Latest News ===")
        print(f"{news_result.final_result()}")
        
        print("\n=== Key Analysis ===")
        print(f"{analysis_result.final_result()}")
        
        print("\n=== Industry Impact ===")
        print(f"{impact_result.final_result()}")
        
        print("\n=== Summary ===")
        print(f"{final_result.final_result()}")
        
    except BrowserError as e:
        logger.error(f"Browser error occurred: {e}")
        raise
    except FileError as e:
        logger.error(f"File operation error: {e}")
        raise
    except AnalysisError as e:
        logger.error(f"Analysis error occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

async def generate_html(output_data, timestamp):
    """Generate HTML page from the output data"""
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI in India - Latest Analysis ({timestamp})</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .header h1 {{ color: #2c3e50; }}
        .section {{ background: #f8f9fa; padding: 20px; margin-bottom: 20px; border-radius: 8px; }}
        .section h2 {{ color: #34495e; margin-top: 0; }}
        .timestamp {{ color: #7f8c8d; font-size: 0.9em; }}
        .analysis {{ white-space: pre-wrap; }}
        .footer {{ text-align: center; color: #7f8c8d; margin-top: 40px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>AI in India - Comprehensive Analysis</h1>
        <p class="timestamp">Generated on: {timestamp}</p>
    </div>

    <div class="section">
        <h2>Latest News</h2>
        <div class="analysis">{output_data['news']}</div>
    </div>

    <div class="section">
        <h2>Key Analysis</h2>
        <div class="analysis">{output_data['analysis']}</div>
    </div>

    <div class="section">
        <h2>Industry Impact</h2>
        <div class="analysis">{output_data['impact']}</div>
    </div>

    <div class="section">
        <h2>Summary</h2>
        <div class="analysis">{output_data['summary']}</div>
    </div>

    <div class="footer">
        <p>Generated by AI Agents with BrowserUse</p>
    </div>
</body>
</html>
"""
    
    # Create news directory if it doesn't exist
    news_dir = "news"
    os.makedirs(news_dir, exist_ok=True)
    
    # Write HTML file
    html_path = os.path.join(news_dir, f"ai_analysis_{timestamp}.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Write JSON file
    json_path = os.path.join(news_dir, f"ai_analysis_{timestamp}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    return html_path, json_path

if __name__ == "__main__":
    asyncio.run(main())