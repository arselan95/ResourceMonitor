import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

root = Tk() 
root.title('System monitor') 

device = Label(root, font=("Helvetica", 16),  text='MacBook Pro', justify=LEFT) 
device.pack(anchor=W ) 


processor= Label(root, font=("Helvetica", 16),  text='Processor: intel x86 ', justify=LEFT) 
processor.pack(anchor=W) 

a = "User: Arselan"
user= Label(root, font=("Helvetica", 16),  text=a, justify=LEFT) 
user.pack(anchor=W) 

#divider
w = Canvas(root, width=600, height =20) 
w.pack(anchor=W) 
canvas_height=20
canvas_width=500
y = int(canvas_height ) 
w.create_line(0, y, canvas_width, y) 

#buttons
frame = Frame(root) 
frame.pack(anchor=W) 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM , anchor=W) 

cpu = Button(frame, text = 'CPU', fg ='red') 
cpu.pack( side = BOTTOM, anchor=W) 

mem = Button(frame, text = 'MEM P', fg='brown') 
mem.pack( side = BOTTOM,anchor=W ) 

memb = Button(frame, text ='MEM B', fg ='blue') 
memb.pack( side = BOTTOM, anchor=W ) 

disk = Button(frame, text ='DISK USAGE', fg ='black') 
disk.pack( side = BOTTOM, anchor=W) 




root.mainloop() 