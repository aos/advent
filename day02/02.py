# Day 2 - Puzzle 2
# What letters are common between the two correct (diff by 1 char) IDs

ALL_IDS = []

with open('./day02-input.txt') as f:
    for line in f:
        ALL_IDS.append(line.strip())


def get_correct(arr):
    common = ''
    box_id_1 = ''
    box_id_2 = ''

    for i_1, s_1 in enumerate(arr):
        for i_2, s_2 in enumerate(arr):
            diff = 0
            # Skip the same word
            if i_1 == i_2:
                continue

            for j, _ in enumerate(s_1):
                if s_1[j] != s_2[j]:
                    diff += 1

                if diff > 1:
                    break

            if diff == 1 and not (box_id_1 and box_id_2):
                box_id_1 = s_1
                box_id_2 = s_2

    for i, char in enumerate(box_id_1):
        if box_id_1[i] == box_id_2[i]:
            common += char

    return common


def corr_two(arr):
    d = set()
    for s in arr:
        for i in range(len(s)):
            new_str = s[:i] + '_' + s[i+1:]
            if new_str in d:
                result = ''.join([n for n in new_str if n != '_'])
                return result
            d.add(new_str)


print(corr_two(ALL_IDS))

# Test example
tests = [
    'abcde',
    'fghij',  # This one
    'klmno',
    'pqrst',
    'fguij',  # and this one
    'axcye',
    'wvxyz'
]

assert(get_correct(tests) == 'fgij')
