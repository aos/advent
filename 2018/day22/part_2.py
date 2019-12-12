# Day 22 - Part 2
# What is the fewest # of minutes you can take to reach the target?


from heapq import heappush, heappop
from part_1 import cave_system


def rescue(start, end, max_x, max_y, cave):
    # Queue up the start point along with the starting tool (torch)
    heap = [(0, start, 1)]
    distance = {(start, 1): 0}

    while heap:
        time, current, tool = heappop(heap)
        nbs = neighbors(current, max_x, max_y)

        if current == end:
            if tool == 1:
                return time
            else:
                return time + 7

        if distance[(current, tool)] < time:
            continue

        for nxt in nbs:
            allowed_tools = tools(cave[nxt[1]][nxt[0]])
            current_tools = tools(cave[current[1]][current[0]])

            # Check to see if our current tool is allowed in the next region
            # If not, add time to switch + make sure we switch to a tool that's
            # allowed in current region and next region
            if tool in allowed_tools:
                new_tool = tool
                new_time = time + 1
            else:
                new_time = time + 8
                current_tools.remove(tool)
                new_tool = current_tools[0]

            if new_time < distance.get((nxt, new_tool), float('inf')):
                heappush(heap, (new_time, nxt, new_tool))
                distance[(nxt, new_tool)] = new_time


def neighbors(current, max_x, max_y):
    U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)
    return list(filter(
        lambda p: (
            p[0] >= 0 and
            p[0] <= max_x and
            p[1] >= 0 and
            p[1] <= max_y),
        [tuple(sum(a) for a in zip(current, d)) for d in (U, D, L, R)]))


def tools(r_type):
    """
    Tools:
        None: 0
        Torch: 1
        Climbing gear: 2
    Region type:
        Rocky: 0
        Wet: 1
        Narrow: 2
    """
    if r_type == 0:
        return [1, 2]
    elif r_type == 1:
        return [0, 2]
    else:
        return [0, 1]


# Tests
assert neighbors((1, 0), 10, 10) == [(1, 1), (0, 0), (2, 0)]
assert tools(1) == [0, 2]

test_depth = 510
test_target = (10, 10)
cave = cave_system(test_target, test_depth, 100, 100)[1]
shortest = rescue((0, 0), test_target, 100, 100, cave)
assert shortest == 45
print('All tests passed!')

with open('./day22-input.txt') as f:
    depth, target = [line.rstrip().split(': ')[1] for line in f.readlines()]
    target = tuple(int(c) for c in target.split(','))
    soln_cave = cave_system(target, int(depth), target[0]*8, target[1]*8)[1]
    print(rescue((0, 0), target, target[0]*8, target[1]*8, soln_cave))
