# Day 20 - Part 1
# What is the largest number of doors you would be required to pass thru to
# reach a room? Find the room for which the shortest path from start to room
# requires passing through the most doors.


def id(current, to):
    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    return tuple(sum(p) for p in zip(current, dirs[to]))


def create_graph(inp, graph):
    graph = {}
    start = (0, 0)

    for i in inp:
        if i in 'ESNW':
            pass


class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


# Tests
simple = {
    'regex': '^WNE$',
    'map': """\
#####
#.|.#
#-###
#.|X#
#####
""",
    'doors': 3
}
