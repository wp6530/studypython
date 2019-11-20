# -*- coding:utf-8 -*-
# class Phone:
#     def __init__(self):
#         print("---------init----------")
#
#     def call(self):
#         print('price: ', self.price)
#
#
# p = Phone()
# p.price = 1000
# p.call()

class Person:
    name = '张三'

    def __init__(self):
        self.name = 'zhangsan'
        self.age = 18

    def eat(self):
        print('{}正在吃饭。。。'.format(self.name))

    def run(self):
        print('{}今年{}岁，正在跑步。。。'.format(self.name, self.age))


p = Person()
# p.name = '李四'
p.eat()
p.run()
