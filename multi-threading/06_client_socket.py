# -*- coding: utf-8 -*-

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

s_client = socket(AF_INET, SOCK_STREAM)
s_client.connect(("127.0.0.1", 8000))


def chat():
    print("wait...")
    while True:
        message = input("请输入消息:")
        if not message:
            continue
        s_client.send(bytes(message, encoding="utf-8"))
        if message == "quit":
            break

    s_client.close()
    print("close()")


def get_message():
    while True:
        try:
            message = s_client.recv(1024)
            print(message.decode())
        except Exception as e:
            print(e)
            break
        finally:
            pass


t = Thread(target=chat)
t.start()
t = Thread(target=get_message)
t.start()
