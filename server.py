from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    """Send a greeting"""
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", uvicorn_kwargs={"host": "0.0.0.0", "port": 8000})

