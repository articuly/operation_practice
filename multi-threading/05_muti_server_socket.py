# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

s_server = socket(AF_INET, SOCK_STREAM)
s_server.bind(("127.0.0.1", 8000))
s_server.listen()


def chat(client):
    while True:
        try:
            message = client.recv(1024)
        except:
            break
        else:
            print(message.decode("utf-8"))
            # 空字符串跳过
            if not message:
                continue
            if message == "quit":
                print("close")
                client.close()
                break
            else:
                print("send")
                client.send(b"\r\nrecived...")


while True:
    print("wait......")
    s_client, addr = s_server.accept()
    t = Thread(target=chat, args=(s_client,))
    t.start()
