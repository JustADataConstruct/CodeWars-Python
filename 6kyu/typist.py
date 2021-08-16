"""
6kyu "Typist" kata
https://www.codewars.com/kata/592645498270ccd7950000b4/python

Given a string s. Your task is to count how many times the keyboard has been tapped by John.

You can assume that, at the beginning the Caps Lock light is not lit.
16-08-21
"""

import codewars_test as test


def typist(s: str) -> int:
    result = 0
    for i in range(0, len(s)):
        if i == 0:
            if s[i].isupper():
                result += 2
            else:
                result += 1
        else:
            if (s[i].islower() and s[i-1].isupper()) or (s[i].isupper() and s[i-1].islower()):
                result += 2
            else:
                result += 1
    return result


sample_test_cases = [
    ('Basic tests', [
        ('a', 1),
        ('aa', 2),
        ('A', 2),
        ('AA', 3),
        ('aA', 3),
        ('Aa', 4),
    ]),
    ('Longer words', [
        ('BeiJingDaXueDongMen', 31),
        ('AAAaaaBBBbbbABAB', 21),
        ('AmericanRAILWAY', 18),
        ('AaAaAa', 12),
        ('DFjfkdaB', 11),
    ]),
]


@test.describe('Sample tests')
def sample_tests():
    for name, test_cases in sample_test_cases:
        @test.it(name)
        def tests():
            for s, expected in test_cases:
                test.assert_equals(typist(s), expected, f'{s=}')
