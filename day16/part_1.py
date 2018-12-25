# Day 16 - Puzzle 1
# How many samples behave like three or more opcodes?


import opcodes as opc
import re
from copy import copy


def count_match(bfr, aft, stmnt):
    opcs = []
    for i in [m for m in dir(opc) if not m.endswith('__')]:
        n_b = copy(bfr)
        if eval(f"opc.{i}({n_b}, {stmnt[1]}, {stmnt[2]}, {stmnt[3]})") == aft:
            opcs.append(i)
    return opcs


def parse_samples(file):
    all_input = []
    nxt = 0
    rx_reg = r'\[(\d+), (\d+), (\d+), (\d+)]'
    with open(file) as f:
        before = None
        statement = None
        after = None
        for line in f:
            if before and statement and after:
                all_input.append({
                    'before': before,
                    'statement': statement,
                    'after': after
                })
                before = statement = after = None
                nxt = 0
                continue

            if line == '\n':
                nxt += 1
                if nxt >= 2:
                    return all_input
                continue

            if 'Before' in line.strip():
                before = [int(i) for i in re.search(rx_reg, line).groups()]
            elif 'After' in line.strip():
                after = [int(i) for i in re.search(rx_reg, line).groups()]
            else:
                statement = [int(i) for i in re.search(
                    r'(\d+)\s(\d+)\s(\d+)\s(\d+)', line
                ).groups()]


def solve(inp_arr):
    total = 0
    for sample in inp_arr:
        if len(count_match(
            sample['before'], sample['after'], sample['statement']
        )) >= 3:
            total += 1
    return total


if __name__ == '__main__':
    # Test
    before = [3, 2, 1, 1]
    after = [3, 2, 2, 1]
    statement = [9, 2, 1, 2]
    parsed = parse_samples('./example-input.txt')
    assert len(count_match(before, after, statement)) == 4
    assert parsed == [{'before': [2, 3, 0, 3],
                       'statement': [11, 2, 0, 2],
                       'after': [2, 3, 1, 3]},
                      {'before': [1, 2, 0, 0],
                       'statement': [3, 0, 3, 0],
                       'after': [1, 2, 0, 0]},
                      {'before': [0, 2, 3, 3],
                       'statement': [1, 3, 2, 0],
                       'after': [1, 2, 3, 3]}]
    assert solve(parsed) == 2
    print('All tests passed!')

    # Solution
    parse_soln = parse_samples('./day16-input.txt')
    print(solve(parse_soln))
