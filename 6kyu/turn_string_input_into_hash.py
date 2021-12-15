"""
6kyu "Turn string input into hash" kata
https://www.codewars.com/kata/52180ce6f626d55cf8000071
Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.

"a=1, b=2, c=3, d=4"
This string should return a hash that looks like

{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
15-12-2021
"""

import codewars_test as test
import ast
import re


def str_to_hash(s: str) -> dict:
    s = re.sub(r'([a-z]+)', r'"\1"', s)
    s = s.replace("=", ":")
    return ast.literal_eval("{" + s.strip() + "}")


@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(str_to_hash("a=1, b=2, c=3, d=4"), {
                           'a': 1, 'b': 2, 'c': 3, 'd': 4})
        test.assert_equals(str_to_hash(""), {})
