from socket import *
from threading import Thread

s_server = socket(AF_INET, SOCK_STREAM)
s_server.bind(("127.0.0.1", 5000))
s_server.listen()


def application(client):
    response = "HTTP/1.1 200 OK \r\n" \
               "Content-Type: text/html; charset=utf-8 \r\n" \
               "Content-Length: 25 \r\n" \
               "Server: Werkzeug/0.16.0 Python/3.7.4\r\n\r\n" \
               "<h1>%s</h1>"
    print("recv....")
    data = client_sock.recv(2048).decode()
    print(data)
    response = response % data  # 加粗内容
    client.send(bytes(response, encoding="utf-8"))
    client.close()


if __name__ == '__main__':
    while True:
        print("等待连接中....")
        client_sock, client_addr = s_server.accept()
        t = Thread(target=application, args=(client_sock,))
        t.start()

# s_server.close()
