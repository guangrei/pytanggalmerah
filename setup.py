#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

requirements = [
    'requests',
    'pytz',
    'zcache'
]
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='Pytanggalmerah',
    version='2.0.1',
    packages=['pytanggalmerah', 'pytanggalmerahcache'],
    scripts=["harilibur"],
    license='MIT',
    author="guangrei",
    author_email="myawn@pm.me",
    description="python module to check indonesia holiday calendar (include sunday)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="holiday indonesia calendar sunday",
    url="https://github.com/guangrei/pytanggalmerah",
    install_requires=requirements,
)
