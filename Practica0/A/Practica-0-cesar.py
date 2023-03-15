try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")
#-------------------------------------------------------------------------------------------------------------------------------#
archivoEntrada = ""
archivoSalida = ""

def archivoReadtxt():       #Archivo de lectura 
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


def archivoWritetxt():      #Archivo de escritura
        global archivoSalida 
        archivoSalida = filedialog.askopenfilename()
        pwds = StringVar()
        pwds.set(archivoSalida)
        rutaSalida.config(textvariable=pwds)
        botonRuta2['bg'] = 'blue' # Al presionar queda azul
        botonRuta2['fg'] = 'white' # Si pasamos el Mouse queda blanco


def cifrar():       #Función de cifrado de mensajes
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()

    nmen = ""
    for caracter in textoPlano:
        nmen += str(chr((ord(caracter)+3)))

    if archivoSalida != "":
        salida = archivoSalida
    else:
        metsplit = str(archivoEntrada).split('/')
        n = len(metsplit)
        nomarchi = metsplit[n-1]
        print(nomarchi)
        nomarchi = nomarchi.split('.')
        salida = str(nomarchi[0]) + "-c.txt"
    
    f2 = open(salida, 'a')
    f2.write(nmen)
    f2.close()  

def decifrar():     #Función de decifrado de mensajes
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()
    
    nmen = ""
    for caracter in textoPlano:
        if ord(caracter) != 10:
            nmen += str(chr(ord(caracter)-3))
        else:
            nmen += str(chr(ord(caracter)))
    
    if archivoSalida != "":
        salida = archivoSalida
    else:
        metsplit = str(archivoEntrada).split('/')
        n = len(metsplit)
        nomarchi = metsplit[n-1]
        print(nomarchi)
        nomarchi = nomarchi.split('.')
        salida = str(nomarchi[0]) + "-d.txt"
    
    f2 = open(salida, 'a')
    f2.write(nmen)
    f2.close()
    

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x600")
igu.title("Práctica No.0 - Criptografía")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto 'txt':")
etiquetaCifrar.grid(pady=70 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRuta1 = tk.Button(igu, text="  RUTA-Entrada ", command=archivoReadtxt)
botonRuta1.grid(row=1, column=2)

#Mensaje al usuario
etiquetaDecifrar = tk.Label(text="La ruta del archivo 'txt' de salida es : ")
etiquetaDecifrar.grid(pady=20 ,padx=20 ,row=3, column=0)

#Campo para validar la ruta
rutaSalida = tk.Label(igu, text="Sin selección", width=60)
rutaSalida.grid(row=3, column=1)

#Botón de acción del explorador de archivos
botonRuta2 = tk.Button(igu, text="  RUTA-Salida ", command=archivoWritetxt)
botonRuta2.grid(row=4, column=2)

#Botón cifrar - 
botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón decifrar - 
botonDecifrar = tk.Button(igu, text="Decifrar", command=decifrar)
botonDecifrar.grid(pady=150 ,row=5, column=2)


igu.mainloop()