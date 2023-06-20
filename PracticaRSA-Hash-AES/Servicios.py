from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import * 
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64
from cryptography.hazmat.primitives import hashes as hashff
from cryptography.hazmat.primitives.asymmetric import padding as paddf
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


#   Generar la firma con la llave privada del remitente
def firmar_archivo(archivo, clave_privada):
    with open(archivo, 'rb') as file:
        contenido = file.read()
    
    realizar_firma = load_pem_private_key(open(clave_privada,'rb').read(), password=None)
    firma = realizar_firma.sign(contenido,paddf.PSS(mgf=paddf.MGF1(hashff.SHA256()),salt_length=paddf.PSS.MAX_LENGTH),hashff.SHA256())
    
    return firma

#   Verificar el Hash con la llave publica del remitente
def verificar_firma(textoclaro, firma, clave_publica):
    print(str(textoclaro))
    pub = open(clave_publica,'rb').read()
    revisar_firma = load_pem_public_key(pub)
    
    try:
        print(f'Firma digital generada: {firma.hex()}')
        revisar_firma.verify(firma, textoclaro,paddf.PSS(mgf=paddf.MGF1(hashff.SHA256()),salt_length=paddf.PSS.MAX_LENGTH),hashff.SHA256())
        return True
    except Exception:
        return False

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

    nmen = cipher.decrypt(textocifrado)

    textoClaro = nmen

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