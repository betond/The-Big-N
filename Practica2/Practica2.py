try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    from Crypto.PublicKey import RSA # Importamos el módulo RSA
    from Crypto.Cipher import PKCS1_OAEP # Importamos el modulo de cifrado y descifrado

except ImportError:
    raise ImportError("Se requiere el modulo Tkinter y pycryptodome")
#-------------------------------------------------------------------------------------------------------------------------------#
archivoMensaje = ""
archivokey = ""

def archivoReadtxt():       #Archivo de lectura 
    global archivoMensaje 
    archivoMensaje = filedialog.askopenfilename()
    if archivoMensaje:
    # Leer el contenido (en bytes) del archivo.
        #textoPlano = Path(archivoEntrada).read_bytes()
        pwd = StringVar()
        pwd.set(archivoMensaje)
        ruta.config(textvariable=pwd)
        botonRuta1['bg'] = 'blue' # Al presionar queda azul
        botonRuta1['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")

def importReadkey():       #Archivo de la llave
    global archivokey 
    archivokey = filedialog.askopenfilename()
    if archivokey:
    # Leer el contenido (en bytes) del archivo.
        #textoPlano = Path(archivoEntrada).read_bytes()
        pwd = StringVar()
        pwd.set(archivokey)
        rutaSalida.config(textvariable=pwd)
        botonRuta2['bg'] = 'blue' # Al presionar queda azul
        botonRuta2['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")

def cifrar():       #Función de cifrado de mensajes
    f1 = open(archivoMensaje, 'r')
    textoPlano = f1.read()
    f1.close()

    llave = RSA.import_key(open(archivokey).read())
    nuevoCifrado = PKCS1_OAEP.new(llave)

    nmen = str(nuevoCifrado.encrypt(textoPlano.encode()).decode())

    metsplit = str(archivoMensaje).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    print(nomarchi)
    nomarchi = nomarchi.split('.')
    salida = str(nomarchi[0]) + "-c.txt"
    
    f2 = open(salida, 'a')
    f2.write(nmen)
    f2.close()  

def decifrar():     #Función de decifrado de mensajes
    f1 = open(archivoMensaje, 'r')
    textoPlano = f1.read()
    f1.close()
    
    llave = RSA.importKey(open(archivokey).read())
    nuevoDescifrado = PKCS1_OAEP.new(llave)

    nmen = nuevoDescifrado.decrypt(textoPlano)

    metsplit = str(archivoMensaje).split('/')
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
igu.title("Práctica No.2 - Criptografía")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto que contiene el mensaje:")
etiquetaCifrar.grid(pady=70 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRuta1 = tk.Button(igu, text="  RUTA-Mensaje ", command=archivoReadtxt)
botonRuta1.grid(row=1, column=2)

#Mensaje al usuario
etiquetaDecifrar = tk.Label(text="La ruta del archivo con la llave a utilizar : ")
etiquetaDecifrar.grid(pady=20 ,padx=20 ,row=3, column=0)

#Campo para validar la ruta
rutaSalida = tk.Label(igu, text="Sin selección", width=60)
rutaSalida.grid(row=3, column=1)

#Botón de acción del explorador de archivos
botonRuta2 = tk.Button(igu, text="  RUTA-Llave ", command=importReadkey)
botonRuta2.grid(row=4, column=2)

#Botón cifrar - 
botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón decifrar - 
botonDecifrar = tk.Button(igu, text="Decifrar", command=decifrar)
botonDecifrar.grid(pady=150 ,row=5, column=2)


igu.mainloop()