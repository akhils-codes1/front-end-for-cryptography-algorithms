from tkinter import *

root = Tk()


#Title(root, text = "Simple calculator")



e = Entry(root, width = 35)
e.grid(row = 0, columnspan = 3)


def button_click(num):
    a = e.get()
    e.delete(0,END)
    e.insert(0,str(a)+str(num))
    

def clear():
    e.delete(0,END)

def evaluate():
    sol = eval(e.get())
    e.delete(0,END)
    e.insert(0,sol)

b1 = Button(root, text = "1",padx=40,pady=20, command = lambda:button_click(1)).grid(row = 3, column = 0)
b2 = Button(root, text = "2",padx=40,pady=20, command = lambda:button_click(2)).grid(row = 3, column = 1)
b3 = Button(root, text = "3",padx=40,pady=20, command = lambda:button_click(3)).grid(row = 3, column = 2)
b4 = Button(root, text = "4",padx=40,pady=20, command = lambda:button_click(4)).grid(row = 2, column = 0)
b5 = Button(root, text = "5",padx=40,pady=20, command = lambda:button_click(5)).grid(row = 2, column = 1)
b6 = Button(root, text = "6",padx=40,pady=20, command = lambda:button_click(6)).grid(row = 2, column = 2)
b7 = Button(root, text = "7",padx=40,pady=20, command = lambda:button_click(7)).grid(row = 1, column = 0)
b8 = Button(root, text = "8",padx=40,pady=20, command = lambda:button_click(8)).grid(row = 1, column = 1)
b9 = Button(root, text = "9",padx=40,pady=20, command = lambda:button_click(9)).grid(row = 1, column = 2)
b0 = Button(root, text = "0",padx=40,pady=20, command = lambda:button_click(0)).grid(row = 4, column = 0)
bclear = Button(root, text = "Clear",padx=75,pady=20, command = clear).grid(row = 4, column = 1, columnspan = 2)
badd = Button(root, text = "+",padx=40,pady=20, command = lambda:button_click('+')).grid(row = 5, column = 0)
beq = Button(root, text = " = ",padx=80,pady=20, command = evaluate).grid(row = 5, column = 1, columnspan = 2)


root.mainloop()










