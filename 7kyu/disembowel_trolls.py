"""
7kyu "Disembowel Trolls" kata
https://www.codewars.com/kata/52fba66badcd10859f00097e/python
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
6-6-21
"""
import codewars_test as test


def disemvowel(string: str) -> str:
    return ''.join([l for l in string if l.lower() not in 'aeiou'])


@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(disemvowel(
        "This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
