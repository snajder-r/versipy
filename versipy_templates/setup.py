#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

# Long description from README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Collect info in a dictionary for setup.py
setup(
    name="__package_name__",
    description="__package_description__",
    version="__package_version__",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="__package_url__",
    author="__author_name__",
    author_email="__author_email__",
    license="__package_licence__",
    python_requires="__minimal_python__",
    classifiers=["__classifiers_1__", "__classifiers_2__", "__classifiers_3__", "__classifiers_4__", "__classifiers_5__"],
    install_requires=["__dependency1__", "__dependency2__", "__dependency3__"],
    packages=["__package_name__"],
    package_dir={"__package_name__": "__package_name__"},
    package_data={"__package_name__": ["templates/*"]},
    entry_points={"console_scripts": ["__entry_point1__"]},
)
