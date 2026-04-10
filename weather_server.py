from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

# Initialize FastMCP
mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the current weather for a specific location.
    """
    url = f"https://wttr.in/{location}?format=3"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                return response.text.strip()
            else:
                return f"Could not retrieve weather for {location}. Status: {response.status_code}"
        except Exception as e:
            return f"Error connecting to weather service: {str(e)}"

async def run_test():
    print("-----How's the weather in California today?------")
    print(await get_weather("California"))
    print("-----Chicago------")
    print(await get_weather("Chicago"))

if __name__ == "__main__":
    # To run as a server for your client.py:
    mcp.run(transport="stdio")
    
    # asyncio.run(run_test())
