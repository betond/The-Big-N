from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from file_manager import *
import binascii


def encrypt_message(path_file="message.txt",path_key='publicKey_A.pem'):
    # Leer archivo
    msg = bytes(open_read_file(path_file), encoding='utf8')
    
    #   Abrir llave publica A
    f = open(path_key,'r')
    pubKey_B = RSA.importKey(f.read())
    publicKey_B = pubKey_B.publickey()
    f.close()

    #   Cifrar usando llave publica A
    encryptor = PKCS1_OAEP.new(publicKey_B)
    encrypted = encryptor.encrypt(msg)
    
    #   Escribit txt
    f = open('message_C.txt','wb')
    f.write(encrypted)
    f.close()


def decrypt_message(path_encrypt_file="message_C.txt",path_key="privateKey_A.pem"):   
    #   Leer archivo cifrado
    f = open(path_encrypt_file, 'rb')
    msg = f.read()

    #   Abrir llave privada A
    f = open(path_key,'r')
    privKey_A = RSA.importKey(f.read())
    
    #   Decifrar con privada A
    cipher = PKCS1_OAEP.new(privKey_A)
    message = cipher.decrypt(msg)

    #   Escribir mensaje 
    f = open('message_C_D.txt','w')
    f.write(str(message.decode("utf-8")))
    f.close()


def main():
    encrypt_message()
    decrypt_message()

if __name__ == "__main__":
    main()
