#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread, Lock, current_thread
from time import sleep
from random import randint

lock = Lock()
number = [0]


def loop(i):
    lock.acquire()
    try:
        if i > number[-1]:
            # print(i, number[-1])
            sleep(randint(0, 5))
            number.append(i)
    except:
        pass
    finally:
        print("thread %s ended." % current_thread().name, number, "\r\n")
        lock.release()
        pass


if __name__ == "__main__":
    for i in range(10):
        t = Thread(target=loop, args=(i,))
        t.start()
