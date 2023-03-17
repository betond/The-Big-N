try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requieren los modulos Tkinter")
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
        botonRuta1['bg'] = 'green' # Al presionar queda azul
        botonRuta1['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        botonRuta1['bg'] = 'red' # Al presionar queda azul
        botonRuta1['fg'] = 'white' # Si pasamos el Mouse queda blanco
        print("No se ha seleccionado ningún archivo.")

#Algoritmo de Euclides con recursividad
def maximo_comun_divisor(n, a):
    if a == 0:
        return n
    return maximo_comun_divisor(a, n % a)    

def validarEntradas():
    
    mcd = maximo_comun_divisor(int(entradaN.get()), int(entradaAlfa.get()))

    msguser = StringVar()

    if mcd != 1:
        msguser.set("Los valores seleccionados no son correctos ( mcd(n,alfa) != 1 ). \n" + "mcd(" + entradaN.get() + "," + entradaAlfa.get() + ") = " + str(mcd))
        botonValEnt['bg'] = 'red' # Al presionar queda azul
        botonValEnt['fg'] = 'white' # Si pasamos el Mouse queda blanco
    else:
        msguser.set("Los valores seleccionados son correctos ( mcd(n,alfa) = 1 ). \n" + "mcd(" + entradaN.get() + "," + entradaAlfa.get() + ") = " + str(mcd))
        botonValEnt['bg'] = 'green' # Al presionar queda azul
        botonValEnt['fg'] = 'white' # Si pasamos el Mouse queda blanco

    mensajeUsuario.config(textvariable=msguser)

def cifrar():       #Función de cifrado de mensajes
    
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()

    a = int(entradaAlfa.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    nmen = ""
    for caracter in textoPlano:
        nmen += str(chr(( a * ord(caracter) + b % n ))) ## Corregir rango y revisar alfabeto
    
    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    nomarchi = nomarchi.split('.')
    salida = str(nomarchi[0]) + "-c.txt"
    
    f2 = open(salida, 'a')
    f2.write(nmen)
    f2.close()  


def descifrar():     #Función de descifrado de mensajes
    f1 = open(archivoEntrada, 'r')
    textoPlano = f1.read()
    f1.close()

    a = int(entradaAlfa.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    invmulta = 3           ## pendiente de solución
    invaddb = n - b

    print(str(invmulta) + "<------------------------->" + str(invaddb))

    nmen = ""
    for caracter in textoPlano:
        nmen += str(chr(( invmulta * ord(caracter) + invaddb % n ))) ## Corregir rango y revisar alfabeto
    
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
igu.geometry("1100x800")
igu.title("Práctica No.1 - Criptografía - MCD (Maximo Comun Divisor) - Algoritmo ")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta de la imagen '.bmp':")
etiquetaCifrar.grid(pady=50 ,padx=20 ,row=0, column=0)

#Campo para validar la ruta
ruta = tk.Label(igu, text="Sin selección", width=60)
ruta.grid(row=0, column=1)

#Botón de acción del explorador de archivos
botonRuta1 = tk.Button(igu, text="  RUTA-Entrada ", command=archivoReadBMP)
botonRuta1.grid(row=1, column=2)

#Mensaje al usuario Alfa
etiquetaAlfa = tk.Label(text="Introduzca el valor de alfa: ")
etiquetaAlfa.grid(pady=20 ,padx=20 ,row=3, column=0)

#Entrada de Alfa
entradaAlfa = tk.Entry(justify=CENTER)
entradaAlfa.grid(pady=15, row=4, column=0)

#Mensaje al usuario Beta
etiquetaBeta = tk.Label(text="Introduzca el valor de beta: ")
etiquetaBeta.grid(pady=20 ,padx=20 ,row=3, column=1)

#Entrada de Beta
entradaBeta = tk.Entry(justify=CENTER)
entradaBeta.grid(pady=15, row=4, column=1)

#Mensaje al usuario n
etiquetaN = tk.Label(text="Introduzca el valor de n:")
etiquetaN.grid(pady=20 ,padx=20 ,row=3, column=2)

#Entrada de n
entradaN = tk.Entry(justify=CENTER)
entradaN.grid(pady=15, row=4, column=2)

#Campo mensaje usuario
mensajeUsuario = tk.Label(igu, text="Sin probar", width=60)
mensajeUsuario.grid(row=6, column=1)

#Botón Validar entradas
botonValEnt = tk.Button(igu, text="Validar entradas", command=validarEntradas)
botonValEnt.grid(pady=150, row=5, column=0)

#Botón cifrar - 
botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón descifrar - 
botonDescifrar = tk.Button(igu, text="Descifrar", command=descifrar)
botonDescifrar.grid(pady=150 ,row=5, column=2)

igu.mainloop()