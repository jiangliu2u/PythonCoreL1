import time
from functools import wraps

def haha(func):
	'''
		hahahah
	'''
	@wraps(func)
	def wocao(*args,**kwargs):
		start = time.time()
		result= func(*args,**kwargs)
		end =time.time()
		print(func.__name__,end-start)
		print('wolegequ')
		return result
	return wocao
@haha
def go(n):
	s =0
	while n >0:
		s+=n
		n-=1
	return s
print(go(10))