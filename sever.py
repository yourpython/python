#coding=gbk

import socket

HOST = ''
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
conn,addr = s.accept()
print("客户端地址:",addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
        print("接收的数据",data.decode('utf-8'))
        conn.send(data)
        conn.close()

