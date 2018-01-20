from threading import Thread
from time import sleep, ctime

msgs = []
format_msgs = []
def msg_input():
	while True:
		msg = input('>>:').strip()
		print(msg)
		if not msg:continue
		msgs.append(msg)

def msg_trans():
	while True:
		if msgs:
			res=msgs.pop()
			format_msgs.append(res.upper())

def msg_save():
	while True:
		if format_msgs:
			with open('D:\db.txt','a') as f:
				res=format_msgs.pop()
				print(res)
				f.write(res)
			
			
def main():
	t1= Thread(target=msg_input)
	t2= Thread(target=msg_trans)
	t3= Thread(target=msg_save)
	t1.start()
	t2.start()
	t3.start()
	
if __name__ == '__main__':
    main()
