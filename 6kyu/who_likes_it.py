"""
6kyu "Who likes it?" kata
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples
26-05-21
"""
import codewars_test as test


def likes(names: list[str]) -> str:
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return "{} likes this".format(names[0])
    if len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    if len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    if len(names) >= 4:
        num = len(names)-2
        return "{}, {} and {} others like this".format(names[0], names[1], num)


@ test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']),
                       'Max, John and Mark like this')
    test.assert_equals(
        likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
