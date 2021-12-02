"""
6kyu "Find the missing letter" kata
https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
02-12-2021
"""

import codewars_test as test
import string


def find_missing_letter(chars: list) -> str:
    all_chars = ""
    if chars[0].isupper():
        all_chars = string.ascii_uppercase
    else:
        all_chars = string.ascii_lowercase
    start = all_chars.index(chars[0])
    seq = all_chars[start:start+len(chars)]
    return [a for a in seq if a not in chars][0]


test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
test.assert_equals(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
