from tkinter import *


class MC():

    def __init__(self, Text):

        self.Texto = Text
        self.crear_MC()
        self.Texto.bind("<Button-3>", self.mostar_MC)

    def crear_MC(self):

        self.menu_MC = Menu(self.Texto, tearoff=0)
        self.menu_MC.add_command(label="Deshacer")
        self.menu_MC.add_separator()
        self.menu_MC.add_command(label="Cortar")
        self.menu_MC.add_command(label="Copiar")
        self.menu_MC.add_command(label="Pegar")
        self.menu_MC.add_command(label="Eliminar")
        self.menu_MC.add_separator()
        self.menu_MC.add_command(label="Seleccionar todo")
        self.menu_MC.add_separator()
        self.menu_MC.add_command(label="Lectura de derecha a izquierdao")

    def funcion_MC(self):

        self.Texto.bind("<Button-3>", self.mostar_MC)

    def mostar_MC(self, event):

        try:
            self.menu_MC.tk_popup(event.x_root, event.y_root)

        finally:
            self.menu_MC.grab_release()





        