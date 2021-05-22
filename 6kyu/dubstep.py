"""
6 kyu kata "Dubstep"
https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
22-05-21
"""


def song_decoder(song):
    return " ".join(song.replace("WUB", ' ').split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
