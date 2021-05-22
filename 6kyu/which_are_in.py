"""
6kyu "Which are in?" kata
https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
23-05-21
"""

import codewars_test as test


def in_array(array1, array2):
    result = []
    for word in array1:
        for word2 in array2:
            if word in word2:
                result.append(word)
    lst = list(set(result))  # Removing duplicates.
    lst.sort()
    return lst


@test.describe("in_array")
def tests():
    def testing(array1, array2, expect):
        actual = in_array(array1, array2)
        test.assert_equals(actual, expect)

    @test.it("Basic tests")
    def basics():
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        testing(a1, a2, r)
        a1 = ["arp", "mice", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        testing(a1, a2, r)
