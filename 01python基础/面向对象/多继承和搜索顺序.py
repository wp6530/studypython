# -*- coding=utf-8 -*-
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print('eating...')
#
#     def eat(self, food):
#         print('{} eating {} ...'.format(self.name, food))
#     # 不能出现同名的方法，同名的方法会被第二个覆盖
#
#
# p = Person('jack', 20)
# p.eat('fish')
import inspect
class Base:
    def test(self):
        print('--->Base')


class A(Base):
    def test(self):
        print('--->AAA')


class B(Base):
    def test(self):
        print('--->BBB')


class C(Base):
    def test(self):
        print('--->CCC')


class D(A, B, C):
    pass


d = D()
d.test()
print(inspect.getmro(D))
print(D.mro())

'''
python 允许多继承
搜索顺序是广度优先
'''