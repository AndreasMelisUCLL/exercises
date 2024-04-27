import pytest
from pytest import approx
from mystatistics import average

@pytest.mark.parametrize('ns, expected', [
    ([], 0),
    ([1], 1),
    ([1, 3], 2),
    ([0.1, 0.1, 0.1], 0.1),
])
def test_average(ns, expected):
    actual = average(ns)
    assert approx(expected, abs=0.01) == actual, f'Average of numbers {ns} is {expected}, got {actual} instead.'
    