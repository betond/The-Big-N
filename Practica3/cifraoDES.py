try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog
    from PIL import Image
    from Cryptodome.Cipher import DES
    from Cryptodome.Util.Padding import *
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
    
    key = pad(bytes(entradaClave.get(), 'utf-8'), 8)
    ivs = pad(bytes(entradaVector.get(), 'utf-8'), 8)

    modoDoperacipon = combo.get()

    cipher = None

    if modoDoperacipon == "ECB":    #Para modo "EBC"
        cipher = DES.new(key, DES.MODE_ECB)
    elif modoDoperacipon == "CBC":    #Para modo "CBC"
        cipher = DES.new(key, DES.MODE_CBC, ivs)
    elif modoDoperacipon == "CFB":    #Para modo "CFB"
        cipher = DES.new(key, DES.MODE_CFB, ivs)
    elif modoDoperacipon == "OFB":    #Para modo "OFB"
        cipher = DES.new(key, DES.MODE_OFB, ivs)
    else:                               #Para error de selección
        msguser = StringVar()
        msguser.set("Selección de metodo erronea")
        mensajeUsuario.config(textvariable=msguser)
        mensajeUsuario['bg'] = 'red'   #Color rojo - Advertencia


    ct_bytes = cipher.encrypt(pad(image.tobytes(),DES.block_size,))

    img_data = numpy.frombuffer(ct_bytes)

    image_nva = Image.frombuffer("RGB",image_size,img_data)
   
    #Nombre del nuevo archivo
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    print(nomarchi)
    nomarchi = nomarchi.split('.')
    archivoSalida = str(nomarchi[0]) + "_MODE_" + combo.get() + "-c.bmp"

    #Guradado de la imagen cifrada
    image_nva.save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida


def descifrar():     #Función de descifrado de mensajes
    clave = entradaClave.get()
    vector = entradaVector.get()

    img = Image.open(archivoEntrada)
    image = numpy.array(img)
    image_size = img.size

    # clave propuesta equipo10

    key = pad(bytes(clave, 'utf-8'), 8)
    ivs = pad(bytes(vector, 'utf-8'), 8)

    cipher = None
    modoDoperacipon = combo.get()

    cipher = None

    if modoDoperacipon == "ECB":    #Para modo "EBC"
        cipher = DES.new(key, DES.MODE_ECB)
    elif modoDoperacipon == "CBC":    #Para modo "CBC"
        cipher = DES.new(key, DES.MODE_CBC, ivs)
    elif modoDoperacipon == "CFB":    #Para modo "CFB"
        cipher = DES.new(key, DES.MODE_CFB, ivs)
    elif modoDoperacipon == "OFB":    #Para modo "OFB"
        cipher = DES.new(key, DES.MODE_OFB, ivs)
    else:                               #Para error de selección
        msguser = StringVar()
        msguser.set("Selección de metodo erronea")
        mensajeUsuario.config(textvariable=msguser)
        mensajeUsuario['bg'] = 'red'

    aux = image.tobytes()
    pt = cipher.decrypt(aux)

    img_data = numpy.frombuffer(pt)

    #Nombre del nuevo archivo
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    print(nomarchi)
    nomarchi = nomarchi.split('.')
    archivoSalida = str(nomarchi[0]) + "_MODE_" + combo.get() + "-d.bmp"

    #Guardado de la imagen descifrada
    Image.frombuffer("RGB",image_size,img_data).save(archivoSalida)

    archivoSalida = "-"     #Limpieza de la variable archivo de salida

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x800")
igu.title("Práctica No.3 - Cifrador de imagenes DES - Criptografía")

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
entradaClave = tk.Entry(justify=CENTER)
entradaClave.grid(pady=15, row=4, column=0)

#Mensaje al usuario Vector
etiquetaVector = tk.Label(text="Introduzca el vector de inicio: ")
etiquetaVector.grid(pady=20 ,padx=20 ,row=3, column=1)

#Entrada del Vector
entradaVector = tk.Entry(justify=CENTER)
entradaVector.grid(pady=15, row=4, column=1)

#Menú desplegable
combo = ttk.Combobox(state="readonly", values=["ECB","CBC","CFB","OFB"])
combo.grid(row=4, column=2)

#Botón cifrar - 
botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón descifrar - 
botonDescifrar = tk.Button(igu, text="Descifrar", command=descifrar)
botonDescifrar.grid(pady=150 ,row=5, column=2)

#Campo mensaje usuario
mensajeUsuario = tk.Label(igu, text="Sin probar", width=60)
mensajeUsuario.grid(row=6, column=1)
mensajeUsuario['bg'] = 'white'


igu.mainloop()