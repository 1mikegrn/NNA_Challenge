from os import path
import numpy as np

def build(length, n_dim):
    '''builds dummy input files for testing, using random np.float64 values. 
    Outputs to this directory'''
    
    here = path.abspath(path.dirname(__file__))

    # data = np.random.random_sample((length, n_dim))
    data = (2*10**7
    *np.random.default_rng().random((length, n_dim), dtype=np.float64)
    -10**7
    )

    lines = []

    for idx, row in enumerate(data, start=1):
        string = (
            '#{}'.format(idx) + ' (' + ', '.join([str(x) for x in row])+')'
        )

        lines.append(string)

    with open(path.join(here, 'test_input.txt'), 'w') as w:
        w.writelines(
            [x+'\n' if x != lines[-1] else x
            for x in lines]
        )

if __name__ == "__main__":
    build(10000, 3)