"""
6kyu "Count characters in your string" kata
https://www.codewars.com/kata/52efefcbcdf57161d4000091/python
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
14-06-21
"""
import codewars_test as test
from collections import Counter


def count(string: str) -> dict:
    return Counter(string)


test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
