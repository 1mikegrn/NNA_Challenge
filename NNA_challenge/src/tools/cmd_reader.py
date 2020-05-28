import sys

def reader():
    '''CLI for NNA_Challenge. Accepts initializer, input file, radius as 
    a float64, and subsequent kwargs through Commmand Line. 
    If '?' is passed as the first argument, prints help menu and terminates.'''

    # print and exit if help is toggled
    if sys.argv[1] == '?':
        print_help()
        sys.exit()

    assert len(sys.argv) >= 3, (
        'Expected CLI input: NNA_Challenge <input_file.txt> <radius> **kwargs'
    )

    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        radius = float(sys.argv[2])
        kwargs = parse_kwargs({})   

    else:
        input_file = sys.argv[1]
        radius = float(sys.argv[2])
        kwargs = parse_kwargs(sys.argv[3:])        

    assert isinstance(input_file, str) is True, (
        'Expected <input_file.txt> value of type str()'
    )

    return input_file, radius, kwargs

def parse_kwargs(kwargs):
    '''parses extra kwargs, builds subsequent kwarg dictionary, 
    overriding defaults if requested'''

    kwargs = dict([x.split('=') for x in kwargs])

    defaults = {
        'method': 'KDTree',         
        'axis': 'variance',         
        'BFM': 'np',                
        'output': 'print',          
        'timeit': 'False'
    }

    final = {**defaults, **kwargs}

    return final

def print_help():
    string = '''

    The NNA_Challenge program takes the following arguments:

    NNA_Challenge <input_file.txt> <radius> **kwargs

        NNA_Challenge is the initializer from the command prompt

        <input_file.txt> is the full path to the input file.

        <radius> is the float64 value which is to be checked for Nearest Neighbors

        **kwargs are programmatic options for computation. 
        
    The default **kwargs values are:

    kwargs = {                  # Options #
        'method': 'KDTree',     # ['KDTree', 'BFM']
        'axis': 'variance',     # ['variance', 'uniform']
        'BFM': 'np',            # ['np', 'py']
        'output': 'print',      # ['print', 'return', 'path/to/save/directory']
    }

    '''
    print(string)