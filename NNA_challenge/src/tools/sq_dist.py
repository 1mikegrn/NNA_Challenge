def sq_dist(p0, p1):
    '''calculate the square distance between two n_dim points as sum of 
    squares'''
    return sum([(x[0]-x[1])**2 for x in zip(p0, p1)])