#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "vanhack",
    version='0.1dev',
    py_modules=['vanhack'],
    packages=find_packages(),
    description = "Vanhack - Ormuco coding challenge",
    author = "Felipe Vieira",
    author_email = "felipe.lv.90@gmail.com",
    url = "https://github.com/FelipeLVieira/ormuco-vanhack",
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
