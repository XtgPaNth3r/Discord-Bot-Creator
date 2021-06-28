from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()
window.geometry('1000x1000')

def newimpo():
    label = Label(window,text = 'Imports = i',bg="red",width=10,height=5)
    label.place(x=100,y=100)

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)

def setprefix():
    label = Label(window,text = 'Set Prefix = p',bg="red",width=10,height=5)
    label.place(x=100,y=100)

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)

def newcommand():
    label = Label(window,text = 'Command = c',bg="red",width=10,height=5)
    label.place(x=100,y=100)

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)

def token():
    label = Label(window,text = 'Token = t',bg="red",width=10,height=5)
    label.place(x=100,y=100)

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)

def say():
    label = Label(window,text = 'Say = s',bg="red",width=10,height=5)
    label.place(x=100,y=100)

    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)
    
newimp = Button(window, text='Imports', command=newimpo).pack()
newpre = Button(window, text='Prefix', command=setprefix).pack()
ncmd = Button(window, text='Command', command=newcommand).pack()
say = Button(window, text='Say', command=say).pack()
tok = Button(window, text='Token', command=token).pack()

window.mainloop()
