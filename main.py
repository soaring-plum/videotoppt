import shutil
import time

import converter
import compare
import jpgtoppt
import os


def RemoveDir(filepath):
    '''
    如果文件夹不存在就创建，如果文件存在就清空！
    '''
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)

filePath="C:/Users/li/Desktop/videotoppt/workspace/video/"
for i,j,k in os.walk(filePath):
    print(i,k)
img = 'C:/Users/li/Desktop/videotoppt/workspace/temp/'
img2 = 'C:/Users/li/Desktop/videotoppt/workspace/temp2/'
pptx='C:/Users/li/Desktop/videotoppt/workspace/pptx/'
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
    compare.main(filePath =img,outputpath=img2)
    time.sleep(2)
    print('-------第', i, '次转换---------')
    jpgtoppt.main(ppt_filename=pptx+a,picPath=img2)
    t2=time.time()
    print('第',i,'次耗时',t2-t1)
    time.sleep(2)
all=time.time()
print(all-t)