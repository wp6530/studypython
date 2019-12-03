# -*- coding = utf-8 -*-
import threading
from time import sleep


def download(q):
    images = ['1.jpg', '2.jpg', '3.jpg']
    for image in images:
        print("{} is downloading".format(image))
        sleep(1)
        print("{} saved successfully".format(image))


def listen_music(q):
    musics = ['music1', 'music2', 'music3', 'music4', 'music5']
    for music in musics:
        print("listenning {}".format(music))
        sleep(1)


if __name__ == '__main__':

    t1 = threading.Thread(target=download, name='down', args=(1,))
    t1.start()

    t2 = threading.Thread(target=listen_music, name='listen', args=(1,))
    t2.start()

    n = 1
    while True:
        print(n)
        sleep(1)
        n += 1
