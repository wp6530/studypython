# -*- coding:utf-8 -*-

# 魔术方法就是一个类/对象中的方法，和普通方法唯一的不同时，普通方法需要调用！而魔术方法是在特定时刻自动触发。

'''
__init__: 初始化魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）


__new__: 实例化的魔术方法
触发时机：在实例化的时候触发

__call__: 调用对象的魔术方法
触发时机：将对象当做函数调用时触发

__del__: 析构魔术方法
触发时机：

__str__:
触发时机：打印对象名时
'''

import sys


# class Person:
#     def __init__(self, name):
#         print('----------->init', self)
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):  # 申请内存空间
#         print('----------->new')
#         # super(Person, cls).__new__(*args, **kwargs)
#         position = object.__new__(cls)
#         print(position)
#         return position  # 地址
#
#     def __call__(self, name):
#         print('------------>call')
#         print('执行对象得到的参数是：', name)
#
#
# p = Person('aa')
#
# # print(p)
# p('call')


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('----------del----------')

    def __str__(self):
        return self.name


p = Person('jack')
# p1 = p
# p2 = p
#
# del p1
# print(p.name)
# del p2
# print(p.name)
# # del p
# # print(p.name)
# print(sys.getrefcount(p))
'''
删除地址的引用
查看对地址的引用次数：
import sys
sys.getrefcount(p)
当一个空间没有了任何应用，则会默认执行__del__

python解释器会在程序结束时回收所有程序执行过程中使用的空间

'''

print(p)
