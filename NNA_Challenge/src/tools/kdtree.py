import pprint
import numpy as np
import pandas as pd
import NNA_Challenge

class Node:
    '''Node class for LeafyKDTree. Repr returns the axis and splitting value.'''
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.data = value
        self.right = right

    def __repr__(self):
        return str(self.data)

    def branches(self):
        '''returns tuple of (self.left, self.right) sub trees'''
        return self.left, self.right
        

class LeafyKDTree:
    '''KDTree where data is stored in leaves of the tree. Sub branches 
    are generated purely as a function of the splitting axis.'''
    def __init__(self, points, **kwargs):
        self.n_dim = len(points[0][1])
        self.n_points = len(points)
        self.points = points
        self.kwargs = kwargs
        self.tree = self.build_tree(self.points)

    def build_tree(self, points, depth=0):
        '''recursively build tree from data points. Returns nested Nodes'''

        n = len(points)

        if n > 1:
            axis = NNA_Challenge.src.tools.cython.calculate.get_axis(
                points, self.n_dim, depth, method=self.kwargs['method']
            )

            sorted_points = sorted(points, key=lambda point: point[1][axis])
            divisor = n // 2

            return Node(
                ({'axis': axis, 'divisor': sorted_points[divisor][1][axis]}), 
                left=self.build_tree(sorted_points[:divisor], depth + 1),
                right=self.build_tree(sorted_points[divisor:], depth + 1)
            )

        else: return points

    def query_radius(self, radius):
        '''traverses KDTree w/r to each point, returns points within radius'''
        res = dict()
        for point in self.points:
            res[point[0]] = find_points(self.tree, point, radius)

        return res


def find_points(
        tree, point, radius, depth=0
    ):
    '''recursive function which traverses the tree; if the radial
    bounds around a point for a given axis are contained by a subtree, use that
    subtree. If tree bisects radial points, flatten remainder of tree and 
    analyze via brute force'''

    # if we get to end of tree, then no points 
    # are within radius and return an empty list
    if isinstance(tree, Node) is False:
        return []

    # radial bounds along axis
    condition_1 = point[1][tree.data['axis']] - radius <= tree.data['divisor']
    condition_2 = point[1][tree.data['axis']] + radius <= tree.data['divisor']

    # if both radial bounds are below splitting axis, use left branch
    if condition_1 and condition_2:
        next_branch = tree.left

    # if radial bound bisect splitting axis, 
    # flatten tree and use smaller set in brute force calculation
    elif condition_1 or condition_2:
        return NNA_Challenge.src.tools.cython.calculate.calculate(
            strip_tree(tree), point, radius
        )

    # if both radial bounds are above splitting axis, use right branch
    else:
        next_branch = tree.right

    # recursively apply function to traverse tree
    return find_points(next_branch, point, radius, depth=depth+1)

def strip_tree(tree):
    '''takes tree and flattens the data structure into a list of (label, point) 
    tuples'''
    
    # recursively traverse tree grabbing all leaves 
    # and appending them to results list
    if isinstance(tree, Node) is True:
        res = []
        for sub in tree.branches():
            res += strip_tree(sub)
        return res
    
    # leafy tree always ends in list, so return said list when encountered
    else: return tree
