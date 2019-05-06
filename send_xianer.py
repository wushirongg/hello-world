import time
from wxpy import *
import requests

bot = Bot(console_qr=True, cache_path=True)


def get_news():
    '''获取金山词霸每日一句'''
    url = 'http://open.iciba.com/dsapi'
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note

b = 100

while True:

    days = time.strftime('%d', time.localtime(time.time()))

    if days == b:
        pass
    else:

        if "07" == str(time.strftime('%H', time.localtime(time.time()))):
            b = days
            contents = get_news()
            my_friend =bot.friends().search(u'啾咪、')[0]#这里是你微信好友的昵称
            my_friend.send(contents[0])
            my_friend.send('早安，宝宝！')
            my_self =bot.friends().search(u'QAQ')[0]#这里是你微信好友的昵称
            my_self.send(contents[0])
            print("xianer wushirong")
            print (time.strftime('%Y.%m.%d %H:%M[%S] ',time.localtime(time.time())))
            time.sleep(18000)
            my_self.send(contents[1])
            my_friend.send(contents[1])
            time.sleep(39600)
            my_friend.send('吃药药，快点吃药药！')
            time.sleep(28700)
