# -*- coding=utf-8 -*-
import os
from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Pool
from threading import Thread


def server(client):
    print("server_pid=", os.getpid())

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
                    ack_message = "\r\n %s recived..." % str(os.getpid())
                    client.send(bytes(ack_message, encoding="utf-8"))

    # while True:
    #     client, addr = s_server.accept()
    t = Thread(target=chat, args=(client,))
    t.start()


if __name__ == "__main__":
    s_server = socket(AF_INET, SOCK_STREAM)
    s_server.bind(("127.0.0.1", 8000))
    s_server.listen()
    p = Pool(3)
    while True:
        client, addr = s_server.accept()
        print(client)
        p.apply(server, args=(client,))
