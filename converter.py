# 导入所需要的库
import os
import shutil

import cv2
import numpy as np
def RemoveDir(filepath):
    '''
    如果文件夹不存在就创建，如果文件存在就清空！
    '''
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)

def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)
def main(videopath,imgpath):
    videoCapture = cv2.VideoCapture(videopath)
    success, frame = videoCapture.read()
    i = 1000
    timeF = 20 * 5
    j = 0
    while success:
        i = i + 1
        if (i % timeF == 0):
            j = j + 1
            save_image(frame, imgpath, str(j).zfill(3))
        success, frame = videoCapture.read()

if __name__=='__main__' :
    RemoveDir('C:/Users/li/Desktop/videotoppt/workspace/temp/')
    RemoveDir('C:/Users/li/Desktop/videotoppt/workspace/temp2/')
    main(videopath= 'C:/Users/li/Desktop/videotoppt/workspace/video/' + '花卉学28.mp4',imgpath='C:/Users/li/Desktop/videotoppt/workspace/temp/')