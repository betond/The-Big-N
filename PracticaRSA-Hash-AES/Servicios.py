from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import *
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import hashlib, base64


def generarHash(textoPlano):
    h = hashlib.new('sha256')
    h.update(textoPlano)
    digesto = base64.b64encode(h.digest())
    digest = digesto.decode("UTF-8")
    return digest

#   Cifra el Hash con la llave privada del remitente
def firmar(hash, llavePriv):
    llave = RSA.import_key(open(llavePriv).read())
    nuevoCifrado = PKCS1_OAEP.new(llave)
    tp = bytes(hash,encoding='utf-8')
    
    firma = nuevoCifrado.encrypt(tp)
    
    return firma

#   Descifra el Hash con la llave publica del remitente
def validar(hash, llavePub):
    llave = RSA.import_key(open(llavePub).read())
    nuevoCifrado = PKCS1_OAEP.new(llave)

    firma = nuevoCifrado.decrypt(hash)

    firmaDes = firma.decode("UTF-8")

    return firmaDes

#   Cifrar mensaje AES y pasar en bytes
def cifrar(clave, vector, textoplano):
    key = pad(bytes(clave,'utf-8'),16)
    ivs = pad(bytes(vector,'utf-8'),16)
    textoplanob = textoplano

    cipher = AES.new(key,AES.MODE_CFB, ivs)

    textoCifradob = cipher.encrypt(textoplanob)

    return textoCifradob

#   Descifrar mensaje AES y convertir a string
def descifrar(clave, vector, textocifrado):
    key = pad(clave,16)
    ivs = pad(vector,16)

    cipher = AES.new(key,AES.MODE_CFB, ivs)

    nmen = cipher.decrypt(textocifrado).decode('utf-8')

    textoClaro = str(nmen)

    return textoClaro

#   Cifrar la clave y el vector con la llave publica del destinatario
def confidencial(clave, vector, llavePub):
    llave = RSA.import_key(open(llavePub).read())
    nuevoCifrado = PKCS1_OAEP.new(llave)

    clavecif = nuevoCifrado.encrypt(bytes(clave,encoding='utf8'))
    vectorcif = nuevoCifrado.encrypt(bytes(vector,encoding='utf8'))

    return clavecif, vectorcif

#   Descifrar la clave y el vector con la llave privada personal
def desConfidencial(clave, vector, llavePriv):
    llave = RSA.import_key(open(llavePriv).read())
    nuevoCifrado = PKCS1_OAEP.new(llave)

    clavedes = nuevoCifrado.decrypt(clave)
    vectordes= nuevoCifrado.decrypt(vector)

    return clavedes, vectordes