try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    from PIL import Image
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


def generarHash():       #Función de cifrado de mensajes

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
    archivoSalida = str(nomarchi[0]) + "-h.bmp"

    #Guradado de la imagen cifrada
    image_nva.save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida


def validarHash():     #Función de descifrado de mensajes
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
    archivoSalida = str(nomarchi[0]) + "-v.bmp"

    #Guardado de la imagen descifrada
    Image.frombuffer("RGB",image_size,img_data).save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x600")
igu.title("Práctica No.5 - Función Hash")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto '.txt':")
etiquetaCifrar.grid(pady=50 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRuta1 = tk.Button(igu, text="  Ruta del archivo ", command=archivoReadBMP)
botonRuta1.grid(row=1, column=2)

#Botón generarHash - 
botonGenerar = tk.Button(igu, text="Generar Hash", command=generarHash)
botonGenerar.grid(pady=150, row=5, column=1)

#Botón validarHash - 
botonValidar = tk.Button(igu, text="Validar Hash", command=validarHash)
botonValidar.grid(pady=150 ,row=5, column=2)


igu.mainloop()