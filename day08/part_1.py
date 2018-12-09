# Day 8 - Puzzle 1
# What is the sum of all metadata entries


class Node:
    def __init__(self, num_child, num_meta):
        self.header = (num_child, num_meta)
        self.children = [None] * num_child
        self.metadata = [None] * num_meta

    def __repr__(self):
        return '<header:{} | children:{} | metadata: {}>'.format(self.header,
                                                                 self.children,
                                                                 self.metadata)


def metadata(inp):
    root, _ = _generate_tree(inp)
    return _get_sum(root)


def _get_sum(node):
    if len(node.children) == 0:
        return sum(node.metadata)

    s = sum(node.metadata)

    for n in node.children:
        s += _get_sum(n)

    return s


def _generate_tree(inp_arr, index=0):
    num_child, num_meta = inp_arr[index:index + 2]
    node = Node(num_child, num_meta)
    lh = len(node.header)

    if num_child == 0:
        node.metadata = inp_arr[(index + lh):(index + lh + num_meta)]
        return node, index + lh + num_meta

    index = index + lh
    for i in range(num_child):
        node.children[i], index = _generate_tree(inp_arr, index)

    node.metadata = inp_arr[index:index + num_meta]
    return node, index + num_meta


TEST_INPUT = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
TEST_INPUT_ARR = [int(i) for i in TEST_INPUT.split()]

if __name__ == '__main__':
    assert(metadata(TEST_INPUT_ARR) == 138)
    print('All tests passed!')

    with open('./day08-input.txt') as f:
        to_arr = [int(i) for i in f.read().rstrip().split()]
        print(metadata(to_arr))
