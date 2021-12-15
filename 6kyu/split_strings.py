"""
6kyu "Split strings" kata
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
15-12-2021
"""
import codewars_test as test
import re


def solution(s: str) -> list[str]:
    if len(s) % 2 != 0:
        s += "_"
    return re.findall('..', s)


test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
