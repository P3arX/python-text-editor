import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.title("Text Editor")

def NewFile():
    savingcurrent = messagebox.askquestion(title="Unsaved file", message="You have unsaved work. Do you want to save it?")
    if savingcurrent == "yes":
        SaveFile()
            
    editor.delete(1.0, tk.END)

def OpenFile():
    filelocation = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Texts", "*.txt"), ("All files", "*.*")))
    file = open(filelocation, "r")
    editor.delete(1.0, tk.END)
    editor.insert(tk.END, file.readlines())

def SaveFile():
    file = filedialog.asksaveasfile(filetypes=[("Text (.txt)", "*.txt")])
    if file is None:
        return None
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
fileMenu.add_command(label="New file", command=NewFile)
fileMenu.add_command(label="Open file", command=OpenFile)
fileMenu.add_command(label="Save file", command=SaveFile)
menubar.add_cascade(label="File", menu=fileMenu)

root.mainloop()