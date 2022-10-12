"""
6kyu "Unique in order" kata
https://www.codewars.com/kata/54e6533c92449cc251001667
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
12-10-22
"""

import codewars_test as test


def unique_in_order(iterable) -> list:
    last = None
    list = []
    for x in iterable:
        if x != last:
            list.append(x)
        last = x
    return list


test.assert_equals(unique_in_order('AAAABBBCCDAABBB'),
                   ['A', 'B', 'C', 'D', 'A', 'B'])
