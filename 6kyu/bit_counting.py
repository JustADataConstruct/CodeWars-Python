"""
6kyu "Bit counting" kata
https://www.codewars.com/kata/526571aae218b8ee490006f4/python
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
16-06-21
"""
import codewars_test as test


def count_bits(n: int) -> int:
    return f"{n:b}".count('1')


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count_bits(0), 0)
        test.assert_equals(count_bits(4), 1)
        test.assert_equals(count_bits(7), 3)
        test.assert_equals(count_bits(9), 2)
        test.assert_equals(count_bits(10), 2)
