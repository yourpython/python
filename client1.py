#coding=gbk
import socket,base64

HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = "��ã��ͻ���ʹ��base64�������ı�����������"
while data:
    b64 = data.encode('gbk')
    s.sendall(base64.b64encode(b64))
    data = s.recv(512)
    data = base64.b64decode(data)
    b64 = data.decode('gbk')
    print ("���������յ���Ϣ�ǣ�\n",b64)
    data = input('��������Ϣ��\n')

s.close()