from mcp.server.fastmcp import FastMCP

mcp_app = FastMCP(name="MCP client", stateless_http=True)

mcp_server = mcp_app.streamable_http_app()