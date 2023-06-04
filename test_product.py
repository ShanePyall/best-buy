import pytest
import products


def test_normal_product_creation():
    assert products.Product(name="Iphone 10", price=920, quantity=50)


def test_invalid_product_creation():
    assert products.Product(name=99, price="help", quantity=7.5)


def test_product_deactivates_qnt_0():
    iphone = products.Product(name="Iphone 10", price=920, quantity=50)
    iphone.is_active()
    iphone.buy(50)
    assert iphone.is_active() == False


def test_product_quantity_changes_when_ordered():
    iphone = products.Product(name="Iphone 10", price=920, quantity=50)
    iphone.buy(6)
    assert iphone.get_quantity()


def test_exception_when_quantity_less_than_ordered():
    iphone = products.Product(name="Iphone 10", price=920, quantity=50)
    assert iphone.buy(51) == 0.0


pytest.main()
