from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
def paste():
    pass
def new():
    global file
    file = None 
    code.title("Untittle - Notepad")
    textarea.delete(1.0,END)  
def Cut():
    textarea.delete(1.0,END)
def exit():
    a=showinfo("Attention","Do you want to exit")
    # print(a)
    if a == "ok":
        textarea.destroy()
        code.quit()

    
def save():
     global file
     if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
                file = None

        else:
            
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
     else:
        
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    
def about():
    showinfo("Detail","this is notepad made by deepak")
def edit():

    pass
def copy():
    val=textarea.get(1.0,END)
    f.close()
    code.title(os.path.basename(file) + " - Notepad")
    print ("file saved")
    showinfo("Done","Your whole contant is copied \nuse Ctrl+v to  paste ")
    textarea.clipboard_append(val)
def openfile():
     global file
     file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
     if file == "":
        file = None 
     else:
        code.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file,"r")
        textarea.insert(1.0, f.read())
        f.close()

if __name__== "__main__":
    code = Tk()
    code.geometry ("753x653")
    code.title("Untittle - Notepad")
    textarea = Text(code,font= "lucida 25 italic")
    file= None
    textarea.pack(expand= True,fill = BOTH)
    
    MenuBar = Menu(code)
    m = Menu(MenuBar)
    m.add_command(label= "new",command = new )
    m.add_command(label= "save",command = save )
    m.add_command(label= "open",command = openfile )
    
    m.add_command(label= "exit",command = exit )
    code.config(menu=MenuBar)
    MenuBar.add_cascade(label="file",menu= m)
    m1 = Menu(MenuBar)
    m1.add_command(label= "Edit",command = edit )
    m1.add_command(label= "Paste",command = paste )
    m1.add_command(label= "Copy",command = copy )
    
    m1.add_command(label= "Cut",command = Cut )
    code.config(menu=MenuBar)
    MenuBar.add_cascade(label="Edit",menu= m1)
    m2 =Menu(MenuBar)
    m2.add_command(label="About ",command = about)
    MenuBar.add_cascade(label ="About",menu= m2)
    
    val= None
    
    
    code.mainloop()





