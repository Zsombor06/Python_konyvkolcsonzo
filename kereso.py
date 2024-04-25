from tkinter import *
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
from db import getBooksByTitle
from db import getAuthorsByID
from db import getAuthorsByName
from db import getBooksByAuthor
from db import getBooksByCategory
from db import startRent
from tkinter.ttk import *
from raktar import konyvek


def kereso(kereso_oldal):
    def torles():
        cimek_Entry.delete(0,END)
        cimek_Entry.insert(0,"")
        kereses_kivalaszt.delete(0,END)
        kereses_kivalaszt.insert(0,"Cím")
        konyvtar_kivalaszt.delete(0,END)
        konyvtar_kivalaszt.insert(0,"A könyvtár")
    def keresett():
        global konyv_id
        if(kereses_kivalaszt.get()=="Cím"):
            canvas.pack_forget()
            frame.pack()
            for adat in getBooksByTitle(cimek_Entry.get()):
                label=Label(frame,text=adat.title)
                label.grid(row=0,column=1)
                for adat2 in getAuthorsByID(adat.author_id):
                    label2=Label(frame,text=adat2.name)
                    label2.grid(row=1,column=1)
                label2=Label(frame,text=adat.category)
                label2.grid(row=2,column=1)

                konyv_id=adat.id
        if(kereses_kivalaszt.get()=="Szerző"):
            canvas.pack_forget()
            frame.pack()
            for adat in getAuthorsByName(cimek_Entry.get()):
                label2=Label(frame,text=adat.name)
                label2.grid(row=1,column=1)
                for adat2 in getBooksByAuthor(adat.name):
                    label=Label(frame,text=adat2.title)
                    label.grid(row=0,column=1)
                    label2=Label(frame,text=adat2.category)
                    label2.grid(row=2,column=1)
                    konyv_id=adat2.id
        if(kereses_kivalaszt.get()=="Kategória"):
            canvas.pack_forget()
            frame.pack()
            for adat in getBooksByCategory(cimek_Entry.get()):
                label=Label(frame,text=adat.title)
                label.grid(row=0,column=1)
                for adat2 in getAuthorsByID(adat.author_id):
                    label2=Label(frame,text=adat2.name)
                    label2.grid(row=1,column=1)
                label2=Label(frame,text=adat.category)
                label2.grid(row=2,column=1)
                konyv_id=adat.id


    def berles():
        startRent(konyv_id)
    #keresés
    kereso_oldal.title("Kereső")
    kereso_oldal.geometry("520x300")
    canvas=Canvas(kereso_oldal,width=500,height=500)
    oldal_cim=Label(canvas,text="Egyszerű keresés:",font="Arial 18")
    canvas.create_window(100,20,window=oldal_cim)
    cimek=Label(canvas,text="Keresett szó:")
    cimek_Entry=Entry(canvas,width=30)
    canvas.create_window(50,60,window=cimek)
    canvas.create_window(180,60,window=cimek_Entry)
    kereses=Label(canvas,text="Mező a kereséshez:")
    canvas.create_window(65,85,window=kereses)
    kereses_kivalaszt = Combobox(canvas,values=["Cím","Szerző","Kategória"],width=17)
    kereses_kivalaszt.insert(0,"Cím")
    canvas.create_window(180,85,window=kereses_kivalaszt)
    konyvtar=Label(canvas,text="Adtabázis:")
    canvas.create_window(65,110,window=konyvtar)
    konyvtar_kivalaszt = Combobox(canvas,values=["A Könytár"],width=17)
    konyvtar_kivalaszt.insert(0,"A könyvtár")
    canvas.create_window(180,110,window=konyvtar_kivalaszt)
    gomb1=Button(canvas,text="Mehet",command=keresett)
    canvas.create_window(130,150,window=gomb1)
    gomb2=Button(canvas,text="Törlés",command=torles)
    canvas.create_window(210,150,window=gomb2)
    canvas.pack()
    #keresett
    frame=Frame(kereso_oldal,width=500,height=500)
    cim=Label(frame,text="Cím:")
    cim.grid(row=0,column=0)
    iro=Label(frame,text="Író")
    iro.grid(row=1,column=0)
    kategoria=Label(frame,text="Kategória:")
    kategoria.grid(row=2,column=0)
    gomb3=Button(frame,text="Felvétel",command=berles)
    gomb3.grid(row=4,column=1,columnspan=2,padx=20)
    gomb3.config(width=20)
    
 
