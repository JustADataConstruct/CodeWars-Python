"""
6kyu "Multiples of 3 or 5" kata
https://www.codewars.com/kata/514b92a657cdc65150000006/python
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
26-05-21
"""
import codewars_test as test


def solution(number):
    return 0 if number < 0 else sum([t for t in range(0, number) if t % 3 == 0 or t % 5 == 0])


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should handle basic cases")
    def basic_tests():
        test.assert_equals(solution(10), 23)
