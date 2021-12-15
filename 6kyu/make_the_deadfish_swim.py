"""
6kyu "Make the deadfish swim" kata
https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
15-12-2021
"""

import codewars_test as test


def parse(data: str) -> list[int]:
    val = 0
    res = []
    for dt in list(data):
        if dt == "i":
            val += 1
        elif dt == "d":
            val -= 1
        elif dt == "s":
            val = pow(val, 2)
        elif dt == "o":
            res.append(val)
    return res


test.assert_equals(parse("ooo"), [0, 0, 0])
test.assert_equals(parse("ioioio"), [1, 2, 3])
test.assert_equals(parse("idoiido"), [0, 1])
test.assert_equals(parse("isoisoiso"), [1, 4, 25])
test.assert_equals(parse("codewars"), [0])
