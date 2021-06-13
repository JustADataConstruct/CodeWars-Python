"""
7kyu "Highest and lowest" kata
https://www.codewars.com/kata/554b4ac871d6813a03000035/python

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
13-06-21
"""
import codewars_test as test


def high_and_low(numbers: str) -> str:
    result = [int(n) for n in numbers.split(" ")]
    result.sort()
    return "{} {}".format(result[len(result)-1], result[0])


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high_and_low(
            "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
        test.assert_equals(high_and_low("1 -1"), "1 -1")
        test.assert_equals(high_and_low("1 1"), "1 1")
        test.assert_equals(high_and_low("-1 -1"), "-1 -1")
        test.assert_equals(high_and_low("1 -1 0"), "1 -1")
        test.assert_equals(high_and_low("1 1 0"), "1 0")
        test.assert_equals(high_and_low("-1 -1 0"), "0 -1")
        test.assert_equals(high_and_low("42"), "42 42")
