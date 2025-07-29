from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-mcp", stateless_http=True)

@mcp.tool()
def search_online(query: str) -> str:
    # TODO: Implement search logic
    return f"Results for {query}..."

@mcp.tool()
async def get_weather(city: str) -> str:
    #TODO: Implement search logic
    return f"Weather in {city} is sunny."
mcp_app = mcp.streamable_http_app()
