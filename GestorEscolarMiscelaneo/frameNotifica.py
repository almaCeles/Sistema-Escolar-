import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog
from PIL import Image,ImageTk
import Insert
import BdUsuario
import ConsultasBd
import delete
import update
import carucelito

class frameNotifica(ttk.Frame):
  
  def __init__(self ):
    #super().__init__(main_window)
    self.color = "#%02x%02x%02x" % (64, 83, 104)
    self.Fnotifi=tk.Frame()
    self.Fnotifi.config(width=900, height=900, bg=self.color)
    self.pint()
    self.Fnotifi.pack()
    self.c=ConsultasBd.ConsultarBd()
    self.d=delete.delete()
    self.u=update.update()
    
  def pint(self): 

    l=Label(self.Fnotifi, text="", bg="SeaGreen1",borderwidth=2, relief="groov")
    l.config(width=142, height=2) #x ,y
    l.place(x=0, y=0)

    relock=Label(l,text="hola" ,bg="gray60" )
    relock.place(x=680, y=5)

    self.bc=Button(l, text="Crear", command= self.crea,bg="gray60", fg="snow")
    self.bc.config(width=25, height=1)
    self.bc.place(x=30,y=1)


    self.cajatex=Entry(l)#validatecommand
    self.cajatex.place(x=870,y=3)
    self.cajatex.bind('<Key>',self.Filtrito)

    fileb=Button(self.Fnotifi, text="Cargar Imagen", command= self.file ,bg="gray60", fg="snow")
    fileb.config(width=15, height=2)
    fileb.place(x=120,y=320)

    self.titulo=Entry(self.Fnotifi)
    self.titulo.place(x=430,y=50)
    

    self.cuadroTxt=tk.Text(self.Fnotifi, wrap=WORD )
    self.cuadroTxt.config(width=60, height=22)
    self.cuadroTxt.place(x=300,y=80)

    self.tabla=tk.Listbox(self.Fnotifi, selectmode=tk.SINGLE, activestyle=tk.NONE, selectforeground="DarkSeaGreen1", bg="Aquamarine4",fg="white smoke", selectborderwidth=2, 	
    width=23, height=21,  font=("AvantGarde Bk BT",13))
    self.tabla.place(x=850,y=36)

    self.tabla.bind('<<ListboxSelect>>', self.eve_tab)

    self.bEliminar=tk.Button(self.Fnotifi, text="Eliminar" ,bg="gray60", fg="snow", comman=self.eve_eliminar)
    self.bModificar=tk.Button(self.Fnotifi, text="Modificar", bg="gray60", fg="snow", comman=self.eve_modifica)
    self.bCancelar=tk.Button(self.Fnotifi, text="Cancelar", bg="gray60", fg="snow",comman=self.eve_cancela )

  #--Evento selección de tabla  
  def eve_tab(self, evt):
    try:
        self.label.place_forget()
    except:
        print("no hay imagen prebia")

    self.cuadroTxt.delete("1.0",'end-1c')
    self.titulo.delete(0, END)
    self.bc.config(state=DISABLED)

    var=self.tabla.get(self.tabla.curselection())
    print(var[0])

    self.i=self.c.ConsultaSuNoti(str(BdUsuario.BdUsurio.Adminstrador),str(var[0]))
    
    self.titulo.insert(0,self.i[0])
    self.titulo.config(state=DISABLED)
    self.cuadroTxt.insert(tk.INSERT,self.i[2])
    self.filename=self.i[1]
    self.cargaImagen()
    self.mostrarImagen()

   
    self.bEliminar.place(x=790, y=120)
    self.bModificar.place(x=790, y=170)
    self.bCancelar.place(x=790, y=220)

    

  #Evento de entry filtrar
  def Filtrito(self,  event):
      self.tabla.delete(0, END )
      li=self.c.Filtro(str(BdUsuario.BdUsurio.Adminstrador),str(self.cajatex.get()))
      self.tabla.insert(tk.END,*li)
  #evento de boton modificar
  def eve_modifica(self):
      self.u.updateNoticia(str(self.i[0]),self.filename , self.cuadroTxt.get("1.0",'end-1c'),str(BdUsuario.BdUsurio.Adminstrador))
      MessageBox.showinfo("Modificado", "Noticia----"+ self.i[0] + "----modificada en la base de datos" )
  #evento de boton eliminar 
  def eve_eliminar(self):
      self.d.deleteNoticia(str(self.i[0]),str(BdUsuario.BdUsurio.Adminstrador))
      MessageBox.showinfo("Eliminar", "Noticia----"+ self.i[0] + "----eliminada de la base de datos" )
      self.titulo.config(state=NORMAL)
      self.bc.config(state=ACTIVE)

      self.cuadroTxt.delete("1.0",'end-1c')
      self.titulo.delete(0, END)
      self.label.place_forget()
      self.bEliminar.place_forget()
      self.bModificar.place_forget()
      self.bCancelar.place_forget()

  #evento de boton cancelar
  def eve_cancela(self):
      self.titulo.config(state=NORMAL)
      self.cuadroTxt.delete("1.0",'end-1c')
      self.titulo.delete(0, END)
      self.bEliminar.place_forget()
      self.bModificar.place_forget()
      self.bCancelar.place_forget()
      self.bc.config(state=ACTIVE)
      self.label.place_forget()
  ##carga la direción
  def file(self):

    try:
     self.filename=filedialog.askopenfilename(initialdir= "/", title ="Selecciona una Foto", filetype=(("jpeg", "*.jpg"),("All Files","*.*")))
    
     
     self.cargaImagen()
     self.cambiarTamaño()
     self.mostrarImagen()
    except:
        print("no cargo el archivo")
   #convierte la imagen a tipo img  
  def cargaImagen(self):
     
     try:
       self.img=Image.open(""+self.filename+"")  #C:/Users/Alma Cuevas/Desktop/1.png

     except:
       print("no se puede convertir a img")
       
  #muestra la imagen
  def mostrarImagen(self):
    try:
     self.imgg=Image.open(""+self.filename+"")
     ta = ImageTk.PhotoImage(self.imgg)
     self.label = Label(self.Fnotifi, image=ta, bg=self.color) #, bg="#%02x%02x%02x"
     
       
     self.label.image = ta
        
     self.label.place(x=50,y=100)
    except:
        print("error a mostrar la imagen")

     
  #cambia tamaño
  def cambiarTamaño(self):
   
    self.reducida = self.img.resize((200, 200))

    # Guardar imagen obtenida
    self.reducida.save(""+self.filename+"")
  

  def buscar (self):
    print("estoy buscando")

  #evento de boton crear  la noticia
  def crea(self):
    i=Insert.Insert()
    try:
     i.insertarNoticia(self.filename ,  self.cuadroTxt.get("1.0",'end-1c')  , BdUsuario.BdUsurio.Adminstrador , self.titulo.get()) 
     print("insercion correcta")
     self.cuadroTxt.delete("1.0",'end-1c')
     self.titulo.delete(0, END)
     self.label.config(image="")
     self.label.place_forget()
     
    except:
      MessageBox.showerror("Error", "Tienes que llenar todos los campos")

def main():
 f=frameNotifica()
 return 0 



if __name__=='__main__':
  main() 


  
