#! python2
# -*- coding:gbk -*-
import uniout

def file_hdl(name='123.txt'):
    f = open(name)
    res = 0
    i = 0
    for line in f:
        i += 1
        print('��%s�е�����Ϊ��'% line.strip(),line)
        res += int(line)

    print('��Щ���ĺ�Ϊ:',res)
    f.close()

if __name__ == '__main__':
    file_hdl()
