# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 17:26
# @Author  : Seceast
# @File    : yield_from.py


def ran(it):
    # for i in it:
    #     yield i
    yield from it

a_lis = [1, 2, 3, 4, 5, 6, 7]

print(list(ran(a_lis)))

