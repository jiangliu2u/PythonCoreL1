#采用多线程爬虫爬取豆瓣电影250榜单所有电影名称，并保存在txt文件中

from lxml import etree
import requests
from bs4 import BeautifulSoup
import threading
from time import sleep, ctime

title = []
start_url = 'https://movie.douban.com/top250?start='
i = [x for x in range(16)]
f = open('D:/豆瓣电影250.txt','w+')

def getMovie(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    a= soup.find('div',id='content').find_all('li')
    for h in a:
        aaa= h.find('span',class_='title')
        title.append(aaa.text)

def main():
    print('开始获取豆瓣电影250，开始时间为:', ctime())
    threads = []
    for j in i:
        url_ = start_url + str(j*25)
        t = threading.Thread(target=getMovie,args=(url_,))
        threads.append(t)
    for j in i:
        threads[j].start()
    for j in i:
        threads[j].join()
    f.write(str(title))
    f.close()
    print('所有电影名称获取完毕，结束时间为:', ctime())

if __name__ == '__main__':
    main()
