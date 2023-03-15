from pathlib import Path
from tkinter import filedialog

filename = filedialog.askopenfilename()
if filename:
    # Leer e imprimir el contenido (en bytes) del archivo.
    print(Path(filename).read_bytes())
else:
    print("No se ha seleccionado ningún archivo.")