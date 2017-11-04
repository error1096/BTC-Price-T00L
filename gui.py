from Tkinter import *
import tkMessageBox
import requests
import ttk as tk

root = Tk()

rootLeft = Frame(root)
rootLeft.pack(side=LEFT)

rootRight = Frame(root)
rootRight.pack(side=RIGHT)

rootBottom = Frame(root)
rootBottom .pack(side=BOTTOM)

rootTop = Frame(root)
rootTop .pack(side=TOP)


def window():
    root.configure(background='gray15')
    root.title("BTC Price")
    root.geometry("300x300")
    root.resizable(0 , 0)
def Price():

    try:
        re = requests.get("https://www.bitstamp.net/api/ticker/")
        out = re.json()
        return out
    except:
        print "Error"
        tkMessageBox.showinfo("error","ERROR IN INTERNET")
def loadImg():
    ph = PhotoImage(file="btc.gif")
    la = Label(root,image=ph)
    la.pack()



window()
loadImg()
p = Price()

def LabelDrw(pos,Tex,ro,col):
    Label(pos, text=Tex,fg="SteelBlue1",bg='gray15').grid(row=ro, column=col)


def fText(pos,Tex,ro,col):
    Label(pos, text=Tex,fg="light green",bg='gray15').grid(row=ro, column=col)


def Lshow():

    LabelDrw(rootTop, "     Last BTC price. : ", 0, 0)
    LabelDrw(rootTop, "$"+str(p["last"])+"\n", 0, 1)

    LabelDrw(rootTop, "Last 24 hours price high: ", 1, 0)
    LabelDrw(rootTop, "$"+str(p["high"])+"\n", 1, 1)

    LabelDrw(rootTop, "Last 24 hours price low : ", 2, 0)
    LabelDrw(rootTop, "$"+str(p["low"])+"\n", 2, 1)

    LabelDrw(rootTop, "   Highest buy order : ", 3, 0)
    LabelDrw(rootTop, "$"+str(p["bid"])+"\n", 3, 1)

    LabelDrw(rootTop, "   Lowest sell order : ", 4, 0)
    LabelDrw(rootTop, "$"+str(p["ask"])+"\n", 4, 1)

    LabelDrw(rootTop, "   First price of the day: ", 5, 0)
    LabelDrw(rootTop, "$"+str(p["open"])+"\n", 5, 1)
def footer():
    fText(rootBottom,"- Code By err0r1096 -\n c-137.org",0,0)


Lshow()
footer()
root.mainloop()