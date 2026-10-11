import pytest

from src.calculator import add, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_number():
    assert add(-2, 5) == 3


def test_divide_numbers():
    assert divide(8, 2) == 4


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="division by zero"):
        divide(8, 0)
