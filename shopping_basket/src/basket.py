from typing import List
from src.item import Item


class Basket:
    def __init__(self, items, subset_bonus_discount=None):
        if subset_bonus_discount is None:
            subset_bonus_discount = set()  # non-mutable default arg
        self.items: List[Item] = items
        self.subset_bonus_discount: set = subset_bonus_discount

    def get_subtotal(self) -> float:
        return sum([item.price for item in self.items])

    def get_total(self) -> float:
        return self.get_subtotal() - self.get_discount()

    def get_discount(self) -> float:
        """
        n: number if items in buy n get one free
        :return:
        """
        return self.apply_normal_discount() + self.apply_buy_n_get_one_free_discount() + self.apply_bonus_discount()

    def apply_normal_discount(self) -> float:
        discount = sum([item.discount_normal * item.price for item in self.items])
        return discount

    def apply_buy_n_get_one_free_discount(self) -> float:
        discount = 0.0
        for item in set(self.items):
            n_items = self.items.count(item)
            if item.discount_bogof > 0 and n_items > 1:
                discount += item.price * (n_items // (item.discount_bogof + 1))
        return discount

    def apply_bonus_discount(self) -> float:
        filtered_items = [item for item in self.items if item.discount_bonus]  # get relevant items
        sorted_items = sorted(filtered_items, key=lambda x: x.price, reverse=True)
        discount = sum([item.price for item in sorted_items[2::3]])  # get every third item starting from third item
        return discount
