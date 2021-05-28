"""
6kyu "Your order, please" kata
https://www.codewars.com/kata/55c45be3b2079eccff00010f
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
28-05-21
"""
import codewars_test as test


def order(s: str) -> str:
    if s == "":
        return s
    words = s.split(' ')
    result = []
    for i in range(len(words)):
        for word in words:
            if str(i+1) in word:
                result.append(word)
    return " ".join(result)


test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"),
                   "Fo1r the2 g3ood 4of th5e pe6ople")
test.assert_equals(order(""), "")
