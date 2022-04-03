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
box1 = tk.Label(window,text="box 1")
box1.pack(ipadx=20,ipady=10)

#box 2
box2 = tk.Label(window, text="box 2")
box2.pack(ipadx=25,ipady=10)

#top test
for x in range(2):
    window2 = tk.Toplevel()
    box3 = tk.Label(window2, text="box")
    box3.pack(ipadx=65,ipady=25)
    button = tk.Button(window2, text="click", command=Destroy).pack(ipadx=10,ipady=10)

window.mainloop()
