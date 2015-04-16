#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import platform
import warnings

from setuptools import setup, Extension

setup(
        author = 'Francesco De Carlo, Argonne National Laboratory',
        author_email='decarlo@aps.anl.gov',
        name='xtomo',
        version='0.0.1',

        #packages = find_packages(),

        # include_package_data = True,

        # Specify C/C++ file paths. They will be compiled and put into tomopy.lib:
        # ext_modules=[ext_fftw, ext_gridrec],

        description='Tomography Data Exchange Toolbox',
        keywords=['tomography', 'data', 'format'],
        url='http://aps.anl.gov/DataExchange',
        #download_url='http://github.com/data-exchange/data-exchange',

        license='BSD',
        platforms='Any',
        version = '1.4',

        classifiers=['Development Status :: 1 - Beta',
                     'License :: OSI Approved :: BSD License',
                     'Intended Audience :: Science/Research',
                     'Intended Audience :: Education',
                     'Intended Audience :: Developers',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7']
)
