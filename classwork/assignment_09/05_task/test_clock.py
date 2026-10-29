"""
29.10.2026
classwork 5 
"""

import pytest
from clock import to_minutes, to_time, add_minutes


@pytest.mark.parametrize("t,expected", [("00:00", 0), ("01:30", 90), ("23:59", 1439)])
def test_to_minutes(t, expected):
    assert to_minutes(t) == expected


@pytest.mark.parametrize("minutes,expected", [(0, "00:00"), (90, "01:30"), (1439, "23:59"), (1440, "00:00"), (1450, "00:10")])
def test_to_time(minutes, expected):
    assert to_time(minutes) == expected


@pytest.mark.parametrize("start,delta,expected", [
    ("23:50", 20, "00:10"), ("00:00", 60, "01:00"),
    ("12:30", 30, "13:00"), ("00:10", -20, "23:50"),
])
def test_add_minutes(start, delta, expected):
    assert add_minutes(start, delta) == expected

if __name__ == "__main__": # :,(
    pass