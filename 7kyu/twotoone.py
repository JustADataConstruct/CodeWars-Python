"""
7 kyu kata "Two to one"
https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
22-05-21
"""
import codewars_test as test


def longest(a1, a2):
    s = set(a1+a2)
    return "".join(sorted(s))

    
@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        test.assert_equals(longest("lordsofthefallen", "gamekult"), "adefghklmnorstu")
        test.assert_equals(longest("codewars", "codewars"), "acdeorsw")
        test.assert_equals(longest("agenerationmustconfrontthelooming", "codewarrs"), "acdefghilmnorstuw")
