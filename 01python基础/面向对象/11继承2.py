# -*- coding=utf-8 -*-
# 　避免重复的代码


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 10

    def run(self):
        print(self.name + ' is running...')

    def eat(self):
        print(self.name + ' is eating...')


class Student(Person):
    def __init__(self, name):
        print("----------->student's init")

        # 调用父类的__init__
        super().__init__(name)
        # super()表示父类对象


class Teacher(Person):
    pass


class Employee(Person):
    pass


s = Student('jack')
s.run()
t = Teacher('lucy')
t.eat()
