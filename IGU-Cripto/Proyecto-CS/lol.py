from tkinter import *
from tkinter.filedialog import askopenfilename
from cryptography import *

#Funciones de cifrado y decifrado

#

#

#

#

#




#Ventana
ventana = Tk()
ventana.geometry("1100x950")
ventana.title("Practica 0")


#Etiquetas
intro = Label(ventana, text="------- :", width=18, height=3)
intro.grid(row=1 , column=0)

url = Button(ventana, text="Ingresa la ruta del archivo :", width=20, height=2)
url.grid(row=3 , column=0)

#Botones




#file = askopenfilename()
textrut = Label(ventana, text="file", width=60, height=3)
textrut.grid(row=3, column=1)

intro = Label(ventana, text="Introduce el texto :", width=18, height=3)
intro.grid(row=4 , column=0)

#Botones 
botmsg = Button(ventana, text="Enviar mensaje", width=15, height=2)
botmsg.grid(row=5 , column=0)

bottxt = Button(ventana, text="Enviar archivo", width=15, height=2)
bottxt.grid(row=5 , column=1)

botverfile = Button(ventana, text="Ver archivos", width=15, height=2)
botverfile.grid(row=6 , column=1)

ventana.mainloop()

