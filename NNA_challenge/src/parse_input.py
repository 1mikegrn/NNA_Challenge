import re
import pandas as pd
import numpy as np

class ParseInput():
    def __init__(self, file_name, **kwargs):        
        with open(file_name, 'r') as f:
            data = f.read()       
        lines = data.split('\n')

        self.n_pts = len(lines)
        self.constraints = [parentheses_parse(line) for line in lines]
        self.n_dim = len(string_fmt(self.constraints[0][1]))
          
    def get_npts(self):
        return self.n_pts

    def get_ndim(self):
        return self.n_dim

    def parse_constraints(self):
        return [(c[0], string_fmt(c[1])) for c in self.constraints]

    def parse_to_df(self):
        return pd.DataFrame(
             np.array([string_fmt(c[1]) for c in self.constraints]), 
            index=[c[0] for c in self.constraints],
            columns=['x{}'.format(i) for i in range(self.get_ndim())]
        )

def parentheses_parse(string):
    rtn = (
        string.split(' ')[0], 
        string[string.index(r'('):string.index(r')')+1]
    )
    return rtn

def string_fmt(string):
    remove = ['(',')']
    for char in remove:
        string=string.replace(char,'')
    string=string.split(',')
    return list([float(x) for x in string])