import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

async def main():
    # Initialize the model
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')
    
    agent = Agent(
        task="Check Iphone 16 512gb price in Amazon.in and Flipkart.com. And then compare the prices",
        llm=llm
    )
    await agent.run()

asyncio.run(main())