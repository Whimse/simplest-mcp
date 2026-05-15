from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("SimpleCalc")

@mcp.tool()
def add_numbers(x: int, y: int) -> int:
    """Adds two integers together and returns the result."""
    return x + y

def main():
    # Run using the standard input/output transport layer
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
