

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # Test case
    assert max_subarray_sum([1]) == 1                      # Test for single element list
    assert max_subarray_sum([-1]) == -1                    # Test for single negative element list
    assert max_subarray_sum([-2,-3,-1]) == -1             # Test for all negative numbers
    assert max_subarray_sum([5,4,-1,7,8]) == 23           # Test for all positive numbers with one negative number
    assert max_subarray_sum([-2,1]) == 1                   # Test for two elements with one negative and one positive
    assert max_subarray_sum([-2,-1]) == -1                # Test for two