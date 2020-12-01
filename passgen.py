import tkinter as tk
from tkinter import ttk
###################pwd
import random

def letter(n):
    return [random.choice(list("qwertyuiopasdfghjklzxcvbnm")) for x in range(int(n))]

def number(n):
    return [random.choice(list("1234567890")) for x in range(int(n))]

def symbol(n):
    return [random.choice(list("$@#&=-_|¥*;+:?.,")) for x in range(int(n))]

def Generate(n1,n2,n3):
    l = letter(n1)+number(n2)+symbol(n3)
    random.shuffle(l)
    return ''.join(l)



##############################pwd
window = tk.Tk()
window.title("Password Generator")
label = tk.Label(window, text="How Many Letters Do You \nWant In The Password", font=("Comic Sans MS", 24))
label.pack()
askletnum = tk.ttk.Combobox (window,values = list(range(11)))
askletnum.pack()
label = tk.Label(window, text="\nHow Many Number Do You \nWant In The Password", font=("Comic Sans MS", 24))
label.pack()
asknumnum = tk.ttk.Combobox (window,values = list(range(11)))
asknumnum.pack()
label = tk.Label(window, text="\nHow Many Symbol Do You \nWant In The Password", font=("Comic Sans MS", 24))
label.pack()
asknumsym = tk.ttk.Combobox (window,values = list(range(101)))
asknumsym.pack()

entry = tk.Entry(window,font=("Comic Sans MS", 24))
entry.pack()
numleng = tk.Label(window,font=("Comic Sans MS", 24))
numleng.pack()
def submit():
    gen = Generate(askletnum.get(),asknumnum.get(),asknumsym.get())
    entry.delete(0,tk.END)
    entry.insert(0,gen)
    length =int(askletnum.get())+int(asknumnum.get())+int(asknumsym.get())
    numleng.configure(text = length)


btn = tk.Button(window,text = "Submit",font=("Comic Sans MS", 24),command = submit)
btn.pack()
window.geometry("600x600")
window.mainloop()
