import time
from threading import Timer
from wxpy import *
import requests

bot = Bot(console_qr=True, cache_path=True)
# bot = Bot(cache_path=True)  # 连接微信,会出现一个登陆微信的二维码


def get_news():
    # 获取金山词霸每日一句
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note


def send_time(time_of_send):
    # 参数time_of_send的格式为：070000
    print("等待时间到达%s" % time_of_send)
    while True:
        if time_of_send == time.strftime('%H%M%S', time.localtime(time.time())):
            print("时间已到达%s" % time_of_send)

            return


def send_news():
    print("正在执行发送信息函数")
    try:
        print("Send message...")
        contents = get_news()
        my_friend = bot.friends().search(u'啾咪、')[0]  # 这里是你微信好友的昵称
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u'宝贝，早安！你是最美的宝宝！爱你哟！')
        t = Timer(86400,send_news)  # 这里是一天发送一次，86400s = 24h

        t.start()

    except:
        my_friend = bot.friends().search(u'QAQ')[0]  # 这里是你的微信昵称，发送失败时接收提醒
        my_friend.send(u'今天消息发送失败了')


send_time("070000")
send_news()

