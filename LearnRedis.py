#学习redis的使用

import redis


r = redis.Redis(host="127.0.0.1",port=6379)
r.set('haha','wolegequ')
print(r.get('haha'))
