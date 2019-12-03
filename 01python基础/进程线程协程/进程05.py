# -*- coding=utf-8 -*-
import os
from multiprocessing import Pool
import time
from random import random


# 阻塞模式: 添加一个任务执行一个任务，如果一个任务不结束另一个任务就进不来

def work(task_name):
    print("{} start".format(task_name))
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print("{} over, last {},id = {}".format(task_name, end - start, os.getpid()))
    # return "{} over, last {},id = {}".format(task_name, end - start, os.getpid())


container = []

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7']
    for task in tasks:
        pool.apply(work, args=(task,))
    pool.close()
    pool.join()
