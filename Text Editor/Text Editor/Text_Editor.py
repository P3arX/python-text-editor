import tkinter as tk

root = tk.Tk()

def ImportFile():
    print("Menu works")

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