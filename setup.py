# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

from mnemelib import get_version

scripts = ['mneme']

setup(
    name='mneme',
    version=get_version(),
    scripts=scripts,
    author='Apostolos Bessas',
    author_email='mpessas@gmail.com',
    description=('Index the content of urls locally for easier searching.'),
    license='GPL',
    packages=find_packages()
)
