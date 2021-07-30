from tkinter import *
from tkinter import filedialog as f
from io import open
from tkinter import messagebox
import time


class MS():

    def __init__(self, root, titulo, Text):

        self.root = root
        self.Text = Text

        #Instanciondo el menu y el submenu superior
        self.menu = Menu(self.root)
        self.archivo_menu = Menu(self.menu, tearoff=0)
        self.edicion_menu = Menu(self.menu, tearoff=0)
        self.formato_menu = Menu(self.menu, tearoff=0)
        self.ver_menu = Menu(self.menu, tearoff=0)
        self.ayuda_menu = Menu(self.menu, tearoff=0)

        self.root.configure(menu=self.menu)

        self.url_archivo = ""
        self.titulo = titulo

    def crear_MS(self):

        #Menu de archivos
        self.archivo_menu.add_command(label='Nuevo', command=self.nuevo_archivo)
        self.archivo_menu.add_command(label='abrir', command=self.abrir_archivo)
        self.archivo_menu.add_command(label='Guardar', command=self.guardar_archivo)
        self.archivo_menu.add_command(label='Guardar como...', command=self.guardarComo)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label='Configurar pagina')
        self.archivo_menu.add_command(label='Imprimir')
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label='Salir', command=self.salir)
        self.menu.add_cascade(label='Archivo', menu=self.archivo_menu)

        #Menu de edicion
        self.edicion_menu.add_command(label='Deshacer', command=self.deshacer)
        self.edicion_menu.add_separator()
        self.edicion_menu.add_command(label='Cortar', command=self.cut)
        self.edicion_menu.add_command(label='Copiar', command=self.copy)
        self.edicion_menu.add_command(label='Pegar', command=self.paste)
        self.edicion_menu.add_command(label='Eliminar', command=self.delete)
        self.edicion_menu.add_separator()
        self.edicion_menu.add_command(label='Seleccionar todo', command=self.select_all)
        self.edicion_menu.add_command(label='Fecha y Hora', command=self.fachaHora)
        self.menu.add_cascade(label='Edicion', menu=self.edicion_menu)

        #Menu de formato
        self.formato_menu.add_command(label='Fuentes')
        self.menu.add_cascade(label='Formato', menu=self.formato_menu)

        #Menu de vista
        self.ver_menu.add_checkbutton(label='Barra de estado')
        self.menu.add_cascade(label='Ver', menu=self.ver_menu)

        #Menu de ayuda
        self.ayuda_menu.add_command(label='Ver la ayuda')
        self.ayuda_menu.add_command(label='Acerda de Phoenix Text')
        self.menu.add_cascade(label='Ayuda', menu=self.ayuda_menu)

        #funcion 'nuevo archivo'
    def nuevo_archivo(self):


        if self.url_archivo != "":

            self.valor = messagebox.askyesno(title="Nuevo documento", message=
                "se perdera toda la informacion en el documento.\n¿Desea continuar?")

            if self.valor == True:

                self.Text.delete(1.0, 'end')
                self.url_archivo = ""
                self.root.title(self.url_archivo + self.titulo)
        
        else:

            self.contenido = self.Text.get(1.0, "end")

            if self.contenido != "":

                self.valor = messagebox.askyesno(title="Nuevo documento", message=
                    "se perdera toda la informacion en el documento.\n¿Desea continuar?")

                if self.valor == True:

                    self.Text.delete(1.0, 'end')
                    self.url_archivo = ""
                    self.root.title(self.url_archivo + self.titulo)

            else:

                self.Text.delete(1.0, 'end')
                self.url_archivo = ""
                self.root.title(self.url_archivo + self.titulo)

        #funcion 'Abrir nuevo archivo'   
    def abrir_archivo(self):

        self.url_archivo = f.askopenfilename(filetypes=(("Documento de texto", "*.txt"),
                ("HTML files", "*.html;*.htm"),
                ("All files", "*.*"), 
                ("Template files", "*.tplate"), ), 
                title="Open file")

        if self.url_archivo != "":

            self.file = open(self.url_archivo, 'r')
            self.contenido = self.file.read()
            self.Text.delete(1.0, 'end')
            self.Text.insert('insert', self.contenido)
            self.file.close()

            self.titulo = " | Phoenix Text"
            self.root.title(self.url_archivo + self.titulo)

        #Funcion 'Guardar archivo'  
    def guardar_archivo(self):

        if self.url_archivo != "":

            self.contenido = self.Text.get(1.0, 'end - 1c')
            self.file = open(self.url_archivo, 'w+')
            self.file.write(self.contenido)

            self.titulo = " | Phoenix Text"
            self.root.title("Archivo guardado " + self.url_archivo + self.titulo)
            self.file.close()

        else:

            self.file = f.asksaveasfile(title='Guardar archivo', mode='w', defaultextension='.txt', filetypes=(
                ("Archivos de plantillas", "*.tplate"),
                ("Archivo HTML", "*.html;*.htm"), 
                ("Documento de texto", "*.txt")))

            if self.file is not None:

                self.url_archivo = self.file.name
                self.contenido = self.Text.get(1.0, 'end-1c')
                self.file = open(self.url_archivo, 'w+')
                self.file.write(self.contenido)

                self.titulo = " | Phoenix Text"
                self.root.title("Archivo guardado " + self.url_archivo + self.titulo)
                self.file.close()

    #Funcion 'Guardar archivo como...'
    def guardarComo(self):

        self.file = f.asksaveasfile(title='save file', mode='w',)

        if self.file is not None:

            self.url_archivo = self.file.name
            self.contenido = self.Text.get(1.0, 'end-1c')
            self.file = open(self.url_archivo, 'w+')
            self.file.write(self.contenido)

            self.titulo = " | Phoenix Text"
            self.root.title("Archivo guardado " + self.url_archivo + self.titulo)
            self.file.close()

    def salir(self):

        self.valor = messagebox.askyesnocancel(title="Salir", message=
            "¿Desea guadra los cambios antes de serrar la aplicacion?")

        if self.url_archivo != "":

            if self.valor == True:

                self.contenido = self.Text.get(1.0, 'end - 1c')
                self.file = open(self.url_archivo, 'w+')
                self.file.write(self.contenido)

                self.titulo = " | Phoenix Text"
                self.root.title("Archivo guardado " + self.url_archivo + self.titulo)
                self.file.close()

            elif self.valor == False:

                self.root.destroy()

        else:

            if self.valor == True:

                self.file = f.asksaveasfile(title='Guardar archivo', mode='w', defaultextension='.txt', filetypes=(
                    ("Archivos de plantillas", "*.tplate"),
                    ("Archivo HTML", "*.html;*.htm"), 
                    ("Documento de texto", "*.txt")))

                if self.file is not None:

                    self.url_archivo = self.file.name
                    self.contenido = self.Text.get(1.0, 'end-1c')
                    self.file = open(self.url_archivo, 'w+')
                    self.file.write(self.contenido)

                    self.titulo = " | Phoenix Text"
                    self.root.title("Archivo guardado " + self.url_archivo + self.titulo)
                    self.file.close()

                self.root.destroy()

            elif self.valor == False:

                self.root.destroy()

        #Funcion 'Deshacer Accion'
    def deshacer(self):

        pass

    def cut(self):

        pass

    def copy(self):

        pass

    def paste(self):

        pass

    def delete(self):

        pass

    def select_all(self):

        pass

    def fachaHora(self):

        self.fecha = time.strftime('%c')

        self.Text.insert("insert", self.fecha)











        

