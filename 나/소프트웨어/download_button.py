import tkinter as tk

class DownloadButton:
    def __init__(self, parent, x, y, width, height, text="다운로드", font=("Arial", 18), bg="white", command=None):
        self.parent = parent
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.bg = bg
        self.command = command

        self.button = tk.Button(self.parent, text=self.text, font=self.font, bg=self.bg, command=self.command)
    
    def create(self):
        self.button.place(x=self.x, y=self.y, width=self.width, height=self.height)
    
    def disable(self):
        self.button.config(state=tk.DISABLED)
    
    def enable(self):
        self.button.config(state=tk.NORMAL)
    
    def hide(self):
        self.button.place_forget()
    
    def show(self):
        self.button.place(x=self.x, y=self.y, width=self.width, height=self.height)
