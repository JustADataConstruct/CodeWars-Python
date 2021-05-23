"""
6kyu "IQ Test" kata
https://www.codewars.com/kata/552c028c030765286c00007d/train/python
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
23-05-21
"""
import codewars_test as test


def iq_test(numbers: str):

    lst = [int(n) for n in numbers.split(" ")]

    even = [int(n) for n in lst if int(n) % 2 == 0]
    odd = [int(n) for n in lst if int(n) % 2 != 0]

    return lst.index(even[0])+1 if len(even) < len(odd) else lst.index(odd[0])+1


test.assert_equals(iq_test("2 4 7 8 10"), 3)
test.assert_equals(iq_test("1 2 2"), 1)
