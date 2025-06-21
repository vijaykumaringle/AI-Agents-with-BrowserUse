import asyncio
import logging
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_gemini_agent():
    """Create a BrowserUse agent with Google Gemini 2.0 flash-exp model"""
    # Load environment variables
    load_dotenv()
    
    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash-exp',
        temperature=0.7,
        max_output_tokens=2048
    )
    
    # Create the agent
    agent = Agent(
        task="Analyze web content and provide insights",
        llm=llm
    )
    
    return agent

async def run_analysis(url: str):
    """Run analysis on a given URL using the Gemini agent"""
    try:
        # Create the agent
        agent = await create_gemini_agent()
        
        # Navigate to the URL
        await agent.navigate(url)
        
        # Extract content
        content = await agent.extract_content(
            goal="Extract key information and insights from this page",
            include_links=True
        )
        
        # Analyze the content
        analysis = await agent.analyze(
            goal="Provide a concise analysis of the extracted content",
            content=content
        )
        
        return analysis
        
    except Exception as e:
        logger.error(f"Error running analysis: {e}")
        raise

async def main():
    """Main function to demonstrate the agent"""
    try:
        # Example URL to analyze
        url = "https://www.example.com"  # Replace with actual URL
        
        # Run the analysis
        result = await run_analysis(url)
        
        # Print the results
        print("\nAnalysis Results:")
        print("-" * 80)
        print(result)
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())