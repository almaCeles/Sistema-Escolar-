import conexion

class update():
    
    def __init__(self):
      self.c=conexion.DataBase()

    def updateNoticia(self, titulo,fot ,noti,fk):
      x="UPDATE mydb.notificaciones SET Noticia = '"+str(noti)+"' , Foto= '"+str(fot)+"' where Titulo='"+str(titulo)+"' and Fk_Adminstrativo="+fk+";"
      self.c.cursor.execute(x)
      self.c.connection.commit()
      




