"""
7kyu kata "Square every digit"
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
In this kata, you are asked to square every digit of a number and concatenate them.
30-11-21
"""

import codewars_test as test


def square_digits(num: int) -> int:
    result = ""
    for a in str(num):
        result += str(pow(int(a), 2))
    return int(result)


@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
        test.assert_equals(square_digits(0), 0)
