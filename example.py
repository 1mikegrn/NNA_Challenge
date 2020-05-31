from os import path
import NNA_Challenge
import numpy as np
import time
import sys
from scipy.special import gamma

from sklearn.neighbors import KDTree
import NNA_Challenge

here = path.abspath(path.dirname(__file__))

radius = 5000000

kwargs = {
    'method': 'KDTree',
    'axis': 'variance',
    'BFM': 'np',
    'output': 'print',
    'timeit': 'False'
}

input_file = path.join(here, 'test_input.txt')

input_class = NNA_Challenge.src.parse_input.ParseInput(input_file)

data = input_class.parse_constraints()
points = input_class.parse_to_df().values


t1 = time.time()
tree = NNA_Challenge.src.tools.kdtree.LeafyKDTree(data, **kwargs).query_radius(radius)
t2 = time.time()
brute = NNA_Challenge.src.tools.brute.BruteForce(data, **kwargs).query_radius(radius)
t3 = time.time()

# vol = input_class.apx_volume()

# print(
#     ((np.pi**(input_class.n_dim/2)/gamma((input_class.n_dim/2)+1))
#     *radius**input_class.n_dim/vol)
# )

# print(
#     (tree.n_points/vol)
# )

# kwargs['BFM'] = 'py'
# #brutepy = NNA_Challenge.src.tools.brute.BruteForce(data, **kwargs).query_radius(radius)
# t4 = time.time()
# skl = KDTree(points).query_radius(points, r=radius)
# t5 = time.time()


NNA_Challenge.src.tools.output.output(tree, **kwargs)
NNA_Challenge.src.tools.output.output(brute, **kwargs)

print("myKDTree "+str(t2-t1))
print("myNpBrute: "+str(t3-t2))

# print('\n')
# print("PyBrute: " +str(t4-t3))
# print("sklearn: "+str(t5-t4))