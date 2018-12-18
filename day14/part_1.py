# Day 14 - Puzzle 1
# What are the scores of the 10 recipes immmediately after the number of
# recipes in your puzzle input?


def recipes(it):
    elves = [0, 1]
    sb = [3, 7]

    while len(sb) < it + 10:
        # Create new recipe
        new = sb[elves[0]] + sb[elves[1]]
        sb.extend([int(i) for i in str(new)])

        for i, n in enumerate(elves):
            elves[i] = (n + 1 + sb[n]) % len(sb)

    return ''.join(map(str, sb[it:it+10]))


# Tests
assert(recipes(5) == '0124515891')
assert(recipes(9) == '5158916779')
assert(recipes(18) == '9251071085')
assert(recipes(2018) == '5941429882')

# Solution
print(recipes(846021))
