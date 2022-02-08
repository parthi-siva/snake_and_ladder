# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='snakegame',
    version='0.1.0',
    description='Simple snake game',
    long_description=readme,
    author='Parthiban Sivasamy',
    author_email='parthiban.sivasamy90@gmail.com',
    url='https://github.com/parthi-siva/snake_and_ladder',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

