import tkinter as tk
from CurrencyConvertor.View.MainView import MainView

class Application:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.main_view = MainView(root=root, controller=None)
    
    def run(self):
        self.main_view.put_modules()
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()
