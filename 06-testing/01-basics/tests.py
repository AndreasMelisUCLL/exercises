from intervals import overlapping_intervals


def test_overlapping_interval():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((0, 5), (2, 3))
    assert overlapping_intervals((2, 3), (0, 5))
    assert overlapping_intervals((1, 2), (1, 2))
    assert not overlapping_intervals((0, 5), (3, 2))
    assert not overlapping_intervals((3, 2), (0, 5))
    assert not overlapping_intervals((3, 2), (3, 2))