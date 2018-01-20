import threading
from time import ctime, sleep

def loop1():
	print('start loop1 func at:',ctime())
	sleep(5)
	print('end loop1 hhhhh')
	
def loop2():
	print('star loop2 func at:',ctime())
	sleep(2)
	print('end loop2')


def main():
	threads = []
	t1 = threading.Thread(target=loop1)
	t1.setDaemon(True)
	threads.append(t1)
	t2 = threading.Thread(target=loop2)
	threads.append(t2)
	for i in range(2):
		threads[i].start()
	#for i in range(2):#等待所有线程结束，加了这个也会等待守护线程结束
	#	threads[i].join()

if __name__=='__main__':
	main()