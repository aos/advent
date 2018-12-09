# Day 9 - Puzzle 1 and 2
# What is the winning Elf's score?


import collections
import re


def marbles(string):
    num_players, last_marble = _parse(string)
    players = collections.defaultdict(int)
    # Initialize the circle with marble 0 and 1
    circle = collections.deque([0])
    curr_player = 1
    curr_marble = 1

    while curr_marble <= last_marble:
        if curr_marble % 23 == 0:
            players[curr_player] += curr_marble
            circle.rotate(7)
            players[curr_player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(len(circle) - 1)
            circle.append(curr_marble)

        curr_marble += 1
        curr_player = (curr_player + 1) % num_players

    return max(players.values())


def _parse(string):
    return tuple(
        int(i) for i in re.search(r'(\d+)\D*(\d+).*', string).groups()
    )


TEST_INPUT = [
    ('10 players; last marble is worth 1618 points', 8317),
    ('13 players; last marble is worth 7999 points', 146373),
    ('17 players; last marble is worth 1104 points', 2764),
    ('21 players; last marble is worth 6111 points', 54718),
    ('30 players; last marble is worth 5807 points', 37305)
]
small_test = '9 players; last marble is worth 25 points'
assert(_parse(TEST_INPUT[0][0]) == (10, 1618))
assert(marbles(small_test) == 32)
for ex, score in TEST_INPUT:
    assert(marbles(ex) == score)
print('All tests passed!')

# Part 1
print(marbles('428 players; last marble is worth 72061 points'))

# Part 2
print(marbles('428 players; last marble is worth 7206100 points'))
