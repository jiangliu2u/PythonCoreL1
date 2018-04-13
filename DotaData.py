from multiprocessing import Process, Pool
import requests
import pymongo

  # 得到所有比赛信息，为list
refuser_id= 137193239
url = 'https://api.opendota.com/api/players/137193239/matches'
connection = pymongo.MongoClient("127.0.0.1:27017")
refuser = connection.dota.refuser

def getMatch(playerMatches_url):
	raw_data = requests.get(playerMatches_url).json()
	for i in raw_data:
		k = i['kills']
		d = i['deaths']
		a = i['assists']
		match_id = i['match_id']
		duration = i['duration']
		hero_id = i['hero_id']
		radiant_win = i['radiant_win']
		
		if d == 0:
			kda = k + a
		else:
			kda = (k + a) / d
		yield {"match_id":match_id,"hero_id":hero_id,"kills":k,"deaths":d,"assists":a,"kda":kda,"radiant_win":radiant_win,"duration":duration}
		# yield match_id


def getMatchInfo(url):
	players = requests.get('https://api.opendota.com/api/matches/'+str(url['match_id'])).json()['players']
	if players:
		for i in players:
			is_win = False
			if i['account_id']==137193239:
				if i['isRadiant']==i['radiant_win']:
					print({"match_id":url['match_id'],"hero_id":url['hero_id'],"is_win":is_win,"kills":url['k'],"deaths":url['d'],"assists":url['a'],"kda":url['kda'],"radiant_win":url['radiant_win'],"duration":url['duration']})
					print('================')
					is_win = True


g = getMatch(url)
if __name__ == '__main__':
	pool = Pool()
	for i in g:
		pool.apply_async(getMatchInfo,(i,))
	pool.close()
	pool.join()
	# connection.close()