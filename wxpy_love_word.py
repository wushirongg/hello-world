import random
from wxpy import *
import time

bot = Bot(console_qr=True, cache_path=True)
# bot = Bot(cache_path=True)  # 连接微信,会出现一个登陆微信的二维码


def read_line():

    count = len(open("words_love.txt").readlines())

    select_line = random.randint(0,count-1)
    # 打开文件
    file = open("words_love.txt")
    a = 0
    while True:
        # 读取一行内容
        a += 1
        text = file.readline()

        # 判断是否读到内容
        if a > select_line:
            break

    # 关闭文件
    file.close()
    return text


def send_words_love():
    while True:
        try:
            space_time = random.randint(10800,18000)
            love_word = read_line()
            time.sleep(space_time)
            my_friend = bot.friends().search(u'啾咪、')[0]  # 这里是你的微信昵称，发送失败时接收提醒
            my_friend.send(love_word)
            print("已发送: %s" % love_word)

        except:
            print("运行出错 try:")
            my_friend = bot.friends().search(u'QAQ')[0]  # 这里是你的微信昵称，发送失败时接收提醒
            my_friend.send(u'今天消息发送失败了')


send_words_love()
