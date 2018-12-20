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


class Unit:
    def __init__(self, u_type, start_x, start_y, hp=200, ap=3):
        self.u_type = u_type
        self.start_x = start_x
        self.start_y = start_y
        self.hp = hp
        self.ap = ap
