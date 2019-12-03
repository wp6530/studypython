# -*- coding=utf-8 -*-
from multiprocessing import Queue

q = Queue(5)
q.put('A')
q.put('A')
q.put('A')
q.put('A')
q.put('A')
print(q.qsize())
if q.full():
    print("queue is full")
else:
    q.put('A', timeout=3)

# put(),如果队列满了只能等待队列有空间。
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get(timeout=3))
