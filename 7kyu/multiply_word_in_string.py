"""
7kyu "Multiply word in string" kata
https://www.codewars.com/kata/5ace2d9f307eb29430000092
You are to write a function that takes a string as its first parameter. This string will be a string of words.

You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the given string. The first word would be represented by 0.

Once you have the located string you are finally going to multiply by it the third provided parameter, which will also be an integer. You are additionally required to add a hyphen in between each word.
20/10/2022
"""
import codewars_test as test


def modify_multiply(st: str, loc: int, num: int) -> str:
    return "-".join([st.split(" ")[loc]]*num)


@ test.describe("Fixed test")
def test_group():
    @ test.it("Example tests")
    def test_case():
        test.assert_equals(modify_multiply("This is a string", 3, 5),
                           "string-string-string-string-string", "The string is incorrect")
        test.assert_equals(modify_multiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.",
                           8, 10), "that-that-that-that-that-that-that-that-that-that")
        test.assert_equals(modify_multiply(
            "Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence", 1, 1), "means")
        test.assert_equals(modify_multiply("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",
                           6, 8), "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance")
        test.assert_equals(modify_multiply(
            "Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.", 2, 5), "around-around-around-around-around")
