#coding=gbk

import socket,base64

HOST = ''
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
conn,addr = s.accept()
print("�ͻ��˵�ַ:",addr,conn)

while True:
    data = conn.recv(1024)
    if not data:
        break
    b64 = base64.b64decode(data)
    print("���յ�����",data,"����������",b64.decode('gbk'))
    conn.send(data)
conn.close()

