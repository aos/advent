# Day 24 - Part 1
# How many units would the winning army have?

# Target selection:
# 1. Effective power
#   Tie-breakers:
#   -> Initiative
# Target: group to deal most damage (+ weaknesses and immunities)
#   Tie-breakers:
#   -> Largest effective power
#   -> Highest initiative
# If no damage - no target
# Only 1 choice

# Attacking phase:
# 1. Attack in decreasing order of initiative
# Immune: no damage, weak: double damage
# Only _whole_ units are lost
# Ex. 10 units x 10 hp each -> take 75 dmg -> 7 units lost
# Repeat combat until 1 army remaining


import re
from math import ceil
from copy import deepcopy


class Group:
    def __init__(self, a_type, units, hp, att_dmg, att_type, init, weak, imms):
        self.a_type = a_type
        self.num_units = units
        self.hp = hp
        self.att_dmg = att_dmg
        self.att_type = att_type
        self.init = init
        self.weaks = weak
        self.imms = imms
        self.ep = units * att_dmg
        self.target_to_attack = None
        self.targeted = False
        self.alive = True

    def calc_dmg_taken(self, enemy_dmg, enemy_dmg_type):
        if enemy_dmg_type in self.weaks:
            enemy_dmg *= 2
        elif enemy_dmg_type in self.imms:
            enemy_dmg = 0

        return enemy_dmg

    def take_dmg_from(self, group):
        dmg = self.calc_dmg_taken(group.ep, group.att_type)
        total_hp_remaining = (self.num_units * self.hp) - dmg
        self.num_units = ceil(total_hp_remaining / self.hp)
        self.ep = self.num_units * self.att_dmg
        if self.num_units <= 0:
            self.alive = False
            self.ep = 0
        return self.num_units

    def __repr__(self):
        return ('Group({}, Units: {}, HP: {}, DMG: {}, D_type: {}, Init: {}, '
                'Weakness: {}, Immune: {}, EP: {}, {})').format(
            self.a_type, self.num_units, self.hp, self.att_dmg, self.att_type,
            self.init, self.weaks, self.imms, self.ep, self.alive
        )

    def __str__(self):
        return f'Group({self.a_type}, {self.num_units})'


def parse_input(file):
    a_type = None
    groups = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if 'Immune' in line:
                a_type = 0
                continue
            if 'Infection' in line:
                a_type = 1
                continue

            num_units, hp, dmg, init = list(map(int, re.findall(r'\d+', line)))
            weaks = re.search(r'(?<=weak to ).[^;\)]*', line) or []
            imms = re.search(r'(?<=immune to ).[^;\)]*', line) or []
            att_type = re.search(r'(\w+)(?= damage)', line).group(0)

            if weaks:
                weaks = [x.strip() for x in re.search(
                    r'(?<=weak to ).[^;\)]*', line
                ).group(0).split(',')]
            if imms:
                imms = [x.strip() for x in re.search(
                    r'(?<=immune to ).[^;\)]*', line
                ).group(0).split(',')]

            groups.append(
                Group(a_type, num_units, hp, dmg, att_type, init, weaks, imms)
            )

    return groups


def reset_round(gs):
    groups_alive = [g for g in gs if g.alive]
    for g in groups_alive:
        g.targeted = False
        g.target_to_attack = None
    return groups_alive


def filter_enemies(group, rest):
    return [e for e in rest if (
        e.a_type != group.a_type and
        not e.targeted and
        e.calc_dmg_taken(group.ep, group.att_type) != 0
    )]


def groups_left(gs):
    return set(g.a_type for g in gs)


def check_win_first(gl):
    return len(gl) == 1


def check_win_second(gl):
    return 0 in gl and len(gl) == 1


def boost_immunity(gs, num):
    for g in gs:
        if g.a_type == 0:
            g.att_dmg += num
            g.ep = g.num_units * g.att_dmg
    return gs


def fight(gs):
    new_groups = reset_round(gs)
    # 1. Target selection
    # Sort on effective power, tie-breaker initiative
    new_groups.sort(key=lambda g: (g.ep, g.init), reverse=True)
    for group in new_groups:
        enemies = filter_enemies(group, new_groups)
        if enemies:
            enemies_to_attack = sorted(
                enemies,
                key=lambda e: e.calc_dmg_taken(group.ep, group.att_type),
                reverse=True
            )
            group.target_to_attack = enemies_to_attack[0]
            enemies_to_attack[0].targeted = True

    # 2. Attacking
    # Sort by initiative
    new_groups.sort(key=lambda g: g.init, reverse=True)
    for group in new_groups:
        if group.target_to_attack:
            group.target_to_attack.take_dmg_from(group)

    return new_groups


# Tests
groups = parse_input('./example-input.txt')
groups_left_test = groups_left(groups)
while not check_win_first(groups_left_test):
    groups = fight(groups)
    groups_left_test = groups_left(groups)
assert sum(g.num_units for g in groups) == 5216
print('All tests passed!')

# Solution -- part 1
groups_input = parse_input('./day24-input.txt')
groups_left_one = groups_left(groups_input)
while not check_win_first(groups_left_one):
    groups_input = fight(groups_input)
    groups_left_one = groups_left(groups_input)
print(sum(g.num_units for g in groups_input))

# Solution -- part 2
groups_two = parse_input('./day24-input.txt')
groups_left_two = groups_left(groups_two)
boost = 0
while not check_win_second(groups_left_two):
    rnds = 0
    boost += 1
    groups_two_boosted = boost_immunity(deepcopy(groups_two), boost)
    groups_left_two = groups_left(groups_two_boosted)

    while not check_win_first(groups_left_two):
        if rnds >= 10000:
            break
        groups_two_boosted = fight(groups_two_boosted)
        groups_left_two = groups_left(groups_two_boosted)
        rnds += 1
print(sum(g.num_units for g in groups_two_boosted))
