from os import path
import NNA_Challenge
import numpy as np
import time
import sys

here = path.abspath(path.dirname(__file__))

radius = 3000000

kwargs = {
    'method': 'KDTree',
    'axis': 'variance',
    'BFM': 'np',
    'output': 'return',
    'timeit': 'False'
}

input_file = path.join(here, 'test_input.txt')

input_class = NNA_Challenge.src.parse_input.ParseInput(input_file)

data = input_class.parse_constraints()

t1 = time.time()
tree = NNA_Challenge.src.tools.kdtree.LeafyKDTree(data, **kwargs).query_radius(radius)
t2 = time.time()
brute = NNA_Challenge.src.tools.brute.BruteForce(data, **kwargs).query_radius(radius)
t3 = time.time()

NNA_Challenge.src.tools.output.output(tree, **kwargs)
NNA_Challenge.src.tools.output.output(brute, **kwargs)