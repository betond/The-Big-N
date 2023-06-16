try:
    from Cryptodome.PublicKey import RSA
    from Cryptodome.Cipher import PKCS1_OAEP
    import base64

except ImportError:
    raise ImportError("Se requiere el modulo Tkinter y pycryptodome")
# -------------------------------------------------------------------------------------------------------------------------------#

class rsaCipher:
    archivoMensaje = ""
    archivokey = ""
    key_dir = None
    digest = ""

    def __int__(self):
        pass

    def setAttributesFile(self, digest: str, key_path: str):
        #self.dir = path
        #aux = path.split("/")
        #name = aux[-1].split(".")
        #self.namefile = name[0]
        #self.path = self.dir.replace(aux[-1], "")
        self.key_dir = key_path
        self.digest = digest


    def cifrar(self):  # Función de cifrado de mensajes

        textoPlano = bytes(self.digest, encoding='utf-8')

        llave = RSA.importKey(open(self.key_dir).read())
        nuevoCifrado = PKCS1_OAEP.new(llave)

        nmen = nuevoCifrado.encrypt(textoPlano)
        nmen = base64.b64encode(nmen)
        decode_digest = nmen.decode("UTF-8")

        return decode_digest


    def descifrar(self):  # Función de decifrado de mensajes

        textoPlano = self.digest

        llave = RSA.importKey(open(self.key_dir).read())
        nuevoDescifrado = PKCS1_OAEP.new(llave)

        textoPlano = base64.b64decode(textoPlano.encode("UTF-8"))

        nmen = nuevoDescifrado.decrypt(textoPlano)
        decode_digest = str(nmen.decode("UTF-8"))

        return decode_digest

