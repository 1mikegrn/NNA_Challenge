'''
use this file to locally build cython files with by calling:

python build_cython.py build_ext --inplace


'''

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("**/*.pyx"),
    zip_safe=False,
)