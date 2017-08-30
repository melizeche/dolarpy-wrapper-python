# -*- encoding: utf-8 -*-
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dolarpy',
    packages=['dolarpy'],
    version='0.3',
    description=('Wrapper for DolarPy, an PYG/USD exchange rate API.'),
    author='Marcelo Elizeche Landó',
    author_email='melizeche@gmail.com',
    url='https://github.com/melizeche/dolarpy-wrapper-python',
    license='MIT',
    use_2to3=True,
    install_requires=required,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial'
    ]
)
