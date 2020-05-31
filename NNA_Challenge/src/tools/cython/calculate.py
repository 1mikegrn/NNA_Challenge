import numpy as np

def calculate(flat_tree, point, radius):
    '''determine which points in flat tree are within radius, append results
    which pass check to list and return list when done'''

    n = len(flat_tree)
    res = np.empty(n, dtype=object)

    for i in range(n):
        item = flat_tree[i]
        d = sq_dist(point[1], item[1])
        if (d <= radius**2) and (d > 0):
            res[i] = item[0]
    return res[res!=None]


def sq_dist(p0, p1):
    '''calculate the square distance between two n_dim points as sum of 
    squares'''
    return sum([(x[0]-x[1])**2 for x in zip(p0, p1)])


def get_axis(points, n_dim, depth, method):
    '''picks splitting axis as the axis with the highest variance. This can be
    changed to iterate through dimensions sequentially through 
    method = 'uniform'
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