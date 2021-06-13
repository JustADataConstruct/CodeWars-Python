"""
6kyu "Find the odd int" kata
https://www.codewars.com/kata/54da5a58ea159efa38000836/python
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
13-06-21
"""

import codewars_test as test
from collections import Counter

def find_it(seq:list[int]) -> int:
    count = Counter(seq)
    return [a for a in count if count[a]%2 != 0][0]

test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1) 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
test.assert_equals(find_it([10]), 10)
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)
