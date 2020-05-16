from datetime import datetime

class Fecha:
   
    
    def __init__(self):
        self.ahora=datetime.now()
        self.fecha=self.ahora.strftime("%Y-%m-%d")  #"%d-%m-%Y"
        self.hora=self.ahora.strftime("%H")
        self.diaN=self.ahora.isoweekday()


def main():
   
    f=Fecha() 
    print(f.ahora)
    print(f.fecha)
    print(f.hora) 
    print(f.ahora.isoweekday())
    return 0
   
if __name__=='__main__':
   main() 


