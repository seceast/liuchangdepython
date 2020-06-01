# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 16:30
# @Author  : Seceast
# @File    : 支持函数式编程的包.py


from functools import reduce
from operator import mul


def fact(n):
    return reduce(mul, range(1, n + 1))


print(fact(5))


