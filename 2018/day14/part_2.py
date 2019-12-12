# Day 14 - Puzzle 2
# How many recipes appear on the scoreboard to the left of the score sequence
# in your puzzle input?


def recipes(it):
    elves = [0, 1]
    sb = [3, 7]
    digits = list(map(int, str(it)))

    while True:
        # Create new recipe
        new = sb[elves[0]] + sb[elves[1]]
        sb.extend([int(i) for i in str(new)])

        for i, n in enumerate(elves):
            elves[i] = (n + 1 + sb[n]) % len(sb)

        if sb[-len(digits)-1:-1] == digits:
            return len(sb) - len(digits) - 1
        if sb[-len(digits):] == digits:
            return len(sb) - len(digits)


# Tests
assert(recipes('51589') == 9)
assert(recipes('01245') == 5)
assert(recipes('92510') == 18)
assert(recipes('59414') == 2018)
print('All tests passed!')

# Solution
print(recipes('846021'))
