# NNA_Challenge

[![DocSite](https://img.shields.io/badge/Docs-Site-blue)](https://1mikegrn.github.io/NNA_Challenge/)

## A Python module for the Nearest-Neighbors Algorithm Challenge portion from Karagozian and Case

---

This module is the second of two challenge submissions to be provided on behalf of Michael Green, candidate for employment with Karagozian and Case. 

This NNA_Challenge implementation is written in Python v3.8.3, which by default sets float values to double precision float64 objects. The module takes as input directly from the command line:
```
NNA_Challenge <input.txt> <radius> **kwargs
```
Where <input.txt> is the filepath to a .txt file of the following format:

```
#1 (0, 0, 0)
#2 (1, 0, 0)
#3 (0, 1, 0)
...      ...
#N (0, 0, 1)
```

WIth nodes #1 -> #N being a tuple of x-dimensional points existing in an arbitrary domain space,

Where <radius> is a float64 value to search for over the design space,

and where **kwargs are subsequent keyword arguments which can be passed as `key=value`. See below for details.

The algorithm defaults to building a K-dimensional tree (KDTree), with each splitting point being the median value sorted along the axis with the highest variance in an effort to maximize balance. The KDTree is generated recursively and stored as a class object for later use. Generating a KDTree is of `O(n log n)` computational complexity with `O(n)` space complexity. The KDTree is ultimately a pruning mechanism so to reduce the search space by eliminating irrelevant trees.

In this implementation, the each point traverses the tree, selecting subtrees which contain the bounds (radius +/- point). At the point where the tree divisor splits the bounds, the remaining subtree is flattened, and then searched through brute-force so to find the final data set of points which are within the radius.

It should be noted that KDTrees are only most efficient when this 'pruning' mechanism is well optimized. I.E. if the radius is comparatively large w/ respect to the design space, for example, then the performance will actually be *worse* than the brute-force method (BFM) of simply comparing all points to all points. This is because under such circumstances, when the tree traversal terminates at a relatively shorter tree depth, the computational cost of creating the tree will have been higher than the time saved on the back end by attempting to trim off the higher values of N which dictate the computational and storage complexity of the BFM at `O(n^2)`. As such, also included herein is a NumPy optimized brute-force approach to the calculation, which can be toggled through the module **kwargs. The NumPy approach uses the broadcasting methods of the library to run the computation at a level closer to that of the hardware. Since Python is a high-level dynamic language, the NumPy BFM will actually perform on par with the KDTree method in some situations (which is more-or-less pure Python). However, both methods generally outperform the pure Python implementation of the BFM (Which is also provided, though mostly for benchmarking purposes and comedic relief). Future versions can expect to have this decision be determined programmatically.


### kwargs:

The following default kwargs:

```
    kwargs = {                      # Options
        'method': 'KDTree',         # ['KDTree', 'BFM']
        'axis': 'variance',         # ['variance', 'uniform']
        'BFM': 'np',                # ['np', 'py']
        'output': 'print',          # ['print', 'return', 'path/to/dir']
    }
```

Are amenable with the given options. `BFM` is ignored if method is `KDTree`. 
`axis` ignored if method is `BFM`.