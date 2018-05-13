#照片拼接
from os import listdir
from PIL import Image

#获取当前文件夹所有jpg图像
ims = [Image.open(fn) for fn in listdir() if fn.endswith('.jpg')]

#单图尺寸
width,height=ims[0].size
#创建空白长图，宽度为单图宽度，长度为所有图的高度总和
result = Image.new(ims[0].mode,(width,height*len(ims)))

#拼接
for i,im in enumerate(ims):
    result.paste(im,box=(0,i*height))
#保存
result.save('result.jpg')