#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel = Label(self, text = 'Hello, World!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text = 'Quit', command = self.quit)
		self.quitButton.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text = 'Hello', command = self.hello)
		self.alertButton.pack()
		
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)
		
app = Application()
app.master.title('Hello World')
app.mainloop()		
		
		
from turtle import *

width(6)
forward(200)
right(45)
pencolor('red')
forward(100)
right(90)
forward(100)
pencolor('green')
right(45)
forward(200)
pencolor('blue')
right(90)
forward(100*1.41421)
done()

def drawStar(x, y):
	pu()
	goto(x, y)
	pd()
	seth(0)	
	for i in range(5):
		fd(40)
		rt(144)

pencolor('red')
width(3)
for x in range(0, 250, 50):		
	drawStar(x, 10)

done()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	