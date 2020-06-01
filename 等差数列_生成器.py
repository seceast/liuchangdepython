# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 17:05
# @Author  : Seceast
# @File    : 等差数列_生成器.py


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin+self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step*index


ap = ArithmeticProgression(1, 2, 20)

print(list(ap))
