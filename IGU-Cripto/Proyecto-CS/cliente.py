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
import os

class Cliente():

	def __init__(self, host="LocalHost", port=4000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recibido = threading.Thread(target=self.msgRecibido)

		msg_recibido.daemon = True
		msg_recibido.start()
		
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
		
		def cesar(texto):
			nmen = ''
			for caracter in texto:
				nmen += str(chr(ord(caracter)+3))
			return nmen
		
		#def OneTimePad(texto):
			#nmen = onetimepad.encrypt(texto,'XLR8')
			#return nmen

		def sendMsg():
			mens = msg.get()
			mensaje = ''
			opcion = radioValue.get()
			if opcion == 1 :
				mensaje = '1,' + cesar(mens)
			elif opcion == 2 :
				mensaje = '2,' #+ OneTimePad(mens)
			self.sendMensaje(mensaje)
			tumensaje = "Tu: " + mens
			textbox.insert(INSERT, tumensaje)
		
		#Botones 
		botmsg = Button(ventana, text="Enviar mensaje", command=sendMsg, width=15, height=2)
		botmsg.grid(row=5 , column=0)
		
		def sendFile():
			#file = askopenfilename()
			lineascif = []
			#archi1=open(file,"r")
			archi2=open("rec.txt", "w")
			#lineas=archi1.readlines()
			opcion = radioValue.get()

			if opcion == 2:
				#for linea in lineas:
					line = '2,' #+ OneTimePad(linea)
					lineascif.append(line)
					self.sendMensaje(line)
			elif opcion == 1:
				#for linea in lineas:
					line = '1,' + cesar(linea)
					lineascif.append(line)
					self.sendMensaje(line)

			for linea in lineascif:
				archi2.write(linea)
			
			#archi1.close()
			archi2.close()

			archi3 = open("rec.txt", "r")
			data = archi3.readlines()
						
			print(data)
						
			archi3.close()


		bottxt = Button(ventana, text="Enviar archivo", command=sendFile, width=15, height=2)
		bottxt.grid(row=5 , column=1)
		
		#def showFile():
			#archivo_abierto=askopenfilename()
			#archivo_abierto
		#botverfile = Button(ventana, text="Ver archivos", command=showFile, width=15, height=2)
		#botverfile.grid(row=6 , column=1)
	
		ventana.mainloop()

	def sendMensaje(self, msg):
		self.sock.send(pickle.dumps(msg))


	def msgRecibido(self):
		
		def descesar(msgrec):
			nrecmen = ''
			for caracter in msgrec:
				nrecmen += str(chr(ord(caracter)-3))
			return nrecmen

		#def desOneTimePad(msgrec):
			#msg = onetimepad.decrypt(msgrec, 'XLR8')
			#return msg

		while True:
			try:
				rec = self.sock.recv(1024)
				if rec:
					data = pickle.loads(rec)
					splt = data.split(sep=',', maxsplit=1)
					tipo = splt[0]
					mens = splt[1]
					print(splt[1])
					if tipo == '1':
						mensaje = descesar(mens)
					#elif tipo == '2':
						#mensaje = desOneTimePad(mens)
					print(time.strftime("%c") + "--" + mensaje)
					
			except:
				pass
	


c = Cliente()