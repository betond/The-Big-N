try:
    from six.moves import tkinter as tk
    from tkinter import *
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requieren los modulos Tkinter")
#-------------------------------------------------------------------------------------------------------------------------------#
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

def cifrar():       #Función generadora de función de cifrado

    a = int(entradaAlfa.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    funcCifrado = StringVar()
    funcCifrado.set("C = " + str(a) + " m " + " + " + str(b) + " mod " + str(n))
    fCifrado.config(textvariable=funcCifrado)

def descifrar():     #Función de descifrado de mensajes

    a = int(entradaAlfa.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    gcd, x, invmulta = extended_gcd(n, a)
    invaddb = n - b

    nvalores = StringVar()
    nvalores.set("El maximo comun divisor es: " + str(gcd) + "\nEl inverso miltiplicativo de n es: " + str(x) + "\nEl inverso multiplicativo de alfa es: " + str(invmulta))
    valoresdes.config(textvariable=nvalores)

    simpli = (invmulta*invaddb)%n

    funcDesc = StringVar()
    funcDesc.set("m = " + str(invmulta) + "( C + " + str(invaddb) + " ) mod " + str(n) + "\nm = " + str(invmulta) + " C + " + str(simpli) + " mod " + str(n))
    fDescifrado.config(textvariable=funcDesc)

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1100x800")
igu.title("Práctica No.1 - Criptografía - MCD (Maximo Comun Divisor) - Algoritmo ")

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

#Campo mensaje inverso multiplicativo
valoresdes = tk.Label(igu, text="Sin valores", width=60)
valoresdes.grid(pady=15 ,row=7, column=1)

#Botón Validar entradas
botonValEnt = tk.Button(igu, text="Validar entradas", command=validarEntradas)
botonValEnt.grid(pady=150, row=5, column=0)

#Botón Función de Cifrado
botonCifrar = tk.Button(igu, text="Generar Función de Cifrado", command=cifrar)
botonCifrar.grid(pady=150, row=5, column=1)

#Botón Función de Descifrado
botonDescifrar = tk.Button(igu, text="Generar Función de Descifrado", command=descifrar)
botonDescifrar.grid(pady=150 ,row=5, column=2)

#Función de cifrado
fCifrado = tk.Label(igu, text="Sin valores", width=60)
fCifrado.grid(pady=15 ,row=8, column=1)

#Función de Descifrado
fDescifrado = tk.Label(igu, text="Sin valores", width=60)
fDescifrado.grid(pady=15 ,row=9, column=1)

igu.mainloop()