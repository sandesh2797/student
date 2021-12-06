#Python program for internet  speed checker

from tkinter import *
from tkinter import message
import pyspeedtest

def one() :
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1=str(speed.download()  ) + "[Bytes per sec"
    
    messagebox.showinfo("Your download speed is ",a1)
root=tk()
root.title("Internet speed checker .....")
root.config(bg="lightellow")
root.geometry("500x250")
l1 = Label(root,text="Internet Speed Checker ", font="Arial",26, "bold", bg="lightblue").pack()
b1=Button(root,text="click ..", font=("Arial",18,"Bold",bg="yellow", height=1, width=10, command=one()).pack()

root.mainloop()