from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

frame = ttk.Frame(root, borderwidth=20, width=400, height=640)
frame.grid(column=0, row=0, sticky=(N, W, E, S))

display_box = StringVar()
ttk.Label(frame, textvariable=display_box).grid(column=0, row=0, columnspan=4, rowspan=3)
clear = ttk.Button(frame, text="C").grid(column=1, row=4, padx=3, pady=3)
multiply = ttk.Button(frame, text="X").grid(column=2, row=4, padx=3, pady=3)
divide = ttk.Button(frame, text="/").grid(column=3, row=4, padx=3, pady=3)
delete = ttk.Button(frame, text="del").grid(column=4, row=4, padx=3, pady=3)
one = ttk.Button(frame, text="1").grid(column=1, row=5, padx=3, pady=3)
two = ttk.Button(frame, text="2").grid(column=2, row=5, padx=3, pady=3)
three = ttk.Button(frame, text="3").grid(column=3, row=5, padx=3, pady=3)
add = ttk.Button(frame, text="+").grid(column=4, row=5, padx=3, pady=3)
four = ttk.Button(frame, text="4").grid(column=1, row=6, padx=3, pady=3)
five = ttk.Button(frame, text="5").grid(column=2, row=6, padx=3, pady=3)
six = ttk.Button(frame, text="6").grid(column=3, row=6, padx=3, pady=3)
subtract = ttk.Button(frame, text="-").grid(column=4, row=6, padx=3, pady=3)
seven = ttk.Button(frame, text="7").grid(column=1, row=7, padx=3, pady=3)
eighty = ttk.Button(frame, text="8").grid(column=2, row=7, padx=3, pady=3)
nine = ttk.Button(frame, text="9").grid(column=3, row=7, padx=3, pady=3)
zero = ttk.Button(frame, text="0").grid(column=1, row=8, columnspan=2, ipadx=40, padx=3, pady=3)
dot = ttk.Button(frame, text=".").grid(column=3, row=8, padx=3, pady=3)
equal = ttk.Button(frame, text="=").grid(column=4, row=7, rowspan=2, ipady=17, padx=3, pady=3)

mainloop()