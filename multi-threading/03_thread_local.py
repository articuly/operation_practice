# -*- coding=utf-8 -*-

from threading import Thread, current_thread, local
from random import randint
from time import sleep

# 线程局部对象
# 线程局部对象可以被所有线程访问，比如local_data，可以被所有线程访问
# 但是线程局部对象的属性只能被定义该属性的线程自身访问，比如local_data的data属性，只能被自己的线程访问与修改，即使
# 所有的线程中都包含同名的local_data.data属性，因此这个data实际上只是线程内部的局部变量
# 借助线性局部对象可以简化代码逻辑，保持线程间变量隔离
local_data = local()
data = 100


def set_data():
    local_data.data = randint(0, 100)
    print(current_thread().name + "::data=" + str(local_data.data))
    sleep(randint(0, 3))
    print(current_thread().name + ":: after_sleep::data=" + str(local_data.data))
    # global data
    # data = local_data.data+data
    out()


def out():
    print(local_data.data)
    # print(data)


def main():
    for i in range(3):
        t1 = Thread(target=set_data)
        t1.start()


if __name__ == "__main__":
    main()
