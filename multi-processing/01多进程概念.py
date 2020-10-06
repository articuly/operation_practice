#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start....' % os.getpid())

# 创建子进程
# pid在子进程中返回0，父进程中返回子进程id
pid = os.fork()  # windows 没有

# 子进程中执行==0段
if pid == 0:
    print("当前进程号：", os.getpid())
    print("父进程：", os.getppid())
else:
    # 父进程执行部分
    print("我是父进程：", os.getpid())
while True:
    pass
