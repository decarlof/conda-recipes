from __future__ import print_function

from distutils.core import setup
from distutils.extension import Extension

setup(
    author = 'Stuart B. Wilkins',
    description = 'Read SPE files.',
    py_modules = ['spefile'],
    name = 'spefile',
    requires = (
        'python',
        ),
    version = '1.6',
)
