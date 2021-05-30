"""
6kyu "+1 array" kata
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/python
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.
30-05-2021
"""
import codewars_test as test
from typing import List


def up_array(arr: List[int]) -> List[int]:
    if len(arr) == 0 or any(t > 9 or t < 0 for t in arr):
        return None
    num = int("".join(map(str, arr)))
    num += 1
    return list(map(int, str(num)))


test.assert_equals(up_array([2, 3, 9]), [2, 4, 0])
test.assert_equals(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
test.assert_equals(up_array([1, -9]), None)
