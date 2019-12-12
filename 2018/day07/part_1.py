# Day 7 - Puzzle 1
# In what order should the steps in your instructions be completed?


import collections
import re
import heapq


# Using a modified Kahn's algorithm for topological sorting
# The min-heap will lexicographically insert items with priority:
# 'A' > 'H' > 'Z'
def tops(input_arr):
    G, indegree = _generate_graph(input_arr)
    visited = collections.defaultdict(bool)
    Q = []
    tops = ''

    for node, degree in indegree.items():
        if degree == 0:
            heapq.heappush(Q, node)

    while len(Q) > 0:
        vert = heapq.heappop(Q)

        if vert in visited:
            continue

        visited[vert] = True
        tops += vert

        neighbors = G[vert]
        for n in neighbors:
            indegree[n] -= 1
            if indegree[n] == 0:
                heapq.heappush(Q, n)

    return tops


def _generate_graph(input_arr):
    G = collections.defaultdict(list)
    indegree = collections.defaultdict(int)

    for inp in input_arr:
        head, tail = re.search(
            r'^Step\s([A-Z]+).*step\s([A-Z]+).*',
            inp
        ).groups()
        G[head].append(tail)

        indegree[tail] += 1

        if tail not in G:
            G[tail] = []

        if head not in indegree:
            indegree[head] = 0

    return G, indegree


TEST_INPUT = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]
if __name__ == '__main__':
    # Tests
    G, ind = _generate_graph(TEST_INPUT)
    assert(G == {
        'C': ['A', 'F'],
        'A': ['B', 'D'],
        'F': ['E'],
        'B': ['E'],
        'D': ['E'],
        'E': []
    })
    assert(ind == {'C': 0, 'A': 1, 'F': 1, 'B': 1, 'D': 1, 'E': 3})
    assert(tops(TEST_INPUT) == 'CABDFE')
    print('All tests passed!')

    with open('./day07-input.txt') as f:
        a = [l.rstrip() for l in f]
        print(tops(a))
