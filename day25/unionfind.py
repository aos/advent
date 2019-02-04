class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0

    def __repr__(self):
        return f'Node({self.data})'


class UnionFind:
    def __init__(self, pts):
        self.node_map = {}
        self.num_sets = len(pts)

        for i in pts:
            self.__make_set(i)

    def find(self, item):
        if item not in self.node_map:
            return False
        node = self.node_map[item]

        traversed = []
        while node.parent != node:
            traversed.append(node)
            node = node.parent

        return self.__compress(traversed, node)

    def union(self, first, second):
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        if root_first.rank > root_second.rank:
            self.node_map[root_second.data].parent = \
                self.node_map[second].parent = root_first
        elif root_second.rank > root_first.rank:
            self.node_map[root_first.data].parent = \
                self.node_map[first].parent = root_second
        else:
            self.node_map[root_second.data].parent = \
                self.node_map[second].parent = root_first
            root_first.rank += 1

        self.num_sets -= 1
        return True

    def __make_set(self, item):
        if item in self.node_map:
            return False
        self.node_map[item] = Node(item)
        return item

    # Path compression
    def __compress(self, traversed, root):
        for node in traversed:
            node.parent = root
        return root
