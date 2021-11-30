#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='resettabletimer',
    version='0.7.0',
    author='Toni Kangas',
    description='Wrapper for threading.Timer to allow resetting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kangasta/resettabletimer",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
