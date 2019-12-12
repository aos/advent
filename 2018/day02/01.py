# Day 2 - Puzzle 1
# Find the checksum of the list of box IDs


import collections


def count(string):
    counter = collections.Counter(string)
    two = 0
    three = 0

    for _, value in counter.items():

        if two and three:
            break

        if value == 2:
            two = 1
        if value == 3:
            three = 1

    return two, three


def checksum(file):
    total_two = 0
    total_three = 0

    with open(file) as f:
        for line in f:
            two, three = count(line)
            total_two += two
            total_three += three

    return total_two * total_three


print(checksum('./day02-input.txt'))

# Tests
inp = {
    'abcdef': (0, 0),
    'bababc': (1, 1),
    'abbcde': (1, 0),
    'abcccd': (0, 1),
    'aabcdd': (1, 0),
    'abcdee': (1, 0),
    'ababab': (0, 1)
}

for key, value in inp.items():
    two, three = value
    test_two, test_three = count(key)

    assert(two == test_two)
    assert(three == test_three)

print('All tests passed!')
