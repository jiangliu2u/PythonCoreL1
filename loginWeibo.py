import requests
import http.cookiejar as cookielib
import re
import time
from PIL import Image
import json
import sys
import pymongo

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
headers = {
    "Host": "passport.weibo.cn",
    "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F",
    'User-Agent': agent
}

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  # 解决Non-BMP character问题
# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://weibo.com/2279881761/follow"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code
    if login_code == 200:
        return True
    else:
        return False


weibo_3pages = []


def getWeibo():
    api = []
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://m.weibo.cn/beta',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': agent
    }
    url = "https://m.weibo.cn/feed/friends?&max_id="
    follow = session.get(url, headers=head)
    for i in range(6):
        data = follow.json()['data']['statuses']
        next_api = data[19]['mid']  # 第20条微博的mid为下拉页面加载更多微博的参数 请求链接为'https://m.weibo.cn/feed/friends?&max_id='+next_api
        for i in data:
            b = i['text'].translate(non_bmp_map)
            c = re.sub(r'<a .*?>', '', b)
            c = re.sub(r'<span .*?</span>', '', c)
            c = re.sub(r'</a>', '', c)
            c = re.sub(r'<br/>', '', c)
            weibo_3pages.append(c)
        follow = session.get(url + next_api, headers=head)


def login(username, password):
    postdata = {
        'username': username,
        'password': password,
        'entry': 'mweibo',
        'r': 'https://m.weibo.cn/beta',
        'pagerefer': 'https://passport.weibo.cn/ignin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fbeta'
    }
    session.post("https://passport.weibo.cn/sso/login", data=postdata, headers=headers)
    session.cookies.save()

def main():
    if isLogin():
        print('已经登录')
    else:
        account = '***@163.com'
        secret = '***'
        login(account, secret)
    getWeibo()
    connection = pymongo.MongoClient('127.0.0.1', 27017)#把爬到的微博内容写入mongodb
    weibo = connection.weibo
    weibo = weibo.weibo
    for i in weibo_3pages:
        weibo.insert({'weibo_content': i})


if __name__ == '__main__':
    main()
