# -*- coding=utf-8 -*-
import os
from multiprocessing import Pool
import time
from random import random


# 非阻塞模式
# 全部添加到队列中，立刻返回，并没有等待其他的进程完毕，但是回调函数是等待任务完成之后才调用。
def work(task_name):
    print("{} start".format(task_name))
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    # print("{} over, last {},id = {}".format(task_name, end - start, os.getpid()))
    return "{} over, last {},id = {}".format(task_name, end - start, os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7']
    for task in tasks:
        pool.apply_async(work, args=(task,), callback=callback_func)
    pool.close()
    pool.join()

    for i in container:
        print(i)
    print('over!!!')
