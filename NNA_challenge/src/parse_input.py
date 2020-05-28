import pandas as pd
import numpy as np

class ParseInput():
    '''Creates a class object of the parsed input file. Constraints are accessed
    by the object function 'parse constraints' which returns a tuple of 
    (id, [x0, x1, x2, ...])'''
    def __init__(self, file_name, **kwargs):        
        with open(file_name, 'r') as f:
            data = f.read()       
        lines = data.split('\n')

        self.n_pts = len(lines)
        self.constraints = [parentheses_parse(line) for line in lines]
        self.n_dim = len(string_fmt(self.constraints[0][1]))
          
    def get_npts(self):
        '''returns number of points in input file'''
        return self.n_pts

    def get_ndim(self):
        '''returns dimensionality of the input points'''
        return self.n_dim

    def parse_constraints(self):
        return [(c[0], string_fmt(c[1])) for c in self.constraints]

    def parse_to_df(self):
        '''generates pandas DataFrame of n_dim, index=id'''
        return pd.DataFrame(
             np.array([string_fmt(c[1]) for c in self.constraints]), 
            index=[c[0] for c in self.constraints],
            columns=['x{}'.format(i) for i in range(self.get_ndim())]
        )

def parentheses_parse(string):
    '''splits line into string parts in tuple(id, string(coords)) '''
    rtn = (
        string.split(' ')[0], 
        string[string.index(r'('):string.index(r')')+1]
    )
    return rtn

def string_fmt(string):
    '''formats coordinates from string to list of coordinates'''
    remove = ['(',')']
    for char in remove:
        string=string.replace(char,'')
    string=string.split(',')
    return list([float(x) for x in string])