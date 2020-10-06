# -*- coding: utf-8 -*-

from threading import Thread, current_thread
from time import sleep
from random import randint
from queue import Queue

q = Queue(20)


def put_data():
    while True:
        n = randint(0, 3)
        sleep(n)
        q.put(n)
        print(current_thread(), "向队列写入>>:", n)


def get_data():
    while True:
        data = q.get()
        print(current_thread(), "从队列读取>>", data)


def main():
    t1 = Thread(target=put_data)
    t2 = Thread(target=get_data)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
