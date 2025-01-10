from promotions import Promotion

class Product:
    """
    class Product to handle all information of a product
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a Product object
        :param name:
        :param price:
        :param quantity:
        bool active = True (default)
        additional instance variable for promotion object: _promotion
        """
        _promotion = None #instance variable of class Promotion
        if quantity:
            if is_int_type_check(quantity):
                if quantity > 0:
                    self._quantity = quantity
                else:
                    raise Exception("quantity can not be negative")

        else:
            raise Exception("quantity can not be empty")
        if price:
            if is_int_or_float_type_check(price):
                if price > 0:
                    self._price = price
                else:
                    raise Exception("price can not be negative")
        else:
            raise Exception("price can not be empty")
        if name:
            if is_str_type_check(name):
                self._name = name
        else:
            raise Exception("empty name, please enter a valid string")
        self._active = True

    # A getter and setter for the promotion instance variable using
    @property
    def promotion(self):
        return self._promotion
    @promotion.setter
    def set_promotion(self, promotion):
        if isinstance(promotion, Promotion):
            self._promotion = promotion
        else:
            raise Exception("the input parameter is not an object of Class Promotion")


    def get_quantity(self):
        """
        returns the quantity of the product
        """
        return self._quantity

    def set_quantity(self, quantity):
        """
        set the quantity of the product
        """
        if is_int_type_check(quantity):
            self._quantity = quantity

    def is_active(self):
        """
        return either True or False for whether a product is active or not
        """
        return self._active

    def activate(self):
        """
        activate the product
        set the active attribute of the product to True
        """
        self._active = True

    def deactivate(self):
        """
        deactivate the product
        set the active attribute of the product to False
        """
        self._active = False

    def show(self):
        """
        return the information of the product
        """
        if self._promotion:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, Promotion: {self._promotion}"
        else:
            return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"


    def buy(self, quantity):
        """
        reduce the total quantity of the product by the quantity passed as argument
        """
        if is_int_type_check(quantity):
            if 0 < quantity <= self._quantity:
                self._quantity -= quantity
                if self._quantity == 0:
                    self.deactivate()
                return quantity * self._price
            elif quantity < 0:
                raise Exception("please give a quantity larger than 0!")
            else:
                raise Exception(f"not enough {self._name} in the warehouse")


def is_int_type_check(num):
    """
    check whether a variable has the type of integer
    """
    if type(num) is int:
        return True
    else:
        raise Exception("please only enter an integer!")


def is_int_or_float_type_check(num):
    """
    check whether a variable has the type of float or integer
    """
    if isinstance(num, int or float):
        return True
    else:
        raise Exception("please only enter an integer or a float!")


def is_str_type_check(input_str):
    """
    check whether a variable has the type of string
    """
    if type(input_str) is str:
        return True
    else:
        raise Exception("please only enter a string!")
