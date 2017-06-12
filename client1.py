#coding=gbk
import socket,base64

HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = "你好！客户端使用base64编码后的文本传输给服务端"
while data:
    b64 = data.encode('gbk')
    s.sendall(base64.b64encode(b64))
    data = s.recv(512)
    data = base64.b64decode(data)
    b64 = data.decode('gbk')
    print ("服务器接收到信息是：\n",b64)
    data = input('请输入信息：\n')

s.close()