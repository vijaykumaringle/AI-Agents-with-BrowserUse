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
        
        # Extract and format the summary
        try:
            # Find the last action result which contains the summary
            summary_result = result.all_results[-1]
            summary_text = summary_result.extracted_content
            
            # Format the output
            print("\n=== Vitthal Vari Summary ===")
            print("\n" + summary_text)
            print("\n=== Summary Data ===")
            
            # Try to extract JSON data if available
            for action in result.all_results:
                if "summary" in action.extracted_content:
                    try:
                        import json
                        json_data = json.loads(action.extracted_content.split("```json")[1].split("```")[0])
                        print("\nExtracted JSON Data:")
                        print(json.dumps(json_data, indent=2))
                    except Exception as e:
                        logger.warning(f"Could not extract JSON data: {e}")
                        
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