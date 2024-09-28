import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root:tk.Tk, controller, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        
        root.geometry("300x400")
        self.pack()
        
        self.controller = controller
        self._main_label = tk.Label(self, text="Currency Convertor")
        
    def put_modules(self):
        self._main_label.pack()
