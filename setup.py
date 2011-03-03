# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name='mneme',
    version='0.1',
    author='Apostolos Bessas',
    author_email='mpessas@gmail.com',
    description=('Index the content of urls locally for easier searching.'),
    license='GPL',
    packages=['mnemelib', ],
    py_modules=['mneme', ],
    entry_points={
        'console_scripts': [
            'mneme=mneme:main',
        ]
    }
)
