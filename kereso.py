from tkinter import *
from tkinter import Entry
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox
import tkinter
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
        canvas.pack_forget()
        frame.pack()
        kivalaszt=kereses_kivalaszt.get()
        print(konyvek.index(kivalaszt))
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
    kereses_kivalaszt = Combobox(canvas,values=["Cím","Vonalkód","Szerző","Kiadó","Nyelvkód"],width=17)
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
    for adat in konyvek:
        sorok=0
        konyv_cim=Label(frame,text=adat.cim)
        cim=Label(frame,text="Cím:")
        cim.grid(row=sorok,column=0)
        konyv_cim.grid(row=sorok,column=1)
        konyv_vonalkod=Label(frame,text=adat.vonalkod)
        sorok+=1
        vonalkod=Label(frame,text="Vonalkód:")
        vonalkod.grid(row=sorok,column=0)
        konyv_vonalkod.grid(row=sorok,column=1)
        konyv_szerzo=Label(frame,text=adat.szerzo)
        sorok+=1
        szerzo=Label(frame,text="Szerző:")
        szerzo.grid(row=sorok,column=0)        
        konyv_szerzo.grid(row=sorok,column=1)
        konyv_kiado=Label(frame,text=adat.kiado)
        sorok+=1
        kiado=Label(frame,text="Kiadó:")
        kiado.grid(row=sorok,column=0)        
        konyv_kiado.grid(row=sorok,column=1)
        konyv_ev=Label(frame,text=adat.ev)
        sorok+=1        
        konyv_ev.grid(row=sorok,column=1)
        ev=Label(frame,text="Év:")
        ev.grid(row=sorok,column=0)
        konyv_nyelvkod=Label(frame,text=adat.nyelvkod)
        sorok+=1        
        nyelvkod1=Label(frame,text="Nyelvkód:")
        nyelvkod1.grid(row=sorok,column=0)
        konyv_nyelvkod.grid(row=sorok,column=1)
        konyv_konyvtar=Label(frame,text=adat.konyvtar)
        sorok+=1
        konyvtar1=Label(frame,text="Könyvtár")
        konyvtar1.grid(row=sorok,column=0)        
        konyv_konyvtar.grid(row=sorok,column=1)       
