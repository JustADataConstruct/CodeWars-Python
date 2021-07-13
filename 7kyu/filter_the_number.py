"""
7kyu "Filter the number" kata
https://www.codewars.com/kata/55b051fac50a3292a9000025/python

You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in the order they occur.
13-07-21

"""
import codewars_test as test


def filter_string(string: str) -> int:
    return int(''.join([a for a in string if a.isnumeric()]))


test.assert_equals(filter_string("123"), 123, 'Just return the numbers')
test.assert_equals(filter_string("a1b2c3"), 123, 'Just return the numbers')
test.assert_equals(filter_string("aa1bb2cc3dd"),
                   123, 'Just return the numbers')
test.assert_equals(filter_string("aa 112 3dd"),
                   1123, 'Just return the numbers')
test.assert_equals(filter_string("11bb2c23c3"),
                   112233, 'Just return the numbers')
