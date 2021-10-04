# Created By Samyak Bumb

from tkinter import *
from tkinter import font
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Clock By Samyak Bumb")

def time():
   string=strftime('%H:%M:%S %p')
   Label.config(text=string)
   Label.after(1000, time)

Label=Label(root,font=("ds-digital",80),background="black",foreground="#00FFFF")
Label.pack(anchor='center')

time()
mainloop()
