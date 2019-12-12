# Day 19 - Puzzle 1
# What value is left in register 0 when the background process halts?


import opcodes as opc  # noqa: F401


def parse_line(line):
    if '#' in line:
        return int(line[4])

    inst, a, b, c = line.split(' ')
    return [inst, int(a), int(b), int(c)]


def parse_file(file):
    inputs = []
    ip = None
    with open(file) as f:
        for line in f:
            ln = parse_line(line.strip())
            if type(ln) is int:
                ip = ln
            else:
                inputs.append(ln)
    return ip, inputs


def solve(inp, first_reg):
    registers = [first_reg, 0, 0, 0, 0, 0]
    bound_reg = inp[0]
    ip = 0
    instructions = inp[1]

    while ip < len(instructions):
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


if __name__ == '__main__':
    # Tests
    test_line = 'addr 1 2 3'
    p = parse_file('./example-input.txt')
    assert parse_line(test_line) == ['addr', 1, 2, 3]
    assert solve(p, 0) == 6
    print('All tests passed!')

    # Part 1
    ps = parse_file('./day19-input.txt')
    print(solve(ps, 0))
