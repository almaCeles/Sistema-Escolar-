from tkinter import*
from tkinter import filedialog
from PIL import Image,ImageTk

class imagenes():
  global laFile
  def __init__(self):
   print("entro a constuctor")

  def file(self, Fnotifi):
     self.filename=filedialog.askopenfilename(initialdir= "/", title ="Selecciona una Foto", filetype=(("jpeg", "*.jpg"),("All Files","*.*")))
    
     self.laFile=Label(Fnotifi ,text="")
     
     self.laFile.place(x=50,y=300)
     self.laFile.configure(text=self.filename , bg="snow")

     self.lFile=self.filename
     self.cargaImagen()
     self.cambiarTamaño()
     self.mostrarImagen(Fnotifi)
     
  def cargaImagen(self):
     
     try:
      self.img=Image.open(""+self.filename+"")  #C:/Users/Alma Cuevas/Desktop/1.png

     except IOError:
       print("Unable to load image")
       
  
  def mostrarImagen(self,Fnotifi):
     self.imgg=Image.open(""+self.filename+"")
     ta = ImageTk.PhotoImage(self.imgg)
     label = Label(Fnotifi, image=ta)
     
       
     label.image = ta
        
     label.place(x=50,y=100)
  
  def cambiarTamaño(self):
    # Obtener imagen con el tamaño indicado
    self.reducida = self.img.resize((200, 200))

    # Mostrar imagen
    #self.reducida.show()

    # Guardar imagen obtenida
    self.reducida.save(""+self.filename+"")

    




