from PIL import Image
import tkMessageBox as popup
import os
from PIL import ImageDraw
from PIL import ImageFont
import textwrap


def second(path,nm):
    img=path+nm
    n,e=nm.split(".")
    im=Image.open(img)
    if im.size[0]>668:
        size = 668,668
        im.thumbnail(size,Image.ANTIALIAS)
        im.save(n+"_copy."+e)
        return n+"_copy."+e
    

def ascii(brightness):
    if brightness>230:
        return " "
    if brightness>200:
        return '.'
    if brightness>170:
        return '7'
    if brightness>130:
        return '+'
    if brightness>100:
        return 'H'
    if brightness>60:
        return '8'
    if brightness>30:
        return '@'
    else:
        return "#"


def ascii2(brightness):
    if brightness>230:
        return "1"
    if brightness>200:
        return '7'
    if brightness>170:
        return '2'
    if brightness>130:
        return '5'
    if brightness>100:
        return '6'
    if brightness>60:
        return '3'
    if brightness>30:
        return '9'
    else:
        return "8"


def Bright(pic,x,y):
    s=0
    c=0
    for y_ in range(y,y+5):
        for x_ in range(x,x+4):
            c+=1
            r,g,b=pic.getpixel((x_,y_))
            b=(r*r*0.241+g*g*0.691+b*b*0.068)**0.5
            s+=b     
    brightness=s/c
    return int(brightness)


def generate(path,nm):
    img=path+nm
    global flag
    img2=second(path,nm)
    if img2==None:
        img2=img
        flag=1
    else:
        flag=0
    pic=Image.open(img2)
    s=pic.size
    f=open(path+nm.split(".")[0]+".txt","w")
    pic=pic.convert('RGB')
    y=0
    x=0
    while y<s[1]-5:
        x=0
        string=""
        while x<s[0]-4:
            c=ascii(Bright(pic,x,y))
            string+=c
            x+=4
        y+=5
        f.write(string+"\n")
    f.close()
    if flag==0:
        os.remove(img2)
    popup.showinfo("File Conveted!!","file saved to the same directory of image")
    

