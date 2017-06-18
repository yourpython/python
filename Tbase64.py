#coding=utf-8
import base64,codecs
"""h ='haha'
str =h.encode('utf-8')
print (str)
str1= base64.b64encode(str)  # Encode for string
print(u'转码base64后的haha：'+str1.decode()) #打印64
deco = base64.b64decode(str1)
print (deco)
print (u'转为utf-8的haha：'+deco.decode('utf-8'))
"""
f = codecs.open("1112.txt",'r','ascii')
a = f.read()
"""try:
    print(a.decode('gb2312'))
except:
    print ("printError")

finally:"""
f.close()

b=base64.b64encode(a)

b1=b
file1 = open("1234.txt",'wb')
file1.write(b1)
file1.close()
print  (b1)

"""f = open('temp.jpg', 'rb')
c = f.read()

x = base64(c)  # Encode for file
f.close()
print
len(x)
print
"".join(x.split())

base64(x)  # Decode for file
file1 = open('temp', 'wb')
file1.write(base64(x))"""