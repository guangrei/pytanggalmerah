#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

requirements = [
    'requests',
    'pytz'
]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Pytanggalmerah',
    version='1.0',
    packages=['pytanggalmerah',],
    license='MIT',
    author="guangrei",
    author_email="grei@tuta.io",
    description="python module to check indonesia holiday calendar (include sunday)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="holiday indonesia calendar sunday",
    url="https://github.com/guangrei/pytanggalmerah",
    install_requires=requirements,    
)