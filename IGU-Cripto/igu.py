try:
    ##from six.moves
    import tkinter as tk
    from tkinter import *
    #from Crypto.Cipher import AES
    from pathlib import Path
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")
#-------------------------------------------------------------------------------------------------------------------------------#
archivoEntrada = ""
archivoSalida = ""

def archivoReadtxt():
    global archivoEntrada 
    archivoEntrada = filedialog.askopenfilename()
    if archivoEntrada:
    # Leer el contenido (en bytes) del archivo.
        #textoPlano = Path(archivoEntrada).read_bytes()
        pwd = StringVar()
        pwd.set(archivoEntrada)
        ruta.config(textvariable=pwd)
        botonRuta1['bg'] = 'blue' # Al presionar queda azul
        botonRuta1['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")


def archivoWritetxt():
        global archivoSalida 
        archivoSalida = filedialog.askopenfilename()
        pwds = StringVar()
        pwds.set(archivoSalida)
        rutaSalida.config(textvariable=pwds)
        botonRuta2['bg'] = 'blue' # Al presionar queda azul
        botonRuta2['fg'] = 'white' # Si pasamos el Mouse queda blanco


def cifrar():
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()

    nmen = ""
    for caracter in textoPlano:
        nmen += str(chr(ord(caracter)+3))
    
    f2 = open(archivoSalida, 'a')
    f2.write(nmen)
    f2.close()
    

def decifrar():
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()
    
    nmen = ""
    for caracter in textoPlano:
        nmen += str(chr(ord(caracter)-3))
    
    f2 = open(archivoSalida, 'a')
    f2.write(nmen)
    f2.close()
    

igu = tk.Tk()
igu.geometry("1100x600")
igu.title("Práctica No.01 - Criptografía")

etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto 'txt':")
etiquetaCifrar.grid(pady=70 ,padx=20 ,row=0, column=0)

ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

botonRuta1 = tk.Button(igu, text="  RUTA-Entrada ", command=archivoReadtxt)
botonRuta1.grid(row=1, column=2)

etiquetaDecifrar = tk.Label(text="La ruta del archivo 'txt' de salida es : ")
etiquetaDecifrar.grid(pady=20 ,padx=20 ,row=3, column=0)

rutaSalida = tk.Label(igu, text="Sin selección", width=60)
rutaSalida.grid(row=3, column=1)

botonRuta2 = tk.Button(igu, text="  RUTA-Salida ", command=archivoWritetxt)
botonRuta2.grid(row=4, column=2)

botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

botonDecifrar = tk.Button(igu, text="Decifrar", command=decifrar)
botonDecifrar.grid(pady=150 ,row=5, column=2)


igu.mainloop()