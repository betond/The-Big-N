from cryptography.hazmat.primitives import hashes as hashff
from cryptography.hazmat.primitives.asymmetric import padding as paddf
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def firmar_archivo(archivo, clave_privada):
    with open(archivo, 'rb') as file:
        contenido = file.read()
    
    realizar_firma = load_pem_private_key(open(clave_privada,'rb').read(), password=None)

    firma = realizar_firma.sign(contenido,paddf.PSS(mgf=paddf.MGF1(hashff.SHA256()),salt_length=paddf.PSS.MAX_LENGTH),hashff.SHA256())
    #firma = crypto.sign(pkey, contenido, 'sha256')
    return firma

def verificar_firma(archivo, firma, clave_publica):
    with open(archivo, 'rb') as file:
        contenido = file.read()
    
    pub = open(clave_publica,'rb').read()
    revisar_firma = load_pem_public_key(pub)
    
    try:
        print(f'Firma digital generada: {firma.hex()}')
        revisar_firma.verify(firma, contenido,paddf.PSS(mgf=paddf.MGF1(hashff.SHA256()),salt_length=paddf.PSS.MAX_LENGTH),hashff.SHA256())
        return True
    except Exception:
        return False

# Ejemplo de uso
archivo = '/home/betond971227/Escritorio/The-Big-N/PracticaRSA-Hash-AES/SpeedDemon.txt'
clave_privada = '/home/betond971227/Escritorio/.sec/NMJA-Privada.pem'
clave_publica = '/home/betond971227/Escritorio/.sec/NMJA-Publica.pem'

firma = firmar_archivo(archivo, clave_privada)
print(f'Firma digital generada: {firma.hex()}')

verificado = verificar_firma(archivo, firma, clave_publica)
print(f'Firma digital verificada: {verificado}')
