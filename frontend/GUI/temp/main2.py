from tkinter import *

root = Tk()

root.title("Encryption and Decryption")

w = Canvas(root, width=100, height=150)
w.pack()

la = Label(w, text = "        ").grid(row = 0, column=0, columnspan =3)

l1 = Label(w, text = "    Plaintext : ")
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


lb = Label(w, text = "        ").grid(row = 2, column=0, columnspan =3)

l2 = Label(w, text = "     Ciphertext : ")
l2.grid(row=3,column=0)

t2 = Text(w, height=5, width=60,padx = 10, pady=10)
t2.grid(row=3, column = 1)







c1_width = 80
c1_height = 40
z = Canvas(root, width=80, height=40)
z.pack()




b1 = Button(z, text = "DES ECB", padx = 50, command = lambda:exe("DES ECB")).grid(row = 0, column = 1)
b2 = Button(z, text = "DES CBC",  padx = 50, command = lambda:exe("DES CBC")).grid(row = 0, column = 2)
b2 = Button(z, text = "DES3 ECB", padx = 45,  command = lambda:exe("DES3 ECB")).grid(row = 1, column = 1)
b2 = Button(z, text = "DES3 CBC", padx = 45,  command = lambda:exe("DES3 CBC")).grid(row = 1, column = 2)
b2 = Button(z, text = "AES ECB", padx = 50,  command = lambda:exe("AES ECB")).grid(row = 2, column = 1)
b2 = Button(z, text = "AES CBC", padx = 50,  command = lambda:exe("AES CBC")).grid(row = 2, column = 2)
b2 = Button(z, text = "Blowfish ECB", padx = 35,  command = lambda:exe("Blowfish ECB")).grid(row = 3, column = 1)
b2 = Button(z, text = "Blowfish CBC", padx = 35,  command = lambda:exe("Blowfish ECB")).grid(row = 3, column = 2)


lb = Label(z, text = "        ").grid(row = 4, column=0, columnspan =3)




root.mainloop()
