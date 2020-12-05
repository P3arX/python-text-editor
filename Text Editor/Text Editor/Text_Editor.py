import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()

def ImportFile():
    filelocation = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Texts", "*.txt"), ("All files", "*.*")))
    file = open(filelocation, "r")
    editor.insert(tk.END, file.readlines())
    

canvas = tk.Canvas(root, width = 500, height = 200)
canvas.pack()

editor = tk.Text(canvas)
editor.place(relwidth=1, relheight=1)
editor.pack()

menubar = tk.Menu(root)
root.config(menu = menubar)

#FILE MENUBAR
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label="Import", command=ImportFile)
menubar.add_cascade(label="File", menu=fileMenu)

root.mainloop()