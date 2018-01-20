#获取目录下所有的子文件夹名称
import os

path = ["D:\\专利"]
dirnames=[]
filenames=[]
def get_all_dirs(ab_path):
	for i in ab_path:
		all = os.listdir(i)
		dir_name = [name for name in all if os.path.isdir(os.path.join(i,name))]
		for j in dir_name:
			d = [os.path.join(i,j)]
			dirnames.append(d)
			get_all_dirs(d)
get_all_dirs(path)
print(dirnames)
#获取目录下所有文件夹及子文件夹下的文件名称

def get_all_files(ab_path):
	file_dir=[]
	for i in ab_path:
		all = os.listdir(i)
		file_name = [name for name in all if os.path.isfile(os.path.join(i,name))]
		filenames.append(file_name)
		dir_name = [name for name in all if os.path.isdir(os.path.join(i,name))]
		for j in dir_name:
			d = os.path.join(i,j)
			file_dir.append(d)
		get_all_files(file_dir)

get_all_files(path)
print(filenames)