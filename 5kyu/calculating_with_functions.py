"""
5kyu "Calculating with functions" kata
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. 
23-05-21
"""
import codewars_test as test


def calculate(s: str):
    a = int(s[0])
    b = int(s[2])
    op = s[1]
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return int(a/b)


def check(i: str, func=None):
    if func != None:
        s = i+func
        if len(s) == 3:
            return calculate(s)
        return i + func
    return i


def zero(func=None):
    return check("0", func)


def one(func=None):
    return check("1", func)


def two(func=None):
    return check("2", func)


def three(func=None):
    return check("3", func)


def four(func=None):
    return check("4", func)


def five(func=None):
    return check("5", func)


def six(func=None):
    return check("6", func)


def seven(func=None):
    return check("7", func)


def eight(func=None):
    return check("8", func)


def nine(func=None):
    return check("9", func)


def plus(func=None):
    if func != None:
        return "+" + func
    return "+"


def minus(func=None):
    if func != None:
        return "-" + func
    return "-"


def times(func=None):
    if func != None:
        return "*" + func
    return "*"


def divided_by(func=None):
    if func != None:
        return "/" + func
    return "/"


test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
