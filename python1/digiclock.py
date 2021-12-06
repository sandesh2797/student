from tkinter import *
from time import strftime    # to return time in str format
root=Tk()
root.title('DIGITAL CLOCK .....')
root.geometry('600x130')     # width and ht
def disp_time():
    c_time=strftime("%H:%M:%S %p")
    lbl.config(text=c_time)
    lbl.after(1000, disp_time)      # disp live digital clock
lbl=Label(root,text="Time",font=('Arial',60), bg='white' , fg='blue')
lbl.pack()
disp_time()
root.mainloop()