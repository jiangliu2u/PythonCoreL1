#登录H5微博，并邮件通知你某个关注的人有没有更新微博
import requests
import http.cookiejar as cookielib
import re
import sys
from time import sleep

non_bmp_map = dict.fromkeys(
    range(0x10000, sys.maxunicode + 1), 0xfffd
)  # 解决Non-BMP character问题


class LoginWeibo(object):

    def __init__(self, uid):#uid为你实时想关注的人的id
        # 构造 Request headers
        self.agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
        )
        self.login_headers = {
            "Host": "passport.weibo.cn",
            "Origin": "https://passport.weibo.cn",
            "Referer": "https://passport.weibo.cn/signin/login",
            "User-Agent": self.agent,
        }
        self.get_header = {
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://m.weibo.cn/beta",
            "Host": "m.weibo.cn",
            "MWeibo-Pwa": "1",
            "User-Agent": self.agent,
        }
        self.uid = uid
        self._init_session()
        self.latest = self.get_weibo(self.uid)[0]

    def _init_session(self):  # 使用登录cookie信息
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename="cookies")
        try:
            self.session.cookies.load(ignore_discard=True)
            print("使用Cookie登录")
        except:
            print("Cookie未能加载,准备使用用户名和密码登录")
            self._login('yourusername','yourpassword ')#填写自己的用户名密码，也可以在login函数中更改为input手动输入

    def _is_login(self):
        # 通过查看用户个人信息来判断是否已经登录
        # url = "https://m.weibo.cn/users/{0}?set=1".format(yourid)
        # login_code = session.get(
        #    url, headers=self.get_header, allow_redirects=False
        # ).status_code
        # if login_code == 200:
        # return True
        # else:
        #    return False
        pass

    def get_weibo(self, id):
        url = "https://m.weibo.cn/profile/info?uid={0}".format(id)
        weibo = self.session.get(url, headers=self.get_header).json()
        print("1111111", type(weibo["data"]["statuses"][0]))
        return weibo["data"]["statuses"]
        # for i in weibo['data']['statuses']:
        #   b = i["text"].translate(non_bmp_map)
        #   c = re.sub(r"<a .*?>", "", b)
        #   c = re.sub(r"</a>", "", c)
        #    c = re.sub(r"<span .*?</span>", "", c)
        #    c = re.sub(r"<span .*?>", "", c)
        #    weibo_content = re.sub(r"<br/>", "", c)  # 微博内容

    def _login(self, username, password):
        postdata = {
            "username": username,
            "password": password,
            "entry": "mweibo",
            "r": "https://m.weibo.cn/beta",
            "pagerefer": "https://passport.weibo.cn/ignin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fbeta",
        }
        self.session.post(
            "https://passport.weibo.cn/sso/login",
            data=postdata,
            headers=self.login_headers,
        )
        self.session.cookies.save()

    def has_new_weibo(self):
        top_weibo = self.get_weibo(self.uid)[0]
        if top_weibo["id"] == self.latest["id"]:
            print("no new weibo!")
            return False
        else:
            print("new weibo,content is {} !".format(top_weibo["text"]))
            self.latest = top_weibo
            #send_email()
            return True


if __name__ == "__main__":
    a = LoginWeibo(2279881761)
    while True:
        sleep(10)
        a.has_new_weibo()
