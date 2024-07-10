import tkinter as tk

class InputEntry:
    def __init__(self, parent, x, y, width, height, font=("Arial", 18)):
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.entry = tk.Entry(self.parent, font=font, width=self.width)
    
    def create(self):
        self.entry.place(x=self.x, y=self.y)

    def hide(self):
        self.entry.place_forget()

    def show(self):
        self.entry.place(x=self.x, y=self.y)
