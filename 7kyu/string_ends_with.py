"""
7kyu "String ends with?" kata
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
28-05-21
"""
import codewars_test as test


def solution(string: str, ending: str) -> bool:
    return string.endswith(ending)


test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
