try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    from PIL import Image
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import *
    import numpy

except ImportError:
    raise ImportError("Se requieren los modulos Tkinter, PIL, PyCryptodome, numpy")
#-------------------------------------------------------------------------------------------------------------------------------#
archivoEntrada = ""


def archivoReadBMP():       #Archivo de lectura 
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


def cifrar():       #Función de cifrado de mensajes

    img = Image.open(archivoEntrada)
    image = numpy.array(img)
    image_size = img.size
    
    key = pad(bytes(entradaClave.get(), 'utf-8'), 16)
    ivs = pad(bytes(entradaVector.get(), 'utf-8'), 16)

    cipher = None
    #Para "CBC"
    cipher = AES.new(key, AES.MODE_CBC, ivs)
    #Para "ECB"
    #cipher = AES.new(key, AES.MODE_ECB)

    ct_bytes = cipher.encrypt(pad(image.tobytes(),AES.block_size,))

    img_data = numpy.frombuffer(ct_bytes)

    image_nva = Image.frombuffer("RGB",image_size,img_data)
   
    #Nombre del nuevo archivo
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    print(nomarchi)
    nomarchi = nomarchi.split('.')
    archivoSalida = str(nomarchi[0]) + "-c.bmp"

    #Guradado de la imagen cifrada
    image_nva.save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida


def descifrar():     #Función de descifrado de mensajes
    clave = entradaClave.get()
    vector = entradaVector.get()

    img = Image.open(archivoEntrada)
    image = numpy.array(img)
    image_size = img.size

    key = pad(bytes(clave, 'utf-8'), 16)
    ivs = pad(bytes(vector, 'utf-8'), 16)

    cipher = None
    #Para "CBC"):
    cipher = AES.new(key, AES.MODE_CBC, ivs)
    #"ECB"
    #cipher = AES.new(key, AES.MODE_ECB)

    aux = image.tobytes()
    pt = cipher.decrypt(aux)

    img_data = numpy.frombuffer(pt)

    #Nombre del nuevo archivo
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    print(nomarchi)
    nomarchi = nomarchi.split('.')
    archivoSalida = str(nomarchi[0]) + "-d.bmp"

    #Guardado de la imagen descifrada
    Image.frombuffer("RGB",image_size,img_data).save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x600")
igu.title("Práctica No.0 - Criptografía")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta de la imagen '.bmp':")
etiquetaCifrar.grid(pady=50 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRuta1 = tk.Button(igu, text="  RUTA-Entrada ", command=archivoReadBMP)
botonRuta1.grid(row=1, column=2)

#Mensaje al usuario Clave
etiquetaClave = tk.Label(text="Introduzca la clave 'key': ")
etiquetaClave.grid(pady=20 ,padx=20 ,row=3, column=0)

#Entrada de la Cleave-Key
entradaClave = tk.Entry(justify=CENTER, show='*')
entradaClave.grid(pady=15, row=4, column=0)

#Mensaje al usuario Vector
etiquetaVector = tk.Label(text="Introduzca el vector de inicio: ")
etiquetaVector.grid(pady=20 ,padx=20 ,row=3, column=1)

#Entrada del Vector
entradaVector = tk.Entry(justify=CENTER, show='*')
entradaVector.grid(pady=15, row=4, column=1)

#Botón cifrar - 
botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón descifrar - 
botonDescifrar = tk.Button(igu, text="Descifrar", command=descifrar)
botonDescifrar.grid(pady=150 ,row=5, column=2)


igu.mainloop()
