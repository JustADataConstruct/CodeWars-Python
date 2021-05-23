"""
6 kyu kata "Dubstep"
https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
22-05-21
"""
import codewars_test as test


def song_decoder(song):
    return " ".join(song.replace("WUB", ' ').split())


test.assert_equals(song_decoder("AWUBBWUBC"), "A B C",
                   "WUB should be replaced by 1 space")
test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"),
                   "A B C", "multiples WUB should be replaced by only 1 space")
test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C",
                   "heading or trailing spaces should be removed")
