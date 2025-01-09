from products import *


class Store:
    """
    class Store handles all information of a store object. This class is also a composition of class Products
    """

    def __init__(self, products_list):
        """
        initialize the store with a list of product objects
        """
        self._products_list = products_list

    def add_product(self, product):
        """
        add a product to the store's products_list
        """
        if is_product_type_check(product):
            if product not in self._products_list:
                self._products_list.append(product)
            else:
                raise Exception("product is already in the store")

    def remove_product(self, product):
        """
        remove a product from the store's products_list
        """
        if product in self._products_list:
            self._products_list.remove(product)

    def get_total_quantity(self):
        """
        get the total quantity of all products in the store
        return a sum of all product's quantities
        """
        total_quantity = 0
        for product in self._products_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        return a list of all products in the store
        """
        active_products_list = []
        for product in self._products_list:
            if product.is_active():
                active_products_list.append(product)
        return active_products_list

    def order(self, shopping_list):
        """
        Handle the ordering process in the store
        """
        order_price = 0
        # shopping_list is a list of tuples, each tuple has 2 elements: product_name, amount
        if len(shopping_list) > 0:
            for order_tuple in shopping_list:
                if type(order_tuple) is tuple:
                    if is_product_type_check(order_tuple[0]) and is_int_type_check(order_tuple[1]):
                        if order_tuple[0] in self._products_list:
                            order_price += order_tuple[0].buy(order_tuple[1])
                        else:
                            raise Exception("product doesn't exist in the store")
                else:
                    raise Exception("shopping list element is not a tuple!")
            return order_price
        else:
            raise Exception("empty shopping list")


def is_product_type_check(product):
    """
    check whether a variable points to an object of class Product
    """
    if type(product) is Product:
        return True
    else:
        raise Exception("This is not an instance of class Product!")
