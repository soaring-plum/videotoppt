# videotoppt
先运行mkdir.py
视频文件放入workspace/video中
运行main.py
图像差异的参数请修改compare.py中的if np.std(difference)<4:

converter用的是ffmpeg切割视频，converterold用的是cv2切割视频
