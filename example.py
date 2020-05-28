from os import path
import NNA_challenge
import numpy as np
import time
import sys

here = path.abspath(path.dirname(__file__))

radius = 3000000

kwargs = {
    'method': 'KDTree',
    'axis': 'variance',
    'BFM': 'np',
    'output': 'print',
    'timeit': 'False'
}

input_file = path.join(here, 'test_input.txt')

input_class = NNA_challenge.src.parse_input.ParseInput(input_file)

data = input_class.parse_constraints()

t1 = time.time()
tree = NNA_challenge.src.tools.kdtree.LeafyKDTree(data, **kwargs).query_radius(radius)
t2 = time.time()

print(t2-t1)

# brute = NNA_challenge.src.tools.brute.BruteForce(data).query_radius(radius, kwargs['BFM'])
# t3 = time.time()

# NNA_challenge.src.tools.output.output(tree, **kwargs)
# NNA_challenge.src.tools.output.output(brute, **kwargs)