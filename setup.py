#!/usr/bin/env python
#  -*- coding: utf8 -*-

from setuptools import setup

setup(
    name='pytket-wasm',
    version='1.0',
    packages=['pytket-wasm'],
    keywords=['wasm', 'disassembler', 'decoder'],
    license='MIT',
    author='Melf Johannsen',
    author_email='melf.johannsen@quantinuum.com',
    description='WebAssembly decoder & disassembler',
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'wasmdump = wasm.__main__:dump'
        ]
    }
)
