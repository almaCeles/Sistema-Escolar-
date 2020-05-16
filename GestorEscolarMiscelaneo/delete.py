import conexion

class delete():
    
    def __init__(self):
      self.c=conexion.DataBase()

    def deleteNoticia(self, titulo, fk):
      x="DELETE FROM mydb.notificaciones WHERE Titulo='"+titulo+"' and Fk_Adminstrativo="+fk+";"
      self.c.cursor.execute(x)
      self.c.connection.commit()
      