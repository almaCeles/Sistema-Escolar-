import tkinter as tk
from tkinter import font
from tkinter import *
import ConsultasBd

class divide():
    listaZ=[]
    liztaya=[]
    distancia=1
 
    
    
    
    dimencionX="100"
    dimencionY="60"
    c=ConsultasBd.ConsultarBd()


    

    def __init__(self): 
        self.letra = font.Font(family="Helvetica", size=12, weight="bold")

    
    def CargarReservaciones(self,dia):
       self.distancia=1
       self.liztaya=[]
       self.listaZ=[]
       self.listaZ=self.c.ConsultaReservacionesDia(dia)
       #print(self.listaZ)
       for x in self.listaZ:
           
           self.CrearSTR(x)

    def CrearSTR(self,x):
        texto=str(x[0])+"-"+str(x[1])+" Reservado Por El Profesor "+str(x[2])
        
        self.liztaya.append(texto)

    def Cargatabs(self,donde):
        color = "#%02x%02x%02x" % (64, 83, 104)
        for x in self.liztaya :
            l=tk.Label(donde, text=x, bg=color,font=self.letra, fg="black")
            l.place(x=10,y=50*self.distancia)
            self.distancia=self.distancia+1
        
        


def main():
   
    v=divide()
    v.CargarReservaciones("1")
    n=input()
    v.CargarReservaciones("1")
    return 0
   
if __name__=='__main__':
   main() 
