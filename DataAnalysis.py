import matplotlib.pyplot as plt
import numpy as np
import requests
import pymongo

url = 'https://api.opendota.com/api/players/137193239/matches'
  # 得到所有比赛信息，为list
refuser_id= 137193239
connection = pymongo.MongoClient("127.0.0.1:27017")
refuser = connection.dota.refuser

def getMatch(playerMatches_url):
	raw_data = requests.get(playerMatches_url).json()
	for i in raw_data:
		k = i['kills']
		d = i['deaths']
		a = i['assists']
		match_id = i['match_id']
		match_date=i['start_time']
		duration = i['duration']
		if d == 0:
			kda = k + a
		else:
			kda = (k + a) / d
		yield getMatchInfo(match_id)

    #refuser.insert({"matche_id":match_id,"start_time":match_date,"duration":duration,"kills":k,"deaths":d,"assists":a,"kda":kda})
    #return mk,d,a,kda

def getMatchInfo(match_id):
	match_info = requests.get('https://api.opendota.com/api/matches/'+str(match_id)).json()
	print(match_info['players'][5])

for i in getMatch(url):
	print(i)
connection.close()