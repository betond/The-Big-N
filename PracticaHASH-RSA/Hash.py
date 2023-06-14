import hashlib
from RSA import *

class HASH:

    dir = None #Dirección completa de almacenamiento del archivo
    path = None #Ruta de la carpeta del archivo
    namefile = None #Nombre sin extension
    key_dir = None

    def __int__(self):
        pass

    def setAttributesFile(self, path: str, key_path):

        self.dir = path
        aux = path.split("/")
        name = aux[-1].split(".")
        self.namefile = name[0]
        self.path = self.dir.replace(aux[-1], "")
        self.key_dir = key_path

    def getDigest(self):

        # Abrimos el archivo a cifrar
        with open(self.dir, 'rb') as f:
            texto_plano = f.read()

        #SHA 1
        h = hashlib.new('sha1')
        h.update(texto_plano)

        digesto = base64.b64encode(h.digest())
        digest = digesto.decode("UTF-8")

        rsa = rsaCipher()
        rsa.setAttributesFile(digest, self.key_dir)
        enc_digest = rsa.cifrar()

        # Guardamos el texto cifrado en un archivo
        with open(f'{self.namefile}_firmado.txt', 'wb') as f:
            f.write(texto_plano)
            f.close()

        with open(f'{self.namefile}_firmado.txt', 'a') as f:
            f.write(f"------FIRMA------{enc_digest}")
            f.close()

    def verify(self):
        #Leer el contenido del archivo
        with open(self.dir, 'rb') as f:
            texto = f.read()


        partes = texto.split(b"------FIRMA------")
        texto = partes[0].decode('utf-8')
        try:
            digesto_cifrado = partes[1].decode('utf-8')
        except:
            return "ERROR: EL ARCHIVO NO CONTIENE UN DIGESTO CIFRADO"

        #DESCIFRAR DIGESTO
        rsa = rsaCipher()
        rsa.setAttributesFile(digesto_cifrado, self.key_dir)
        dec_digest = rsa.descifrar()

        #OBTENGO EL DIGESTO REAL SHA 1
        h = hashlib.new('sha1')
        h.update(texto.encode('utf-8'))

        digesto = base64.b64encode(h.digest())
        digesto_real = digesto.decode("UTF-8")

        if dec_digest == digesto_real:
            return "INTEGRIDAD y AUTENTICACIÓN CUMPLIDA \U0001F600"
        else:
            return "LA INTEGRIDAD Y AUTENTICACIÓN NO SE CUMPLE! D= \U0001F624"