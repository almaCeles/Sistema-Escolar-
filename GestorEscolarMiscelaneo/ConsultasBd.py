import conexion
import BdUsuario



class ConsultarBd():
    
    def __init__(self):
        self.c=conexion.DataBase()
      
        
     

    def ConsultaMyReservaciones(self,usuario):
          x="select HoraI,HoraF,nombre,nombred from docentes inner join (reservaciones) inner join (dia) where (idDocentes=Docentes_Reservaciones and Docentes_Reservaciones='"+usuario+"')  and (dia_idDia=idDia);"
          self.c.cursor.execute(x)
          r=self.c.cursor.fetchall()
          
          return r

    def ConsultaReservacionesDia(self,dia):
          x="select HoraI,HoraF,nombre,nombred  from docentes inner join (reservaciones)"+" inner join (dia)  where (idDocentes=Docentes_Reservaciones)  and (dia_idDia=idDia and dia_idDia='"+dia+"');"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          r=self.c.cursor.fetchall()
          return r

    def ConsultaUsuario(self,usua,contra):
        try:  
          x="select usuario, contraseña, Administrador_Usuario, Docente_Usuario from usuarios where usuario='"+ usua +"' and contraseña='"+contra+"';"
          self.c.cursor.execute(x)
          self.c.connection.commit()
          ro=self.c.cursor.fetchone()
          print(ro)
          BdUsuario.BdUsurio.Usuario=ro[0]
          BdUsuario.BdUsurio.Contra=ro[1]
          BdUsuario.BdUsurio.Adminstrador=ro[2]
          BdUsuario.BdUsurio.Docente=ro[3]
          #print(BdUsuario.BdUsurio.Usuario)
          #print(BdUsuario.BdUsurio.Contra) 
        except:
         print("error en usu y contra")

    def Filtro(self, fk, ini):
         x="select Titulo from notificaciones where Fk_Adminstrativo="+fk+" and (Titulo like '"+ini+"%');"
         self.c.cursor.execute(x)
         self.c.connection.commit()
         r=self.c.cursor.fetchall()

         return r

    def ConsultaSuNoti(self, fk, titulo):
        x="select Titulo, Foto, Noticia from notificaciones where Fk_Adminstrativo="+fk+" and Titulo='"+titulo+"';"
        self.c.cursor.execute(x)
        self.c.connection.commit()
        r=self.c.cursor.fetchone()

        return r
    def noticias(self):
        try:
            x="select Foto, Noticia from mydb.notificaciones;"
            self.c.cursor.execute(x)
            self.c.connection.commit()
            r=self.c.cursor.fetchall()
            t=r[2]
            print(t[0])
            return r
        except:
            print("no se encontro")
        
       
def main():
    c=ConsultarBd()
    print(c.ConsultaMyReservaciones("1"))

    #print(c.ConsultaUsuario("ai","ali"))
    #print(BdUsuario.BdUsurio.Usuario)
    #print(c.Filtro("4","l"))
  
    return 0

if __name__=='__main__':
  main()  