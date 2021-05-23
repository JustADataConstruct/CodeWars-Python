"""
5kyu "ROT 13" kata
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
23-05-21
"""

import codewars_test as test

import string


def rot13(message: str):
    # I do lowercase only for the sake of simplicity.
    letters = list(string.ascii_lowercase)
    words = message.split(" ")
    result = []
    for w in words:
        word = ""
        for char in list(w):
            if char.lower() in letters:
                index = letters.index(char.lower())
                letter = letters[index +
                                 13] if index < 13 else letters[index-13]
                word += letter.upper() if char.isupper() else letter
            else:
                word += char
        result.append(word)
    return " ".join(result)


test.assert_equals(rot13("test"), "grfg")
test.assert_equals(rot13("Test"), "Grfg")
test.assert_equals(rot13("This is a + test"), "Guvf vf n + grfg")
