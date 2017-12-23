import matplotlib.pyplot as plt
import numpy as np
import requests

url = 'https://api.opendota.com/api/players/137193239/matches'
raw_data = requests.get(url).json()  # 得到所有比赛信息，为list
r = []
for i in raw_data:
    k = i['kills']
    d = i['deaths']
    a = i['assists']
    match_id = i['match_id']
    if d == 0:
        kda = k + a
    else:
        kda = (k + a) / d
    r.append([match_id, kda])
results = np.array(r)
print(r)
plt.plot(np.arange(5842),results[:,1])
plt.show()