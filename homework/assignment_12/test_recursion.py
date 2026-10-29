"""
29.10.2026
homework
"""

import pytest
from recursion import factorial, fib, fib_fast, to_binary, hanoi


@pytest.mark.parametrize("n,expected", [(0, 1), (1, 1), (5, 120)])
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (10, 55)])
def test_fib(n, expected):
    assert fib(n) == expected


@pytest.mark.parametrize("n", range(21))
def test_fib_matches_fast(n):
    assert fib(n) == fib_fast(n)


def test_fib_fast_100():
    assert fib_fast(100) == 354224848179261915075


@pytest.mark.parametrize("n,expected", [
    (0, "0"), (1, "1"), (2, "10"), (5, "101"), (8, "1000")
])
def test_to_binary(n, expected):
    assert to_binary(n) == expected


@pytest.mark.parametrize("n", range(65))
def test_to_binary_like_bin(n):
    assert to_binary(n) == bin(n)[2:]


def test_hanoi_small():
    assert hanoi(1) == [("A", "C")]
    assert hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]


@pytest.mark.parametrize("n", range(1, 9))
def test_hanoi_count(n):
    assert len(hanoi(n)) == 2 ** n - 1


def test_hanoi_valid_moves():
    for n in range(1, 6):
        pegs = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        for source, target in hanoi(n):
            assert pegs[source]
            disk = pegs[source].pop()
            assert not pegs[target] or pegs[target][-1] > disk
            pegs[target].append(disk)
        assert pegs["C"] == list(range(n, 0, -1))


@pytest.mark.parametrize("f", [factorial, fib, fib_fast, to_binary])
def test_invalid_negative(f):
    with pytest.raises(ValueError):
        f(-1)


def test_hanoi_invalid_zero():
    with pytest.raises(ValueError):
        hanoi(0)

if __name__ == "__main__":
    pass