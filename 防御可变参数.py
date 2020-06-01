# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 11:04
# @Author  : Seceast
# @File    : 防御可变参数.py


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers  # 这会导致实例在进行列表修改时会同时修改传入的参数
            # self.passengers = list(passengers)  # 这就不会影响初始化传入的参数

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __iter__(self):
        pass


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
tw_bus = TwilightBus(basketball_team)
tw_bus.pick('ana')
tw_bus.drop('Tina')
# tw_bus.drop('Maya')

print('basketball_team:', basketball_team)
print('passengers:', tw_bus.passengers)

