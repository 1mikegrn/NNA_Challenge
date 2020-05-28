from os import path
import NNA_Challenge

def main():

    radius = 3000000

    kwargs = {
        'method': 'KDTree',
        'axis': 'variance',
        'BFM': 'np',
        'output': 'return',
        'timeit': 'False'
    }

    here = path.abspath(path.dirname(__file__))

    input_file = path.join(here, 'test_input.txt')

    input_class = NNA_Challenge.src.parse_input.ParseInput(input_file)
    data = input_class.parse_constraints()

    tree = NNA_Challenge.src.tools.kdtree.LeafyKDTree(data, **kwargs).query_radius(radius)   
    brute = NNA_Challenge.src.tools.brute.BruteForce(data, **kwargs).query_radius(radius)

    tree = NNA_Challenge.src.tools.output.output(tree, **kwargs)
    brute = NNA_Challenge.src.tools.output.output(brute, **kwargs)

    return tree, brute

def test_main():
    tree, brute = main()
    assert tree == brute

if __name__ == "__main__":
    test_main()
