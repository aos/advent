# Day 7 - Puzzle 2
# How long will it take to complete all of the steps?
# 5 workers, 60+ seconds


import collections
from queue import Queue
from threading import Thread
from time import sleep
from timeit import default_timer as timer
from math import floor
from string import ascii_uppercase
from part_1 import _generate_graph, TEST_INPUT


def times(input_arr, workers):
    Q = Queue(maxsize=0)
    G, indegree = _generate_graph(input_arr)
    visited = collections.defaultdict(bool)

    # Worker
    def _do_work(q):
        while True:
            item = q.get()

            if item in visited:
                continue

            visited[item] = True
            sleep(TIME_CONTROL[item])

            neighbors = G[item]
            for n in neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.put(n)

            q.task_done()

    for i in range(workers):
        worker = Thread(target=_do_work, args=(Q,))
        worker.setDaemon(True)
        worker.start()

    for node, degree in indegree.items():
        if degree == 0:
            Q.put(node)

    Q.join()
    return True


# Tests
STEP_LENGTH = 0
TIME_CONTROL = {c: i + 1 + STEP_LENGTH for i, c in enumerate(ascii_uppercase)}
NUM_WORKERS = 2

start = timer()
times(TEST_INPUT, NUM_WORKERS)
end = timer()
assert(floor((end - start)) == 15)
print('All tests passed!')

# Solution
STEP_LENGTH = 60
NUM_WORKERS = 15
TIME_CONTROL = {c: i + 1 + STEP_LENGTH for i, c in enumerate(ascii_uppercase)}

with open('./day07-input.txt') as f:
    a = [l.rstrip() for l in f]
    start = timer()
    times(a, NUM_WORKERS)
    end = timer()
    print(floor((end - start)))
