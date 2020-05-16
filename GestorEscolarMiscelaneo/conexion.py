import pymysql

class DataBase():
    
    def __init__(self):
        
        self.connection = pymysql.connect(
          host='localhost',
          user='morenasa',
          password='best2',
          db='mydb'
          )
        #no setia mejor un try Cahs ahi no mostrata el fallo nunca
        if(self.connection):
            #print("La conexion fue un exito")
            self.cursor=self.connection.cursor()
        else:
            print("La conexion fallo con exito")
      





