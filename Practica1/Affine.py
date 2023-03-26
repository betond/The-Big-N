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
    texto = StringVar()
    texto.set("Sin valores")
    fCifrado.config(textvariable=texto)
    fCifrado['bg'] = 'white'
    fDescifrado.config(textvariable=texto)
    fDescifrado['bg'] = 'white'
    mensajeUsuario.config(textvariable=texto)
    mensajeUsuario['bg'] = 'white'

    a = int(entradaAlpha.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    errorbeta = StringVar()
    
    if b<0:
        equiv = abs(n+b)
        errorbeta.set("Error: Beta debe ser parte del conjunto (0," + str(n) + "]\n Beta debe ser mayor que 0 : Valor equivalente= " + str(equiv))
        mensajeBeta['bg'] = 'red'   #Color rojo - Advertencia
        entradaBeta['bg'] = 'red'   #Color rojo - Advertencia
    elif b>n:
        equiv = b%n
        errorbeta.set("Error: Beta debe ser parte del conjunto (0," + str(n) + "]\n Beta debe ser menor que " + str(n) + " : Valor equivalente= " + str(equiv))
        mensajeBeta['bg'] = 'red'   #Color rojo - Advertencia
        entradaBeta['bg'] = 'red'   #Color rojo - Advertencia
    else:
        errorbeta.set("El valor pertenece al conjunto (0,"+ str(n) +"]")
        mensajeBeta['bg'] = 'green'   #Color verde - Validado
        entradaBeta['bg'] = 'green'   #Color verde - Validado

    mensajeBeta.config(textvariable=errorbeta)

    mcd = maximo_comun_divisor(n, a)

    msguser = StringVar()
    errorAlpha = StringVar()
    errorN = StringVar()

    if mcd != 1:
        msguser.set("Los valores seleccionados no son correctos ( mcd(n,Alpha) != 1 ). \n" + "mcd(" + entradaN.get() + "," + entradaAlpha.get() + ") = " + str(mcd))
        botonValEnt['bg'] = 'red' # Al presionar queda rojo
        botonValEnt['fg'] = 'white' # Si pasamos el Mouse queda blanco
        errorAlpha.set("Error: El valor de Alpha = " + str(a) + " no es correcto.\nIntroduzca un nuevo valor para Alpha.")
        mensajeAlpha['bg'] = 'red'   #Color rojo - Advertencia
        entradaAlpha['bg'] = 'red'   #Color rojo - Advertencia
        errorN.set("El valor de n es correcto.")
        mensajeN['bg'] = 'red'   #Color rojo - Advertencia
        entradaN['bg'] = 'red'   #Color rojo - Advertencia
    else:
        msguser.set("Los valores seleccionados son correctos ( mcd(n,Alpha) = 1 ). \n" + "mcd(" + entradaN.get() + "," + entradaAlpha.get() + ") = " + str(mcd))
        botonValEnt['bg'] = 'green' # Al presionar queda verde
        botonValEnt['fg'] = 'white' # Si pasamos el Mouse queda blanco
        errorAlpha.set("El valor de Alpha es correcto")
        mensajeAlpha['bg'] = 'green'   #Color verde - Validado
        entradaAlpha['bg'] = 'green'   #Color verde - Validado
        errorN.set("El valor de n es correcto.")
        mensajeN['bg'] = 'green'   #Color verde - Validado
        entradaN['bg'] = 'green'   #Color verde - Validado

    if a<0:
        equiv = n+b
        errorAlpha.set("Error: Alpha debe ser parte del conjunto (0," + str(n) + "]\n Alpha debe ser mayor que 0 : Valor equivalente= " + str(equiv))
        mensajeAlpha['bg'] = 'red'   #Color rojo - Advertencia
        entradaAlpha['bg'] = 'red'   #Color rojo - Advertencia
    elif a>n:
        equiv = a%n
        errorAlpha.set("Error: Alpha debe ser parte del conjunto (0," + str(n) + "]\n Alpha debe ser menor que " + str(n) + " : Valor equivalente= " + str(equiv))
        mensajeAlpha['bg'] = 'red'   #Color rojo - Advertencia
        entradaAlpha['bg'] = 'red'   #Color rojo - Advertencia

    mensajeUsuario.config(textvariable=msguser)
    mensajeAlpha.config(textvariable=errorAlpha)
    mensajeN.config(textvariable=errorN)

def cifrar():       #Función generadora de función de cifrado

    a = int(entradaAlpha.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    funcCifrado = StringVar()
    funcCifrado.set("La función de cifrado es:\n C = " + str(a) + " m " + " + " + str(b) + " mod " + str(n))
    fCifrado.config(textvariable=funcCifrado)
    fCifrado['bg'] = 'yellow'

def descifrar():     #Función de descifrado de mensajes

    a = int(entradaAlpha.get())
    b = int(entradaBeta.get())
    n = int(entradaN.get())

    gcd, invn, inva = extended_gcd(n, a)
    invaddb = n - b
    
    if inva < 0:
        invmulta = inva + n
    else:
        invmulta = inva

    simpli = (invmulta*invaddb)%n

    funcDesc = StringVar()
    funcDesc.set("La función de descifrado es:\n m = " + str(invmulta) + "( C + " + str(invaddb) + " ) mod " + str(n) + "\nm = " + str(invmulta) + " C + " + str(simpli) + " mod " + str(n))
    fDescifrado.config(textvariable=funcDesc)
    fDescifrado['bg'] = 'yellow'

#Ventana principal de la interfaz grafica
igu = tk.Tk()
igu.geometry("1000x800")
igu.title("Práctica No.1 - Criptografía - MCD (Maximo Comun Divisor)")

#Mensaje al usuario Alpha
etiquetaAlpha = tk.Label(text="Introduzca el valor de Alpha: ")
etiquetaAlpha.grid(pady=40 ,padx=30 ,row=1, column=0)

#Campo advertencia al usuario Alpha
mensajeAlpha = tk.Label(igu)
mensajeAlpha.grid(row=3, column=0)

#Entrada de Alpha
entradaAlpha = tk.Entry(justify=CENTER)
entradaAlpha.grid(pady=15, row=2, column=0)

#Mensaje al usuario Beta
etiquetaBeta = tk.Label(text="Introduzca el valor de beta: ")
etiquetaBeta.grid(pady=40 ,padx=20 ,row=1, column=1)

#Campo advertencia al usuario Beta
mensajeBeta = tk.Label(igu)
mensajeBeta.grid(row=3, column=1)

#Entrada de Beta
entradaBeta = tk.Entry(justify=CENTER)
entradaBeta.grid(pady=15, row=2, column=1)

#Mensaje al usuario n
etiquetaN = tk.Label(text="Introduzca el valor de n:")
etiquetaN.grid(pady=40 ,padx=20 ,row=1, column=2)

#Campo advertencia al usuario N
mensajeN = tk.Label(igu)
mensajeN.grid(row=3, column=2)

#Entrada de n
entradaN = tk.Entry(justify=CENTER)
entradaN.grid(pady=15, row=2, column=2)

#Botón Validar entradas
botonValEnt = tk.Button(igu, text="Validar entradas", command=validarEntradas)
botonValEnt.grid(pady=50, row=4, column=0)

#Botón Función de Cifrado
botonCifrar = tk.Button(igu, text="Generar Función de Cifrado", command=cifrar)
botonCifrar.grid(pady=50, row=4, column=1)

#Botón Función de Descifrado
botonDescifrar = tk.Button(igu, text="Generar Función de Descifrado", command=descifrar)
botonDescifrar.grid(pady=50 ,row=4, column=2)

#Campo mensaje usuario
mensajeUsuario = tk.Label(igu, text="Sin probar", width=60)
mensajeUsuario.grid(row=5, column=1)
mensajeUsuario['bg'] = 'white'

#Función de cifrado
fCifrado = tk.Label(igu, text="Sin valores", width=60)
fCifrado.grid(pady=15 ,row=6, column=1)
fCifrado['bg'] = 'white'

#Función de Descifrado
fDescifrado = tk.Label(igu, text="Sin valores", width=60)
fDescifrado.grid(pady=15 ,row=7, column=1)
fDescifrado['bg'] = 'white'

igu.mainloop()