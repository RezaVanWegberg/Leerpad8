from ast import With
from distutils.command.config import config
from operator import truediv
from textwrap import fill
import tkinter as tk


window = tk.Tk()

window.title("test")
window.geometry('500x200')
window.config(bg='pink')
#deel van top test
#window.withdraw()

#Destroy
def Destroy():
    window.destroy()

#box 1
box1 = tk.Label(window,text="box 1", bg='green', fg='white')
box1.pack(ipadx=20,ipady=10, fill='both', expand=True)

#box 2
box2 = tk.Label(window, text="box 2")
box2.pack(ipadx=25,ipady=10)

#top test
for x in range(2):
    DestroyWindow = tk.Toplevel()
    DestroyWindow.geometry('200x50')
    # box3 = tk.Label(DestroyWindow, text="box")
    # box3.pack(ipadx=60,ipady=25)
    button = tk.Button(DestroyWindow, text="destroy", command=Destroy).pack(ipadx=10,ipady=10, fill='both', expand=True)

# #top test2    alles van top test2 werkt niet, zodra ik de code actief heb wirdt de window gelijk withdrawed 
# WindowDeiconify = tk.Toplevel()
# WindowDeiconify.geometry('250x100')
# button = tk.Button(WindowDeiconify, text="show", command= window.deiconify()).pack(ipadx=10,ipady=10, fill='both', expand=True)

# WindowHide = tk.Toplevel()
# WindowHide.geometry('250x100')
# button2 = tk.Button(WindowHide, text="hide", command= window.withdraw()).pack(ipadx=10,ipady=10, fill='both', expand=True)





window.mainloop()
