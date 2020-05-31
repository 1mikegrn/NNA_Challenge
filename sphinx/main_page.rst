This site is a docstring repository for the Nearest Neighbors Algorithm 
Challenge, written by Michael Green in part for a technical challenge submission 
to Karagozian and Case.

Use the tabs on the left-hand side of the page to navigate to the
various document sections.

**Connect:**

Michael Green
`@Website <https://1mikegrn.github.io>`_
`@Github <https://github.com/1mikegrn>`_
`@StackOverflow <https://stackoverflow.com/users/10881573/michael-green?tab=profile>`_

Getting Started
===============

From the command prompt, the latest version this library can be installed 
via pip and git.

:code:`pip install git+https://github.com/1mikegrn/NNA_Challenge`

Where the setup file will automatically check dependencies and install
to the main module library. Once installed, calling
:code:`NNA_Challenge <input.txt> <radius> **kwargs` from the command prompt 
will execute the calculation.

Though not necessary, the CLI will accept string kwargs of the form
:code:`key=value` for the following parameters:

::

    kwargs = {                      # Options
        'method': 'KDTree',         # ['KDTree', 'BFM']
        'axis': 'variance',         # ['variance', 'uniform']
        'BFM': 'np',                # ['np', 'py']
        'output': 'print',          # ['print', 'return', 'path/to/dir']
    }

The method controls the main algorithmic method, using either the :code:`KDTree` 
(default) method, or a :code:`BFM` brute-force approach. For the KDTree, the 
method for determining the splitting axis can be either using a variance 
approach, splitting the data-set along the axis of highest variance, or a 
uniform approach, splitting along axis [x0, x1, x2, ...] sequentially and 
repeatedly. For the brute-force approach, the calculation can be executed using
NumPy broadcasting or with a pure-Python approach. Finally the output of the 
program can be set as 'print' to print to console, 'return' to return the 
results as a list of strings, or a directory path in which to save a 
:code:`NNA_results.txt` file. 

Library Structure
=================

::

    NNA_Challenge/
        __init__.py                         # initialize NNA_Challenge
        __main__.py                         # CLI access point
        src/                                # source module
            __init__.py                     # initialize submodule                    
            calculate.py                    # main calculation module
            parse_input.py                  # restructures CLI input to module
            tools/                          # tools module
                __init__py                  # initialize tools
                cmd_reader.py               # CLI reader
                kdtree.py                   # kdtree class location
                brute.py                    # brute-force approach module
                output.py                   # file output module
                cython/                     # cython module
                    _calculate.pyx          # main cython implementation
                    calculate.py            # fallback python implementation
