import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master);
        root.title("Text Editor")

root = tk.Tk()
myapp = Application(root)
myapp.mainloop()