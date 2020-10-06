from socket import *

HOST = "127.0.0.1"
PORT = 21111
BUFSIZE = 1024

# 创建udp服务器
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind((HOST, PORT))

data, addr = udpSerSock.recvfrom(BUFSIZE)

udpSerSock.close()
