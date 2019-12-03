# -*- coding=utf-8 -*-
from multiprocessing import Process
from time import sleep
import os


def task1(s, name):
    while True:
        sleep(s)
        print("This is task 1", os.getpid(), "----", os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print("This is task 2", os.getpid(), "----", os.getppid(), name)


number = 1
if __name__ == '__main__':
    p1 = Process(target=task1, name='task1', args=(1, 'aa'))
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='task2', args=(2, 'bb'))
    p2.start()
    print(p2.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(number)
