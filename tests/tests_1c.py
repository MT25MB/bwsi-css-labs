

from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # basic sample
    assert max_subarray_sum([1]) == 1                      # single element
    assert max_subarray_sum([-1]) == -1                    # single negative
    assert max_subarray_sum([-2,-3,-1]) == -1             # all negative
    assert max_subarray_sum([5,4,-1,7,8]) == 23           # mostly positive
    assert max_subarray_sum([-2,1]) == 1                   # neg+pos pair
    assert max_subarray_sum([-2,-1]) == -1                # two negatives