# -*- coding = utf -8-*-
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

    def get_time(self):
        ran_time = random.randint(1, 10)
        msg = ''









