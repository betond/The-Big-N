import base64
import os
import struct
from Crypto.PublicKey import RSA

# función para cifrar un mensaje utilizando la llave pública
def encrypt(public_key, message):
    return public_key.encrypt(message.encode('utf-8'), 32)[0]

# función para descifrar un mensaje utilizando la llave privada
def decrypt(private_key, cipher):
    return private_key.decrypt(cipher).decode('utf-8')

# ejemplo de uso
if __name__ == '__main__':
    # leemos la llave pública y privada del archivo PEM
    with open('llaves.pem', 'r') as f:
        key_data = f.read()

    # convertimos la llave pública y privada al formato RSA
    key = RSA.import_key(key_data)

    # obtenemos la llave pública y privada del objeto RSA
    public_key = key.publickey()
    private_key = key

    # ciframos el mensaje 'Hola, mundo!'
    message = 'Hola, mundo!'
    cipher = encrypt(public_key, message)

    # imprimimos el mensaje cifrado
    print('Mensaje cifrado:', base64.b64encode(cipher))

    # desciframos el mensaje cifrado
    decrypted_message = decrypt(private_key, cipher)

    # imprimimos el mensaje descifrado
    print('Mensaje descifrado:', decrypted_message)