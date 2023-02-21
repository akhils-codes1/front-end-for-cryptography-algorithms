from tkinter import *
from tkinter import filedialog
from functions import *
import os


plaintext = ""
key = ""
iv = ""
res_text_path = ""
res_iv_path = ""

def execute():
    global plaintext
    global key
    global iv
    #print("\n\n\nplaintext = ",plaintext)
    #print(len(plaintext))
    #print("key = ",key)
    #print(len(key))
    #print(list(key))
    #print("iv = ",iv)
    #print(len(iv))
    #print(list(iv))
    cipher = clicked1.get()
    mode = clicked2.get()
    option = clicked3.get()
    #plaintext = t1.get(1.0, "end-1c")
    #key = t2.get(1.0, "end-1c")
    #encoding into byte format
    plaintext = plaintext.encode('ascii')
    key = key.encode('ascii')
    #iv = iv.encode('ascii')
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
                s = des_decrypt_cbc((iv,plaintext), key)
    
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
                s = des3_decrypt_cbc((iv,plaintext), key)
    
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
                s = aes_decrypt_cbc((iv,plaintext), key)
    
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
                s = blowfish_decrypt_cbc((iv,plaintext), key)
    
    #s = '\nCipher = '+str(cipher)+"\nmode = "+str(mode)+"\noption = "+str(option)+"\nPlaintext = "+str(plaintext)+"\nkey = "+str(key)
    #t3.delete("1.0","end")
    #t3.insert(INSERT,s)
    global res_text_path
    global res_iv_path
    if(option=='Encrypt'):
        if(type(s)==tuple):
            #print(s)
            newf = open("ciphertext.txt","w")
            newf.write(s[1])
            newf.close()
            res_text_path = os.path.abspath(os.curdir)+"/ciphertext.txt"
            newf = open("iv.txt","w")
            newf.write(s[0])
            newf.close()
            res_iv_path = os.path.abspath(os.curdir)+"/iv.txt"
        else:
            newf = open("ciphertext.txt","w")
            newf.write(s)
            newf.close()
            res_text_path = os.path.abspath(os.curdir)+"/ciphertext.txt"
    else:
        newf = open("decrypted_file.txt","w")
        s = s.decode()
        #print(s)
        newf.write(s)
        newf.close()
        res_text_path = os.path.abspath(os.curdir)+"/decrypted_file.txt"
    desc4.configure(text="EXECUTION SUCCESSFUL",font='Ubuntu 10 bold')
    

def clear():
    t1.delete("1.0","end")
    t2.delete("1.0","end")
    t3.delete("1.0","end")
    t4.delete("1.0","end")
    desc4.configure(text="EXECUTION :",font='Ubuntu 10 bold')

def generate_random_text():
    n = int(t1.get(1.0, "end-1c"))
    f = open("random_text.txt","w")
    f.write(random_text(n))
    f.close()
    global res_text_path
    res_text_path = os.path.abspath(os.curdir)+"/random_text.txt"

def upload_txt():
    global plaintext
    f = filedialog.askopenfilename()
    t2.insert(INSERT,f)
    g = open(f,"r")
    plaintext = g.read()
    if(plaintext[-1]=='\n'):
        plaintext = plaintext[:-1]    

def upload_iv():
    global iv
    f = filedialog.askopenfilename()
    t3.insert(INSERT,f)
    g = open(f,"r")
    iv = g.read()
    if(iv[-1]=='\n'):
        iv = iv[:-1]

def upload_key():
    global key
    f = filedialog.askopenfilename()
    t4.insert(INSERT,f)
    g = open(f,"r")
    key = g.read()
    if(key[-1]=='\n'):
        key = key[:-1]


def open_res_text():
    os.system("gedit "+res_text_path+" &")


def open_res_iv():
    os.system("gedit "+res_iv_path+" &")

root = Tk()
root.title("Encryption and Decryption")


