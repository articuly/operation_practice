#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os, random


def myprint(i):
    print(os.getpid(), i)


if __name__ == "__main__":
    print("主进程 %s " % os.getpid())
    p1 = Process(target=myprint, args=(10,))
    p2 = Process(target=myprint, args=(20,))
    print('Child process will start')
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
