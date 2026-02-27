
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]          # Test case
    assert two_sum([3, 2, 4], 6) == [1, 2]  # multiple pairs
    assert two_sum([3, 3], 6) == [0, 1]  # duplicates
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]  # negatives
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]          # Test for zeroes in the list