#canvas-1 for random text
rt = Canvas(root, width = 100, height = 150)
rt.pack()

space1 = Label(rt, text = "").grid(row = 0, column=0, columnspan =4)
desc1 = Label(rt, text = "RANDOM TEXT GENERATION ",  font='Ubuntu 10 bold').grid(row=1,column=1)
Label(rt, text = "").grid(row = 2, column=0, columnspan =4)
l1 = Label(rt, text = "    Number of Random bytes : ").grid(row=4,column=0)
t1 = Text(rt, height=1, width=80, padx = 10, pady=10)
t1.grid(row=4, column = 1)
b1 = Button(rt, text = "Generate Random text file", command = generate_random_text).grid(row=4, column=2)
downspace1 = Label(rt, text = "").grid(row = 5, column=0, columnspan =4)

#canvas-2 for input file(s) information
w = Canvas(root, width=100, height=150)
w.pack()

space3 = Label(w, text = "        ").grid(row = 0, column=0, columnspan =4)
desc2 = Label(w, text = "INPUT TEXT FILE(S) INFORMATION : ",  font='Ubuntu 10 bold').grid(row=1,column=0)

space4 = Label(w, text = "        ").grid(row = 2, column=0, columnspan =4)
l2 = Label(w, text = "     Text file : ").grid(row=3,column=0)
t2 = Text(w, height=1, width=80,padx = 10, pady=10)
t2.grid(row=3, column = 1)
b2 = Button(w, text = "Upload", command = upload_txt).grid(row=3, column=2)


space5 = Label(w, text = "        ").grid(row = 4, column=0, columnspan =4)
l3 = Label(w, text = "     IV file : ").grid(row=5,column=0)
t3 = Text(w, height=1, width=80,padx = 10, pady=10)
t3.grid(row=5, column = 1)
b2 = Button(w, text = "Upload", command = upload_iv).grid(row=5, column=2)


space6 = Label(w, text = "        ").grid(row = 6, column=0, columnspan =4)
l4 = Label(w, text = "     Key file : ").grid(row=7,column=0)
t4 = Text(w, height=1, width=80,padx = 10, pady=10)
t4.grid(row=7, column = 1)
b4 = Button(w, text = "Upload", command = upload_key).grid(row=7, column=2)

#canvas-3 for result related information
res = Canvas(root, width=80, height=40)
res.pack()

space7 = Label(res, text = "        ").grid(row = 0, column=0, columnspan =4)
desc3 = Label(res, text = "RESULT :",  font='Ubuntu 10 bold').grid(row=1,column=1)
Label(res, text = "        ").grid(row = 2, column=0, columnspan =4)
b5 = Button(res, text = "Open resulted text file", command = open_res_text).grid(row=3, column=2)
b6 = Button(res, text = "Open resulted IV file", command = open_res_iv).grid(row=4, column=2)

#canvas-4 for execution
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

space8 = Label(z, text = "        ").grid(row = 0, column=0, columnspan =4)
desc4 = Label(z, text = "EXECUTION :",  font='Ubuntu 10 bold')
desc4.grid(row=1,column=0)

cipher_drop = OptionMenu( z , clicked1 , *cipher ).grid(row = 2, column = 1)
mode_drop = OptionMenu( z , clicked2 , *mode ).grid(row = 2, column = 2)
drop = OptionMenu( z , clicked3 , *options ).grid(row = 2, column = 3)

Label(z, text = "").grid(row = 3, column=0, columnspan =4)
b7 = Button(z, text = "EXECUTE", command = execute).grid(row=4, column=2)
Label(z, text = "").grid(row = 5, column=0, columnspan =4)
b8 = Button(z, text = "CLEAR", command = clear).grid(row=6, column=2)
Label(z, text = "").grid(row = 7, column=0, columnspan =4)
Label(z, text = "").grid(row = 7, column=0, columnspan =4)

root.mainloop()
