import Fecha
from tkinter import*
import BdUsuario
import Insert 


class Breserva():

    opcioness=["07:00-07:50","07:00-07:50","07:50-08:40","08:40-09:30","09:30-10:20","10:20-10:50","10:50-11:40","11:40-12:30","12:30-13:20",
                  "13:20-14:10","14:10-15:00"]
    opcionessD=["1-Lunes","1-Lunes","2-Martes","3-Miercoles","4-Jueves","5-Viernes"]


    def __init__(self):
        print()


    def estado(self):
            print(str(self.varda.get()))

            if self.varda.get()==1:
                opcioness=["07:00-07:50","07:50-08:40","08:40-09:30","09:30-10:20","10:20-10:50","10:50-11:40","11:40-12:30","12:30-13:20",
                  "13:20-14:10","14:10-15:00"]
                self.option.set_menu(*opcioness)
                self.seleccionadoInicial()
            else :
                 opcioness=["07:00-08:40","07:00-08:40","08:40-10:20","10:20-11:40","11:40-13:20",
                  "13:20-15:00"]
                 self.option.set_menu(*opcioness)
                 self.seleccionadoInicial()
        
       
    #metodo de bonon recerva    
    def Guardar(self):
        idDocente=BdUsuario.BdUsurio.Docente
        i=Insert.Insert()      
        d=self.varmenuD.get()
        horaI=self.varmenuH.get()[0:5]
        horaF=self.varmenuH.get()[6:11]
        i.addReservacion(d[0:1],idDocente,horaI,horaF)      
    
    

    def reservarB(self,reserva):
      
      #creando radio button
      self.varda=IntVar()
      rb=ttk.Radiobutton(reserva,text="Una Hora",value=1,variable=self.varda,command=self.estado).place(x=20,y=100)
      rb1=ttk.Radiobutton(reserva,text="Dos Hora",value=2,variable=self.varda,command=self.estado).place(x=20,y=250)
      #creando menus
      self.varmenuH=StringVar(reserva)
      self.option=ttk.OptionMenu(reserva,self.varmenuH,*self.opcioness )
      self.option.configure(width=50)
      self.option.place(x=200,y=175)
      self.varmenuD=StringVar(reserva)
      self.optionD=ttk.OptionMenu(reserva,self.varmenuD,*self.opcionessD )
      self.optionD.configure(width=30)
      self.optionD.place(x=650,y=175)
      
      self.seleccionadoInicial()
      #creando boton Reservar
      
     
     
      
    def seleccionadoInicial(self):
        f=Fecha.Fecha()
  
        for l in self.opcionessD:
             if(str(f.diaN ) in l):
                    self.varmenuD.set(l)
                    break
  

        for h in self.opcioness:
                if  str(f.hora)in h[0:2]:
                    self.varmenuH.set(h)
                    print(f.hora)
                    print(h[0:2])
                    break
      

def main():
   
    v=RDreserva()    

    return 0
   
if __name__=='__main__':
   main() 


