#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'fyby'

from Tkinter import *           # 导入 Tkinter 库
win = Tk()                     # 创建窗口对象的背景色
win.title('Hello Python')    #定义窗体标题

# 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(win)          #  创建两个列表组件
listb2 = Listbox(win)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()

def hello():
    print('hello Python!')

btn = Button(win, text='Click me', command=hello)
#注意这个地方，不要写成hello(),如果是hello()的话，
#会在mainloop中调用hello函数，
# 而不是单击button按钮时出发事件
btn.pack(expand=YES, fill=BOTH) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)


win.mainloop()                 # 进入消息循环