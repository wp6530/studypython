# -*- coding:utf-8 -*-
import sys

# 迭代器
list = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(list)
print(next(it))
print(next(it))

# 迭代器对象可以用常规for语句进行遍历

list = [1, 2, 3, 4, 5, 6]
it = iter(list)
print(it)
print(id(it))
# for x in it:
#     print(x, end=" ")
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
