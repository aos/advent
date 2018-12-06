# Day 5 - Puzzle 2
# What is the length of the shortest polymer you can produce?


from part_1 import alch_stack
CHARS = [u for u in range(65, 91)]


def solve(file):
    string = ''
    with open(file) as f:
        string = f.read().rstrip()

    return min([alch_stack(
                string
                .replace(chr(i), '')
                .replace(chr(i + 32), '')) for i in CHARS])


print(solve('./day05-input.txt'))

# Test
test_input = 'dabAcCaCBAcCcaDA'
res = min([alch_stack(
            test_input
            .replace(chr(i), '')
            .replace(chr(i + 32), '')) for i in CHARS])
assert(res == 4)
print('All tests passed!')
