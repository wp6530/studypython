# -*- coding:utf-8 -*-

# 迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素都被访问到为止
# 迭代器只能往前，不能往后
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器

# 可迭代的对象：1.生成器 2.元组 列表 集合 字典 字符串

from collections.abc import Iterable

# 使用isistance()判断是否可以迭代

list1 = [1, 2, 3, 4, 5]
f = isinstance(list1, Iterable)
print(f)

f = isinstance('abc', Iterable)
print(f)

f = isinstance(100, Iterable)
print(f)

g = (x for x in range(10))
f = isinstance(g, Iterable)
print(f)

# 可迭代的不一定是迭代器，必须可以通过next()取值的可迭代的对象才是迭代器
# 通过iter()函数可以将一个可迭代的对象变成一个迭代器
list = [1, 2, 3, 4, 5]
list = iter(list)
print(next(list))
