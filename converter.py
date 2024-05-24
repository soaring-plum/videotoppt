
import subprocess
def main(videopath,imgpath,r=1):
    w='./workspace/video/'
    r="-r "+r#每秒几帧
    s = "ffmpeg -i " +videopath+" "+r +" -start_number 1 "+ imgpath+"%05d.jpg "+"-threads auto "
    subprocess.call(s,shell=True)
if __name__=='__main__' :
    main("ts.ts",1)