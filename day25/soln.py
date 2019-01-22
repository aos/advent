# Day 25
# How many constellations are formed by the fixed points in spacetime?


import re
from sklearn.cluster import DBSCAN
import numpy as np


def parse_input(file):
    with open(file) as f:
        return [tuple(map(int, re.findall(r'-?\d+', line.strip())))
                for line in f.readlines()]


# Test
cluster_size = [None, 2, 4, 3, 8]
for i in range(1, 5):
    test_points = np.array(parse_input(f'./example{i}-input.txt'))
    labels = DBSCAN(eps=3, min_samples=1, algorithm='ball_tree',
                    metric='manhattan').fit(test_points).labels_
    num_clusters = len(set(labels))
    assert num_clusters == cluster_size[i]
print('All tests passed!')

# Solution
soln_pts = np.array(parse_input('./day25-input.txt'))
soln_labels = DBSCAN(eps=3, min_samples=1, algorithm='ball_tree',
                     metric='manhattan').fit(soln_pts).labels_
print(len(set(soln_labels)))
