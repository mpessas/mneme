# -*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
    name='mneme',
    version='0.2',
    author='Apostolos Bessas',
    author_email='mpessas@gmail.com',
    description=('Index the content of urls locally for easier searching.'),
    license='GPL',
    packages=['mneme', 'mneme.store', 'mneme.document', ],
    entry_points={
        'console_scripts': [
            'mneme=mneme.mneme:main',
        ]
    }
)
