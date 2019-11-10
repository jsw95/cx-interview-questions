class Item:
    def __init__(self, name, price, discount_normal=0.0, discount_bogof=0, discount_bonus=False):
        """
        :param name: Product Display Name
        :param price: Price in GBP
        :param discount_normal: Proportion of price taken off product (0 to 1)
        :param discount_bogof: buy n get one free, eg discount_bogof=2 -> buy two get one free
        :param discount_bonus: True if product in the bonus discount subset, False if not
        """
        self.name: str = name
        self.price: float = price
        self.discount_normal: float = discount_normal
        self.discount_bogof: int = discount_bogof
        self.discount_bonus: bool = discount_bonus
