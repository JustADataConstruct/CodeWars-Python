"""
7kyu kata Last Survivor
https://www.codewars.com/kata/609eee71109f860006c377d1
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.
23-05-21
"""
import codewars_test as test


def last_survivor(letters: str, coords=[]):
    for c in coords:
        letters = letters[:c] + letters[c+1:]
    return letters


@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(last_survivor('abc', [1, 1]), 'a')
        test.assert_equals(last_survivor('kbc', [0, 1]), 'b')
        test.assert_equals(last_survivor('zbk', [2, 1]), 'z')
        test.assert_equals(last_survivor('c', []), 'c')
        test.assert_equals(last_survivor('foiflxtpicahhkqjswjuyhmypkrdbwnmwbrrvdycqespfvdviucjoyvskltqaqirtjqulprjjoaiagobpftywabqjdmiofpsr', [8, 59, 52, 93, 21, 40, 88, 85, 59, 10, 82, 18, 74, 59, 51, 47, 75, 49, 23, 56, 1, 33, 39, 33, 34, 44, 25, 0, 51,
                           25, 36, 32, 57, 10, 57, 12, 51, 55, 24, 55, 31, 49, 6, 15, 10, 48, 27, 29, 38, 30, 35, 42, 23, 32, 9, 39, 39, 36, 8, 29, 2, 33, 14, 3, 13, 25, 9, 25, 18, 10, 1, 2, 20, 8, 2, 11, 5, 7, 0, 10, 10, 8, 12, 3, 5, 1, 7, 7, 5, 1, 4, 0, 4, 0, 0, 1]), 'd')
