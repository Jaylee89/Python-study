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
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text=u'生成', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        #name = self.nameInput.get() or 'world'
        #tkMessageBox.showinfo('Message', 'Hello, %s' % name)
        #exit()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()