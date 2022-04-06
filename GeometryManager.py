import tkinter as tk
import random

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
box1 = tk.Label(window, text="box 1", bg='green').pack(ipadx=25,ipady=10, fill='x')

#box 2
box2 = tk.Label(window, text="box 2", bg='red').pack(ipadx=25,ipady=10, fill='x')

#box 3
box3 = tk.Label(window, text="box 3", bg='yellow').pack(ipadx=25,ipady=10, fill='y')

#box 4
box4 = tk.Label(window, text="box 4", bg='purple', fg='white').pack(ipadx=25,ipady=10, fill='both', expand=True, side='right')

#box 5
box5 = tk.Label(window, text="box 5", bg='blue', fg='white').pack(ipadx=25,ipady=10, fill='both', expand=True, side='right')

#box 6
box6 = tk.Label(window, text="box 6", bg='magenta', fg='white').pack(ipadx=25,ipady=10, fill='y', expand=True, side='right')


#top test
for x in range(2):
    DestroyWindow = tk.Toplevel()
    DestroyWindow.geometry('200x50')
    # box3 = tk.Label(DestroyWindow, text="box")
    # box3.pack(ipadx=60,ipady=25)
    button = tk.Button(DestroyWindow, text="destroy", command=Destroy, activebackground='black', activeforeground='white').pack(ipadx=10,ipady=10, fill='both', expand=True)

#top test2    alles van top test2 werkt niet, zodra ik de code actief heb wirdt de window gelijk withdrawed 
WindowDeiconify = tk.Toplevel()
WindowDeiconify.geometry('250x100')
button = tk.Button(WindowDeiconify, text="show", command= window.deiconify).pack(ipadx=10,ipady=10, fill='both', expand=True)

def PrintHello():
    print("hello")

def PrintGoodbye():
    print("goodbye")

def clicked():
    coin = random.randint(0,1)

    if coin == 0:
        return PrintHello
    else:
        return PrintGoodbye


WindowHide = tk.Toplevel()
WindowHide.geometry('250x100')
button2 = tk.Button(WindowHide, text="hide", command= window.withdraw).pack(ipadx=10,ipady=10, fill='both', expand=True)

clicked()()



window.mainloop()
