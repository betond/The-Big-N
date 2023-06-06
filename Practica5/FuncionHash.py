try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog
    import hashlib, base64

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


def generarHash():       #Función de generación de hash
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()
#######################################################
    textoPlanob = textoPlano.encode()
    m = hashlib.sha1(textoPlanob).hexdigest()

    print(str(m))

    nmen = m + '|||' + textoPlano
#######################################################
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    nomarchi = nomarchi.split('.')
    salida = str(nomarchi[0]) + "-hash.txt"
    
    f2 = open(salida, 'a')
    f2.write(nmen)
    f2.close() 


def validarHash():     #Función de descifrado de mensajes
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()
    funcDesc = StringVar()

    metsplit = textoPlano.split('|||')
    if len(metsplit) == 2:

        msghash = metsplit[0]

        print(metsplit)

        newhash = hashlib.sha1(metsplit[1].encode()).hexdigest()


        if msghash == newhash:
            funcDesc.set('El mensaje se recibio integro. \n El Hash recibido y el calculado son iguales')
            validarHash['bg'] = 'green'
        else:
            funcDesc.set('Alerta: \n El mensaje NO se recibio integro. \n El Hash recibido y el calculado NO son iguales')
            validarHash['bg'] = 'red'

    else:
        funcDesc.set('Alerta: \n El archivo seleccionado NO se genero con esta aplicación. \n Verifique la ruta del archivo seleccionado.')
        validarHash['bg'] = 'yellow'
    validarHash.config(textvariable=funcDesc)
    


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

#Función de Validación de Hash
validarHash = tk.Label(igu, text=" Esperando validar hash ", width=60)
validarHash.grid(pady=30 ,row=6, column=1)
validarHash['bg'] = 'white'


igu.mainloop()