"""
7kyu "Get the middle character" kata
https://www.codewars.com/kata/56747fd5cb988479af000028/python
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
13-06-21
"""


import codewars_test as test
import math


def get_middle(s: str) -> str:
    return s[math.floor(len(s)/2)] if len(s) % 2 != 0 else s[math.floor(len(s)/2)-1] + s[math.floor(len(s)/2)]


test.assert_equals(get_middle("test"), "es")
test.assert_equals(get_middle("testing"), "t")
test.assert_equals(get_middle("middle"), "dd")
test.assert_equals(get_middle("A"), "A")
test.assert_equals(get_middle("of"), "of")
