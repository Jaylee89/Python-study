#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #self.nameInput = Label(self, text='Hello, world!')
        self.nameInput = Entry(self)
        self.nameInput.pack()
        #self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton = Button(self, text='Hello', command=self.hello)
        #pack() 方法把 Widget 加入到父容器中，并实现布局。 pack() 是最简单的布局， grid() 可以实现更复杂的布局
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)
        #exit()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()