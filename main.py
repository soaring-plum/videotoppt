import shutil
import time

import converter
import compare
import jpgtoppt
import os


def RemoveDir(filepath):
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)
global h,w
filePath="./workspace/video/"
for i,j,k in os.walk(filePath):
    print(i,k)
h=0
w=0
img = './workspace/temp/'
img2 = './workspace/temp2/'
pptx='./workspace/pptx/'
t=time.time()
for i in range(len(k)):
    a= k[i].replace('.mp4', '')
    a= a.replace('.ts', '')
    t1 = time.time()
    RemoveDir(img)
    RemoveDir(img2)
    print('-------第',i,'次切片---------')
    converter.main(videopath=filePath+k[i],imgpath=img)
    time.sleep(2)
    print('-------第', i, '次精简---------')
    compare.main(filePath1 =img,filePath2=img2)
    time.sleep(2)
    print('-------第', i, '次转换---------')
    jpgtoppt.main(ppt_filename=pptx+a,picPath=img2)
    t2=time.time()
    print('第',i,'次耗时',t2-t1)
    time.sleep(2)
all=time.time()
print(all-t)