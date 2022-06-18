import os
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image 

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
        #new_pic = ImageTK.PhotoImage(Image.open("images/aspen.png").resize((300, 225), Image.ANTIALIAS))
        self.python_image = ImageTk.PhotoImage(Image.open(base_folder+'AutomataINT.png').resize((40, 25)), Image.ANTIALIAS)
        
        ttk.Label(self, image=self.python_image).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()