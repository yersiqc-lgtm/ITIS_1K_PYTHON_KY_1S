"""
29.10.2026
class work 4
"""
import pytest
from exam import grade


@pytest.mark.parametrize(
        "score,expected", [
    (0, 2), (1, 2), (59, 2), (60, 3), (74, 3),
    (75, 4), (89, 4), (90, 5), (100, 5),
])
def test_grade(score, expected):
    assert grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_grade_out_of_range(score):
    with pytest.raises(ValueError):
        grade(score)
