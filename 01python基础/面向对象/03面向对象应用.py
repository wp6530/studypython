# -*- coding:utf-8 -*-
class Cat:
    type = 'cat'

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print("{}喜欢吃{}".format(self.nickname, food))

    def catch_mouth(self, color, weight):
        print("{},抓了一只{}kg的，{}的老鼠".format(self.nickname, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print("继续")
        else:
            print("工作")

    def show(self):
        print("猫的详细信息:")
        print("猫的名字：{}".format(self.nickname))
        print("猫的年龄：{}".format(self.age))
        print("猫的颜色：{}".format(self.color))


cat = Cat('jack', 12, 'blue')
cat.eat('mouse')
cat.show()
