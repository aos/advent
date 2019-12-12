# Day 5 - Puzzle 1
# How many units remain after fully reacting the polymer?


# The ugly solution (slicing the array everytime a match happens)
# Run through string, for each match: slice out the match
# Runtime: O(StringLength^2 * Number of matches)
def alchemy(string):
    i = 0

    while i < len(string):
        first = string[i]
        try:
            second = string[i+1]
            if abs(ord(first) - ord(second)) == 32:
                string = string[0:i] + string[i+2:]
                i -= 1
                if i == -1:
                    i = 0
                continue
        except IndexError:
            pass
        i += 1

    return len(string)


# The smart solution -- using a stack to keep track
# Drops the runtime to O(n)
def alch_stack(string):
    stack = []
    for c in string:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)

    return len(stack)


if __name__ == '__main__':
    with open('./day05-input.txt') as f:
        print(alch_stack((f.read().rstrip())))

    test_input = 'dabAcCaCBAcCcaDA'
    test_input_two = 'dDabAcCaCBAcCcaDA'
    assert(alchemy(test_input) == 10)
    assert(alchemy(test_input_two) == 9)
    assert(alch_stack(test_input) == 10)
    assert(alch_stack(test_input_two) == 9)
    print('All tests passed!')
