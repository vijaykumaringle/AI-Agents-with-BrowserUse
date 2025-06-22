import asyncio
import logging
from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_web_agent():
    """Create a basic web automation agent"""
    try:
        # Load environment variables
        load_dotenv()

        llm = ChatGoogleGenerativeAI(
            model='gemini-2.0-flash-exp'
        )
        
        # Create the agent with browser capabilities
        agent = Agent(
            task="Go to google and search for Vitthal Vari and extract summary data.",
            llm=llm,
            #browser=True  # Enable browser capabilities
        )
        
        return agent
    except Exception as e:
        logger.error(f"Error creating agent: {e}")
        raise

async def main():
    """Main function to demonstrate browser automation"""
    try:
        logger.info("Starting browser automation...")
        
        # Create the agent
        agent = await create_web_agent()
        
        # Run the agent
        result = await agent.run()
        
        # Print the result
        print(result)
        
        logger.info("Automation completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        raise

# Run the main function

if __name__ == "__main__":
    asyncio.run(main())