from socket import *

HOST = "127.0.0.1"
PORT = 21111
BUFSIZE = 2048  # 缓冲长度

# 创建udp服务器
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind((HOST, PORT))
while True:
    # recvform返回数据data，与发送消息端的(ip, port)
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    print(addr, ">>", data)
    udpSerSock.sendto(bytes("ok", encoding="utf-8"), addr)

udpSerSock.close()
