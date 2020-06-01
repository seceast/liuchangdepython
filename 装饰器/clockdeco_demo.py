# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 15:40
# @Author  : Seceast
# @File    : clockdeco_demo.py


import time
from clockdeco import clock


@clock
def snooze(sec):
    time.sleep(sec)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


snooze(1)
factorial(4)
