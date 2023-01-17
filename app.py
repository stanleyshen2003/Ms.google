import tkinter as tk
import os
from gtts import gTTS
from playsound import playsound

root = tk.Tk()
slitemove=-10
# set icon & title
if(os.path.isdir('icon')):
    if(os.path.isfile('icon/icon.png')):
        root.iconphoto(True, tk.PhotoImage(file='icon/icon.png'))
root.title('speak with the voice of Ms. Google')


records=[]
dis=[]


# open save.txt & create directory for storing .mp3s
if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempR = f.read()
        temp = tempR.split('@#')
        temp.pop(-1)
        records = temp
if(os.path.isdir('./mp3s')==False):
    os.mkdir('mp3s')

# update the records
def renewRecord():
    for i in dis:
        i.destroy()
    y=350
    for i in range(len(records)):
        label = tk.Label(root,text=str(i+1)+'. '+records[i],bg="black",fg='white')
        dis.append(label)
        canvas.create_window(200, y+slitemove, window=label)
        y+=20

# generate and read the txt sent as parameter by creating .mp3
def readtxt(txt):
    tts=gTTS(text=txt, lang='zh-tw')
    voicepath = "./mp3s/"+txt+".mp3"
    tts.save(voicepath)
    if(os.path.isfile(voicepath)):
        playsound(voicepath)

# for reading records
def readprev():
    num=e3.get()
    if(num==''):
        num="1"
    index=int(num)
    if(len(records)>=index):
        txt=records[index-1]
        readtxt(txt)

# for reading normal input
def read():
    txt = e.get()
    if txt not in records:
        records.append(txt)
        if(len(records)==11):
            delpath="./mp3s/"+records[0]+".mp3"
            if(os.path.isfile(delpath)):
                os.remove(delpath)
            records.pop(0)

    readtxt(txt)
    renewRecord()
    
# only input integer
def validate(P):
    if str.isdigit(P) or P == '':
        return True
    else:
        return False

# draw!
canvas = tk.Canvas(root,height=600,width=600,bg="#263D42")
canvas.pack()

frame = tk.Frame(root,bg="black")
frame.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05)

# normal input
lb=tk.Label(root, text="input a senetence",bg="black",fg='white')
lb.config(font=('helvetica', 17))
canvas.create_window(303,130+slitemove,window=lb)

e = tk.Entry(root,width=30,font=('微軟正黑體',16))
canvas.create_window(303, 200+slitemove, window=e)

btn1 = tk.Button(root, text='read', command=read)   # 放入顯示按鈕，點擊後執行 show 函式
btn1['font']=('times new roman',15)
canvas.create_window(303,270+slitemove,window=btn1)

# use record
lb3=tk.Label(root, text="use record",bg="black",fg='white')
lb3.config(font=('helvetica', 15))
canvas.create_window(403,370+slitemove,window=lb3)

vcmd = (root.register(validate), '%P')
e3 = tk.Entry(root,width=2,font=('微軟正黑體',16),validate='key', validatecommand=vcmd)
canvas.create_window(483, 370+slitemove, window=e3)

btn2 = tk.Button(root, text='read', command=readprev)   # 放入顯示按鈕，點擊後執行 show 函式
btn2['font']=('times new roman',15)
canvas.create_window(423,470+slitemove,window=btn2)

renewRecord()
root.mainloop()

# save the records
with open('save.txt','w') as f:
    for rcd in records:
        f.write(rcd+'@#')