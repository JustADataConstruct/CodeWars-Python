"""
7kyu kata "Build a square"
https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
I will give you an integer. Give me back a shape that is as long and wide as the integer. The integer will be a whole number between 1 and 50.
23-05-21
"""
import codewars_test as test


def generate_shape(integer: int):
    str = ""
    for x in range(integer):
        for i in range(integer):
            str += "+"
        if x != integer-1:
            str += "\n"
    return str


@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(generate_shape(3), '+++\n+++\n+++')
    test.assert_equals(generate_shape(
        8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')
