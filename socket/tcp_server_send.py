# coding:utf-8
from socket import *
import random
import time

# 创建socket对象
s_server = socket(AF_INET, SOCK_STREAM)
# 绑定IP与端口号
s_server.bind(("127.0.0.1", 9999))
# 开始监听
s_server.listen()

client_sock, client_addr = s_server.accept()
print("waiting...........")
print(client_sock, client_addr)
print("-" * 50)

# 创建一个永久循环
if __name__ == '__main__':
    with open(r"D:\Projects\python_projects\big_data\shakespeare_all.txt", encoding='utf-8') as f:
        ss_text = f.readlines()

    for line in ss_text:
        client_sock.send(bytes(line, encoding='utf-8'))
        print(bytes(line, encoding='utf-8'))
        time.sleep(random.randint(0,2))

    s_server.close()