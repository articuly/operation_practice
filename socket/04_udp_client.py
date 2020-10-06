from socket import *

HOST = "127.0.0.1"
PORT = 21111
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建一个socket对象
# SOCK_DGRAM - 套接字类型为udp数据报
udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("请输入:")
    if message == "quit":
        break
    if not message:
        continue
    udpClient.sendto(bytes(message, encoding="utf-8"), ADDR)
    message, addr = udpClient.recvfrom(2048)
    print(addr, ">>", message.decode("utf-8"))

udpClient.close()
