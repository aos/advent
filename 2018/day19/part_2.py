# Day 19 - Puzzle 2
# Use the value 1 in register 0

from part_1 import parse_file
import opcodes as opc  # noqa: F401


def solve(inp, first_reg):
    registers = [first_reg, 0, 0, 0, 0, 0]
    bound_reg = inp[0]
    ip = 0
    instructions = inp[1]

    while ip < len(instructions):
        # Reverse engineered it by pen and paper... but this is essentially
        # finding the factors of register 4
        n = registers[4]
        if ip == 2 and n != 0:
            return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

        # 1. Update bound register to current IP value
        registers[bound_reg] = ip
        # 2. Load instruction from IP location
        word, a, b, c = instructions[ip]
        # 3. Execute instruction
        registers = eval(f'opc.{word}({registers}, {a}, {b}, {c})')
        # 4. Set IP to value of bound register
        ip = registers[bound_reg]
        # 5. Add one to IP
        ip += 1

    return registers[0]


p = parse_file('./day19-input.txt')
print(solve(p, 1))
