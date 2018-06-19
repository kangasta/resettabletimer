#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='resettabletimer',
	version='0.6.2',
	author='Toni Kangas',
	description='Wrapper for threading.Timer to allow resetting',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/kangasta/resettabletimer",
	packages=setuptools.find_packages(),
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	)
)
