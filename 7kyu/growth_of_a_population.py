"""
7kyu "Growth of a population" kata
https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
23-05-21
"""

import codewars_test as test
import math


def nb_year(population: int, percent: float, coming: int, goal: int):
    ages = 0
    while population < goal:
        population += int((population * percent/100)) + coming
        ages += 1
    return ages


@ test.describe("nb_year")
def tests():
    @ test.it("basic tests")
    def basics():
        test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)
