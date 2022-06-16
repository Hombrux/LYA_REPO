import os
import tkinter as tk
from tkinter import Image, ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        base_folder = os.path.dirname(__file__)
        a = base_folder.split(os.sep)
        a[len(a)-1]= 'ARCHIVOS'+os.sep+'IMAGENES'
        base_folder = ''
        i=0
        while(i<len(a)):
            base_folder+= a[i] + os.sep
            i+=1
        
        self.python_image = tk.PhotoImage(file= base_folder+'AutomataINT.png')
        
        
        ttk.Label(self, image=self.python_image).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()