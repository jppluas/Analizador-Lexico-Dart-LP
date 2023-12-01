import tkinter as tk
from tkinter import filedialog
from sintactico import *
import sys
from io import StringIO
class IDE_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DartStudio")
      
        self.root.geometry("800x600")  
        #  menú
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)
        
        # Menú Archivo
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_command(label="Nuevo Documento", command=self.nuevo_documento)
        menu_bar.add_command(label="Abrir", command=self.abrir_archivo)
        menu_bar.add_command(label="Guardar", command=self.guardar_archivo)
        menu_bar.add_command(label="Guardar Como", command=self.guardar_como)
        menu_bar.add_separator()
        menu_bar.add_command(label="Salir", command=root.destroy)

        # principal
        main_frame = tk.Frame(root, bg="#282c34")  
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Botón Ejecutar
        execute_button = tk.Button(main_frame, text="Ejecutar", command=self.ejecutar_codigo, bg="#61dafb")  
        execute_button.pack(pady=10)
    
       # Subframe para alinear y apilar horizontalmente
        a_frame = tk.Frame(main_frame, bg="#282c34", width=300, height=300)
        a_frame.pack(side=tk.TOP)

        # Área de texto para números de línea
        self.linenumbers = tk.Text(a_frame, width=2, bg="#282c34", fg="#61dafb", bd=0, wrap=tk.NONE)
        self.linenumbers.grid(row=0, column=0, sticky=tk.NS)

        # Área de texto
        self.code_text = tk.Text(a_frame, wrap=tk.WORD, bg="#1e1e1e", fg="white", insertbackground="white")
        self.code_text.grid(row=0, column=1, sticky=tk.NSEW)

        # Barra de desplazamiento
        y_scroll_bar = tk.Scrollbar(a_frame, command=self.on_scroll)
        y_scroll_bar.grid(row=0, column=2, sticky=tk.NS)
        self.code_text.config(yscrollcommand=y_scroll_bar.set)

        # subframe2
        subframe2=tk.Frame(main_frame, bg="#282c34")
        subframe2.pack(side=tk.BOTTOM, fill=tk.BOTH)
        # Área de resultados
        self.resultados_text = tk.Text(main_frame, wrap=tk.WORD, bg="#1e1e1e", fg="white", insertbackground="white")
        self.resultados_text.pack(side=tk.BOTTOM, expand=True)
        self.resultados_text.config(state=tk.DISABLED)
        # Ruta del archivo actual
        self.file_path = None

        # Configurar la actualización de los números de línea
        self.actualizar_numeros_de_linea()

        self.code_text.bind('<Configure>', self.actualizar_numeros_de_linea)
        self.code_text.bind('<KeyRelease>', self.actualizar_numeros_de_linea)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Abrir archivo", "*.dart"), ("Todos los archivos", "*.*")])

        if file_path:
            self.file_path = file_path
            with open(file_path, "r") as file:
                content = file.read()
                self.code_text.delete(1.0, tk.END)
                self.code_text.insert(tk.END, content)
                self.actualizar_numeros_de_linea()

    def guardar_archivo(self):
        if self.file_path:
            content = self.code_text.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(content)
            self.actualizar_numeros_de_linea()
        else:
            self.guardar_como()

    def guardar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])

        if file_path:
            self.file_path = file_path
            content = self.code_text.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)
            self.actualizar_numeros_de_linea()

    def nuevo_documento(self):
        self.file_path = None
        self.code_text.delete(1.0, tk.END)
        self.actualizar_numeros_de_linea()

    def ejecutar_codigo(self):
        # Limpiar el área de resultados antes de mostrar la nueva salida
        self.limpiar_resultados()
        # Obtener el código
        codigo = self.code_text.get(1.0, tk.END)
        result = parser.parse(codigo)
        mensajes_de_error = analizar(codigo)
        
        self.resultados_text.config(state=tk.NORMAL)
        if (len(mensajes_de_error)==0):
            self.resultados_text.insert(tk.END, f"Sin errores")
        else:
            self.resultados_text.insert(tk.END, f"{mensajes_de_error}")
       
        self.resultados_text.config(state=tk.DISABLED)

    def limpiar_resultados(self):
        # Limpiar el contenido del área de resultados
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.config(state=tk.DISABLED)

    def on_scroll(self, *args):
        self.code_text.yview_moveto(args[0])
        self.linenumbers.yview_moveto(args[0])

    def actualizar_numeros_de_linea(self, event=None):
        lines = self.code_text.get(1.0, tk.END).count('\n')
        linenumbers_string = '\n'.join(str(i) for i in range(1, lines + 2))
        self.linenumbers.config(state=tk.NORMAL)
        self.linenumbers.delete(1.0, tk.END)
        self.linenumbers.insert(tk.END, linenumbers_string)
        self.linenumbers.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    ide = IDE_GUI(root)
    root.mainloop()
