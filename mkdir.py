import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"
    else:
        print
        "---  There is this folder!  ---"

file = "./workspace/pptx"
file1= "./workspace/temp"
file2= "./workspace/temp2"
file3= "./workspace/temp3"
file4= "./workspace/video"
mkdir(file)
mkdir(file1)
mkdir(file2)
mkdir(file3)
mkdir(file4)

