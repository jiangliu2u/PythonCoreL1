import requests
import http.cookiejar as cookielib
import re
import time
from PIL import Image

# 构造 Request headers
# agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
headers = {
    "Host": "passport.weibo.cn",
    "Referer": "https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F",
    'User-Agent': agent
}

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
    print(login_code)
    if login_code == 200:
        return True
    else:
        return False


def login(username, password):
    postdata = {
        'username': username,
        'password': password,
        'entry': 'mweibo',
        'r': 'https://m.weibo.cn/beta',
        'pagerefer':'https://passport.weibo.cn/ignin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fbeta'
    }
    login_page = session.post("https://passport.weibo.cn/sso/login", data=postdata, headers=headers)
    print(login_page.text)
    session.cookies.save()
    folow = session.get("https://m.weibo.cn/feed/friends?", headers={
    'Accept':'application/json, text/plain, */*',
    'Referer':'https://m.weibo.cn/beta',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': agent
    })
    print(folow.json())


try:
    input = raw_input
except:
    pass


def main():
    if isLogin():
        print('已经登录')
    else:
        account = '**'
        secret = '**'
        login(account, secret)


if __name__ == '__main__':
    main()
