# -*- coding=utf-8 -*-
# is a ,has a
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}的速度行驶了{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度：{}'.format(self.brand, self.speed)


r = Road('青藏高速', 12000)
print(r.name)
r.name = '沈阳高速'
audi = Car('aodi', '120')
print(audi)
audi.get_time(r)
