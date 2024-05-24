import shutil

import cv2
import numpy as np
from PIL import Image
import os
import yolov5.detect_e


def main(filePath1, filePath2):
    for i, j, k in os.walk(filePath1):  # 列出所有图片
        pass
        # print(i, k)
    file1 = filePath1 + k[0]  # 将第一张图片载入
    image1 = cv2.imread(file1)
    cv2.imwrite(filePath2 + '000.jpg', image1)  # 写入到指定位置
    a = 0
    d = 0
    for i in range(len(k) - 1):#前后两张图片开始对比
        file1 = filePath1 + k[i]
        file2 = filePath1 + k[i + 1]
        image1 = cv2.imread(file1)
        image2 = cv2.imread(file2)
        difference = cv2.subtract(image1, image2)
        # print('最大值： ', np.max(difference))
        # print('平均值： ', np.mean(difference))
        if np.std(difference) <= 4.5:#比较差异小于4.5去除
            # print("两张图片一样")
            if d >= 60:#连续命中15次即时间5*15=75秒
                print(str(a).zfill(5) + '.jpg')
                print(d)
                for i in range(d - 1):
                    os.remove(filePath2 + str(a - 1 - i).zfill(5) + '.jpg')
            d = 0
        else:#比较差异大于4.5保存
            # cv2.imwrite("result.jpg", difference)
            # print(k[i], k[i + 1], str(a + 1), '标准差： ', np.std(difference))
            d = d + 1
            cv2.imwrite(filePath2 + str(a + 1).zfill(5) + '.jpg', image2)
            a = a + 1
            # print("两张图片不一样")
    for i, j, k in os.walk(filePath2):#遍历留下的图片
        # print(i, k)
        pass
    img = Image.open(filePath2 + k[0])#留下的图片第一张
    w, h = img.size
    for i in range(len(k)):#去除无信号图片
        img = Image.open(filePath2 + k[i])
        rgb1 = img.getpixel((w * 0.117, h * 0.283))
        rgb2 = img.getpixel((w * 0.883, h * 0.283))
        rgb3 = img.getpixel((w * 0.117, h * 0.771))
        rgb4 = img.getpixel((w * 0.883, h * 0.771))
        if (0, 0, 0) <= rgb1 <= (4, 4, 4) and (0, 0, 0) <= rgb2 <= (4, 4, 4) and (0, 0, 0) <= rgb3 <= (4, 4, 4) and (
                0, 0, 0) <= rgb4 <= (4, 4, 4):
            os.remove(filePath2 + k[i])
        elif (0, 211, 152) <= rgb1 <= (4, 219, 160) and (95, 150, 38) <= rgb2 <= (103, 158, 46) and (
                210, 38, 94) <= rgb3 <= (218, 46, 102) and (94, 94, 251) <= rgb4 <= (102, 102, 255):
            os.remove(filePath2 + k[i])

    opt = yolov5.detect_e.parse_opt()#开始使用yolov5
    opt.source = filePath2#传入文件夹路径
    logo=yolov5.detect_e.main(opt)#开始识别
    for i in logo:
        os.remove(i)
    shutil.rmtree('./yolov5/runs/detect')
    os.makedirs('./yolov5/runs/detect')

    for i, j, k in os.walk(filePath2):#遍历留下图片
        # print(i, k)
        pass
    for i in range(len(k) - 1):#每张图片相互对比，重复去除
        file1 = filePath2 + k[len(k) - 1 - i]
        image1 = cv2.imread(file1)
        for t in range(len(k) - 2 - i):
            file2 = filePath2 + k[t]
            image2 = cv2.imread(file2)
            difference = cv2.subtract(image1, image2)
            if np.std(difference) <= 4.5:
                os.remove(filePath2 + k[len(k) - 1 - i])
                break



if __name__ == '__main__':
    main(filePath1='C:/Users/li/Desktop/videotoppt/workspace/temp/',
         filePath2='C:/Users/li/Desktop/videotoppt/workspace/temp2/')
