from tkinter import *
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
import tkinter
from tkinter.ttk import *
from tkinter import ttk
from tkinter import Menu
import kereso

def megnyitando(epolc_oldal):
    def hozzaad():
        l1_1=Label(frame,text=1)
        l2_1=Label(frame,text=kereso.szerzo)
        l3_1=Label(frame,text=kereso.cim)
        l4_1=Label(frame,text=kereso.kategoria)
        l5_1=Label(frame,text="A konyvtar")

        l1_1.grid(row = 1, column = 1, pady = 20,padx=30)
        l2_1.grid(row = 1, column = 2, pady = 20,padx=30)
        l3_1.grid(row = 1, column = 3, pady = 20,padx=30)
        l4_1.grid(row = 1, column = 4, pady = 20,padx=30)
        l5_1.grid(row = 1, column = 5, pady = 20,padx=30)



   

    epolc_oldal.title("E-polcom")
    epolc_oldal.geometry("540x200")

    frame = Frame(epolc_oldal)
    frame.place(x=10,y=10)
    frame.grid(row=0, column=0, padx=0, pady=0)
    l1 = Label(frame, text = "#")
    l2 = Label(frame, text = "Szerző:")
    l3 = Label(frame, text = "Cím:")
    l4 = Label(frame, text = "Kategória:")
    l5 = Label(frame, text = "Könyvtár:")


    l1.grid(row = 0, column = 1, sticky = W, pady = 20,padx=30)
    l2.grid(row = 0, column = 2, sticky = W, pady = 20,padx=30)
    l3.grid(row = 0, column = 3, sticky = W, pady = 20,padx=30)
    l4.grid(row = 0, column = 4, sticky = W, pady = 20,padx=30)
    l5.grid(row = 0, column = 5, sticky = W, pady = 20,padx=30)



    frame1 = Frame(epolc_oldal)
    frame1.place(x=200,y=100)
    frame1.grid(row=10, column=0, padx=0, pady=0)

    frissites_gomb=tkinter.Button(frame1,text="Frissítés", command=hozzaad)
    frissites_gomb.grid(row = 10, column = 1, sticky = W, pady = 20,padx=30)



