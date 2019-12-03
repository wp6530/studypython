# -*- coding=utf-8 -*-


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eating....")


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self):
        print('{} is study {} ...'.format(self.name, self.clazz))

    def eat(self):
        print('{} is eating cake ...'.format(self.name))


class Employee(Person):
    def __init__(self, name, age, manager):
        super().__init__(name, age)
        self.manager = manager


class Docker(Person):
    def __init__(self, name, age, patients):
        # super().__init__(name, age)
        # self.patients = patients
        super(Docker, self).__init__(name, age)
        self.patients = patients


e = Employee('jack', 23, 'tom')
lists = ['jerry', 'rom', 'bob']
d = Docker('jack', 31, lists)
s = Student('jack', 21, 'music')
s.study()
s.eat()
'''
1.如果类中不定义__init__，调用父类 super class的__init__
2.如果类继承父类也需要定义自己的__init__，则需要在当前类的__init__调用一下父类的__init__
3.调用类的方法，先找当前类再去找父类
4.子类的方法中也可以调用父类方法
'''