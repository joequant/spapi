#!/usr/bin/env python3

from distutils.core import setup

setup(name='spapir',
      version='0.0.1',
      description='SharpPoint API',
      author='Joseph C Wang',
      author_email='joequant@gmail.com',
      url='https://github.com/joequant/sptrader',
      packages=['sptrader'],
      install_requires=[
    'cffi',
    ]
      )
