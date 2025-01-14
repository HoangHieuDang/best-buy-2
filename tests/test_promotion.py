import pytest
from src.products import Product
from src.promotions import Promotion, SecondHalfPrice, ThirdOneFree, PercentDiscount
# Test Promotion Class
def test_second_half_price_promotion():
    """
    Testing SecondHalfPrice class inherited from class Promotion
    """
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
    """
    Testing ThirdOneFree class inherited from class Promotion
    """
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
    """
    Testing PercentDiscount class inherited from class Promotion
    """
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

