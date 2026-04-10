from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "learning_assistant":{
                "command":"python",
                "args":["youtube_learning_server.py"], 
                "transport":"stdio",
            },
            "weather": {
                "command":"python",
                "args":["weather_server.py"], 
                "transport":"stdio",
            },
            "ddg-search": {
                "command": "uv", 
                "args": ["tool", "run", "duckduckgo-mcp-server"],
                "transport": "stdio", 
                "env": {
                    "DDG_SAFE_SEARCH": "STRICT",
                    "DDG_REGION": "us-en",
                    "FASTMCP_LOG_LEVEL": "ERROR" # Prevents log interference
                }
            },
        }
    )
    # ... setup tools and model ...
    model = ChatGroq(model="openai/gpt-oss-20b", temperature=0)
    tools = await client.get_tools()

    agent = create_agent(model, tools)

    # Uses youtube learning server
    prompt1 = await agent.ainvoke(
        {"messages": [
            {"role": "user", "content": "Get the YouTube video details ID: xOS0BhhdUbo"}]}
    )
    print("Summary:", prompt1['messages'][-1].content)
    
    # Uses weather server
    prompt2 = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "How's the weather in California today?"}]}
    )
    print("Weather response:", prompt2['messages'][-1].content)

    # Uses duck duck go search
    prompt4 = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Search for hotels in chicago near downtown"}]}
    )
    print("Result:", prompt4["messages"][-1].content)

asyncio.run(main())