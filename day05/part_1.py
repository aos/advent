# Day 5 - Puzzle 1
# How many units remain after fully reacting the polymer?


# The ugly solution (slicing the array everytime a match happens)
# Run through string, for each match: slice out the match
# Runtime: O(StringLength^2 * Number of matches)
def alchemy(string):
    i = 0
    to_arr = [c for c in string]

    while i < len(to_arr):
        first = to_arr[i]
        try:
            second = to_arr[i+1]
            if abs(ord(first) - ord(second)) == 32:
                to_arr = to_arr[0:i] + to_arr[i+2:]
                i -= 1
                if i == -1:
                    i = 0
                continue
        except IndexError:
            pass
        i += 1

    return len(to_arr)


if __name__ == '__main__':
    with open('./day05-input.txt') as f:
        print(alchemy((f.read().rstrip())))

    test_input = 'dabAcCaCBAcCcaDA'
    test_input_two = 'dDabAcCaCBAcCcaDA'
    assert(alchemy(test_input) == 10)
    assert(alchemy(test_input_two) == 9)
    print('All tests passed!')
