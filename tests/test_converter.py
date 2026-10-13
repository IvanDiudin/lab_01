import pytest

from toolkit.converter import convert
from toolkit.errors import ConversionError


def test_length():
    assert convert(1000, "mm", "m") == 1.0
def test_mass():
    assert convert(1.5, "kg", "g") == 1500.0
def test_temperature():
    assert convert(0, "c", "f") == 32.0
def test_absolute_zero():
    with pytest.raises(ConversionError):
        convert(-300, "c", "k")