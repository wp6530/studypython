# -*- coding:utf-8 -*-
# 进程>线程>协程

def task1(n):
    for i in range(n):
        print("正在搬第{}块砖！".format(i))
        yield None


def task2(n):
    for i in range(n):
        print("正在听第{}首歌！".format(i))
        yield None


# g1 = task1(5)
# g2 = task2(10)
# while True:
#     try:
#         # g1.__next__()
#         # g2.__next__()
#         print(next(g1))
#         print(next(g2))
#     except:
#         pass

'''
定义生成器的方式：
1. 通过函数推导式方式
2. 函数 + yield
    def func():
        ...
        yield
    g = func()

产生元素：
1.next(generator) -->每次调用都会产生一个新的元素，如果元素产生完毕，再次调用就会产生异常
2.生成器自己的方法：
    g.__next()
    g.send(value)
'''












