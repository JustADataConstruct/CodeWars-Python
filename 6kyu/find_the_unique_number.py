"""
6kyu "Find the unique number" kata
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

There is an array with some numbers. All numbers are equal except for one. Try to find it!
2-12-2021

"""

import codewars_test as test
from collections import Counter


def find_uniq(arr: list) -> int:
    return Counter(arr).most_common()[-1][0]


@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        test.assert_equals(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        test.assert_equals(find_uniq([3, 10, 3, 3, 3]), 10)
