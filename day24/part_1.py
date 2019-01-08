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
        self.alive = True

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


# Tests
p = parse_input('./example-input.txt')
