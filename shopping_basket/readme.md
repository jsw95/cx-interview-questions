## Usage

Product details are set in the `product_details.json` file so that an external user can change the offers and prices without having to change the code itself.
These are then applied in the `catalog.py` file and can be imported from the rest of the program.

Discounts are set at the item level rather than the basket level.

As the number of Items grows another field could be introduced to the `product_details` file which is a list of items that a discount applies to rather than
setting it for each item individually. However with this small number of items, setting the discounts for each item separately is acceptable. 

Test cases are written using `pytest` and can be run using the command `python -m pytest shopping_basket_tests/`