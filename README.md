# langchain-mcp-demo
A high-performance AI agent built with LangChain and Groq, utilizing the Model Context Protocol (MCP) to orchestrate multiple specialized servers for YouTube data, Duck Duck Go Search and Weather updates.

# 🚀 Features
- Multi-Server Architecture: Connects to three distinct MCP servers via stdio transport.
- High-Speed Inference: Powered by the gpt-oss-20b model on Groq for sub-second reasoning.
- Dynamic Tool Discovery: Automatically retrieves and initializes tools from all connected servers.
- Task Delegation: Handles complex math, video metadata extraction, and real-time weather queries in a single session.

# 🛠️ Tech Stack
- LLM: Groq (gpt-oss-20b)
- Framework: LangChain & LangChain MCP Adapters
- Async Runtime: Python asyncio
- Environment: python-dotenv

# 📋 Prerequisites
Ensure you have the following server files in your working directory:
- youtube_learning_server.py
- maths_server.py
- weather_server.py

# Configure Environment:
Create a .env file in the root directory and add your Groq API key:
- GROQ_API_KEY=your_api_key_here


# 🏃 Usage
Run the client script to trigger the agent's workflow:
```bash
python client.py
```

# The agent will perform the following sequentially:
- YouTube Extraction: Fetches details for a specific video ID (xOS0BhhdUbo).
- Weather Lookup: Retrieves current weather conditions for California.
- DuckDuckGo Search Logic: Fetches query over the internet, example search hotels in chicago
