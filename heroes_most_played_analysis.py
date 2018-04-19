import pandas as pd
import matplotlib.pyplot as plt
import pymongo
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
hero = df['hero_id'].value_counts()
most_played = hero[:30]

con = pymongo.MongoClient('127.0.0.1:27017')
h = con.dota.hero
names = []
for i in most_played.index:
    name = h.find({'hero_id':int(i)})[0]
    #print(name['short_name'])
    names.append(name['short_name'])

fig=plt.figure(figsize=(27,6))
ax1=plt.subplot(111)
x_zhou = pd.Series(names)
rect = ax1.bar(x_zhou.index,most_played.values,0.7,color='#008FD5')
for rec in rect:#条形图上显示数据标签
    x=rec.get_x()
    height=rec.get_height()
    ax1.text(x-0.05,1.02*height,str(height))
ax1.set_xticks(x_zhou.index)
ax1.set_xticklabels(x_zhou.values)
ax1.set_ylabel("times")
ax1.set_xlabel("heroes")
ax1.set_title("heroes paparazi most played")
plt.show()