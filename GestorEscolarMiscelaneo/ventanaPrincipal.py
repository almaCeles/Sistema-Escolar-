import tkinter as tk
from tkinter import ttk
from tkinter import*
import LateralBar
import tabs
import VentanaUsuario
import BdUsuario
import carucelito



class ventanaPrincipal(tk.Frame):
    vp=tk.Tk()
    f2=tk.Frame()
    hoja = ttk.Notebook()
   
    x=vp.winfo_screenwidth()
    y=vp.winfo_screenheight()
    def __init__(self): 
        
        self.vp.title("Hola")
        self.vp.geometry("{0}x{1}+0+0".format(self.vp.winfo_screenwidth(), self.vp.winfo_screenheight()))
        self.vp.config(bg="purple1")
        
     
        self.v=0
        self.LT = LateralBar.LateralBar()
        self.LT.f3.place(x=self.x/40,y=self.y/80)
        self.definirF()
        
        self.l= tabs.tabs(self.vp)

        self.l.hoja.place(x=self.x/6,y=self.y/4)
    
        self.car=carucelito.Carucel()
        self.car.caru.place(x=self.x/6,y=self.y/80)
        self.ventaUsu=VentanaUsuario.VentanaUsuario()
        self.vp.mainloop()    
    #segundo evento de bton validacion
    def eveValidacion(self, evt):
        if BdUsuario.BdUsurio.Bandera==True:
         self.l.visibleHojitas()
         self.bUsuario.config(text="Salir")
         #poner aquiiii------------- cargar my reservas
         #try:
          #  usuario=BdUsuario.BdUsurio.Docente 
           # self.l.mio(str(usuario))
         #except:
          #  print("no es docente")

    #evento de boton pintar interfas
    def ven(self): 
        
     if self.bUsuario.config('text')[-1] == "Ingresar": 
        self.ventaUsu.bOk.bind("<ButtonRelease-1>",self.eveValidacion)
        self.ventaUsu.fUsu.place(x=self.x/33,y=self.y/3)
        self.bUsuario.config(text="cancelar")

     elif self.bUsuario.config('text')[-1] == "cancelar":
        self.ventaUsu.fUsu.place_forget()
        self.bUsuario.config(text="Ingresar")
        
        
        
     if self.bUsuario.config('text')[-1] == "Salir":
       print("j")
       
       self.l.ocultarTabs()
       print("jgbd")
       BdUsuario.BdUsurio.Usuario="tuu"
       BdUsuario.BdUsurio.Contra="uv"
       BdUsuario.BdUsurio.Adminstrador=""
       BdUsuario.BdUsurio.Docente=""
       BdUsuario.BdUsurio.Bandera=False
       print("saliste" + BdUsuario.BdUsurio.Usuario)
       self.bUsuario.config(text="Ingresar")
       self.car.posicionArreglo()
       
       

    def definirF (self):
        self.bUsuario=Button(self.LT.f3, text="Ingresar",command=self.ven)
        self.bUsuario.config(width=20, height=3)
        self.bUsuario.place(x=10,y=10)
      
   
      
def main():
    v=ventanaPrincipal()
    
    return 0
   
if __name__=='__main__':
   main()    

 