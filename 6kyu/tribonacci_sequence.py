"""
6kyu "Tribonacci sequence" kata
https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)
15-12-2021
"""

import codewars_test as test


def tribonacci(signature: list[float], n: int) -> list[float]:
    if n < len(signature):
        return signature[:n]
    result = signature
    i = 0
    while len(result) < n:
        s = sum(result[i:i+3])
        result.append(s)
        i += 1
    return result


test.describe("Basic tests")
test.assert_equals(tribonacci([1, 1, 1], 10), [
                   1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
test.assert_equals(tribonacci([0, 0, 1], 10), [
                   0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
test.assert_equals(tribonacci([0, 1, 1], 10), [
                   0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test.assert_equals(tribonacci([1, 2, 3], 10), [
                   1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
test.assert_equals(tribonacci([3, 2, 1], 10), [
                   3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
test.assert_equals(tribonacci([1, 1, 1], 1), [1])
test.assert_equals(tribonacci([300, 200, 100], 0), [])
test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5,
                   3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])
