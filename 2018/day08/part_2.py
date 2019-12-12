# Day 8 - Puzzle 2
# What is the value of the root node?


from part_1 import _generate_tree, TEST_INPUT_ARR


def memory(inp):
    root, _ = _generate_tree(inp)
    return _get_sum(root)


def _get_sum(node):
    if len(node.children) == 0:
        return sum(node.metadata)

    s = 0

    for n in node.metadata:
        if n <= len(node.children):
            s += _get_sum(node.children[n - 1])

    return s


assert(memory(TEST_INPUT_ARR) == 66)
print('All tests passed!')
with open('./day08-input.txt') as f:
    to_arr = [int(i) for i in f.read().rstrip().split()]
    print(memory(to_arr))
