"""
6 kyu kata "Convert string to camel case"
https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
22-05-21
"""
import re


def to_camel_case(text):
    split = re.split('-|_', text)
    result = [t.capitalize() for t in split[1:]]
    return split[0] + "".join(result)


print(to_camel_case("the-stealth-warrior") == "theStealthWarrior")
print(to_camel_case("the-stealth-warrior"))
