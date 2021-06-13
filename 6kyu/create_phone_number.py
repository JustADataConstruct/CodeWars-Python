"""
6kyu "Create phone number" kata
https://www.codewars.com/kata/525f50e3b73515a6db000b83/python

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
13-06-21
"""

import codewars_test as test


def create_phone_number(n: list[int]) -> str:
    return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(*n)


test.describe("Basic tests")
test.assert_equals(create_phone_number(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
test.assert_equals(create_phone_number(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number(
    [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
test.assert_equals(create_phone_number(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
