import asyncio
import logging
from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path
from datetime import datetime
import json


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
        
        # Extract and print only the summary text
        try:
            # Find the action with the summary
            for action in result.all_results:
                if action.extracted_content and "summary" in action.extracted_content:
                    try:
                        # Extract JSON data
                        json_str = action.extracted_content.split("```json")[1].split("```json")[0]
                        json_data = json.loads(json_str)
                        print(json_data["summary"])
                        break
                    except Exception as e:
                        logger.warning(f"Could not extract JSON data: {e}")
                        
            # If we didn't find JSON data, try the final result
            if not any("summary" in action.extracted_content for action in result.all_results):
                final_result = result.all_results[-1].extracted_content
                print(final_result)
                
        except Exception as e:
            logger.error(f"Error processing results: {e}")
            print("\n=== Raw Results ===")
            print(result)
        
        logger.info("Automation completed successfully!")
        
    except Exception as e:
        logger.error(f"Error during automation: {e}")
        raise

# Run the main function

if __name__ == "__main__":
    asyncio.run(main())