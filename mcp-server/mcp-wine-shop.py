from fastmcp import FastMCP
import pandas as pd
from typing import Literal

# Create an MCP server
mcp = FastMCP("Wine Shop")

print("Starting Wine Shop MCP server...")
print(" + Loading wine table")
pl = pd.read_excel("../data/wine-price-ru.xlsx")
 
country_map = {
    "IT": "Италия",
    "FR": "Франция",
    "ES": "Испания",
    "RU": "Россия",
    "PT": "Португалия",
    "AR": "Армения",
    "CL": "Чили",
    "AU": "Австрия",
    "GE": "Грузия",
    "ZA": "ЮАР",
    "US": "США",
    "NZ": "Новая Зеландия",
    "DE": "Германия",
    "AT": "Австрия",
    "IL": "Израиль",
    "BG": "Болгария",
    "GR": "Греция",
    "AU": "Австралия",
}

revmap = {v.lower(): k for k, v in country_map.items()}

@mcp.tool()
def find_wines(
    name : str | None, 
    country : str | None, 
    color: Literal["Красное", "Белое", "Розовое"] | None,
    acidity: Literal["Сухое","Полусухое","Полусладкое","Сладкое"] | None,
    sort_order : Literal["Сначала дешевое","Сначала дорогое"] | None,
    top_n : int | None
    ) -> str:
    """
    Найти доступные вина в магазине. Параметры:
    * name - название вина
    * country - страна происхождения, на русском языке
    * color - цвет вина ("Красное", "Белое", "Розовое")
    * acidity - кислотность вина ("Сухое","Полусухое","Полусладкое","Сладкое")
    * sort_order - порядок сортировки ("Сначала дешевое","Сначала дорогое")
    * top_n - количество вин, которое нужно вернуть
    """
    x = pl.copy()
    if country and country.lower() in revmap.keys():
        x = x[x["Country"] == revmap[country.lower()]]
    if acidity:
        x = x[x["Acidity"] == acidity.capitalize()]
    if color:
        x = x[x["Color"] == color.capitalize()]
    if name:
        x = x[x["Name"].apply(lambda x: name.lower() in x.lower())]
    if sort_order and sort_order=="Сначала дешевое":
        x = x.sort_values(by="Price")
    if sort_order and sort_order=="Сначала дорогое":
        x = x.sort_values(by="Price", ascending=False)
    if top_n is None:
        top_n = 10    
    if x is None or len(x) == 0:
        return "Подходящих вин не найдено"
    return "Вот какие вина были найдены:\n" + "\n".join(
        [
            f"{z['Name']} ({country_map.get(z['Country'],'Неизвестно')}) - {z['Price']}"
            for _, z in x.head(top_n).iterrows()
        ])

