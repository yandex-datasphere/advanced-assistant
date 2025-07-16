from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Restaurant")

@mcp.tool()
def get_food_menu() -> str:
    """Get the list of food items in the menu as Markdown table."""
    return open("../data/menu/food_en.md",encoding="utf8").read()

@mcp.tool()
def get_drinks_menu() -> str:
    """Get the list of drinks in the menu as Markdown table."""
    return open("../data/menu/drinks_en.md",encoding="utf8").read()
