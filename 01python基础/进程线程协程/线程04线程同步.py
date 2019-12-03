# -*- coding = utf-8 -*-
import threading
import time
import random

# lock = threading.Lock()
# list1 = [0] * 10
#
#
# def task1():
#     # lock.acquire()
#     for i in range(len(list1)):
#         list1[i] = 1
#         time.sleep(0.5)
#     # lock.release()
#
#
# def task2():
#     # lock.acquire()
#     for i in range(len(list1)):
#         print(list1[i])
#         time.sleep(0.5)
#     # lock.release()
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1, name='task1')
#     t2 = threading.Thread(target=task2, name='task2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(list1)


lockA = threading.Lock()
lockB = threading.Lock()


class Mythread(threading.Thread):
    def run(self):
        if lockA.acquire():
            print(self.name + 'get lock A')
            time.sleep(1)
            if lockB.acquire():
                print(self.name + 'get lock B,and also have lock A')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = Mythread()
    t2 = Mythread()
    t1.start()
    t2.start()
