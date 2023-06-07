from Crypto.PublicKey import RSA

def keysPublic_Generator():
    keyPair = RSA.generate(3072)
    
    f = open('publicKey_A.pem','wb')
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    f.write(pubKeyPEM)
    f.close()

    f = open('privateKey_A.pem','wb')
    privKeyPEM = keyPair.exportKey()
    f.write(privKeyPEM)
    f.close()

#keysPublic_Generator()