from __future__ import print_function

from distutils.core import setup
from distutils.extension import Extension

setup(
    author = 'Alexandre Gobbo European Synchrotron Radiation Facility',
    description = 'Read EDF files.',
    py_modules = ['EdfFile'],
    name = 'edffile',
    requires = (
        'python',
        ),
    version = '1.6',
)
