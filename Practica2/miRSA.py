try:
    #from six.moves import tkinter as tk
    #from tkinter import *
    #from tkinter import filedialog
    from Crypto.PublicKey import RSA # Importamos el módulo RSA
    import sys
except ImportError:
    raise ImportError("Se requiere el modulo pycryptodome")
#-------------------------------------------------------------------------------------------------------------------------------#

#Escritura de claves en archivo
def archivoWritetxt(clavetxt, tipo):
    salida = tipo + ".key"
    f1 = open(salida, 'a')
    f1.write(clavetxt)
    f1.close() 

identidad = sys.argv[1]
bit_size = 3072
key_format = "PEM"

# Generamos el par de claves. Dependiendo del tamaño y el
# procesamiento de nuestro computador es lo que podrá tardar.
keys = RSA.generate(bit_size)

#Clave Pública
tipo = identidad + "-Publica"
clavetxt = (keys.publickey().export_key(key_format).decode())
archivoWritetxt(clavetxt, tipo)


#Clave Privada
tipo = identidad + "-Privada"
clavetxt = (keys.export_key(key_format).decode())
archivoWritetxt(clavetxt, tipo)