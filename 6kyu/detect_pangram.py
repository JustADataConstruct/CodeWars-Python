"""
6kyu "Detect pangram" kata
https://www.codewars.com/kata/545cedaa9943f7fe7b000048
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
15-12-2021
"""


import codewars_test as test
import string


def is_pangram(s: str) -> bool:
    return len([a for a in string.ascii_lowercase if a in s.lower()]) >= 26


pangram = "The quick, brown fox jumps over the lazy dog!"
test.assert_equals(is_pangram(pangram), True)
