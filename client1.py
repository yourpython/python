#coding=gbk
import socket

HOST = 'localhost'
PORT = 10888
s = socket.socket(socket._blocking_errnos,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = "你好！"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print = ("")