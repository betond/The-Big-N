try:
    ##from six.moves
    import tkinter as tk
    from tkinter import ttk
    from pathlib import Path
    from tkinter import filedialog

except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

class UI():

    igu = tk.Tk()
    igu.geometry("900x550")
    igu.title("Práctica No.01 - Criptografía")

    def cifrar():
        print("adios")

    def decifrar():
        print("hola")

    def archivotxt():
        filename = filedialog.askopenfilename()
        if filename:
            # Leer e imprimir el contenido (en bytes) del archivo.
            print(Path(filename).read_bytes())
        else:
            print("No se ha seleccionado ningún archivo.")

    etiquetaCifrar = tk.Label(text="Especifique la ruta del archivo de texto 'txt':")
    etiquetaCifrar.grid(pady=70 ,padx=20 ,row=0, column=0)
    
    ruta = tk.Entry(igu, width=45)
    ruta.grid(row=0, column=1)
    
    botonRuta1 = tk.Button(igu, text="  RUTA-Entrada ", command=archivotxt())
    botonRuta1.grid(row=1, column=2)
    
    etiquetaDecifrar = tk.Label(text="La ruta del archivo 'txt' de salida es : ")
    etiquetaDecifrar.grid(pady=20 ,padx=20 ,row=3, column=0)

    rutaSalida = tk.Entry(igu, width=45)
    rutaSalida.grid(row=3, column=1)
    
    botonRuta2 = tk.Button(igu, text="  RUTA-Salida ")
    botonRuta2.grid(row=4, column=2)

    botonCifrar = tk.Button(igu, text="Cifrar", command=cifrar())
    botonCifrar.grid(pady=150, row=5, column=1)

    botonDecifrar = tk.Button(igu, text="Decifrar", command=decifrar())
    botonDecifrar.grid(pady=150 ,row=5, column=2)
    
    igu.mainloop()


c = UI()