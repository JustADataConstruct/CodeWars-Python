"""
7kyu "Exes and ohs" kata
https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
30-11-2021
"""

import codewars_test as test


def xo(s: str) -> bool:
    s = s.lower()
    return s.count("x") == s.count("o")


test.expect(xo('xo'), 'True expected')
test.expect(xo('xo0'), 'True expected')
test.expect(not xo('xxxoo'), 'False expected')
