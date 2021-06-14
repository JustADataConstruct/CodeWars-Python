"""
6kyu "Counting duplicates" kata
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
14-06-21
"""
import codewars_test as test

from collections import Counter


def duplicate_count(text: str) -> int:
    counter = Counter(text.lower())
    return len([i for i in counter if counter[i] > 1])


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)
