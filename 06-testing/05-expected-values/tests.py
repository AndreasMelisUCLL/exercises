import itertools
import pytest
from pytest import approx

from mergesort import *



@pytest.mark.parametrize('ns', [
    [n for n in range(size)] for size in range(100)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    
    assert left + right == ns
    assert approx(len(left), abs=1) == len(right)
    
    
@pytest.mark.parametrize('left', [
    [],
    [0, 1, 2],
    [1, 5, 5, 10],
    [3, 6, 7, 8],
    [4, 8, 12, 101, 205]
])
@pytest.mark.parametrize('right', [
    [],
    [0, 1, 2],
    [1, 5, 5, 10],
    [3, 6, 7, 8],
    [4, 8, 12, 101, 205]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)
    
@pytest.mark.parametrize('ns, expected', [
    (perm, ns)
    for ns in [
        [],
        [1],
        [1, 2, 3],
        [2, 7, 16],
        [5, 5, 5],
        [1, 1, 8, 12, 12, 16],
    ]
    for perm in itertools.permutations(ns)
])
def test_merge_sort(ns, expected):
    assert merge_sort(ns) == expected