from abc import ABC
from products import Product
class Promotion(ABC):
    @abstractmethod
    def apply_promotion(product, quantity):
        pass

class SecondHalfPrice(Promotion):
    pass

class ThirdOneFree(Promotion):
    pass

class PercentDiscount(Promotion):
    pass

