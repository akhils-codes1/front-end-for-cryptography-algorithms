from tkinter import *

root = Tk()

root.title("Encryption and Decryption")

la = Label(root, text = "        ").grid(row = 0, column=0, columnspan =3)

l1 = Label(root, text = "    Plaintext : ")
l1.grid(row=1,column=0)

t1 = Text(root, height=10, width=60,padx = 10, pady=10)
t1.grid(row=1, column = 1)


f1 = Label(root, text = "    ")
f1.grid(row = 1, column = 2)


lb = Label(root, text = "        ").grid(row = 2, column=0, columnspan =3)

l2 = Label(root, text = "     Key : ")
l2.grid(row=3,column=0)

t2 = Text(root, height=5, width=60,padx = 10, pady=10)
t2.grid(row=3, column = 1)

f2 = Label(root, text = "    ")
f2.grid(row = 1, column = 2)

lc = Label(root, text = "        ").grid(row = 4, column=0, columnspan =3)

lc = Label(root, text = "        ").grid(row = 5, column=0)
b1 = Button(root, text = "DES ECB", command = lambda:exe("DES ECB")).grid(row = 5, column = 1)
lc = Label(root, text = "        ").grid(row = 6, column=0)
b2 = Button(root, text = "DES CBC", command = lambda:exe("DES CBC")).grid(row = 6, column = 1)
lc = Label(root, text = "        ").grid(row = 7, column=0)
b2 = Button(root, text = "DES ECB", command = lambda:exe("DES ECB")).grid(row = 7, column = 1)
lc = Label(root, text = "        ").grid(row = 6, column=0)
b2 = Button(root, text = "DES ECB", command = lambda:exe("DES ECB")).grid(row = 8, column = 1)
lc = Label(root, text = "        ").grid(row = 6, column=0)
b2 = Button(root, text = "DES ECB", command = lambda:exe("DES ECB")).grid(row = 9, column = 1)
lc = Label(root, text = "        ").grid(row = 6, column=0)
b2 = Button(root, text = "DES ECB", command = lambda:exe("DES ECB")).grid(row = 10, column = 1)







root.mainloop()
