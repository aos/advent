# Day 16 - Puzzle 2
# What is the value of register 0 after executing the test program?

import re
from part_1 import count_match, parse_samples
import opcodes as opcs  # noqa: F401


def opcodes(samples):
    opc = [None for i in range(16)]

    for s in samples:
        c = list(filter(
            lambda x: x not in opc,
            count_match(s['before'], s['after'], s['statement'])))

        if len(c) == 1:
            # Opcode
            opc[s['statement'][0]] = c[0]

    return opc


def parse_prog(file):
    instructions = []
    part2 = False
    nxt = 0
    with open(file) as f:
        for index, line in enumerate(f):
            if part2:
                inst = [int(i) for i in re.search(
                    r'(\d*)\s(\d*)\s(\d*)\s(\d*)', line.strip()
                ).groups()]
                instructions.append(inst)
                continue

            if line == '\n':
                nxt += 1
                if nxt > 2:
                    part2 = True
            else:
                nxt = 0

    return instructions


def run_prog(instructions, opcodes):
    state = [0, 0, 0, 0]
    for instr in instructions:
        opc, A, B, C = instr
        state = eval(f"opcs.{opcodes[opc]}({state}, {A}, {B}, {C})")
    return state[0]


# Get instructions
parsed = parse_samples('./day16-input.txt')
ops = opcodes(parsed)

# Tests
test_parse = parse_prog('./example-input.txt')
assert test_parse == [[10, 0, 2, 3], [9, 1, 3, 2]]
assert run_prog(test_parse, ops) == 0
print('All tests passed!')

# Solution
instructions = parse_prog('./day16-input.txt')
print(run_prog(instructions, ops))
