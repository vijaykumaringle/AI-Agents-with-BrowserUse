import asyncio
import logging
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_drawing_agent():
    """Create an agent specialized in drawing using AutoDraw.com"""
    # Load environment variables
    load_dotenv()
    
    try:
        # Initialize the Gemini model
        llm = ChatGoogleGenerativeAI(
            model='learnlm-2.0-flash-experimental'
        )
    except Exception as e:
        logger.error(f"Error initializing Gemini model: {e}")
        raise
    
    # Create the agent with browser configuration
    agent = Agent(
        task="Draw a cute cat using AutoDraw.com tools",
        llm=llm,
        #browser=True  # Enable browser capabilities
    )
    
    return agent
        

async def main():
    """Main function to draw a cat using AutoDraw.com"""
    try:
        logger.info("Starting cat drawing process...")
        await create_drawing_agent()
        logger.info("Drawing process completed!")
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main())