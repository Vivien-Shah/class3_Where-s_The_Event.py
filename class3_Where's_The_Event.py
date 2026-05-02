'''from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    "Print the character associated to the key pressed"
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button - 1>", handle_click)

window.mainloop()'''


'''Virus Detected
Outline:
Create a virus scanner simulation with pop-up alerts using 
Tkinter! Students will learn to use messagebox to display 
warning dialogs, understand button commands, and create 
interactive alert systems for desktop applications.'''

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text = "Scan for Virus", command = msg)
button.place(x = 40, y = 80)

def message1():
    messagebox.showinfo("Alert", "Stop! Virus Found.")

button2 = Button(root, text = "Scan for info", command = message1)
button2.place(x = 40, y = 110)

def message2():
    messagebox.showerror("Alert", "Stop! Virus Found.")

button3 = Button(root, text = "Scan For error", command = message2)
button3.place(x=40, y = 140)
root.mainloop()