from threading import Thread
from random import randint
from time import sleep, time


def myprint(tid):
    sleep(randint(0, 3))
    print("threading:", tid)


# 存放线程列表
threads = []


def main():
    for i in range(100):
        print("create", i)
        t = Thread(target=myprint, args=(i,))
        t.start()
        # t.join()
        threads.append(t)
        print("start", i)


if __name__ == "__main__":
    start_time = time()
    main()
    print("main stop....")
    # 检查每一个线程是否执行完毕
    for i in threads:
        i.join()
        # print(i)
    end_time = time()
    print(end_time - start_time)
