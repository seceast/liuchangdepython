# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 15:33
# @Author  : Seceast
# @File    : clockdeco.py


import time
from functools import wraps


def clock(func):
    @wraps(func)
    # functools.wraps 只是标准库中拿来即用的装饰器之一,把相关的属性从 func 复制到 clocked 中(__doc__,__name__)等
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            kw_lis = ['%s=%r' % (k, w) for k, w in kwargs.items()]
            arg_list.append(kw_lis)
        arg_str = ''.join(arg_list)
        print('[%8fs]%s(%s) -> %r' % (elapsed, name, arg_str, result))
        # %r万能格式符，可将参数按照原样输入，并带类型
        return result
    return clocked


