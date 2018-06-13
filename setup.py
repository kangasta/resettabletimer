#!/usr/bin/env python3

from setuptools import setup

setup(name='resettable-timer',
	version='0.5.0',
	description='Wrapper for threading.Timer to allow resetting',
	author='Toni Kangas',
	py_modules=['ResettableTimer', 'FakeTimer'],
)