import pytest
from src import products
from src.products import Product

def test_creating_prod():
    """
    Test creating a normal object of class Product
    """
    assert Product("Macbook M10 Ultra Mega A.I", price=1900, quantity=1000)

def test_creating_prod_invalid_details():
    """
    Test creating object of class Product with invalid arguments
    """
    # Name with empty string
    with pytest.raises(Exception, match="empty name, please enter a valid string"):
        new_product = Product("", price=1900, quantity=1000)

    # string instead of number for price
    with pytest.raises(Exception, match="please only enter an integer or a float!"):
        new_product = Product("Macbook", price="hello", quantity=1000)

    # string instead of number for quantity
    with pytest.raises(Exception, match="please only enter an integer!"):
        new_product = Product("Macbook", price=1000, quantity="hello")

    # enter a float instead of integer for quantity
    with pytest.raises(Exception, match="please only enter an integer!"):
        new_product = Product("Macbook", price=1000, quantity=10.55)

    # enter 0 for price
    with pytest.raises(Exception, match="price can not be empty"):
        new_product = Product("Macbook", price=0, quantity=1000)

    # enter 0 for quantity
    with pytest.raises(Exception, match="quantity can not be empty"):
        new_product = Product("Macbook", price=1000, quantity=0)

    # enter a negative price
    with pytest.raises(Exception, match="price can not be negative"):
        new_product = Product("Macbook", price=-10, quantity=1000)

    # enter a negative price
    with pytest.raises(Exception, match="quantity can not be negative"):
        new_product = Product("Macbook", price=1000, quantity=-100)

def test_prod_becomes_inactive():
    """
    Test if the product will be deactivated when quantity == 0
    """
    new_product = Product("Macbook", price=1000, quantity=1)
    assert new_product.is_active()
    new_product.buy(1)
    assert new_product.get_quantity() == 0
    assert not new_product.is_active()

def test_buy_modifies_quantity():
    """
    Test if the quantity of a product object will be modified automatically
    when the product object is bought
    """
    new_product = Product("Macbook", price=1000, quantity=10)
    new_product.buy(5)
    assert new_product.get_quantity() == 5

def test_buy_too_much():
    """
    Test if an Exception will be raised if the buying quantity is greater than
    the existing quantity of a product object
    """
    new_product = Product("Macbook", price=1000, quantity=1)
    with pytest.raises(Exception, match="not enough Macbook in the warehouse"):
        new_product.buy(1000)

def test_buy_invalid_quantity():
    """
    Test if an Exception will be raised if the value for buying quantity is invalid
    """
    # Buying a negative amount of quantity
    new_product = Product("Macbook", price=1000, quantity=10)
    with pytest.raises(Exception, match="please give a quantity larger than 0!"):
        new_product.buy(-5)

    # Buying quantity is a string
    with pytest.raises(Exception, match="please only enter an integer!"):
        new_product.buy("hello")

    # Buying quantity left empty
    with pytest.raises(Exception):
        new_product.buy()
