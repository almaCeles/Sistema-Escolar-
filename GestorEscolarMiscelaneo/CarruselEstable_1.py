 #
#
#Version para poder hacer pruevas con la base de datos y esas cosas.
#
#
#


from tkinter  import*
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

cambio = 0
cambio2 = -1
SIZE = 200
#Aqui es donde se mandara el texto para visualizarlo en el Canvas(nota debe de haver un espacio entre cada mensaje como se muestra
textA = ("","Nota 1 la oscuridad es la ausencia \nde los fotones de luz"," ","La luna esta mas cerca \nde lo que crees"," ","Elon musk"," ") 
text = textA[0]
#Link de la imagen que se le va a poner
ima1 = Image.open("C:/Users/Alma Cuevas/Pictures/m2000.jpg")  #"/Users/ftm/Desktop/images/a.png"    "C:/Users/Alma Cuevas/Pictures/m2000.jpg"
im = ima1
MOV_X = 6
MOV_Y = 0
VAR = 50
FPS = 100
TSM = int(1000 / FPS)
class ventanaPrincipal(ttk.Frame):


    def __init__(self,f):
        super().__init__(f)
        global SIZE
        self.canvas = tk.Canvas(width=800, height=SIZE, background="SeaGreen1")
        self.canvas.place(x = 150, y = 0)
        
        global im
        im
        photo = ImageTk.PhotoImage(im)
        coordinates2 = (0,0)
        

        ImagenC = self.canvas.create_image(coordinates2, image = photo, anchor="nw")
        labelN = Label(self.canvas,text=text, background = "SeaGreen1")
        labelN.place(x=650,y=20)

        def Reiniciar():
            global text
            global textA
            global cambio
            text = textA[cambio]
            if cambio >= 5:
                cambio = -1   
            cambio =cambio + 1 
            labelN.config(text = text)           

            coordinates = self.canvas.coords(ImagenC)   
            global VAR
            if VAR <=SIZE:
                VAR = SIZE+530
                update_canvas
            if coordinates[0] <0 or coordinates[0] > 50:
                global MOV_X
                MOV_X *= -1
   
            self.canvas.move(ImagenC, MOV_X, MOV_Y)
            self.canvas.after(1000, update_canvas)
            update_canvas()

        boton  = tk.Button(self.canvas,width = 20, height = 1, text = "NEXT", command = Reiniciar)
        boton.place(x = 650,y = 100)

        def update_canvas():
            coordinates = self.canvas.coords(ImagenC)    
    
            if coordinates[0] <= -550 or coordinates[0] >= 80: 
              
              update_canvas()

        
            self.canvas.move(ImagenC, MOV_X, MOV_Y)
            self.canvas.after(TSM, update_canvas)

        self.canvas.after(TSM, update_canvas)
        mainloop()
