"""
6kyu "Does my number look big in this?" kata
https://www.codewars.com/kata/5287e858c6b5a9678200083c

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.
30-11-2021
"""
import codewars_test as test


def narcissistic(i: int) -> bool:
    return i == sum([pow(int(a), len(str(i))) for a in str(i)])


test.assert_equals(narcissistic(7), True, '7 is narcissistic')
test.assert_equals(narcissistic(371), True, '371 is narcissistic')
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
