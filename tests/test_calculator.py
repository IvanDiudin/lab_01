import pytest

from toolkit.calculator import calculate
from toolkit.errors import CalculatorError


def test_add():
    assert calculate("2 + 3") == 5.0


def test_sub():
    assert calculate("10 - 4") == 6.0


def test_mul():
    assert calculate("3 * 4") == 12.0


def test_div():
    assert calculate("10 / 4") == 2.5


def test_priority():
    assert calculate("2 + 3 * 4") == 14.0


def test_no_spaces():
    assert calculate("2+3") == 5.0


def test_div_by_zero():
    with pytest.raises(CalculatorError):
        calculate("1 / 0")


def test_letters():
    with pytest.raises(CalculatorError):
        calculate("2 + a")


def test_double_operator():
    with pytest.raises(CalculatorError):
        calculate("2 * / 3")


def test_empty():
    with pytest.raises(CalculatorError):
        calculate("")


def test_unary_minus():
    assert calculate("2 * -3") == -6.0
