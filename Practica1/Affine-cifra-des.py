try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requieren los modulos Tkinter")
#-------------------------------------------------------------------------------------------------------------------------------#
archivoEntrada = ""
#alfabeto = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "Ñ":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
alfabeto = {    "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
desalfabeto = { 0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

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

#Algoritmo de Euclides extendido con recursividad
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

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
    textoentrada = f1.read()
    f1.close()

    textoPlano = textoentrada.upper()
    a = int(entradaAlfa.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    nmen = ""
    for caracter in textoPlano:
        nmen += str( desalfabeto.get((((a*int(alfabeto.get(caracter))+b)%n)))) ## Cifrado affine

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

    gcd, x, invmulta = extended_gcd(n, a)
    invaddb = n - b
    print(str(gcd) + "---------" + str(x) + "---------" + str(invmulta))

    nmen = ""
    for caracter in textoPlano:
        nmen += str(desalfabeto.get((((invmulta*(int(alfabeto.get(caracter))+invaddb))%n))))

    metsplit = str(archivoEntrada).split('/')
    n = len(metsplit)
    nomarchi = metsplit[n-1]
    nomarchi = nomarchi.split('.')
    salida = str(nomarchi[0]) + "-d.txt"

    nmenout = nmen.title()
    
    f2 = open(salida, 'a')
    f2.write(nmenout)
    f2.close() 

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x800")
igu.title("Práctica No.1 - Criptografía - MCD (Maximo Comun Divisor) - Algoritmo ")

#Mensaje al usuario
etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto '.txt':")
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