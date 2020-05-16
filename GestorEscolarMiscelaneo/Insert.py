# coding: utf-8 
import conexion
import Fecha
from tkinter import messagebox


class Insert():
    f=Fecha.Fecha()
    def __init__(self):
      self.c=conexion.DataBase()


    def insertarNoticia(self, ruta, noti, fkad, titulo):
       x="INSERT INTO notificaciones(Foto, Noticia, Fk_Adminstrativo ,Titulo) VALUES (%s, %s, %s, %s);"
       v=(""+str(ruta)+"" , ""+str(noti)+"",str(fkad),""+str(titulo)+"")
       self.c.cursor.execute(x, v)
       self.c.connection.commit()
       
    def addReservacion(self,dia,idDocente,horaI,horaF):
              
         x="call mydb.Reservar('"+str(dia)+"','"+str(idDocente)+"','"+str(horaI)+"','"+str(horaF)+"');"    
         self.c.cursor.execute(x)
         self.c.connection.commit()
         self.c.cursor 
         messagebox.showinfo("reservado","Bien")
         
         return 0