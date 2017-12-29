import matplotlib.pyplot as plt
import numpy as np
import requests
import pymongo

url = 'https://api.opendota.com/api/players/137193239/matches'
raw_data = requests.get(url).json()  # 得到所有比赛信息，为list
r = []
connection = pymongo.MongoClient("127.0.0.1:27017")
refuser = connection.dota.refuser
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

    refuser.insert({"matche_id":match_id,"start_time":match_date,"duration":duration,"kills":k,"deaths":d,"assists":a,"kda":kda})
   
connection.close()