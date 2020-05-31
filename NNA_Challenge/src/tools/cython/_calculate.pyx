import numpy as np

cpdef calculate(tree, point, radius):
    '''determine which points in flat tree are within radius, append results
    which pass check to list and return list when done'''

    flat_tree = strip_tree(tree)

    res = []

    cdef int n = len(flat_tree)
    cdef int i

    for i in range(n):
        item = flat_tree[i]
        d = sq_dist(point[1], item[1])
        if (d <= radius**2) and (d > 0):
            res.append(item[0])

    return res


cpdef sq_dist(p0, p1):
    '''calculate the square distance between two n_dim points as sum of 
    squares'''
    return sum([(x[0]-x[1])**2 for x in zip(p0, p1)])


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

cpdef get_axis(points, n_dim, depth, method):
    '''picks splitting axis as the axis with the highest variance. This can be
    changed to iterate through dimensions sequentially through 
    kwargs['axis'] = 'uniform'
    '''

    if method == 'uniform':
        return depth % n_dim

    else:
        axis = (None, -1)
        for i in range(n_dim):
            variance = np.var([a[1][i] for a in points])
            if variance > axis[1]:
                axis = (i, variance)

        return axis[0]