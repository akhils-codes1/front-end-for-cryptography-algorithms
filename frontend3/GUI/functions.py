from Crypto.Cipher import AES, DES, DES3, Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
#from json import dumps, loads


#note: 
# UTF-8 and UTF-16 are methods to encode Unicode strings to byte sequences.
# Base64 is a method to encode a byte sequence to a string.
# so for encryption, we need to convert the string into a byte sequence using base64 and then decode it as unicode, so that we can read
# during decryption, we have to convert this unicode to byte sequence using utf-8 and the byte sequence back to original format using base64

#base64 encoding and decoding functions for use in random text
def base64_encode(message_bytes):
    #message = "Python is fun"
    #message_bytes = message.encode('ascii')#converts into bytes
    base64_bytes = b64encode(message_bytes)#base64 encoding
    base64_message = base64_bytes.decode('utf-8')#bytes to ascii
    return base64_message

def base64_decode(string):
    base64_message = string
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = b64decode(base64_bytes)#base64 decoding
    #message = message_bytes.decode('ascii')
    return message_bytes

#generate random cipher text
def random_text(n):
    text1 = get_random_bytes(n)
    #print(text1)
    #encoding random bytes so generated into base64
    enc = base64_encode(text1)
    return enc
    #print(enc)
    #print(base64_decode(enc))# for decoding the encoded string back to random bytes format



#des
def des_encrypt_cbc(data: str, key: str) -> str:
    cipher = DES.new(key, DES.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(data, DES.block_size))
    init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    encrypted = (init_vector, cipher_text)
    return encrypted

def des_decrypt_cbc(encrypted: list, key: str):
    #b64 = loads(encrypted)
    init_vector = b64decode(encrypted[0])
    cipher_text = b64decode(encrypted[1])
    cipher = DES.new(key, DES.MODE_CBC, init_vector)
    plaintext = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plaintext

def des_encrypt_ecb(data: str, key: str) -> str:
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_bytes = cipher.encrypt(pad(data, DES.block_size))
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    return cipher_text

def des_decrypt_ecb(ciphertext, key):
    cipher_text = b64decode(ciphertext)
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plaintext
    
    
#des3
def des3_encrypt_cbc(data: str, key: str) -> str:
    key = DES3.adjust_key_parity(key)
    cipher = DES3.new(key, DES3.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(data, DES3.block_size))
    init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    encrypted = (init_vector, cipher_text)
    return encrypted

def des3_decrypt_cbc(encrypted: list, key: str):
    key = DES3.adjust_key_parity(key)
    #b64 = loads(encrypted)
    init_vector = b64decode(encrypted[0])
    cipher_text = b64decode(encrypted[1])
    cipher = DES3.new(key, DES3.MODE_CBC, init_vector)
    plaintext = unpad(cipher.decrypt(cipher_text), DES3.block_size)
    return plaintext

def des3_encrypt_ecb(data: str, key: str) -> str:
    key = DES3.adjust_key_parity(key)
    cipher = DES3.new(key, DES3.MODE_ECB)
    cipher_bytes = cipher.encrypt(pad(data, DES3.block_size))
    #init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    return cipher_text

def des3_decrypt_ecb(ciphertext, key):
    key = DES3.adjust_key_parity(key)
    cipher_text = b64decode(ciphertext)
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt(cipher_text), DES3.block_size)
    return plaintext

#aes
def aes_encrypt_cbc(data: str, key: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(data, AES.block_size))
    init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    encrypted = (init_vector, cipher_text)
    return encrypted

def aes_decrypt_cbc(encrypted: list, key: str):
    #b64 = loads(encrypted)
    init_vector = b64decode(encrypted[0])
    cipher_text = b64decode(encrypted[1])
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    plaintext = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plaintext

def aes_encrypt_ecb(data: str, key: str) -> str:
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_bytes = cipher.encrypt(pad(data, AES.block_size))
    #init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    return cipher_text

def aes_decrypt_ecb(ciphertext, key):
    #init_vector = b64decode(b64['init_vector'])
    cipher_text = b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plaintext


#Blowfish
def blowfish_encrypt_cbc(data: str, key: str) -> str:
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
    init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    encrypted = (init_vector, cipher_text)
    return encrypted

def blowfish_decrypt_cbc(encrypted: list, key: str):
    #b64 = loads(encrypted)
    init_vector = b64decode(encrypted[0])
    cipher_text = b64decode(encrypted[1])
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, init_vector)
    plaintext = unpad(cipher.decrypt(cipher_text), Blowfish.block_size)
    return plaintext

def blowfish_encrypt_ecb(data: str, key: str) -> str:
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    cipher_bytes = cipher.encrypt(pad(data, Blowfish.block_size))
    #init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    #encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    return cipher_text

def blowfish_decrypt_ecb(ciphertext, key):
    cipher_text = b64decode(ciphertext)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    plaintext = unpad(cipher.decrypt(cipher_text), Blowfish.block_size)
    return plaintext


