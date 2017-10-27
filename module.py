'''
author:king lin
date:2017/10/27
describe:计算器
'''


class Calculator():

    def __init__(self,a,b): #因为自己错写成int ，所以会提示object() takes no parameters 意思是object()不需要传进参数
        # 自己并不用成功调用了初始化函数，自定义的int 不算默认函数。
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def div(self):
        return self.a / self.b

