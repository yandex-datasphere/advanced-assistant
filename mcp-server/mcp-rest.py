from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Restaurant")

@mcp.tool()
def get_food_menu() -> str:
    """Получить меню блюд ресторана в виде таблицы в формате Markdown."""
    return open("../data/menu/food.md",encoding="utf8").read()

@mcp.tool()
def get_drinks_menu() -> str:
    """Получить меню напитков ресторана в виде таблицы в формате Markdown."""
    return open("../data/menu/drinks.md",encoding="utf8").read()
