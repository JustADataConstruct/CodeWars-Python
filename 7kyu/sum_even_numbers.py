"""
7kyu "Sum even numbers" kata
https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3
Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.

The input is a sequence of numbers: integers and/or floats.
25/10/22
"""

import codewars_test as test


def sum_even_numbers(seq: list[int]) -> int:
    return sum([x for x in seq if x % 2 == 0])


@test.describe("Simple integers input.")
def example_tests():
    test.assert_equals(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    test.assert_equals(sum_even_numbers([]), 0)
