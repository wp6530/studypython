# -*- coding=utf-8 -*-
import threading
from time import sleep

n = 0


def task1():
    global n
    for i in range(10000000):
        n += 1
    print("task1 : {}".format(n))


def task2():
    global n
    for i in range(10000000):
        n += 1
    print("task2 : {}".format(n))


if __name__ == '__main__':
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task1, name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main : {}".format(n))
