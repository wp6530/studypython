# -*- coding:utf-8 -*-

# 通过列表推导式得到生成器

x = [x * 3 for x in range(10)]
print(type(x))
g = (x * 3 for x in range(10))
print(type(g))
# 通过__next__()得到元素
# print(g.__next__())
# 通过系统函数next()得到元素
# print(next(g))


# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print("没有更多元素")
#         break


'''

1.定义一个函数，函数中使用yield类型
2.调用函数，接收函数结果
3.

'''


# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # 类似return n + 暂停


# g = func()
#
# print(g)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def fib(len):
    a, b = 0, 1
    n = 0
    while n < len:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return "没有更多元素了！！！"


# g = fib(8)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp: ', temp)
        for x in range(temp):
            print('------------->',x)
        print('####################')
        i += 1
    return '没有元素了！！！'


g = gen()
print(g.send(None))
n1 = g.send(3)
print('n1:', n1)
n2 = g.send(3)
print('n2:', n2)

