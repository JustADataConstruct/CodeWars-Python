"""
6kyu "Highest scoring word" kata
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.
2-12-2021
"""

import codewars_test as test
import string


def high(s: str) -> str:
    words = s.split(" ")
    goal = {
        'word': '',
        'value': 0
    }
    for word in words:
        value = sum([string.ascii_lowercase.index(x)+1 for x in word])
        if value > goal['value']:
            goal['word'] = word
            goal['value'] = value
    return goal['word']


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(
            high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")
