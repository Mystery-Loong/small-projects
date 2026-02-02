from tkinter import *
from tkinter import ttk


a = ""

# display number functions
def displayone():
    global a
    a += '1'
    display_box.set(a)

def displaytwo():
    global a
    a += '2'
    display_box.set(a)

def displaythree():
    global a
    a += '3'
    display_box.set(a)

def displayfour():
    global a
    a += '4'
    display_box.set(a)

def displayfive():
    global a
    a += '5'
    display_box.set(a)

def displaysix():
    global a
    a += '6'
    display_box.set(a)

def displayseven():
    global a
    a += '7'
    display_box.set(a)

def displayeight():
    global a
    a += '8'
    display_box.set(a)

def displaynine():
    global a
    a += '9'
    display_box.set(a)

def displayzero():
    global a
    a += '0'
    display_box.set(a)

def displaydot():
    global a
    a += '.'
    display_box.set(a)

def displayadd():
    global a
    a += ' + '
    display_box.set(a)

def displaysubtract():
    global a
    a += ' - '
    display_box.set(a)

def displaymultiply():
    global a
    a += ' x '
    display_box.set(a)

def displaydivide():
    global a
    a += ' / '
    display_box.set(a)

# calculate function
def calculate():
    global a
    number_list = a.split()
    if number_list[1] == '+':
        result = float(number_list[0]) + float(number_list[2])
        display_box.set(result)
        a = str(result)
    if number_list[1] == '-':
        result = float(number_list[0]) - float(number_list[2])
        display_box.set(result)
        a = str(result)
    if number_list[1] == 'x':
        result = float(number_list[0]) * float(number_list[2])
        display_box.set(result)
        a = str(result)
    if number_list[1] == '/':
        result = float(number_list[0]) / float(number_list[2])
        display_box.set(result)
        a = str(result)

# clear the numbers
def clearall():
    global a
    a = ''
    display_box.set(a)

# delete number from end
def displaydelete():
    global a
    number_list = list(a)
    del number_list[-1]
    a = ''.join(number_list)
    display_box.set(a)
 

# create root window and title
root = Tk()
root.title("Simple Calculator")

# create frame
frame = ttk.Frame(root, borderwidth=20, width=400, height=640)

#create label widget to be main display box
display_box = StringVar()
label = ttk.Label(frame, textvariable=display_box, font='20', anchor='sw')

# create button widgets
clear = ttk.Button(frame, text="C", command=clearall)
multiply = ttk.Button(frame, text="x", command=displaymultiply)
divide = ttk.Button(frame, text="/", command=displaydivide)
delete = ttk.Button(frame, text="del", command=displaydelete)
one = ttk.Button(frame, text="1", command=displayone)
two = ttk.Button(frame, text="2", command=displaytwo)
three = ttk.Button(frame, text="3", command=displaythree)
add = ttk.Button(frame, text="+", command=displayadd)
four = ttk.Button(frame, text="4", command=displayfour)
five = ttk.Button(frame, text="5", command=displayfive)
six = ttk.Button(frame, text="6", command=displaysix)
subtract = ttk.Button(frame, text="-", command=displaysubtract)
seven = ttk.Button(frame, text="7", command=displayseven)
eight = ttk.Button(frame, text="8", command=displayeight)
nine = ttk.Button(frame, text="9", command=displaynine)
zero = ttk.Button(frame, text="0", command=displayzero)
dot = ttk.Button(frame, text=".", command=displaydot)
equal = ttk.Button(frame, text="=", command=calculate)

# grid button widgets
frame.grid(column=0, row=0, sticky=(N, W, E, S))
label.grid(column=0, row=0, columnspan=4, rowspan=3)
clear.grid(column=1, row=4, padx=3, pady=3)
multiply.grid(column=2, row=4, padx=3, pady=3)
divide.grid(column=3, row=4, padx=3, pady=3)
delete.grid(column=4, row=4, padx=3, pady=3)
one.grid(column=1, row=5, padx=3, pady=3)
two.grid(column=2, row=5, padx=3, pady=3)
three.grid(column=3, row=5, padx=3, pady=3)
add.grid(column=4, row=5, padx=3, pady=3)
four.grid(column=1, row=6, padx=3, pady=3)
five.grid(column=2, row=6, padx=3, pady=3)
six.grid(column=3, row=6, padx=3, pady=3)
subtract.grid(column=4, row=6, padx=3, pady=3)
seven.grid(column=1, row=7, padx=3, pady=3)
eight.grid(column=2, row=7, padx=3, pady=3)
nine.grid(column=3, row=7, padx=3, pady=3)
zero.grid(column=1, row=8, columnspan=2, ipadx=40, padx=3, pady=3)
dot.grid(column=3, row=8, padx=3, pady=3)
equal.grid(column=4, row=7, rowspan=2, ipady=17, padx=3, pady=3)


mainloop()