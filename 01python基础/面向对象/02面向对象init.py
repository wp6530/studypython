# -*- coding:utf-8 -*-
class Phone:
    def __init__(self):
        print("---------init----------")

    def call(self):
        print('price: ', self.price)


p = Phone()
p.price = 1000
p.call()