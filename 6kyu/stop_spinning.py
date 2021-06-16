"""
6kyu "Stop gninnipS My sdroW!" kata
https://www.codewars.com/kata/5264d2b162488dc400000001/python
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
16-06-21
"""
import codewars_test as test


def spin_words(sentence: str) -> str:
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])


test.assert_equals(spin_words("Welcome"), "emocleW")
