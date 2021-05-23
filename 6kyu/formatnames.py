"""
6 kyu kata "Format a string of names like 'Bart, Lisa & Maggie'."
https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
22-05-21
"""
import codewars_test as test

def namelist(names=[]):
    if len(names) == 0:
        return ''
    if len(names) > 1:
        name_list = ", ".join([t["name"] for t in names])
    else:
        return names[0]["name"]
    index = name_list.rfind(", ")  # Finding the last comma in the string.
    # Splits the string around the position of the comma and puts an ampersand between the two pieces.
    result = name_list[:index] + " &" + name_list[index+1:]
    return result

test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
test.assert_equals(namelist([]), '', "Must work with no names")
