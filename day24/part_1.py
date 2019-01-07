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


class Group:
    def __init__(self, army, units, hp, att_dmg, att_type, init, weak, imms):
        self.army = army
        self.num_units = units
        self.hp = hp
        self.att_dmg = att_dmg
        self.att_type = att_type
        self.init = init
        self.weaks = weak
        self.imms = imms
        self.ep = units * att_dmg
        self.alive = True
