from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        product: a product instance of class Product
        quantity: the amount of purchased items for that product
        """
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Every second item gets half price.
        """
        if quantity > 1:
            # Calculate the number of pairs since every second item of the pair gets half the price
            pairs = quantity // 2
            # Calculate the remaining single item (if any)
            remaining_items = quantity % 2
            print(f"--------quantity = {quantity}----------")
            print(f"pairs = {pairs}")
            print(f"remaining = {remaining_items}")
            return (pairs * product.price * 1.5) + (remaining_items * product.price)
        else:
            return quantity * product.price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Every third one is free
        """
        if quantity > 2:
            # Calculate the number of triples since every third item of a triple is free
            triple = quantity // 3
            # Calculate the remaining single item (if any)
            remaining_items = quantity % 3
            return (triple * product.price * 2) + (remaining_items * product.price)
        else:
            return quantity * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        if isinstance(percent, int or float):
            if 0 < percent <= 100:
                self._percent = percent
            else:
                raise Exception("input percentage has to more than 0% and less or equal to 100%")

    def apply_promotion(self, product, quantity):
        """
        PercentageDiscount
        """
        return product.price * (100 - self._percent) / 100 * quantity
