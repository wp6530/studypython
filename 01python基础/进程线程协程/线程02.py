# -*- coding=utf-8 -*-
import threading
from time import sleep

ticket = 1000


def run():
    global ticket
    for i in range(100):
        sleep(0.1)
        ticket -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=run, name='run1')
    t2 = threading.Thread(target=run, name='run2')
    t3 = threading.Thread(target=run, name='run3')
    t4 = threading.Thread(target=run, name='run4')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(ticket)
