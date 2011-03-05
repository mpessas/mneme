# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

scripts = ['mneme']

setup(
    name='mneme',
    version='0.2',
    author='Apostolos Bessas',
    author_email='mpessas@gmail.com',
    description=('Index the content of urls locally for easier searching.'),
    license='GPL',
    packages=find_packages()
)
