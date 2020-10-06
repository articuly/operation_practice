#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import os, random, time


def write(q):
    print("Process to write %s" % os.getpid())
    for value in ["A", "B", "C", "D", "E", "F", "G"]:
        q.put(value)
        print("Put %s to queue ..." % value)
        time.sleep(random.random() * 2)


def read(q):
    print("Process to read : %s" % os.getpid())
    while True:
        try:
            value = q.get()
            print("Get %s from queue." % value)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    q = multiprocessing.Queue(20)
    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # pw.join()
#    pr.terminate()
