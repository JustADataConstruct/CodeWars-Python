"""
7kyu "Mumbling" kata
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

30-11-2021
"""
import codewars_test as test


def accum(s: str) -> str:
    result = ""
    for a in range(0, len(s)):
        result += s[a].upper()
        for i in range(0, a):
            result += s[a].lower()
        if a < len(s)-1:
            result += "-"
    return result


test.describe("accum")
test.it("Basic tests")
test.assert_equals(accum("ZpglnRxqenU"),
                   "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
test.assert_equals(accum("NyffsGeyylB"),
                   "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
test.assert_equals(accum("MjtkuBovqrU"),
                   "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
test.assert_equals(accum("EvidjUnokmM"),
                   "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
test.assert_equals(accum("HbideVbxncC"),
                   "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
