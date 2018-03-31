from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
from wechat_sender import Sender
import time

bot = Bot()
#bot = Bot(console_qr=2,cache_path="botoo.pkl")
def get_news1():
    contents = u'python,睡前私语时：'
    translation = u'越过山丘，才发现有你在等候'

    return contents,translation
def send_news():
    try:
        my_lover = bot.friends().search(u'奇')[0]
        my_lover.send(get_news1()[0])
        my_lover.send(get_news1()[1])
        my_lover.send(u'来自小语')
        t = Timer(86400,send_news)
        t.start()
    except:
        my_lover = bot.friends().search(u'python')[0]
        my_lover.send(u'发送消息失败')

if __name__ == "__main__":
    send_news()
