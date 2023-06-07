import hashlib
import base64

class HASH:

    dir = None #Dirección completa de almacenamiento del archivo
    path = None #Ruta de la carpeta del archivo
    namefile = None #Nombre sin extension

    def __int__(self):
        pass

    def setAttributesFile(self, path: str):

        self.dir = path
        aux = path.split("/")
        name = aux[-1].split(".")
        self.namefile = name[0]
        self.path = self.dir.replace(aux[-1], "")

    def encryptTXT(self):
        # Abrimos el archivo a cifrar
        with open(self.dir, 'rb') as f:
            texto_plano = f.read()

        #SHA 1
        h = hashlib.new('sha1')
        h.update(texto_plano)
        digesto = h.hexdigest()
        #digesto = base64.b64encode(h.digest())
        #encode_digest = digesto.decode("UTF-8")
        print(digesto)

        # Guardamos el texto cifrado en un archivo
        with open(f'{self.namefile}_hash.txt', 'wb') as f:
            f.write(texto_plano)
            f.close()

        with open(f'{self.namefile}_hash.txt', 'a') as f:
            f.write(f"------DIGESTO------{digesto}")
            f.close()

    def verify(self):
        #Leer el contenido del archivo
        with open(self.dir, 'rb') as f:
            texto = f.read()


        partes = texto.split(b"------DIGESTO------")
        texto = partes[0].decode('utf-8')
        try:
            digesto = partes[1].decode('utf-8')
        except:
            return "ERROR: EL ARCHIVO NO CONTIENE UN DIGESTO"

        #SHA 1
        h = hashlib.new('sha1')
        h.update(texto.encode('utf-8'))
        digesto_real = h.hexdigest()


        if digesto == digesto_real:
            return "EL CONTENIDO COINCIDE =D \U0001F600"
        else:
            return "EL CONTENIDO FUE ALTERADO! D= \U0001F624"