# Day 15 - Puzzle 2

from part_1 import Unit, bfs


class Map:
    def __init__(self, file, e_ap=3):
        self.units = []
        self.map = []

        with open(file) as f:
            for y, line in enumerate(f):
                line = line.strip()
                self.map.append([None] * len(line))
                for x, c in enumerate(line):
                    if c in 'EG':
                        ea = e_ap if c == 'E' else 3
                        u = Unit(c, x, y, ap=ea)
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

                if not unit.find_enemies(self.units):
                    return rnd * sum(map(lambda u: u.hp, self.units))

            rnd += 1

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
                if curr_enemy.u_type == 'E':
                    raise Exception
                self.map[curr_enemy.y][curr_enemy.x] = '.'
            return True

        return False

    def _find_nearest(self, unit, sqs_in_range):
        return bfs((unit.x, unit.y), sqs_in_range, self.map)

    def _clean_units(self):
        return [u for u in self.units if u.alive]


# Tests
ex1 = Map('./examples/example1-input.txt', e_ap=15)
ex3 = Map('./examples/example3-input.txt', e_ap=4)
ex4 = Map('./examples/example4-input.txt', e_ap=15)
ex5 = Map('./examples/example5-input.txt', e_ap=12)
ex6 = Map('./examples/example6-input.txt', e_ap=34)
assert ex1.rounds() == 4988
assert ex3.rounds() == 31284
assert ex4.rounds() == 3478
assert ex5.rounds() == 6474
assert ex6.rounds() == 1140
print('All tests passed!')

# Solution
start = 4
while True:
    soln = Map('./day15-input.txt', e_ap=start)
    try:
        final = soln.rounds()
        print(final)
        break
    except Exception:
        print('Current attack power:', start)
        start += 1
