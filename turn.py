import tkinter
import tkinter.messagebox
def turn():
    global tv8, tv1, tv2, tv3, tv6, tv7, tv9,tv4
    master = "https://zhjx.zafu.edu.cn/vapp/classRoomVideo/video.jhtm"
    building = tv1.get()
    room = tv2.get()
    date = tv3.get()
    classSeq = tv4.get()
    courseNo = tv6.get()
    userNo = tv7.get()
    classRoomNo = ""
    if building == "教1":
        classRoomNo = "101500" + room
    elif building == "教2":
        classRoomNo = "101600" + room
    elif building == "教3":
        classRoomNo = "101700" + room
    elif building == "教4":
        classRoomNo = "101800" + room
    elif building == "教5":
        classRoomNo = "101900" + room
    url = master + "?classRoomNo=" + classRoomNo + "X&date=" + date + "&classSeq=" + classSeq + "&courseNo=" + courseNo + "&userNo=" + userNo
    tv8.set(url)

def about():
    tkinter.messagebox.showinfo("about", "园艺202李翔制作,暂时只支持教学楼")
def download():
    global tv9, tv1, tv2, tv3,tv4
    master = "https://vod.zafu.edu.cn/"
    building = tv1.get()
    room = tv2.get()
    date = tv3.get()
    classSeq = tv4.get()
    if building == "教1":
        classRoomNo = "101500" + room
    elif building == "教2":
        classRoomNo = "101600" + room
    elif building == "教3":
        classRoomNo = "101700" + room
    elif building == "教4":
        classRoomNo = "101800" + room
    elif building == "教5":
        classRoomNo = "101900" + room
    url=master+date+"/"+classRoomNo+"X/1/"+classSeq+"_hls.m3u8"
    tv9.set(url)


top = tkinter.Tk()
top.geometry("480x270")
tv1 = tkinter.StringVar()
tv2 = tkinter.StringVar()
tv3 = tkinter.StringVar()
tv4 = tkinter.StringVar()
tv6 = tkinter.StringVar()
tv7 = tkinter.StringVar()
tv8 = tkinter.StringVar()
tv9 = tkinter.StringVar()
top.title("Wisdom in the mind is better than money in the hand.")
tkinter.Label(top, text="教学楼：").place(x=20,y=20)
tkinter.Entry(top, width=15, textvariable=tv1, background="#00ffff").place(x=100,y=20)

tkinter.Label(top, text="教室：").place(x=20,y=50)
tkinter.Entry(top, width=15, textvariable=tv2, background="#00ffff").place(x=100,y=50)

tkinter.Label(top, text="日期：").place(x=20,y=80)
tkinter.Entry(top, width=15, textvariable=tv3, background="#00ffff").place(x=100,y=80)

tkinter.Label(top, text="第").place(x=20,y=110)
tkinter.Entry(top, width=15, textvariable=tv4, background="#00ffff").place(x=100,y=110)
tkinter.Label(top, text="节课").place(x=220,y=110)

tkinter.Label(top, text="课程编号：").place(x=20,y=140)
tkinter.Entry(top, width=15, textvariable=tv6, background="#00ffff").place(x=100,y=140)
tv6.set("（可不填）")
tkinter.Label(top, text="学号：").place(x=20,y=170)
tkinter.Entry(top, width=15, textvariable=tv7, background="#00ffff").place(x=100,y=170)
tv7.set("（可不填）")
tkinter.Button(top, text="生成网页", command=turn).place(x=15,y=200)
tkinter.Entry(top, width=53, textvariable=tv8, background="#00ffff").place(x=100,y=200)
tkinter.Button(top, text="m3u8网址", command=download).place(x=15,y=230)
tkinter.Entry(top, width=53, textvariable=tv9, background="#00ffff").place(x=100,y=235)
tv8.set("在上面输入 例：教1 404 2022-09-21 1 C0302030 20200107000")
tv9.set("m3u8只需要日期+教学楼+教室+第几节课,可以配合idm和ts助手使用")
tkinter.Button(top, text="?？?？?？?？?？?？?？?？",bg="#FF1493",justify="center", command=about,fg="#00ffff",height=8,width=20).place(x=300,y=20)
top.mainloop()
