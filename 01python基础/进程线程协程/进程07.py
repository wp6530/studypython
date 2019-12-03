# -*- coding=utf-8 -*-
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['1.jpg', '2.jpg', '3.jpg']
    for image in images:
        print("{} is downloading".format(image))
        sleep(1)
        q.put(image)


def getfile(q):
    try:
        while True:
            file = q.get(timeout=3)
            print("{} saved successfully ".format(file))
    except:
        print("all saved successfully")


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    # p1.join()
    p2.start()
    # p2.join()
