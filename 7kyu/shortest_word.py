###############################
#  7kyu "Shortest word" kata#
#  https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9 
#  Simple, given a string of words, return the length of the shortest word(s).
#  19/01/2022
##########################

import codewars_test as test

def find_short(s:str) -> int:
    words = sorted(s.split(" "),key=len)
    return len(words[0])

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        test.assert_equals(find_short("lets talk about javascript the best language"), 3)
        test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
        test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)   
        test.assert_equals(find_short("Let's travel abroad shall we"), 2)

