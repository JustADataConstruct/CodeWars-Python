"""
7kyu "What a classy song" kata
https://www.codewars.com/kata/6089c7992df556001253ba7d/python

The method takes an array of people who have listened to the song that day. The output should be how many new listeners the song gained on that day out of all listeners. Names should be treated in a case-insensitive manner, i.e. "John" is the same as "john".
14-07-21
"""
import codewars_test as test
from collections import OrderedDict


class Song():
    def __init__(self, title, artist) -> None:
        self.listeners = []
        self.title = title
        self.artist = artist

    def how_many(self, listeners) -> int:
        newList = [x.lower()
                   for x in listeners if x.lower() not in self.listeners]
        result = list(OrderedDict.fromkeys(newList))
        self.listeners += result
        return len(result)


mount_moose = Song('Mount Moose', 'The Snazzy Moose')

test.assert_equals(mount_moose.title, 'Mount Moose')
test.assert_equals(mount_moose.artist, 'The Snazzy Moose')
test.assert_equals(mount_moose.how_many(
    ['John', 'Fred', 'Bob', 'Carl', 'RyAn']), 5)
test.assert_equals(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']), 2)
test.assert_equals(mount_moose.how_many(
    ['Amanda', 'CalEb', 'CarL', 'Furgus']), 2)
test.assert_equals(mount_moose.how_many(
    ['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']), 1)
