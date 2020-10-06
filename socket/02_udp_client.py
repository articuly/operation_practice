from socket import *

HOST = "127.0.0.1"
PORT = 21111
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建一个socket对象
udpClient = socket(AF_INET, SOCK_DGRAM)
udpClient.sendto(bytes("ok", encoding="utf-8"), ADDR)
udpClient.close()
