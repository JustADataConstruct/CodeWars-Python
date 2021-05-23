"""
6kyu "Mexican Wave" kata
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
23-05-21
"""
import codewars_test as test


def wave(people: str):
    result = []
    for i in range(len(people)):
        if people[i] == " ":
            continue
        result.append(people[:i] + people[i].upper() + people[i+1:])
    return result


@test.describe('Example Tests')
def example_tests():
    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case1():
        test.assert_equals(wave("hello"), result)

    result = ["Codewars", "cOdewars", "coDewars", "codEwars",
              "codeWars", "codewArs", "codewaRs", "codewarS"]

    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case2():
        test.assert_equals(wave("codewars"), result)

    result = []

    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case3():
        test.assert_equals(wave(""), result)

    result = ["Two words", "tWo words", "twO words", "two Words",
              "two wOrds", "two woRds", "two worDs", "two wordS"]

    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case4():
        test.assert_equals(wave("two words"), result)

    result = [" Gap ", " gAp ", " gaP "]

    @test.it("Should return: '["+", ".join(result)+"]'")
    def example_test_case5():
        test.assert_equals(wave(" gap "), result)
