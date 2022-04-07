# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
from turtle import left
 
root = Tk()
root.title('Clock')
 
# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)
 
label = Label(root, font = ('calibri', 50, 'bold'),
            background = 'lightblue',
            foreground = 'white')

label.pack(expand=True, fill="both")
time()
 
mainloop()