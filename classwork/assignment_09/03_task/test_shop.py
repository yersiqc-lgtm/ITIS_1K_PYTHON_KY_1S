"""
29.10.2026
classwork 3
"""
import pytest # requiere descargar en la cmd
from shop import discount, total, is_adult, last_word


@pytest.mark.parametrize("price,percent,expected", [(100, 20, 80), (100, 0, 100), (100, 100, 0)])
def test_discount(price, percent, expected):
    assert discount(price, percent) == pytest.approx(expected)


@pytest.mark.parametrize("prices,expected", [([], 0), ([7], 7), ([2, 3, 4], 9)])
def test_total(prices, expected):
    assert total(prices) == expected


@pytest.mark.parametrize("age,expected", [(17, False), (18, True), (19, True)])
def test_is_adult(age, expected):
    assert is_adult(age) is expected


@pytest.mark.parametrize("text,expected", [("", ""), ("  ", ""), ("hello", "hello"), ("hello world", "world")])
def test_last_word(text, expected):
    assert last_word(text) == expected
