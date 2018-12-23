# Day 15 - Puzzle 1
# Find number of full rounds completed
# Find sum of hitpoints of all remaining units
# Outcome = rounds * sum_hp

# Notes:
# Calculate manhattan distance to target
# Phases:
# 1. Move
#   - Consider squares in range (immediately adjacent to target) and reachable
#   - Picks one by reading order if tie
# 2. Attack
#   - Determine all targets that are in range (immediately adjacent)
#       - if none, end turn
#   - Picks target with fewest hit points -> deals damage equal to attack power


from pprint import pprint
from heapq import heappush, heappop


def add_pts(pt1, pt2):
    return tuple(sum(item) for item in zip(pt1, pt2))


def m_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def bfs(source, targets, m):
    reachable = []

    for i in targets:
        dists = [0]
        q = [source]
        visited = set()
        d = -1

        while q:
            nxt = q.pop(0)
            dist = dists.pop(0)
            if nxt == i:
                reachable.append((dist, nxt))
                continue
            visited.add(nxt)
            d += 1
            for neighbor in neighbors(nxt):
                if (
                    neighbor not in visited and
                    m[neighbor[1]][neighbor[0]] == '.' and
                    neighbor not in q
                ):
                    q.append(neighbor)
                    dists.append(d+dist)

    return sorted(reachable, key=lambda p: (p[0], p[1][1], p[1][0]))


def neighbors(pt):
    U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)
    return sorted(
        [add_pts(a, pt) for a in (U, D, L, R)],
        key=lambda p: (p[1], p[0])
    )


class Unit:
    def __init__(self, u_type, x, y, hp=200, ap=3):
        self.u_type = u_type
        self.x = x
        self.y = y
        self.hp = hp
        self.ap = ap
        self.alive = True

    def __str__(self):
        return f'{self.u_type}'

    def __repr__(self):
        return f'{self.u_type}({self.hp})'

    def step(self, new_x, new_y, m):
        m[self.y][self.x] = '.'
        self.x = new_x
        self.y = new_y
        m[self.y][self.x] = self
        return new_x, new_y

    def adj_sqs(self):
        return neighbors((self.x, self.y))

    def adj_empty_sqs(self, m):
        return [(p[0], p[1]) for p in self.adj_sqs() if m[p[1]][p[0]] == '.']

    def find_enemies(self, sqs):
        return [u for u in sqs if (
            type(u) == Unit and
            u.u_type != self.u_type and
            u.alive
        )]

    def get_attacked(self, ap):
        self.hp -= ap
        if self.hp <= 0:
            self.alive = False
            return True
        return False


class Map:
    def __init__(self, file):
        self.units = []
        self.map = []

        with open(file) as f:
            for y, line in enumerate(f):
                line = line.strip()
                self.map.append([None] * len(line))
                for x, c in enumerate(line):
                    if c in 'EG':
                        u = Unit(c, x, y)
                        self.units.append(u)
                        self.map[y][x] = u
                    elif c == '#':
                        self.map[y][x] = '#'
                    else:
                        self.map[y][x] = '.'

    def print(self):
        print('\n'.join(''.join(str(u) for u in row) for row in self.map))

    def rounds(self):
        rnd = 0

        while True:
            # Queue unit action
            self.units = sorted(self._clean_units(), key=lambda u: (u.y, u.x))
            for unit in self.units:
                if not unit.alive:
                    continue

                if not unit.find_enemies(self.units):
                    return rnd * sum(map(lambda u: u.hp, self.units))

                # Check for adjacent enemies and attack if one
                if self._check_enemies_attack(unit):
                    self.units = self._clean_units()
                    continue

                # Otherwise move
                all_e = unit.find_enemies(self.units)
                in_range = []
                for e in all_e:
                    in_range.extend(e.adj_empty_sqs(self.map))
                nearest = self._find_nearest(unit, in_range)
                if nearest:
                    all_bfs = bfs(
                        nearest[0][1],
                        unit.adj_empty_sqs(self.map),
                        self.map
                    )
                    n_x, n_y = all_bfs[0][1]
                    unit.step(n_x, n_y, self.map)

                self._check_enemies_attack(unit)
                self.units = self._clean_units()

            rnd += 1
            #print('Round:', rnd)
            #self.print()
            #print()
            #print()
            #print('\n'.join([repr(u) for u in self.units]))

    def _get_map_sqs(self, sqs):
        return [self.map[s[1]][s[0]] for s in sqs]

    def _check_enemies_attack(self, unit):
        adjacent_enemies = sorted(
            unit.find_enemies(self._get_map_sqs(unit.adj_sqs())),
            key=lambda u: (u.hp, u.y, u.x)
        )
        if adjacent_enemies:
            curr_enemy = adjacent_enemies[0]
            if curr_enemy.get_attacked(unit.ap):
                self.map[curr_enemy.y][curr_enemy.x] = '.'
            return True

        return False

    def _find_nearest(self, unit, sqs_in_range):
        return bfs((unit.x, unit.y), sqs_in_range, self.map)

    def _clean_units(self):
        return [u for u in self.units if u.alive]


# Tests
ex1 = Map('./examples/example1-input.txt')
ex2 = Map('./examples/example2-input.txt')
ex3 = Map('./examples/example3-input.txt')
ex4 = Map('./examples/example4-input.txt')
ex5 = Map('./examples/example5-input.txt')
ex6 = Map('./examples/example6-input.txt')
ex7 = Map('./examples/corner-case1.txt')
ex8 = Map('./examples/corner-case2.txt')
ex9 = Map('./examples/example-big.txt')
assert ex1.rounds() == 27730
assert ex2.rounds() == 36334
assert ex3.rounds() == 39514
assert ex4.rounds() == 27755
assert ex5.rounds() == 28944
assert ex6.rounds() == 18740
assert ex7.rounds() == 13400
assert ex8.rounds() == 13987
print('All tests passed!')

# Solution
soln = Map('./day15-input.txt')
print(soln.rounds())
