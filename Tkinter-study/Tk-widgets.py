from tkinter import *
from tkinter import ttk


def display():
    print("Hello!")

root = Tk()
frame = ttk.Frame(root, padding=(30, 30, 30, 30))
frame.grid(column=0, row=0, sticky=(N, W, E, S))

# root['width'] = 700
# root['height'] = 500

# frame['width'] = 700
# frame['height'] = 500

# frame['padding'] = (5, 7, 10, 12)

# frame['borderwidth'] = 2
# frame['relief'] = 'sunken'

# s = ttk.Style()
# s.configure('Danger.TFrame', backgroud='red', borderwidth=50, relief='sunken')
# ttk.Frame(root, width=800, height=400, style='Danger.TFrame').grid()

label = ttk.Label(frame, text='Full name:')
resultContents = StringVar()
label['textvariable'] = resultContents
resultContents.set('Initial value to display')

# current = resultContents.get()
# resultContents.set('New value to display')
label.grid()

# label['font'] = "TkdefaultFont"
# label['foreground'] = "blue"
# label['background'] = "#ff340a"

label['anchor'] = "nw"

button = ttk.Button(frame, text="Okay", command=display).grid(column=3, row=2, sticky=N)

mainloop()