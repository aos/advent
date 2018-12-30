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


def solve(inp):
    registers = [0] * 6
    bound_reg = inp[0]
    ip = 0
    instructions = inp[1]

    while True:
        # 1. Load instruction from IP location
        try:
            word, a, b, c = instructions[ip]
        except IndexError:
            return registers[0]
        # 2. Update bound register to current IP value
        registers[bound_reg] = ip
        # 3. Execute instruction
        registers = eval(f'opc.{word}({registers}, {a}, {b}, {c})')
        # 4. Set IP to value of bound register
        ip = registers[bound_reg]
        # 5. Add one to IP
        ip += 1

    return registers[0]


# Tests
test_line = 'addr 1 2 3'
p = parse_file('./example-input.txt')
assert parse_line(test_line) == ['addr', 1, 2, 3]
assert solve(p) == 6
print('All tests passed!')

# Solution
print(solve(parse_file('./day19-input.txt')))
