# -*- coding=utf-8 -*-

from multiprocessing import Process


def calc():
    while True:
        n = 0
        for i in range(1000):
            lists = range(i)
            n += sum(lists)
        print(n)


if __name__ == "__main__":
    for i in range(8):
        p = Process(target=calc)
        p.start()
