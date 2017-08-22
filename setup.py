# -*- encoding: utf-8 -*-
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dolarpy',
    packages=['dolarpy'],
    version='0.1.3',
    description=('Wrapp8er for DolarPy, an PYG/USD exchange rate API.'),
    author='Marcelo Elizeche Landó',
    author_email='melizeche@gmail.com',
    url='https://github.com/melizeche/dolarpy-wrapper-python',
    license='MIT',
    use_2to3=True,
    install_requires=required
)
