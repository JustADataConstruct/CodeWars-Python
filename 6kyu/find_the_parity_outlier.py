"""
6kyu "Find the parity outlier" kata
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
16-06-21
"""


import codewars_test as test


def find_outlier(integers: list[int]) -> int:
    l1 = [n for n in integers if n % 2 == 0]
    l2 = [n for n in integers if n % 2 != 0]
    return l1[0] if len(l1) < len(l2) else l2[0]


test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
