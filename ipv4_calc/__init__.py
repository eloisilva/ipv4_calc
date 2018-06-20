#! /usr/bin/env python3
#################################################################################
#     File Name           :     ipv4_calc/__init__.py
#     Created By          :     Eloi Silva (etch.linux@gmail.com)
#     Creation Date       :     [2018-06-20 11:54]
#     Last Modified       :     [2018-06-20 12:02]
#     Description         :      
#################################################################################

import sys

__version__ = '4.1.0'
__author__ = 'Eloi Luiz da Silva'
__email__ = 'eloi.silva@telefonica.com'

if sys.version_info[0] < 3:
    msg = 'Versoes menor que Python3 nao suportada'
    raise ImportError(msg)
