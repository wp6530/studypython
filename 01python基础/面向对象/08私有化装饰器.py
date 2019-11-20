# -*- coding=utf-8 -*-
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # def setAge(self, age):
    #     if age > 0 and age < 100:
    #         self.__age = age
    #     else:
    #         print("error age input")
    #
    # def getAge(self):
    #     return self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print("error age input")

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.__age)


s = Student('jack', 20)
s.name = 'tom'
s.age = 21
print(s)
