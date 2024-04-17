from tkinter import *
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
import tkinter
from tkinter.ttk import *



def kijelentkezo(kijelentkezo_oldal):
    kijelentkezo_oldal.title("Kijelentkezés")
    kijelentkezo_oldal.resizable(False,False)
    kijelentkezo_oldal.geometry("400x100")

    def meghal():
        kijelentkezo_oldal.quit()

    kilepes=Label(kijelentkezo_oldal,text="Kilépés")
    kilepes_szoveg=Label(kijelentkezo_oldal,text="Kilépés esetén az összes korábbi keresési eredmény elveszik.")
    mehet_gomb=Button(kijelentkezo_oldal,text="Mehet!",command=meghal)
    kilepes.place(x=20,y=10)
    kilepes_szoveg.place(x=20,y=50)
    mehet_gomb.place(x=20,y=70)
