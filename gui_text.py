from Tkinter import *
import tkFileDialog as browse
import os
from PIL import Image
import ImageTk
import tkMessageBox as popup
from ascii_text import *


class App:

    def __init__(self,root):
        frame = Frame(root)
        frame.pack()
        self.b1=Button(frame,text="Convert",fg='red',command=self.hey)
        self.b1.pack(side=RIGHT)
        self.b2=Button(frame,text="Load File",fg='black',command=self.browse_it)
        self.b2.pack(side=LEFT)
        self.frame2=Frame(frame)
        self.frame2.pack()
        self.Artwork=None
        self.p=""
        self.n=""
        
    def hey(self):
        if self.p!="" or self.n!="":
            generate(self.p,self.n)
        else:
            popup.showerror("Error!!","First load a file please...")

    def browse_it(self):
        try:
            self.Artwork.destroy()
        except Exception:
            pass
        
        f=browse.askopenfilename()
        t=f.split("/")
        path=""
        for i in range(0,len(t)-1):
            path+=t[i]
            path+="\\"
        fn=t[-1]
        self.p=path
        self.n=fn
        im1=Image.open(f)
        im2=im1.copy()
        im2.thumbnail((128,128),Image.ANTIALIAS)
        im3=ImageTk.PhotoImage(im2)
        self.Artwork=Label(root,image=im3)
        self.Artwork.im3=im3
        self.Artwork.pack(side=BOTTOM)
        
        
def main():
    global root
    root = Tk()
    root.resizable(width=FALSE,height=FALSE)
    root.geometry("400x400")
    app=App(root)
    root.mainloop()

if __name__=='__main__':
    main()
    

