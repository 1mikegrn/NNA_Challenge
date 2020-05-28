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

.. This library also has a colab jupyter notebook, from which calculations can be
.. executed without any necessary local downloads.

.. .. image:: https://colab.research.google.com/assets/colab-badge.svg
..    :target: https://colab.research.google.com/github/1mikegrn/HypercubeChallenge/blob/master/colab/HypercubeChallenge_notebook.ipynb

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
