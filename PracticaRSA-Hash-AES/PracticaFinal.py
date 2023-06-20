import tkinter as tk
from tkinter import *
from tkinter import filedialog
from Servicios import *
import hashlib
#-------------------------------------------------------------------------------------------------------------------------------#
archivoEntrada = ""
llavePriv = ""
llavePub = ""

def LeerArchivo(archivoEntrada):
    f1 = open(archivoEntrada, 'rb')
    textoPlano = f1.read()
    f1.close()
    return textoPlano
#-------------------------------------------------------------------------------------------------------------------------------#
def archivoRead():       #Archivo de lectura 
    global archivoEntrada
    pwd = StringVar()
    archivoEntrada = filedialog.askopenfilename()
    if archivoEntrada:
        pwd.set(archivoEntrada)
        ruta.config(textvariable=pwd)
        botonRutaArchivo['bg'] = 'blue' # Al presionar queda azul
        botonRutaArchivo['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")

def llavePrivRead():       #Archivo de lectura de la llave privada
    global llavePriv
    pwd = StringVar()
    llavePriv = filedialog.askopenfilename()
    if llavePriv:
        pwd.set(llavePriv)
        rutaPriv.config(textvariable=pwd)
        botonRutaPriv['bg'] = 'blue' # Al presionar queda azul
        botonRutaPriv['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")

def llavePubRead():       #Archivo de lectura de la llave publica
    global llavePub
    pwd = StringVar()
    llavePub = filedialog.askopenfilename()
    if llavePub:
        pwd.set(llavePub)
        rutaPub.config(textvariable=pwd)
        botonRutaPub['bg'] = 'blue' # Al presionar queda azul
        botonRutaPub['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        print("No se ha seleccionado ningún archivo.")
    
#---------------------------------------------------------------------------------------------------------------------------------

def CifrarFirmar():       #Función de generación de hash
    nmen = []
    #Leemos el mensaje
    textoPlano = LeerArchivo(archivoEntrada)
    #Obtenemos la Clave y el Vector
    clave = entradaClave.get()
    vector = entradaVector.get()
    #Ciframos la Clave y el Vector (RSA - Publica Destinatario)
    clavecif, vectorcif = confidencial(clave, vector, llavePub)
    nmen.append(clavecif)
    nmen.append(vectorcif)
    #Ciframos el mensaje ( AES - CFB)
    nmen.append(cifrar(clave,vector,textoPlano))
    #Ciframos el Hash (RSA - Privada del Remitente)
    nmen.append(firmar_archivo(archivoEntrada, llavePriv))

    estado = StringVar()
    estado.set(":)")
    estadovent.config(textvariable=estado)
    estadovent['bg'] = 'yellow'

    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    nomarchi = nomarchi.split('.')
    salida = str(nomarchi[0]) + "-Firmado.txt"

    for i in range(4) :
        with open(salida, 'ab') as f:
            f.write(nmen[i])
            f.close()

        with open(salida, 'a') as f:
            f.write("-----<<>>-----")
            f.close()

#---------------------------------------------------------------------------------------------------------------------------------------------

def DescifrarValidar():     #Función de descifrado de mensajes
    funcDesc = StringVar()
    estado = StringVar()    
    textoplano = LeerArchivo(archivoEntrada)

    metsplit = textoplano.split(b'-----<<>>-----') #Separamos el texto en las diferentes partes
    
    if len(metsplit) == 5:

        clave, vector = desConfidencial(metsplit[0], metsplit[1], llavePriv) #Desciframos la clave y el vector con nuestra llave privada
        textoclaro = descifrar(clave, vector, metsplit[2]) #Desciframos el mensaje con AES
        #Desciframos la firma con la llave publica del remitente
        firma = verificar_firma(textoclaro, metsplit[3], llavePub)

        if firma:
            funcDesc.set('El mensaje se recibio integro. \n El Hash recibido y el calculado son iguales. \n :)')
            DescifrarValidar['bg'] = 'green'
            estado.set("C:")
            estadovent['bg'] = 'green'
    #Nombre del archivo con el mensaje
            metsplitnom = str(archivoEntrada).split('/')
            n = len(metsplitnom)
            nomarchi = metsplitnom[n-1]
            nomarchi = nomarchi.split('.')
            salida = str(nomarchi[0]) + "-Verificado.txt"

            nmen = "\t\t\tEl mensaje ha sido descifrado y verificado correctamente, gracias por confiar en nosotros.\n\n" + "\nClave del cifrado:  " + str(clave,"UTF-8") + "\nVector de inicializacion del cifrado:  " + str(vector,"UTF-8") + "\n\nEl mensaje recibido es: \n" + str(textoclaro,'UTF-8') + "\n\n\n\nFirma del remitente: " + str(metsplit[3].hex())

            print(nmen)

            with open(salida, 'a') as f:
                f.write(nmen)
                f.close()

        else:
            funcDesc.set('Alerta: \n El mensaje NO se recibio integro. \n El Hash recibido y el calculado NO son iguales. \n :(')
            DescifrarValidar['bg'] = 'red'
            estado.set(":C")
            estadovent['bg'] = 'red'

    else:
        funcDesc.set('Alerta: \n El mensaje NO se recibio integro. \n El Hash recibido y el calculado NO son iguales. \n :(')
        DescifrarValidar['bg'] = 'yellow'
        estado.set(":C")
        estadovent['bg'] = 'yellow'
    DescifrarValidar.config(textvariable=funcDesc)
    estadovent.config(textvariable=estado)


#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1400x800")
igu.title("Práctica No.5 - Función Hash")

#Mensaje al usuario             -----------------           Ruta al archivo de texto del Mensaje
etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto '.txt':")
etiquetaCifrar.grid(pady=20 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRutaArchivo = tk.Button(igu, text="  Ruta del archivo ", command=archivoRead)
botonRutaArchivo.grid(row=0, column=3)

#Mensaje al usuario             ------------------          Ruta de la llave Privada del Usuario
etiquetallavePriv = tk.Label(text="Especifique la ruta de su llave privada:")
etiquetallavePriv.grid(pady=20 ,padx=20 ,row=1, column=0)

#Campo para validar la ruta
rutaPriv = tk.Label(igu, text="Sin selección", width=60)
rutaPriv.grid(row=1, column=1)

#Botón de acción del explorador de archivos
botonRutaPriv = tk.Button(igu, text="  Ruta del archivo ", command=llavePrivRead)
botonRutaPriv.grid(row=1, column=3)

#Mensaje al usuario             ------------------          Ruta de la llave Publica del otro Usuario
etiquetallavePub = tk.Label(text="Especifique la ruta de la llave publica del otro usuario:")
etiquetallavePub.grid(pady=20 ,padx=20 ,row=2, column=0)

#Campo para validar la ruta
rutaPub = tk.Label(igu, text="Sin selección", width=60)
rutaPub.grid(row=2, column=1)

#Botón de acción del explorador de archivos
botonRutaPub = tk.Button(igu, text="  Ruta del archivo ", command=llavePubRead)
botonRutaPub.grid(row=2, column=3)


#Mensaje al usuario Clave               ----------------        Clave para AES
etiquetaClave = tk.Label(text="Introduzca la clave 'key', para el Cifrado del mensaje: ")
etiquetaClave.grid(pady=20 ,padx=20 ,row=3, column=0)

#Entrada de la Cleave-Key
entradaClave = tk.Entry(justify=CENTER)
entradaClave.grid(pady=15, row=4, column=0)

#Mensaje al usuario Vector              ----------------        Vector para AES
etiquetaVector = tk.Label(text="Introduzca el vector de inicio, para el Cifrado del mensaje: ")
etiquetaVector.grid(pady=20 ,padx=20 ,row=3, column=1)

#Entrada del Vector
entradaVector = tk.Entry(justify=CENTER)
entradaVector.grid(pady=15, row=4, column=1)

#Imagenes
estadovent = tk.Label(igu, text=":|",font=("Arial", 50))
estadovent.grid(row=4 ,column= 3)

#Botón Cifrar y Firmar  
botonGenerar = tk.Button(igu, text=" Cifrar y Firmar mensaje ", command=CifrarFirmar)
botonGenerar.grid(pady=50, row=5, column=1)

#Botón DescifrarValidar - 
botonValidar = tk.Button(igu, text=" Descifrar y Validar mensaje ", command=DescifrarValidar)
botonValidar.grid(pady=50 ,row=5, column=2)

#Mensaje de Notificación
DescifrarValidar = tk.Label(igu, text=" Esperando validar hash ", width=60)
DescifrarValidar.grid(pady=15 ,row=6, column=1)
DescifrarValidar['bg'] = 'white'

igu.mainloop()