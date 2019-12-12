# Day 12 - Puzzle 1
# After *20* generations, what is the sum of the numbers of all pots which
# contain a plant?

import re


def create_plants(file, gen_max=20):
    initial, states = _parse_input(file)
    gen = 0
    diff = 0
    total = 0
    start = gen_max * 20 if gen_max <= 500 else 500
    # Extend out some empty pots to the left and keep track of first pot
    plants = (['.'] * start) + initial + (['.'] * start)

    while gen < gen_max:
        diff = total
        prev = list(plants)
        for index, pot in enumerate(plants):
            if index < len(plants) - 4:
                local = ''.join(plants[index:index+5])
                if local in states:
                    prev[index+2] = states[local]
                else:
                    prev[index+2] = '.'

        plants = prev
        total = _count(start, plants)
        diff = total - diff

        if diff == 50:
            total = total + ((gen_max - gen - 2) * diff)
            break

        gen += 1

    return total


def _count(start, plants):
    total = 0

    for index, p in enumerate(plants):
        if p == '#':
            total += index - start

    return total


def _parse_input(file):
    initial = ''
    states = {}

    with open(file) as f:
        for index, line in enumerate(f):
            if index == 0:
                initial = _parse_initial(line.strip())

            if index > 1:
                s, r = _parse_state(line.strip())
                states[s] = r

    return initial, states


def _parse_initial(line):
    return list(re.search(
        r'(?<=initial state: ).*', line
    ).group(0))


def _parse_state(line):
    return line.split(' => ')


# Tests
TEST_INITIAL = 'initial state: #..#.#..##......###...###'
TEST_STATE = '...## => #'
assert(_parse_initial(TEST_INITIAL) == list('#..#.#..##......###...###'))
assert(_parse_state(TEST_STATE) == ['...##', '#'])
assert(create_plants('./example-input.txt') == 325)
print('All tests passed!')

# Part 1
print(create_plants('./day12-input.txt', 20))

# Part 2
print(create_plants('./day12-input.txt', 50_000_000_000))
