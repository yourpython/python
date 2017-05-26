
#coding=utf-8
import base64

a = input("Enter string:")
b = base64.b64encode(a)  # Encode for string

print (base64(b))  # Decode for string

f = open('temp.jpg', 'rb')
c = f.read()

x = base64(c)  # Encode for file
f.close()
print
len(x)
print
"".join(x.split())

base64(x)  # Decode for file
file1 = open('temp', 'wb')
file1.write(base64(x))