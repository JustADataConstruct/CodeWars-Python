"""
7kyu "L2: Triple X" kata
https://www.codewars.com/kata/568dc69683322417eb00002c

Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".
23-05-21
"""

import codewars_test as test


def triple_x(s: str):
    return s.find("x") == s.find("xxx") and s.find("x") != -1


@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(triple_x(""), False)
        test.assert_equals(triple_x("there's no XXX here"), False)
        test.assert_equals(triple_x("abraxxxas"), True)
        test.assert_equals(triple_x("xoxotrololololololoxxx"), False)
        test.assert_equals(triple_x("soft kitty, warm kitty, xxxxx"), True)
        test.assert_equals(triple_x("softx kitty, warm kitty, xxxxx"), False)
