from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from menuContextual import *
from menuPrincipal import *

class Aplicacion():

    def __init__(self):

        self.titulo = "Phoenix Text"

        self.root = Tk()
        self.root.title(self.titulo)
        self.root.minsize(width=300, height=300)
        self.root.geometry("900x800")
        self.root.config(bg="white")
        self.root.iconbitmap(default='img/icon.ico')

        self.areaTrabajo = Text(self.root,  relief="flat", width=900, height=800, bd=0,
            highlightthickness=0, font=('Arial', 12), wrap=WORD) 
        self.areaTrabajo.pack( padx=5, pady=5, fill='both', expand=1)

        self.scrollvar()

        self.miMenu = MS(self.root, self.titulo, self.areaTrabajo)
        self.miMenu.crear_MS()
        self.menu_MC = MC(self.areaTrabajo)

        self.root.mainloop()

    def scrollvar(self):

        self.scroll = Scrollbar(self.areaTrabajo, command=self.areaTrabajo.yview, cursor="arrow")
        self.scroll.pack(expand=0, side="right", fill="y")

        self.areaTrabajo.config(yscrollcommand=self.scroll.set)

     
def main():

    miApp = Aplicacion()

    return 0

if __name__ == "__main__":
    
    main()