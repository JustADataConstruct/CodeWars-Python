"""
6kyu "Who has the most money?" kata
https://www.codewars.com/kata/528d36d7cc451cd7e4000339
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
15-12-2021
"""

import codewars_test as test


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students: list[Student]) -> str:
    if len(students) == 1:
        return students[0].name
    res = sorted(students, key=lambda x: sum(
        [5*x.fives, 10*x.tens, 20*x.twenties]), reverse=True)
    if len(set([sum([5*x.fives, 10*x.tens, 20*x.twenties]) for x in students])) == 1:
        return "all"
    return res[0].name


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

test.assert_equals(most_money([cam, geoff, phil]), "Phil")
test.assert_equals(most_money([cam, geoff]), "all")
test.assert_equals(most_money([geoff]), "Geoff")
