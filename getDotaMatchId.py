#获取所有比赛id，此处以Paparazi为例
import requests
import redis

refuser_id= 137193239
url = 'https://api.opendota.com/api/players/137193239/matches'
r = redis.Redis(host="192.168.11.78",port=6379)#redis服务器


def getMatch(playerMatches_url):
	raw_data = requests.get(playerMatches_url).json()
	for i in raw_data:
		match_id = i['match_id']
		yield match_id


if __name__ == '__main__':
	g = getMatch(url)
	for i in g:
		r.lpush("match_id",i)#把比赛id存入redis服务器中的match_id列表中，方便爬虫使用