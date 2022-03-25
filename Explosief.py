import tkinter as tk

window = tk.Tk()

window.title("My first window")

a=0

def colors1():
    window.configure(bg="yellow")
    window.geometry('100x100')
    print("color1")
window.after(a, colors1)
a = 2000

def colors2():
    window.configure(bg="green")
    window.geometry('150x150')
    print("color2")
window.after(a, colors2)
a += 2000

def colors3():
    window.configure(bg="purple")
    window.geometry('200x200')
    print("color3")
window.after(a, colors3)
a += 2000

def colors4():
    window.configure(bg="red")
    window.geometry('250x250')
    print("color4")
window.after(a, colors4)
a += 2000

def colors5():
    window.configure(bg="blue")
    window.geometry('300x300')
    print("color5")
window.after(a, colors5)
a += 2000

def destroy():
    window.destroy()
    print("BOOM")
a+=2000

window.after(a,destroy)
window.mainloop()
