#获取目录下所有的文件夹名称
import os

path = ["C:\\Users\\Administrator\\src\\1"]

def get_all_dirs(ab_path):
	dirnames=[]
	for i in ab_path:
		all = os.listdir(i)
		dir_name = [name for name in all if os.path.isdir(os.path.join(i,name))]
		dirnames.append(dir_name)
		for j in dir_name:
			d = [os.path.join(i,j)]
			get_all_dirs(d)
		print(dir_name)
	#print(dirnames)
get_all_dirs(path)