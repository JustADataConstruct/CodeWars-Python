"""
6kyu "Writer number in expanded form" kata
https://www.codewars.com/kata/5842df8ccbd22792a4000245/python
You will be given a number and you will need to return it as a string in Expanded Form.
3-06-21
"""
import codewars_test as test


def expanded_form(num: int) -> str:
    result = []
    s = str(num)
    for i in range(len(s)):
        if s[i] == "0":
            continue
        zeroes = ""
        for z in range(i, len(s) - 1):
            zeroes += "0"
        result.append(s[i] + zeroes)
    return " + ".join(result)


test.assert_equals(expanded_form(12), '10 + 2')
test.assert_equals(expanded_form(42), '40 + 2')
test.assert_equals(expanded_form(70304), '70000 + 300 + 4')
