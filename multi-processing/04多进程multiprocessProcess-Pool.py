#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:52:54 2018
"""

import multiprocessing
import os


def task(i):
    print('Run task %s ==> (%s)...' % (os.getpid(), i))


if __name__ == "__main__":
    print('Parent process %s.' % os.getpid())
    size = multiprocessing.cpu_count()
    print(size)
    # 创建size个子进程
    # 每个子进程根据任务执行情况会被复用
    # 创建进程需要申请cpu时间，内存空间，关闭进程还需要释放这些资源，整个过程比创建线程费时
    # 因此通常需要预先创建几个进程
    p = multiprocessing.Pool(size)
    for i in range(10000):
        p.apply_async(task, args=(i,))

    print("Waiting for all subprocesses done")
    #    调用close后不能继续添加进程
    p.close()
    #    等待所有子进程执行完毕后执行
    p.join()
    print("All subprocesses done.")
