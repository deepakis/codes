from tkinter import *
code = Tk()
code.geometry("400x500")
def hi(event):
    
    global val
    text= event.widget.cget("text")
    if  text == "=":
        if val.get().isdigit():
            value = int(val.get())
            # val.set(value)
            # screen.update() 
        else:
            try:
                value = eval(screen.get())
                val.set(value)

            except Exception as e:
                print(e)
                value = "Error"
    elif text =="C":
        val.set("")
        screen.update()
    elif text == " Quit ":
        code.quit()
    else:
        text= event.widget.cget("text")
        val.set(val.get()+text)
        screen.update()

val= StringVar()
val.set("")
screen = Entry(code,textvar=val,font ="lucida 45 bold")
screen.pack(pady= 20 )

f = Frame(code,bg = "black")
a=["9","8","7"," * ","C"]
for i in a :

    b = Button(f,text=i,font= "lucida 30 bold")
    # if i == "=":
        # b.
    b.pack(side= LEFT,padx= 10,pady=10)
    b.bind("<Button-1>",hi)
f.pack()
f = Frame(code,bg = "black")
a=["6","5","4","%","+"]
for i in a :
    b = Button(f,text=i,font= "lucida 30 bold")
    b.pack(side= LEFT,padx= 10,pady=10)
    b.bind("<Button-1>",hi)
f.pack()
f = Frame(code,bg = "black")
a=["3","2","1","0"," - "]
for i in a :
    b = Button(f,text=i,font= "lucida 30 bold")
    b.pack(side= LEFT,padx= 10,pady=10)
    b.bind("<Button-1>",hi)
f.pack()
f = Frame(code,bg = "black")
a=[" Quit ","/",".","="]
for i in a :
    b = Button(f,text=i,font= "lucida 30 bold")
    b.pack(side= LEFT,padx= 10,pady=10)
    b.bind("<Button-1>",hi)
f.pack()

code.mainloop()
