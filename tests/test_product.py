import pytest
from src.products import Product, LimitedProduct, NonStockedProduct
from src.promotions import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount


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
    assert new_product.active
    new_product.buy(1)
    assert new_product.quantity == 0
    assert not new_product.active


def test_buy_modifies_quantity():
    """
    Test if the quantity of a product object will be modified automatically
    when the product object is bought
    """
    new_product = Product("Macbook", price=1000, quantity=10)
    new_product.buy(5)
    assert new_product.quantity == 5


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


# Testing other product classes
# Testing LimitedProduct Class
def test_buy_limited_product():
    new_product = LimitedProduct("Macbook", price=100, quantity=100, maximum=10)

    # Normal case
    assert new_product.buy(2) == 200

    # Buying more than allowed maximum
    with pytest.raises(Exception, match="please order a quantity less than 10"):
        new_product.buy(50)

    # Buying negative amount
    with pytest.raises(Exception, match="please give a quantity larger than 0!"):
        new_product.buy(-5)


# Testing NonStockedProduct Class
def test_buy_non_stocked_product():
    new_product = NonStockedProduct("Photoshop", price=1000)

    # Normal case
    assert new_product.buy(1)

    # Buying more than one NonStockedProduct
    with pytest.raises(Exception, match="Non Stocked Product only accepts quantity of 1"):
        new_product.buy(2)

    # Buying negative quantity
    with pytest.raises(Exception, match="please give a quantity larger than 0!"):
        new_product.buy(-1)


# Test Promotion Class
def test_second_half_price_promotion():
    new_product = Product("Macbook", price=1000, quantity=100)
    second_half_price = SecondHalfPrice("Second Half price!")
    new_product.promotion = second_half_price

    # checking if assigning second half price promotion works correctly
    assert isinstance(new_product.promotion, SecondHalfPrice)
    assert new_product.buy(2) == 1500
    assert new_product.buy(4) == 3000
    assert new_product.buy(5) == 4000

    # checking if promotion setter detects whether the assigned object is not an object of Class Promotion
    with pytest.raises(Exception, match="the input parameter is not an object of Class Promotion"):
        new_product.promotion = "hello"


def test_third_one_free_promotion():
    new_product = Product("Macbook", price=1000, quantity=100)
    third_one_free = ThirdOneFree("Third one free!")
    new_product.promotion = third_one_free

    # checking if assigning third-one-free promotion works correctly
    assert isinstance(new_product.promotion, ThirdOneFree)
    assert new_product.buy(1) == 1000
    assert new_product.buy(2) == 2000
    assert new_product.buy(3) == 2000
    assert new_product.buy(6) == 4000

def test_percent_discount_promotion():
    new_product = Product("Macbook", price=1000, quantity=100)
    percent_discount = PercentDiscount("Percent Discount!", 50)
    new_product.promotion = percent_discount
    # percentage negative
    with pytest.raises(Exception,match="input percentage has to more than 0% and less or equal to 100%"):
        percent_discount_negative = PercentDiscount("Percent Discount!", -50)

    # percentage more than 100
    with pytest.raises(Exception,match="input percentage has to more than 0% and less or equal to 100%"):
        percent_discount_more_than_hundred = PercentDiscount("Percent Discount!", 200)

    # checking if assigning percentage discount promotion works correctly
    assert isinstance(new_product.promotion, PercentDiscount)
    assert new_product.buy(1) == 500
    assert new_product.buy(2) == 1000
    assert new_product.buy(3) == 1500
    assert new_product.buy(6) == 3000
