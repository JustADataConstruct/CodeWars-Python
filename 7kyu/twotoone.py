"""
7 kyu kata "Two to one"
https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
22-05-21
"""


def longest(a1, a2):
    s = set(a1+a2)
    return "".join(sorted(s))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b) == "abcdefklmopqwxy")
