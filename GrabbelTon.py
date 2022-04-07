import random
import tkinter as tk

GrabbelList = ['appel', 'peer', 'banaan', 'aardbei', 'mandarijn', 'meloen', 'kiwi', 'kers', 'perzik', 'abrikoos']
Gepakt = ''

def changeText():
    if len(GrabbelList) == 0:
        window.destroy()
    else:
        random.shuffle(GrabbelList)
        Gepakt = GrabbelList.pop(0)
        label['text'] = len(GrabbelList)
        print(f"Gefeliciteerd! Je hebt een {Gepakt} gegrabbeld!")
        label_item['text'] = f"Gefeliciteerd! Je hebt een {Gepakt} gegrabbeld!"
        print(len(GrabbelList))


window = tk.Tk()
window.title("test")
window.geometry('500x200')
window.config(bg='pink')


label = tk.Label(window, text= len(GrabbelList))
label.pack(ipadx=10,ipady=10, fill='x', expand=True)

button = tk.Button(window, text="Grabbel", command=changeText)
button.pack(ipadx=10,ipady=10, fill='x', expand=True)

label_item = tk.Label(window, text=  '')
label_item.pack(ipadx=10,ipady=10, fill='x', expand=True)

window.mainloop()