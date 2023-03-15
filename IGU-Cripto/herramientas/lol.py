from pathlib import Path
from tkinter import filedialog
from functools import partial
import socket
import threading
import sys
import pickle
import time
import hashlib
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#from tkinter.filedialog import askopenfilename
from urllib.request import OpenerDirector


    #Ventana
    ventana = Tk()
    ventana.geometry("600x500")
    ventana.title("Chat con cifrado de Mensajes y archivos de texto")
	
	#Etiquetas
    intro = Label(ventana, text="Mensajes :", width=18, height=3)
    intro.grid(row=1 , column=0)
	
    intro = Label(ventana, text="Introduce el mensaje :", width=18, height=3)
    intro.grid(row=4 , column=0)
	
	#Caja de texto
    textbox = Text(ventana, width=40)
    textbox.grid(row=1 , column=1)
	
    msg = Entry(ventana, width=60)
    msg.grid(row=4, column=1)
	
	#Radiobutton
    radioValue = IntVar(ventana)
    Radiobutton(ventana, text="Algoritmo Cesar", variable=radioValue, value=1).grid(row=2 , column=0)
    Radiobutton(ventana, text="Algoritmo One Time Pad", variable=radioValue, value=2).grid(row=2 , column=1)

    		#Botones 
    botmsg = Button(ventana, text="Enviar mensaje", command=sendMsg, width=15, height=2)
    botmsg.grid(row=5 , column=0)