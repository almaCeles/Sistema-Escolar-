import tkinter as tk
from tkinter import ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import messagebox


texcon = ""
class LateralBar(ttk.Frame):
     color = "#%02x%02x%02x" % (0, 25, 53)
     def __init__(self):
       

#Variable del Frame
        self.f3 = tk.Frame()
        
#Frame de fondo verde bajo los botones

        
         
        self.f3.config(cursor = "pirate")
     

#Generacion de los componentes (Falta agregar un boton y poner unos condicionales)
         
        #Boton Comentario
        self.f3.config(width=169, height=655,bg=self.color)
        self.buttonCommentary = tk.Button(self.f3, text="Report", command=self.Report)
        self.buttonCommentary.config(width=20, height=3)
        self.buttonCommentary.place(x = 10,y = 68)
        #self.buttonCommentary.pack()
        
        #Boton FAQ
       
        self.buttonFAQ= tk.Button(self.f3, text="FAQ", command=self.FAQ)
        self.buttonFAQ.config(width = 20, height = 3)
        self.buttonFAQ.place(x = 10,y = 126)
       
        
        #Text box and Principal Label
        
        self.LabelPrincipal = tk.Label(self.f3, text="",bg = self.color,font = ("Gill Sans",16))
        self.LabelPrincipal.config(width=12, height=2)
        self.LabelPrincipal.place(x = 10,y = 190)

        #button trough of txt1
       



     def Report(self):
         if self.buttonCommentary.config('text')[-1] == 'Report':
            self.buttonFAQ.configure(state ="disabled")
            self.buttonCommentary.config(text='Exit')
            self.txt1 = tk.Text(self.f3,bg = "#6E3980",fg = "white", font = ("Gill Sans",12))
            self.txt1.config(width = 16, height =15)
            

            self.buttonSubmit = tk.Button(self.f3,text="submint")
            self.buttonSubmit.config(width = 10, height = 2,bd = 1, command = self.Enviar)
            
            self.buttonSubmit.place(x=42,y=200)
            self.txt1.place(x=10,y=238)


         else:
            self.buttonFAQ.configure(state ="normal")
            self.buttonCommentary.config(text='Report')
            self.buttonSubmit.destroy()
            self.txt1.destroy()

            

            print("llego")
            
            
     def Enviar(self):

        global texcon
        texcon = self.txt1.get(1.0,4.0)
        print(texcon)
        self.buttonFAQ.configure(state ="normal")
        self.buttonCommentary.config(text='Report')
        self.buttonSubmit.destroy()
        self.txt1.destroy()
        msg = MIMEMultipart()
        message =texcon


        password ="122333444455555666666"
        msg['From'] = "gestesc1@gmail.com"
        msg['To'] = "felipe.t.m.77@gmail.com"
        msg['Subject'] = "Comentario de Gestor Escolar Miscelaneo :p"

        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        messagebox.showinfo(message="successfully sent email :3", title="message confirmed")
        print("successfully sent email to :")





     def FAQ(self):
         if self.buttonFAQ.config('text')[-1] == 'FAQ':
            self.buttonCommentary.configure(state ="disabled")
            self.buttonFAQ.config(text='Exit')
            self.LabelPrincipal.config(text ="¿We can do it?\n\n¿When can do it?\n\n¿Who can do it?\n\n¿They can do it too?\n\n¿What did yo do?\n\n¿What did you play?", 
                                       bg = "#6E3980", bd =2,fg = "white",font=("",12)  )
            self.LabelPrincipal.config(width = 16, height = 15)
            self.buttonCommentary.configure(text='Report')

           

         else:
            self.buttonCommentary.configure(state ="normal")
            self.buttonFAQ.config(text='FAQ')
            self.LabelPrincipal.config(width = 12, height = 0)
            self.LabelPrincipal.config(text="",bd = 2,bg = self.color)
            

def main():
    
    LB = LateralBar()
    
  
        

    return 0
   
if __name__=='__main__':
   main()  

#commits
#Se creo el dia 8 de octubre a las 19:29
# ninguna modificacion   