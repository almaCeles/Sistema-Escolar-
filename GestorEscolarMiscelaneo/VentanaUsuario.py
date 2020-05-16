import tkinter as tk
from tkinter import*
from tkinter import ttk
import tabs
import BdUsuario
import Fecha 
import ConsultasBd

class VentanaUsuario(ttk.Frame):
  
  def __init__(self):
    
    self.fUsu=tk.Frame()
    self.fUsu.config(width="156", height="400",bg="gray84")
    self.pintar()
    self.c=ConsultasBd.ConsultarBd()

#---------evento de el boton validar usuario
  def cambio(self, evt):
    self.llena=Label(self.fUsu, text="")
    self.llena.config(fg="orange red",bg="gray84")
    self.llena.place(x=13,y=240)
    if (self.cContra.get()!=""  and self.cUsuario.get()!=""):
     self.c.ConsultaUsuario(self.cUsuario.get(), self.cContra.get())
     if(BdUsuario.BdUsurio.Usuario==self.cUsuario.get() and  BdUsuario.BdUsurio.Contra==self.cContra.get()):
      BdUsuario.BdUsurio.Bandera=True
      self.cContra.delete(0, END)
      
      
      print("corecto")
      self.fUsu.place_forget()

     else: 
      self.llena.config(text="Datos incorrectos")
    else:
     self.llena.config(text="Datos vacios")
     


  def pintar(self):
    
    l=Label(self.fUsu, text="LOGIN")
    l.config(font=("AvantGarde Bk BT",22), fg="gray13", bg="gray84")
    l.place(x=30, y=10)
    self.cUsuario=Entry(self.fUsu)
    self.cUsuario.place(x=13,y=85)
    self.cUsuario.config(bg="gray94")
    self.lUsuario=Label(self.fUsu, text="Usuario")
    self.lUsuario.config(bg="gray84")
    self.lUsuario.place(x=55,y=110)


    self.cContra=Entry(self.fUsu)
    self.cContra.place(x=13,y= 140)
    self.cContra.config(show="*")
    self.lContra=Label(self.fUsu, text="Pasword")
    self.lContra.config(bg="gray84")
    self.lContra.place(x=55,y=160)
    self.Bandera=False
    self.bOk=Button(self.fUsu, text="Ingresar")
    self.bOk.place(x=55,y=190)
    self.bOk.bind("<ButtonPress-1>",self.cambio)
  
 
      
def main():
    

    v=VentanaUsuario()

  
    return 0

if __name__=='__main__':
  main()  
