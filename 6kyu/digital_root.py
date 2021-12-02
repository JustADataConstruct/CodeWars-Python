"""
6kyu "Sum of digits / digital root" kata
https://www.codewars.com/kata/541c8630095125aba6000c00
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
2-12-2021
"""

import codewars_test as test


def digital_root(i: int) -> int:
    result = i
    while result >= 10:
        result = sum([int(a) for a in str(result)])
    return result


@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)
