import requests
import http.cookiejar as cookielib
import re
import time
from PIL import Image
import json
import sys

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


def getWeibo():
    follow = session.get("https://m.weibo.cn/feed/friends?&max_id=4185694539281878", headers={
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://m.weibo.cn/beta',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': agent
    })

    data = follow.json()['data']['statuses']
    f=open('d:/2.json','a')
    f.write(str(data))
    for i in data:
        b = i['text'].translate(non_bmp_map)
        c = re.sub(r'<a .*?>', '', b)
        c = re.sub(r'<span .*?</span>', '', c)
        c = re.sub(r'</a>', '', c)
        c = re.sub(r'<br/>', '', c)
        print(c)
        print('===================================')


def login(username, password):
    postdata = {
        'username': username,
        'password': password,
        'entry': 'mweibo',
        'r': 'https://m.weibo.cn/beta',
        'pagerefer': 'https://passport.weibo.cn/ignin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fbeta'
    }
    login_page = session.post("https://passport.weibo.cn/sso/login", data=postdata, headers=headers)
    session.cookies.save()


try:
    input = raw_input
except:
    pass


def main():
    if isLogin():
        print('已经登录')
    else:
        account = '***@163.com'
        secret = '***'
        login(account, secret)
    getWeibo()


if __name__ == '__main__':
    main()
