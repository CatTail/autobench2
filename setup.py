# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='autobench2',
    version='0.1.2',
    description='HTTP benchmarking suite for wrk2',
    long_description=readme,
    author='Chiyu Zhong',
    author_email='zhongchiyu@gmail.com',
    url='https://github.com/cattail/autobench2',
    license="MIT License",
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['autobench=autobench2.cli:cli']
    },
    install_requires=['click>=7.0'],
    include_package_data=True,
    python_requires='>=3.6.0'
)
