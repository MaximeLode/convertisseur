from tkinter import *
from tkinter import ttk

window = Tk()
window.title("convertisseur")
window.geometry("600x400")
titel = Label(window, text="convertisseur", font=34,)
titel.place(x=250, y=0)

def convert1():
    
    value = float(saisie.get())
    value_conv = value * USD
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert2():
    
    value = float(saisie.get())
    value_conv = value * EURO
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)


def convert3():
    
    value = float(saisie.get())
    value_conv = value * HKE
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert4():
    
    value = float(saisie.get())
    value_conv = value * HKD
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert5():
    
    value = float(saisie.get())
    value_conv = value * EUROHK
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert6():
    
    value = float(saisie.get())
    value_conv = value * USDHK
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert7():
    
    value = float(saisie.get())
    value_conv = value * YEND
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert8():
    
    value = float(saisie.get())
    value_conv = value * YENE
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert9():
    
    value = float(saisie.get())
    value_conv = value * YENHK
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)

def convert10():
    
    value = float(saisie.get())
    value_conv = value * EUROYEN
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)
def convert11():
    
    value = float(saisie.get())
    value_conv = value * USDYEN
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)
def convert12():
    
    value = float(saisie.get())
    value_conv = value * HKYEN
    saisie2.delete(0, END)
    saisie2.insert(0, value_conv)
USD = 1.07
EURO = 0.93
HKE = 8.43
HKD = 7.85
EUROHK = 0.12
USDHK = 0.12739675
YEND = 131.05833
YENE = 140.71066
YENHK = 16.69616
EUROYEN = 0.0071063219
USDYEN = 0.0076293495
HKYEN = 0.059886012
saisie = Entry(window, width=100, bg='yellow')
saisie.place(x=0, y=120)
bouton = Button( window , text = "USD to euro", width=8, bg = "orange" , fg = "black",command= convert1)
bouton.place(x=0, y=140)

bouton2 = Button( window , text = "Euro to USD", width=8, bg = "orange" , fg = "black",command= convert2)
bouton2.place(x=70, y=140)
bouton3 = Button( window , text = "Euro to HK",  width=8, bg = "orange" , fg = "black",command= convert3)
bouton3.place(x=70, y=170)
bouton4 = Button( window , text = "USD to HK",  width=8, bg = "orange" , fg = "black",command= convert4)
bouton4.place(x=0, y=170)
bouton5 = Button( window , text = "HK to Euro",  width=8, bg = "orange" , fg = "black",command= convert5)
bouton5.place(x=140, y=140)
bouton6 = Button( window , text = "HK to USD",  width=8, bg = "orange" , fg = "black",command= convert6)
bouton6.place(x=140, y=170)
bouton7 = Button( window , text = "USD to YEN",  width=8, bg = "orange" , fg = "black",command= convert7)
bouton7.place(x=0, y=200)
bouton8 = Button( window , text = "Euro to YEN",  width=8, bg = "orange" , fg = "black",command= convert8)
bouton8.place(x=70, y=200)
bouton9 = Button( window , text = "HK to YEN",  width=8, bg = "orange" , fg = "black",command= convert9)
bouton9.place(x=140, y=200)
bouton10 = Button( window , text = "YEN to Euro",  width=8, bg = "orange" , fg = "black",command= convert10)
bouton10.place(x=210, y=140)
bouton11 = Button( window , text = "YEN to USD",  width=8, bg = "orange" , fg = "black",command= convert11)
bouton11.place(x=210, y=170)
bouton12 = Button( window , text = "YEN to HK",  width=8, bg = "orange" , fg = "black",command= convert12)
bouton12.place(x=210, y=200)
saisie2 = Entry(window, width=100, bg='blue')
saisie2.place(x=0, y=240)




window.mainloop()