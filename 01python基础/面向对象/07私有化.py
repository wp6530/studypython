# -*- coding:utf-8 -*-
# 私有化
class Stduent:
    # __age = 18

    def __init__(self, name):
        self.name = name
        self.__age = 20
        self.__score = 59

    # 定义公有的set和get方法
    def set_age(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print("error age input")

    def get_age(self):
        return self.__age

    def __str__(self):
        return '姓名；{}，年龄：{}，考试分数：{}'.format(self.name, self.__age, self.__score)


jack = Stduent('jack')
print(jack)
jack.set_age(21)
print(jack.get_age())
print(dir(Stduent))

print(dir(jack))

