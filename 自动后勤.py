#利用pyautogui模块中的locateOnScreen找出图片在屏幕中的位置，但是locateOnScreen只是简单的颜色对比，所以不同的梯队回归只能抓取左上角的后勤支援获得
#点击后勤支援获得之后会弹出对话框是否继续后勤，这时候找出确定键在屏幕中的位置

import pyautogui as pag #引入pyautogui
import time #引入time

x = 0 #初始化x坐标
y = 0 #初始化y坐标
coordination_list = [] #初始化坐标列表

def mouseclick(pic): #定义鼠标点击函数，pic为图片路径
    coordination_list = pag.locateOnScreen(pic) #locateOnScreen(pic)是寻找图片在屏幕中的位置，会返回图片四个角的坐标点。赋值给坐标列表
    x , y = pag.center((coordination_list[0],coordination_list[1],coordination_list[2],coordination_list[3])) #center求出坐标列表中的四个坐标点的中心点并将中心点坐标赋值给x,y
    pag.click(x,y) #模拟鼠标点击坐标点(x,y)
    time.sleep(1) #暂停1秒

while True: #无限循环
    if pag.locateOnScreen(后勤支援获得.png) != None: #如果能在屏幕中找到后勤支援获得图片的位置
        mouseclick(后勤支援获得.png) #点击后勤支援获得所在位置
        mouseclick(后勤确定.png) #点击后勤确定所在位置
    else:
        time.sleep(10) #暂停10秒
