#!/usr/bin/env python3

import re
from setuptools import setup, find_packages

with open("resettabletimer/_version.py", "r") as f:
    try:
        version = re.search(
            r"__version__\s*=\s*[\"']([^\"']+)[\"']",f.read()).group(1)
    except:
        raise RuntimeError('Version info not available')

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='resettabletimer',
    version=version,
    author='Toni Kangas',
    description='Wrapper for threading.Timer to allow resetting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kangasta/resettabletimer",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)
