import cv2
import numpy as np

import os
def main(filePath,outputpath):
    for i,j,k in os.walk(filePath):
        print(i,k)
    file1 = filePath+k[0]
    image1 = cv2.imread(file1)
    cv2.imwrite(outputpath+'000.jpg' , image1)
    a=0
    for i in range(len(k)-1):
        file1 = filePath+k[i]
        file2 = filePath+k[i+1]
        image1 = cv2.imread(file1)
        image2 = cv2.imread(file2)
        difference = cv2.subtract(image1, image2)
        # print('最大值： ', np.max(difference))
        # print('平均值： ', np.mean(difference))

        if np.std(difference)<4:
            # print("两张图片一样")
            pass
        else:
            # cv2.imwrite("result.jpg", difference)
            print(k[i], k[i + 1],str(a+1), '标准差： ', np.std(difference))
            cv2.imwrite(outputpath+ str(a+1).zfill(3)+'.jpg', image2)
            a = a + 1
            # print("两张图片不一样")

if __name__=='__main__' :

    main(filePath = 'C:/Users/li/Desktop/videotoppt/workspace/temp/',outputpath= 'C:/Users/li/Desktop/videotoppt/workspace/temp2/')