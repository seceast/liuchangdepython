"""
--------------------------------------
 -*- coding: utf-8 -*-
 @author: yangyd
 @file: 命名元组.py
 @time: 2019/11/28 15:12 
--------------------------------------
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'jp', 36.11, (22222, 33333))

print(tokyo)
print(tokyo._fields)

print(namedtuple.__doc__)
