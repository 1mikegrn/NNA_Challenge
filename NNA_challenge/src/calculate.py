import NNA_challenge

def calculate(input_file, radius, **kwargs):
    '''Handles assertion errors, funnels inputs to their respected class objects
    for computation. Returns computation result.'''    
    input_class = NNA_challenge.src.parse_input.ParseInput(input_file)
    data = input_class.parse_constraints()

    valid_method_kwargs = ['KDTree', 'BFM']
    valid_BFM_methods = ['np', 'py']   

    assert kwargs['method'] in valid_method_kwargs, (
        '\n\n Passed method is not in list of valid methods.'
        +' Valid methods include: '
        + ', '.join(valid_method_kwargs)
    )

    assert kwargs['BFM'] in valid_BFM_methods, (
        '\n\n Passed BFM is not in list of valid BFMs. Valid BFMs include: '
        + ', '.join(valid_BFM_methods)
    )

    if kwargs['method'] == 'KDTree':
        tree = NNA_challenge.src.tools.kdtree.LeafyKDTree(data, **kwargs)
        result = tree.query_radius(radius)

        return result

    elif kwargs['method'] == 'BFM':        

        BFM_object = NNA_challenge.src.tools.brute.BruteForce(
            data, **kwargs
        )

        result = BFM_object.query_radius(radius)
        return result



    
