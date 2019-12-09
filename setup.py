# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='autobench2',
    version='0.1.0',
    description='HTTP benchmarking suite for wrk2',
    long_description=readme,
    author='Chiyu Zhong',
    author_email='zhongchiyu@gmail.com',
    url='https://github.com/cattail/autobench2',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['autobench2=autobench2.cli:cli']
    },
)
