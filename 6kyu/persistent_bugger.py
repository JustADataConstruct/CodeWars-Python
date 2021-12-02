"""
6kyu "Persistent bugger" kata
codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
2-12-21

"""

import codewars_test as test
import math


def persistence(n: int) -> int:
    count = 0
    while n > 9:
        n = math.prod([int(a) for a in str(n)])
        count += 1
    return count


@test.describe("Persistent Bugger.")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)
