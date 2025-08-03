import os
import uvicorn
from mcp.server.fastapi import FastMCP

# Your existing MCP server setup
mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    """Send a greeting"""
    return f"Hi {name}"

if __name__ == "__main__":
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get("PORT", 8000))
    
    # Create the FastAPI app from MCP
    app = mcp.get_app()
    
    # Run with uvicorn, binding to 0.0.0.0 for Render
    uvicorn.run(
        app, 
        host="0.0.0.0",  # This is crucial - not 127.0.0.1
        port=port
    )