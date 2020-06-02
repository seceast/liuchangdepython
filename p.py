# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 15:04
# @Author  : Seceast
# @File    : p.py


# info_dic = {'name': 'kaka', 'age': 20.66666}
# # print(f'my name is {name}, age is {age:.2f}')
# for i, v in info_dic.items():
#     print(f'{i}:{v}')


def square(x):
    return x * x


int_lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
add = lambda i: sum(i)

square_res = map(square, int_lis)
print(add(int_lis), list(square_res))
