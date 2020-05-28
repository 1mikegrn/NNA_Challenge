import pprint
import numpy as np
import pandas as pd

class LeafyKDTree():
    '''KDTree where data is stored in leaves of the tree. Sub branches 
    are generated purely as a function of the splitting axis.'''
    def __init__(self, points, **kwargs):
        self.n_dim = len(points[0])
        self.points = points
        self.kwargs = kwargs
        self.tree = self.build_tree(self.points)

    def build_tree(self, points, depth=0):
        '''recursively build tree from data points. Returns nested dictionary'''
        n = len(points)
        if n > 1:
            axis = get_axis(points, self.n_dim, depth, **self.kwargs)
            sorted_points = sorted(points, key=lambda point: point[1][axis])
            divisor = n // 2
            tree = {
                'H': {'axis': axis, 'divisor': sorted_points[divisor][1][axis]},
                'L': self.build_tree(sorted_points[:divisor], depth + 1),
                'R': self.build_tree(sorted_points[divisor:], depth + 1)
            }

            return tree

        else: return points

    def print_tree(self):
        '''pretty print tree'''
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(self.tree)

    def query_radius(self, radius):
        '''traverses KDTree w/r to each point, returns points within radius'''
        res = dict()
        for point in self.points:
            res[point[0]] = find_points(self.tree, point, radius)

        return res


def get_axis(points, n_dim, depth, **kwargs):
    '''picks splitting axis as the axis with the highest variance. This can be
    changed to iterate through dimensions sequentially through 
    kwargs['axis'] = 'uniform'
    '''

    if kwargs['method'] == 'uniform':
        return depth % n_dim

    else:
        axis = (None, -1)
        for i in range(n_dim):
            variance = np.var([a[1][i] for a in points])
            if variance > axis[1]:
                axis = (i, variance)

        return axis[0]


def find_points(
        tree, point, radius, depth=0
    ):
    '''recursive function which traverses the tree; if the radial
    bounds around a point for a given axis are contained by a subtree, use that
    subtree. If tree bisects radial points, flatten remainder of tree and 
    analyze via brute force'''
    # if we get to end of tree, then no points 
    # are within radius and return an empty list
    if isinstance(tree, list) is True:
        return []

    # radial bounds along axis
    condition_1 = point[1][tree['H']['axis']] - radius <= tree['H']['divisor']
    condition_2 = point[1][tree['H']['axis']] + radius <= tree['H']['divisor']

    # if both radial bounds are below splitting axis, use left branch
    if condition_1 and condition_2:
        next_branch = tree['L']

    # if radial bound bisect splitting axis, 
    # flatten tree and use smaller set in brute force calculation
    elif condition_1 or condition_2:
        return calculate(strip_tree(tree), point, radius)

    # if both radial bounds are above splitting axis, use right branch
    else:
        next_branch = tree['R']

    # recursively apply function to traverse tree
    return find_points(next_branch, point, radius, depth=depth+1)

def strip_tree(tree):
    '''takes tree, which is a nested dictionary, 
    and flattens the data structure into a list of (label, point) tuples'''
    
    # leafy tree always ends in list, so return said list when encountered
    if isinstance(tree, list) is True:
        return tree

    # recursively traverse tree grabbing all leaves 
    # and appending them to results list
    if isinstance(tree, dict) is True:
        res = []
        for key in tree.keys():
            if key != 'H':
                res += strip_tree(tree[key])
        return res

def sq_dist(p0, p1):
    '''calculate the square distance between two n_dim points as sum of 
    squares'''
    return sum([(x[0]-x[1])**2 for x in zip(p0, p1)])

def calculate(flat_tree, point, radius):
    '''determine which points in flat tree are within radius, append results
    which pass check to list and return list when done'''

    res = []
    for item in flat_tree:
        d = sq_dist(point[1], item[1])
        if (d <= radius**2) and (d > 0):
            res.append(item[0])

    return res

# pandas implementation, takes longer to build data structure and broadcast

# def calculate(flat_tree, point, radius):
#     '''determine which points in flat tree are within radius, append results
#     which pass check to list and return list when done'''

#     flat_tree=pd.DataFrame(
#         [x[1] for x in flat_tree], [x[0] for x in flat_tree]
#     )

#     flat_tree = np.sum((flat_tree - np.array(point[1]))**2, axis=1)
#     res = list(flat_tree[(flat_tree <= radius**2) & (flat_tree > 0)].index)

#     return res