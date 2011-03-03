# -*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
    name='mneme',
    version='0.1',
    author='Apostolos Bessas',
    author_email='mpessas@gmail.com',
    description=('Index the content of urls locally for easier searching.'),
    license='GPL',
    packages=['mnemelib', 'mnemelib.store', 'mnemelib.document', ],
    entry_points={
        'console_scripts': [
            'mneme=mneme:main',
        ]
    }
)
