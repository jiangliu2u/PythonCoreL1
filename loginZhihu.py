import requests
import re


def getXSRF(url):
    content = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        'Referer': 'http://www.zhihu.com/'}).text
    # print(content)
    pattern = re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?', re.S)
    results = re.findall(pattern, str(content))
    xsrf = results[0]
    return xsrf


def login(url, email, password):
    login_data = {
        '_xsrf': getXSRF(url),
        'password': password,
        'remember_me': 'true',
        'email': email,
    }
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
               'Connection': 'keep-alive',
               'Host': 'www.zhihu.com',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
               'Referer': 'http://www.zhihu.com/', }
    session = requests.Session()
    result = session.post(url, data=login_data, headers=headers)
    s = result.text
    print(s)
    home = session.get("https://www.zhihu.com", verify=False)  # 再次使用session以get去访问知乎首页，一定要设置verify = False，否则会访问失败
    print(home.text)


url = 'https://www.zhihu.com/login/email'
login(url, "*@163.com", "*")
