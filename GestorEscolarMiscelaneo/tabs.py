# coding: utf-8 
import tkinter as tk
from tkinter import ttk
import frameNotifica
import Breservar
import vComponeteH
import BdUsuario 
import Insert
import ConsultasBd


class tabs(ttk.Frame):
    color = "#%02x%02x%02x" % (64, 83, 104)
    
    def __init__(self,m):
        super().__init__(m)
        self.hoja= ttk.Notebook()

        
        # Crear el contenido de cada una de las pestañas.
        self.Lunes = ttk.Label(self.hoja,
            text="",background=self.color)
        self.Martes = ttk.Label(self.hoja,
            text="",background=self.color)
        self.Miercoles = ttk.Label(self.hoja,
            text="",background=self.color)
        self.Jueves = ttk.Label(self.hoja,
            text="",background=self.color)
        self.Viernes = ttk.Label(self.hoja,
            text="",background=self.color)
        self.Reserva = ttk.Label(self.hoja,
           text="",background=self.color)
        self.MyReservas = ttk.Label(self.hoja,
           text="",background=self.color)
        self.n=frameNotifica.frameNotifica()
        
 
        
        
        # Añadirlas al panel con su respectivo texto.
        self.crear()
        self.hoja.add(self.Reserva, text="Reservar", padding=0)
        self.hoja.add(self.MyReservas, text="MyReservas", padding=0)
        self.hoja.add(self.n.Fnotifi, text="Administrador", padding=0)
        self.hoja.config(width="1000", height="450")
        self.barra(self.Reserva)
        self.barra(self.MyReservas)

        self.ocultarTabs()
       ########
        self.BGuardar=ttk.Button(self.Reserva,text="Reservar",command=self.Guardar)
        self.BGuardar.place(x=800,y=300)
       #######
        self.pon()
        self.b=Breservar.Breserva()
        self.b.reservarB(self.Reserva)

   #ocultarlas al inicio antes de ingresar a usuario
    def ocultarTabs(self):
        self.hoja.hide(self.MyReservas)
        self.hoja.hide(self.Reserva)
        self.hoja.hide(self.n.Fnotifi)

    def crear(self):   
        self.hoja.add(self.Lunes, text="Lunes", padding=0)
        self.hoja.add(self.Martes, text="Martes", padding=0)
        self.hoja.add(self.Miercoles, text="Miercoles", padding=0)
        self.hoja.add(self.Jueves, text="Jueves", padding=0)
        self.hoja.add(self.Viernes, text="Viernes", padding=0)
        
        #agregar barra top
        self.barra(self.Lunes)
        self.barra(self.Martes)
        self.barra(self.Miercoles)
        self.barra(self.Jueves)
        self.barra(self.Viernes)
        
        
    #metodo de bonon recerva    
    def Guardar(self):

        idDocente=BdUsuario.BdUsurio.Docente
        i=Insert.Insert()      
        d=self.b.varmenuD.get()
        horaI=self.b.varmenuH.get()[0:5]
        horaF=self.b.varmenuH.get()[6:11]
        print(d[0:1])
        print(idDocente)
        print(horaI)
        print(horaF)
        i.addReservacion(d[0:1],idDocente,horaI,horaF)
        self.pon()
        
        
 
      

    def barra(self,donde):
         l=tk.Label(donde, text="", bg="SeaGreen1",borderwidth=2, relief="groov")#SeaGreen1
         l.config(width=142, height=2) #x ,y
         l.place(x=0, y=0)
         
       
    def pon(self):
         dv=vComponeteH.divide()
         dv.CargarReservaciones('1')
         dv.Cargatabs(self.Lunes)
         dv.CargarReservaciones('2')
         dv.Cargatabs(self.Martes)
         dv.CargarReservaciones('3')
         dv.Cargatabs(self.Miercoles)
         dv.CargarReservaciones('4')
         dv.Cargatabs(self.Jueves)
         dv.CargarReservaciones('5')
         dv.Cargatabs(self.Viernes)
         print("llenaron los taps")
    
    def visibleHojitas(self):
       if (BdUsuario.BdUsurio.Adminstrador==None):
        print("Es Docente")
        self.hoja.add(self.Reserva)
        self.hoja.add(self.MyReservas)
       else:
        print("Es Administrador")  
        self.hoja.add(self.n.Fnotifi)

    def mio(self,usuario):
        color = "#%02x%02x%02x" % (64, 83, 104)
        distancia=1
        cons=ConsultasBd.ConsultarBd()
        liz=cons.ConsultaMyReservaciones(usuario)
        
        for x in liz :
            l=tk.Label(self.MyReservas, text=x, bg=color,  fg="black")
            l.place(x=10,y=50*distancia)
            distancia=distancia+1

def main():
    vp=tk.Tk()
    t=tabs(vp)
    t.hoja.pack()
    t.mio("monteon")
    vp.mainloop()
   
   

    return 0
   
if __name__=='__main__':
   main()  

   