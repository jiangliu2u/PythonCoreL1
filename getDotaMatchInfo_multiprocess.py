import requests
import pymongo
import multiprocessing

c = pymongo.MongoClient("localhost:27017")
h = c.dota.haha
m = c.dota.match
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
					h.insert_one({"match_id":i['match_id'],"hero_id":i['hero_id'],"is_win":is_win,"kills":i['kills'],"deaths":i['deaths'],"assists":i['assists'],"kda":i['kda'],"isRadiant":i['isRadiant'],"radiant_win":i['radiant_win'],"last_hits":i['last_hits'],"denies":i['denies'],"damage":i['hero_damage'],"gold_per_min":i['gold_per_min'],"firstblood_claimed":i['firstblood_claimed'],"duration":i['duration']})

def main():
	pool = multiprocessing.Pool(multiprocessing.cpu_count())
	all= m.find({})
	for i in all:
		pool.apply_async(getMatchInfo,(i['match_id'],))
	pool.close()
	pool.join()

if __name__ == '__main__':
    main()