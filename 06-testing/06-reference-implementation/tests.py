import pytest
from student import Student
from search import *


@pytest.mark.parametrize('students', [
    [Student(id) for id in ids]
    for ids in [
        [1, 2, 3], 
        [2, 6, 8],
        [5, 6, 7, 8],
        [3, 5, 7, 9],
    ]
])
@pytest.mark.parametrize('target_id', [
    n for n in range(11)
])
def test_binary_search_existing(students, target_id):
    assert binary_search(students, target_id) == linear_search(students, target_id)
    