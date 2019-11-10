from src.basket import Basket
from src.item import Item
from src.catalog import Catalog


def test_get_product_details_from_file():
    assert Catalog.baked_beans.price == 0.99
    assert Catalog.sardines.discount_normal == 0.25
    assert Catalog.biscuits.discount_normal == 0.0


def test_basket_assignment_example():
    baked_beans = Item(name='Baked Beans', price=0.99, discount_bogof=2)
    biscuits = Item(name='Biscuits', price=1.20)

    basket = Basket(items=[baked_beans] * 4 + [biscuits])

    assert basket.get_subtotal() == 5.16
    assert basket.get_discount() == 0.99
    assert basket.get_total() == 4.17


def test_basket_bogof():
    baked_beans = Item(name='Baked Beans', price=0.99, discount_bogof=1)
    basket1 = Basket(items=[baked_beans])
    basket2 = Basket(items=[baked_beans] * 2)
    basket3 = Basket(items=[baked_beans] * 3)
    basket6 = Basket(items=[baked_beans] * 6)

    assert basket1.get_discount() == 0
    assert basket2.get_discount() == 0.99
    assert basket3.get_discount() == 0.99
    assert basket6.get_discount() == 0.99 * 3


def test_basket_bonus_discount():
    shampoo_small = Item(name='Shampoo Small', price=2.00, discount_bonus=True)
    shampoo_medium = Item(name='Shampoo Medium', price=2.50, discount_bonus=True)
    shampoo_large = Item(name='Shampoo Large', price=3.50, discount_bonus=True)
    basket = Basket(items=[shampoo_large] * 3 + [shampoo_medium] + [shampoo_small] * 2)

    assert basket.get_subtotal() == 17.00
    assert basket.get_discount() == 5.5
    assert basket.get_total() == 11.5
