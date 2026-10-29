"""
29.10.2026
classwork
trab2
"""

import pytest # need install in your terminal
from calc import add, is_even, average # import from "calc"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.parametrize( # decorator
        "n,expected", 
        [(0, True), (2, True), (3, False), (-2, True), (-3, False)]
)
def test_is_even(n, expected):
    assert is_even(n) is expected


def test_average():
    assert average([1, 2]) == pytest.approx(1.5)
    assert average([2, 4, 6]) == pytest.approx(4.0)
    assert average([7]) == pytest.approx(7.0)


def test_average_empty():
    with pytest.raises(ZeroDivisionError):
        average([])

if __name__ == "__main__": # no hay aun nada :(
    pass