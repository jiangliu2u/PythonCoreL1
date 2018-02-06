from threading import Thread
from multiprocessing import Process
import os

def work():
	print('hello ',os.getpid())
	
if __name__=="__main__":
	#主进程下开启的多个线程pid和主进程一样
	t1 = Thread(target = work)
	t2 = Thread(target = work)
	t1.start()
	t2.start()
	print('主线程/主进程pid', os.getpid())
	#开启多个进程pid都不一样
	p1 = Process(target = work)
	p2 = Process(target = work)
	p1.start()
	p2.start()
	print('主线程/主进程pid', os.getpid())