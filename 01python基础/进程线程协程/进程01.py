# -*- coding=utf-8 -*-
from multiprocessing import Process
from time import sleep
import os

# 不可变类型
m = 1
# 可变类型
list = []


def task1():
    global m
    while True:
        sleep(1)
        # print("This is task 1", os.getpid(), "----", os.getppid())
        # print("This is task1 ,m = ", m)
        list.append(str(m) + 'task1')
        print("This is task1,list = ", list)
        m += 1


def task2():
    global m
    while True:
        sleep(2)
        # print("This is task 2", os.getpid(), "----", os.getppid())
        # print("This is task1 ,m = ", m)
        list.append(str(m) + 'task2')
        print("This is task2,list = ", list)
        m += 1


if __name__ == '__main__':
    number = 1
    p1 = Process(target=task1, name='task1')
    p1.start()

    p2 = Process(target=task2, name='task2')
    p2.start()

    while True:
        sleep(1)
        # print("This is main, m = ", m)
        list.append(str(m) + 'task2')
        print("This is main,list = ", list)
        m += 1

        if number == 10:
            p1.terminate()
            p2.terminate()
            break
        else:
            number += 1
