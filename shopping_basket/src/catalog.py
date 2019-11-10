import json
from src.item import Item
from pathlib import Path

with open(f"{Path(__file__).parent}/../product_details.json") as f:
    prod_file = json.load(f)


class Catalog:
    baked_beans = Item(**prod_file['baked_beans'])
    biscuits = Item(**prod_file['biscuits'])
    sardines = Item(**prod_file['sardines'])
    shampoo_small = Item(**prod_file['shampoo_small'])
    shampoo_medium = Item(**prod_file['shampoo_medium'])
    shampoo_large = Item(**prod_file['shampoo_large'])
