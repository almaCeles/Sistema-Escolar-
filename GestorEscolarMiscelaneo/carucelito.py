import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import threading
import ConsultasBd
import time

class Carucel(ttk.Frame):
    c=ConsultasBd.ConsultarBd()
    conta=0
    def __init__(self):
        self.color = "#%02x%02x%02x" % (64, 83, 104)
        self.caru=tk.Frame()
        self.caru.config(width="1000", height="170", bg=self.color)
        self.posicionArreglo()
        self.contenidoinmovil()
        


        
    def contenidoinmovil(self):
      
     self.label = Label(self.caru, background=self.color) 
     self.mostrarImagen(self.label, "images/izq.png")
     self.label.place(x=0,y=45)
     self.label.bind('<Button-1>', self.izquierda)

     self.foto=Label(self.caru, text="Foto")
     try:
         self.mostrarImagen(self.foto, self.fotoo[0])
         self.foto.place(x=280,y=0)
         self.noticia=Label(self.caru, text=self.noticias[0] , bg=self.color, fg="white smoke", font=("AvantGarde Bk BT",13))
         self.noticia.place(x=550,y=20)
     except:
         print("no hay imagenes")
     

     


     self.label2 = Label(self.caru, background=self.color)
     self.mostrarImagen(self.label2,"images/dere.png")
     self.label2.place(x=950,y=45)
     self.label2.bind('<Button-1>', self.derecha)
    def izquierda(self, evt):
       try:
        self.conta-=1
        self.mostrarImagen(self.foto,self.fotoo[self.conta])
        self.noticia.config(text=self.noticias[self.conta])
       except:
        self.conta=len(self.tupla)
        self.conta-=1
    def derecha(self, evt):
       try: 
        self.conta+=1
        self.mostrarImagen(self.foto,self.fotoo[self.conta])
        self.noticia.config(text=self.noticias[self.conta])
       except:
           self.conta=0
           print("no hay mas noticias")

    def mostrarImagen(self,fot,d ):
        self.imgg=Image.open(""+d+"")
        ta = ImageTk.PhotoImage(self.imgg)
        fot.config( image=ta)
        fot.image = ta
        print("metodo ejecutado")

    def posicionArreglo(self):
      self.tupla=self.c.noticias()
      self.fotoo=[]
      self.noticias=[]

      try:
          for i in range(len(self.tupla)):
            numeroTupla=self.tupla[i]

            self.fotoo.append(numeroTupla[0])
            self.noticias.append(numeroTupla[1])
      except:
          print()
      



