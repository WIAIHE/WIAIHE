# 补充第40行代码，定义文字按钮
# 补充第47行代码，定义图片按钮
# 补充第50行代码，用grid布局显示button3图片按钮
import tkinter
from PIL import Image, ImageTk
import webbrowser
from carton import *

imgNum = 0
# 在nameList里添加每张图片对应的名称
# 一定要和左侧你添加的图片名一一对应，可以添加美食图片、自拍都可以哦！
nameList = [
    "哪吒",
    "中国机长",
    "天气之子",
    "狮子王",
    "蜘蛛侠",
    

] 
def nextOne():
    global root, imgNum
    imgNum = imgNum + 1
    if imgNum > len(nameList)-1:
        imgNum = 0
    button0.configure(text = nameList[imgNum])
    nextPic(button3,nameList[imgNum])

def lastOne():
    global root, imgNum
    imgNum = imgNum - 1
    if imgNum < 0:
        imgNum = len(nameList) - 1
    button0.configure(text = nameList[imgNum])
    lastPic(button3,nameList[imgNum]) 

root = tkinter.Tk()
button0 = tkinter.Button(root, text=nameList[imgNum])
button0.grid(row=0, column=0, columnspan=2)
# ------补充下一行代码，定义按钮button1，按钮显示文字"上一部"并绑定lastOne函数------
button1 = tkinter.Button(root,text="上一部", command=lastOne)
button1.grid(row=1, column=0)
button2 = tkinter.Button(root, text="下一部", command=nextOne)
button2.grid(row=1, column=1)
image = Image.open("哪吒.jpg")
photo = ImageTk.PhotoImage(image)
# ------补充下一行代码，给button3图片按钮添加图片photo------
button3 = tkinter.Button(root,image = photo)
# ------补充下一行代码，用grid布局显示button3图片按钮------
# 提示：button3的行row为2，列column为0，跨度columnspan为2
button3.grid(row = 2,column = 0,columnspan = 2)
root.mainloop()
