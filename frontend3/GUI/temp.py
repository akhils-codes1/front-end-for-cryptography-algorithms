from tkinter import *
from functions import *

def show():
    cipher = clicked1.get()
    mode = clicked2.get()
    option = clicked3.get()
    plaintext = t1.get(1.0, "end-1c")
    key = t2.get(1.0, "end-1c")
    #encoding into byte format
    plaintext = plaintext.encode('ascii')
    key = key.encode('ascii')
    
    if(cipher=='DES'):
        if(mode=='ECB'):
            if(option=='Encrypt'):
                s = des_encrypt_ecb(plaintext, key)
            elif(option=='Decrypt'):
                s = des_decrypt_ecb(plaintext, key)
        elif(mode=='CBC'):
            if(option=='Encrypt'):
                s = des_encrypt_cbc(plaintext, key)
            elif(option=='Decrypt'):
                s = des_decrypt_cbc(plaintext, key)
    
    elif(cipher=='DES3'):
        if(mode=='ECB'):
            if(option=='Encrypt'):
                s = des3_encrypt_ecb(plaintext, key)
            elif(option=='Decrypt'):
                s = des3_decrypt_ecb(plaintext, key)
        elif(mode=='CBC'):
            if(option=='Encrypt'):
                s = des3_encrypt_cbc(plaintext, key)
            elif(option=='Decrypt'):
                s = des3_decrypt_cbc(plaintext, key)
    
    elif(cipher=='AES'):
        if(mode=='ECB'):
            if(option=='Encrypt'):
                s = aes_encrypt_ecb(plaintext, key)
            elif(option=='Decrypt'):
                s = aes_decrypt_ecb(plaintext, key)
        elif(mode=='CBC'):
            if(option=='Encrypt'):
                s = aes_encrypt_cbc(plaintext, key)
            elif(option=='Decrypt'):
                s = aes_decrypt_cbc(plaintext, key)
    
    elif(cipher=='Blowfish'):
        if(mode=='ECB'):
            if(option=='Encrypt'):
                s = blowfish_encrypt_ecb(plaintext, key)
            elif(option=='Decrypt'):
                s = blowfish_decrypt_ecb(plaintext, key)
        elif(mode=='CBC'):
            if(option=='Encrypt'):
                s = blowfish_encrypt_cbc(plaintext, key)
            elif(option=='Decrypt'):
                s = blowfish_decrypt_cbc(plaintext, key)
    
    #s = '\nCipher = '+str(cipher)+"\nmode = "+str(mode)+"\noption = "+str(option)+"\nPlaintext = "+str(plaintext)+"\nkey = "+str(key)
    t3.delete("1.0","end")
    t3.insert(INSERT,s)


def clear():
    t1.delete("1.0","end")
    t2.delete("1.0","end")
    t3.delete("1.0","end")





root = Tk()

root.title("Encryption and Decryption")


w = Canvas(root, width=100, height=150)
w.pack()

la = Label(w, text = "        ").grid(row = 0, column=0, columnspan =3)

l1 = Label(w, text = "    Text : ")
l1.grid(row=1,column=0)

t1 = Text(w, height=10, width=60,padx = 10, pady=10)
t1.grid(row=1, column = 1)


f1 = Label(w, text = "    ")
f1.grid(row = 1, column = 2)


lb = Label(w, text = "        ").grid(row = 2, column=0, columnspan =3)

l2 = Label(w, text = "     Key : ")
l2.grid(row=3,column=0)

t2 = Text(w, height=5, width=60,padx = 10, pady=10)
t2.grid(row=3, column = 1)

f2 = Label(w, text = "    ")
f2.grid(row = 1, column = 2)


lb = Label(w, text = "        ").grid(row = 4, column=0, columnspan =3)

l2 = Label(w, text = "     Result : ")
l2.grid(row=5,column=0)

t3 = Text(w, height=5, width=60,padx = 10, pady=10)
t3.grid(row=5, column = 1)


z = Canvas(root, width=80, height=40)
z.pack()

cipher = ['DES', 'DES3', 'AES', 'Blowfish']
mode = ['ECB','CBC']
options = ['Encrypt', 'Decrypt']

clicked1 = StringVar()
clicked1.set('Select Cipher')
clicked2 = StringVar()
clicked2.set('Select mode')
clicked3 = StringVar()
clicked3.set('Select')


cipher_drop = OptionMenu( z , clicked1 , *cipher )
cipher_drop.grid(row = 0, column = 1)

mode_drop = OptionMenu( z , clicked2 , *mode )
mode_drop.grid(row = 0, column = 2)

drop = OptionMenu( z , clicked3 , *options )
drop.grid(row = 0, column = 3)

b1 = Button(z, text = "Execute", command = show).grid(row=1, column=2)
b1 = Button(z, text = "Clear", command = clear).grid(row=2, column=2)


root.mainloop()
