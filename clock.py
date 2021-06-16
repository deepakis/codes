from tkinter import *
from tkinter.ttk import *
from time import strftime
a=Tk()


# def speak():
    # pass
date ="date="
day = "day="
tim="time="
def time():
    stri=strftime(f"{date}%D \n{tim}%H:%M:%S %A")
    b.config(text=stri)
    b.after(1,time)
    
a.title("clock")
b =Label(a,font=("elegant_4.zip",50),background="black",foreground="cyan")
b.pack(anchor="center")
time()
# def speak():s

    # stri.speak()
mainloop()
# speak()
