"""
7kyu "Divide and conquer" kata
https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python
Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers.
23-05-21
"""

import codewars_test as test


def div_con(x: list):
    strings = [int(s) for s in x if isinstance(s, str)]
    ints = [i for i in x if isinstance(i, int)]

    return sum(ints)-sum(strings)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(div_con([9, 3, '7', '3']), 2)
        test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
        test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']), 13)
        test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
        test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
