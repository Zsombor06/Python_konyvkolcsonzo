from tkinter import *
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
import random
from tkinter import Menu
from kereso import kereso
from kijelentkezo import kijelentkezo

login = Tk()
login.geometry("300x200")
login.resizable(False,False)
login.title("Bejelentkezés")
vonalkod=random.randint(10000000,99999999)

def sugo():
    messagebox.showinfo("Súgó", f"A vonalkódok: {vonalkod}")

def bejelentkez():
    jok=0
    if((vonalkod1_bemenet.get()=="1" and vonalkod2_bemenet.get()=="1")or(vonalkod1_bemenet.get()==str(vonalkod) and vonalkod2_bemenet.get()==str(vonalkod))):
        jok+=1

    if(konyvtar_kivalaszt.get()=="A könyvtár"):
        jok+=1

    if(jok==2):
        kereso(Toplevel())
    else:
        messagebox.showerror("Baj","Baj van")
        vonalkod1_bemenet.delete(0,"") 

def kijelentkezes():
    kijelentkezo(Toplevel())

beazonosit=Label(login,text="Kérem azonosítsa magát:")
vonalkod1 = Label(login,text = "Vonalkód:")
vonalkod2 = Label(login,text = "Vonalkód:")
konyvtar = Label(login,text = "Könyvtár:")
beazonosit.place(x=30,y=20)
vonalkod1.place(x=20,y=45)
vonalkod2.place(x=20,y=75)
konyvtar.place(x=20,y=105)
vonalkod1_bemenet = Entry(login)
vonalkod1_bemenet.insert(0, str(vonalkod)) 
vonalkod2_bemenet = Entry(login)
vonalkod2_bemenet.insert(0, str(vonalkod)) 
vonalkod1_bemenet.place(x=130,y=45)
vonalkod2_bemenet.place(x=130,y=75)


menusav=Menu(login)
menusav.add_command(label="Kijelentkezés",command=kijelentkezes)


konyvtar_kivalaszt = ttk.Combobox(
    values=["A könyvtár"],width=17
)
konyvtar_kivalaszt.insert(0,"A könyvtár")
konyvtar_kivalaszt.place(x=130, y=105)

bejelentkez_gomb=tkinter.Button(login,text="Bejelentkezés", command=bejelentkez)
bejelentkez_gomb.pack()
bejelentkez_gomb.place(x=180,y=150)

sugo_gomb=tkinter.Button(login,text="Súgó", command=sugo)
sugo_gomb.pack()
sugo_gomb.place(x=20,y=150)

login.config(menu=menusav)
login.mainloop()


