#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(name='stratify',
      version='1.0',
      description='ISCFS Stratify',
      packages=['insights'],
      package_dir={"insights": "insights"},
      entry_points={
      },
      setup_requires=['wheel'],
      install_requires=[
    ]
     )