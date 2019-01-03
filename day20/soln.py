# Day 20 - Part 1
# What is the largest number of doors you would be required to pass thru to
# reach a room? Find the room for which the shortest path from start to room
# requires passing through the most doors.

# NB. This problem was not phrased correctly. The current stack solution should
# NOT work in the general case.
from collections import defaultdict
from queue import Queue


def room_id(current, to):
    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    return tuple(sum(p) for p in zip(current, dirs[to]))


def create_graph(string):
    positions = []
    graph = defaultdict(set)
    start = prev = (0, 0)

    for c in string[1:-1]:
        if c == '(':
            positions.append(start)
        elif c == ')':
            start = positions.pop()
        elif c == '|':
            start = positions[-1]
        else:
            start = room_id(start, c)
            graph[prev].add(start)

        prev = start

    return graph


def longest_distance(graph):
    q = Queue()
    start = (0, 0)
    q.put(start)
    d = {}
    d[start] = 0

    while not q.empty():
        current = q.get()
        neighbors = graph[current]
        for nxt in neighbors:
            if nxt not in d:
                q.put(nxt)
                d[nxt] = 1 + d[current]

    return d.values()


# Tests
g1 = create_graph('^WNE$')
assert max(longest_distance(g1)) == 3
g2 = create_graph('^ENWWW(NEEE|SSE(EE|N))$')
assert max(longest_distance(g2)) == 10
g3 = create_graph('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$')
assert max(longest_distance(g3)) == 18
g4 = create_graph(
    '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'
)
assert max(longest_distance(g4)) == 31
print('All tests passed!')

# Part 1
g_soln = create_graph(open('./day20-input.txt').read().strip())
longest = longest_distance(g_soln)
print(max(longest))

# Part 2
print(len(list(filter(lambda x: x >= 1000, longest))))
