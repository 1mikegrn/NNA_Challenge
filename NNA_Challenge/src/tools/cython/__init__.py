"""
### Cython

handles cython file importation in the case where Cython fails to compile. 
_calculate.pyx and calculate.py are functionally the same, though syntax may 
differ due to optimizations. 
"""

try:
    from NNA_Challenge.src.tools.cython import _calculate as calculate

except:
    from NNA_Challenge.src.tools.cython import calculate