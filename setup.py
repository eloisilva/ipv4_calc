#! /usr/bin/env python3
#################################################################################
#     File Name           :     setup.py
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-06-20 11:52]
#     Last Modified       :     [2018-06-20 12:03]
#     Description         :      
#################################################################################

from setuptools import setup
import ipv4_calc

setup(
    name = 'ipv4_calc',
    version = ipv4_calc.__version__,
    author = ipv4_calc.__author__,
    author_email = ipv4_calc.__email__,
    packages = ['ipv4_calc',],
    license = 'GPLv3',
    entry_points={
        'console_scripts': [
            'disaggregate = ipv4_calc.__main__:main',
        ],
    },
)
