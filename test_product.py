import pytest
import products


def test_creating_valid_product():
    products.Product("Aux cord", price=3, quantity=50), "Product with valid inputs, cannot be made"


def test_creating_invalid_product():
    products.Product("just a string", price=4.9, quantity="dont tell anyone"), "Product with invalid inputs, cannot be made"


def test_deactivate_when_qnt_0():
    product = products.Product("Aux cord", price=3, quantity=50)
    product.is_active()
    product.set_quantity(0)
    product.is_active()


def test_purchase_amends_quantity():
    product = products.Product("Aux cord", price=3, quantity=50)
    product.buy(13)
    product.get_quantity()


def test_exception_raised_when_qnt_is_not_satisfied():
    product = products.Product("Aux cord", price=3, quantity=50)
    product.buy(51)


pytest.main()
