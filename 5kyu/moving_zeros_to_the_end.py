"""
5kyu "Moving zeros to the end" kata
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
2-12-2021
"""
import codewars_test as test


def move_zeros(arr: list[int]) -> list[int]:
    return [x for x in arr if x != 0] + [y for y in arr if y == 0]


@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])
