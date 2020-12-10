import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("Text Editor")

def OpenFile():
    filelocation = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Texts", "*.txt"), ("All files", "*.*")))
    file = open(filelocation, "r")
    editor.insert(tk.END, file.readlines())

def SaveFile():
    file = filedialog.asksaveasfile(filetypes=[("Text (.txt)", "*.txt")])
    if file is None:
        return
    file.write(editor.get("0.0", tk.END))
    file.close()
    

canvas = tk.Canvas(root, width = 500, height = 200)
canvas.pack()

editor = tk.Text(canvas)
editor.place(relwidth=1, relheight=1)
editor.pack()

menubar = tk.Menu(root)
root.config(menu = menubar)

#FILE MENUBAR
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Open", command=OpenFile)
fileMenu.add_command(label="Save", command=SaveFile)
menubar.add_cascade(label="File", menu=fileMenu)

root.mainloop()