from tkinter import *

root = Tk()

root.title('Calculator')

e = Entry(root, width=65)
e.grid(row=0, column=0, pady=5, columnspan=4)

first_num = 0
math = None

def Button_click(number):
    prev_num = e.get()
    e.delete(0, END)
    e.insert(0, str(prev_num) + str(number))

def Button_clear():
    e.delete(0, END)
    first_num = None
    math = None

def Button_add():
    global first_num
    first_num = e.get()
    global math
    math = 'addition'
    e.delete(0, END)

def Button_substract():
    global first_num
    first_num = e.get()
    global math
    math = 'substraction'
    e.delete(0, END)

def Button_multiply():
    global first_num
    first_num = e.get()
    global math
    math = 'multiply'
    e.delete(0, END)

def Button_division():
    global first_num
    first_num = e.get()
    global math
    math = 'division'
    e.delete(0, END)

def Button_equal():
    second_num = e.get()
    if (math == 'addition'):
        result = int(first_num) + int(second_num)
        e.delete(0, END)
        e.insert(0, result)
    elif (math == 'substraction'):
        result = int(first_num) - int(second_num)
        e.delete(0, END)
        e.insert(0, result)
    elif (math == 'multiply'):
        result = int(first_num) * int(second_num)
        e.delete(0, END)
        e.insert(0, result)
    elif (math == 'division'):
        result = int(first_num) / int(second_num)
        e.delete(0, END)
        e.insert(0, result)
    else:
        e.insert(0, "ERROR")
        



# Declaring Button

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: Button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: Button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: Button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: Button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: Button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: Button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: Button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: Button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: Button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: Button_click(0))
button_clear = Button(root, text='CLEAR', padx=40, pady=20, command=Button_clear)
button_equal = Button(root, text='=', padx=55, pady=20, command=Button_equal)
button_add = Button(root, text='+', padx=40, pady=20, command=Button_add)
button_substract = Button(root, text='-', padx=40, pady=20, command=Button_substract)
button_multiply = Button(root, text='*', padx=55, pady=20, command=Button_multiply)
button_division = Button(root, text='/', padx=55, pady=20, command=Button_division)

#Placing Buttons

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=1, column=3)
button_add.grid(row=4, column=1)
button_substract.grid(row=4, column=2)
button_multiply.grid(row=2, column=3)
button_division.grid(row=3, column=3)
button_equal.grid(row=4, column=3)


root.mainloop()