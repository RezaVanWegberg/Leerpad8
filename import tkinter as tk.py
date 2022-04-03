from cmath import exp
from msilib.schema import Font
from textwrap import fill
import tkinter as tk

HelloWindow = tk.Tk()

HelloWindow.title("Hello")
HelloWindow.geometry('380x200')
HelloWindow.config(bg='grey')

GreyLabel = tk.Label(HelloWindow, bg="grey").pack(ipady=10, fill='y', expand=True)

HelloLabel = tk.Label(HelloWindow, text="Hello tkinter!", bg="green", fg="yellow")
HelloLabel.pack(ipadx=75, ipady=50)

FontComicSans = ("Comic Sans MS", 20, "bold")
HelloLabel.configure(font=FontComicSans)

GreyLabel = tk.Label(HelloWindow, bg="grey").pack(ipady=10, fill='y', expand=True)

HelloWindow.mainloop()