#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='dash',
      version='0.0.1',
      description='Python Dash Tools',
      author='Vitalik Buterin',
      author_email='vbuterin@gmail.com',
      url='http://github.com/vbuterin/pybitcointools',
      packages=['dash'],
      scripts=['pydashtool'],
      include_package_data=True,
      data_files=[("", ["LICENSE"])],
      )
