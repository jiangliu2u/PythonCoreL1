import requests
import pymongo
import redis,time

r = redis.Redis(host="192.168.11.78",port=6379)
connection = pymongo.MongoClient("mongodb://usernmae:password@host:port")
paparazi = connection.mydatabases.paparazi

def getMatchInfo(match_id):
	players = requests.get('https://api.opendota.com/api/matches/'+str(match_id)).json()
	if players:
		for i in players['players']:
			is_win = False
			if i['account_id']==137193239:
				if i['isRadiant']==i['radiant_win']:
					print(i['match_id'])
					print('==============')
					is_win = True
					paparazi.insert_one({"match_id":i['match_id'],"hero_id":i['hero_id'],"is_win":is_win,"kills":i['kills'],"deaths":i['deaths'],"assists":i['assists'],"kda":i['kda'],"isRadiant":i['isRadiant'],"radiant_win":i['radiant_win'],"last_hits":i['last_hits'],"denies":i['denies'],"damage":i['hero_damage'],"gold_per_min":i['gold_per_min'],"duration":i['duration']})

def main():
	while True:
		match_id = r.lpop('match_id').decode()
		if match_id == None:
			connection.close()
		else:
			getMatchInfo(match_id)
		

if __name__ == '__main__':
    main()