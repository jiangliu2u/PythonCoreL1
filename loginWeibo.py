import requests
import http.cookiejar as cookielib
import re
import sys

non_bmp_map = dict.fromkeys(
    range(0x10000, sys.maxunicode + 1), 0xfffd
)  # 解决Non-BMP character问题


class LoginWeibo:

    def __init__(self):
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
        self.__initSession()

    def __initSession(self):  # 使用登录cookie信息
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename="cookies")
        try:
            self.session.cookies.load(ignore_discard=True)
            print("使用Cookie登录")
        except:
            print("Cookie未能加载,准备使用用户名和密码登录")
            self.login('', '')

    def isLogin(self):
        # 通过查看用户个人信息来判断是否已经登录
        url = "https://m.weibo.cn/users/2279881761?set=1"
        login_code = session.get(
            url, headers=self.get_header, allow_redirects=False
        ).status_code
        if login_code == 200:
            return True
        else:
            return False

    def getWeibo(self):
        url = "https://m.weibo.cn/feed/friends?max_id="
        follow = self.session.get(url, headers=self.get_header).json()
        print(follow)
        for i in range(2):
            print(i)
            data = follow["data"]["statuses"]
            next_api = data[19][
                "mid"
            ]  # 第20条微博的mid为下拉页面加载更多微博的参数 请求链接为'https://m.weibo.cn/feed/friends?max_id='+next_api
            for i in data:
                b = i["text"].translate(non_bmp_map)
                c = re.sub(r"<a .*?>", "", b)
                c = re.sub(r"</a>", "", c)
                c = re.sub(r"<span .*?</span>", "", c)
                weibo_content = re.sub(r"<br/>", "", c)  # 微博内容
                username = i["user"]["screen_name"]  # 用户名
                pub_date = i["created_at"]  # 发布日期
                print(weibo_content, username, pub_date, sep="\n   ")
            follow = self.session.get(url + next_api, headers=self.get_header)

    def login(self, username, password):
        postdata = {
            "username": username,
            "password": password,
            "entry": "mweibo",
            "r": "https://m.weibo.cn/beta",
            "pagerefer": "https://passport.weibo.cn/ignin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fbeta",
        }
        self.session.post(
            "https://passport.weibo.cn/sso/login", data=postdata, headers=self.login_headers
        )
        self.session.cookies.save()


if __name__ == "__main__":
    a = LoginWeibo()
    a.getWeibo()