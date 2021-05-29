"""
6kyu "Quidditch Scoreboard" kata
https://www.codewars.com/kata/5b62f8a5b17883e037000136/python

Quidditch is a sport with two teams. The teams score goals by throwing the Quaffle through a hoop, each goal is worth 10 points.

The referee also deducts 30 points (- 30 points) from the team who are guilty of carrying out any of these fouls: Blatching, Blurting, Bumphing, Haverstacking, Quaffle-pocking, Stooging

The match is concluded when the Snitch is caught, and catching the Snitch is worth 150 points. Let's say a Quaffle goes through the hoop just seconds after the Snitch is caught, in that case the points of that goal should not end up on the scoreboard seeing as the match is already concluded.
You will be given a string with two arguments, the first argument will tell you which teams are playing and the second argument tells you what's happened in the match. Calculate the points and return a string containing the teams final scores, with the team names sorted in the same order as in the first argument.
29-05-2021
"""

import codewars_test as test


def quidditch_scoreboard(teams: str, actions: str) -> str:
    t = teams.split(" vs ")
    board = {
        t[0]: 0,
        t[1]: 0
    }
    points = {
        'goal': 10,
        'foul': -30,
        'Snitch': 150
    }
    for a in actions.split(', '):
        a = a.split(':')
        team = a[0]
        i = [k for k in points if k in a[1]][0]
        board[team] += points[i]
        if i == "Snitch":
            break
    return "{0}: {1}, {2}: {3}".format(t[0], board[t[0]], t[1], board[t[1]])


teams = "Appleby Arrows vs Montrose Magpies"
actions = "Montrose Magpies: Quaffle goal, Montrose Magpies: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Montrose Magpies: Haverstacking foul, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Appleby Arrows: Quaffle goal, Montrose Magpies: Caught Snitch"
test.assert_equals(quidditch_scoreboard(teams, actions),
                   "Appleby Arrows: 60, Montrose Magpies: 140")


teams = "Kenmare Kestrels vs Barnton"
actions = "Barnton: Quaffle goal, Kenmare Kestrels: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Kenmare Kestrels: Blurting foul, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Barnton: Quaffle goal, Kenmare Kestrels: Caught Snitch"
test.assert_equals(quidditch_scoreboard(teams, actions),
                   "Kenmare Kestrels: 130, Barnton: 100")

teams = "Wimbourne Wasps vs Cork"
actions = "Cork: Quaffle goal, Cork: Quaffle-pocking foul, Cork: Quaffle goal, Wimbourne Wasps: Quaffle goal, Cork: Quaffle goal, Wimbourne Wasps: Quaffle goal, Wimbourne Wasps: Quaffle goal, Wimbourne Wasps: Quaffle goal, Cork: Quaffle goal, Wimbourne Wasps: Quaffle goal, Cork: Caught Snitch, Wimbourne Wasps: Quaffle goal"
test.assert_equals(quidditch_scoreboard(teams, actions),
                   "Wimbourne Wasps: 50, Cork: 160")
