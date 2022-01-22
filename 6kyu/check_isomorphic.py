"""
6kyu "Check if two words are isomorphic to each other" kata
https://www.codewars.com/kata/59dbab4d7997cb350000007f
Two strings a and b are called isomorphic if there is a one to one mapping possible for every character of a to every character of b. And all occurrences of every character in a map to same character in b.
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS

Task
In this kata you will create a function that return True if two given strings are isomorphic to each other, and False otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.
22-01-22
"""

import codewars_test as test

def isomorph(a:str,b:str) -> bool:
    if len(a) != len(b):
        return False
    mappings = {}
    for x in range(len(a)):
        if a[x] in mappings:
            if b[x] != mappings[a[x]]: #Return false if we have seen this char before and it doesn't match with what we're seeing now.
                return False
        elif b[x] in mappings.values(): #Return false if we haven't seen this char before but we have seen the equivalent.
            return False
        else:
            mappings[a[x]] = b[x]
    return True

test.assert_equals(isomorph("ESTATE", "DUELED"), True)
test.assert_equals(isomorph("XXX", "YYY"), True)

test.assert_equals(isomorph("SEE", "SAW"), False)
test.assert_equals(isomorph("XXY", "XYY"), False)

# Should handle words with more than 10 characters
test.assert_equals(isomorph("abcdefghijk","abcdefghijba"), False)
