import tkinter as tk
from tkinter import filedialog

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
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Nuevo Documento", command=self.nuevo_documento)
        file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        file_menu.add_command(label="Guardar Como", command=self.guardar_como)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.destroy)

        # principal
        main_frame = tk.Frame(root, bg="#282c34")  
        main_frame.pack(fill=tk.BOTH, expand=True)

        # para abrir archivos
        left_frame = tk.Frame(main_frame, padx=10, pady=10, bg="#282c34")  
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        open_button = tk.Button(left_frame, text="Abrir archivo", command=self.abrir_archivo, bg="#61dafb")  
        open_button.pack(pady=10)

        # Botón Ejecutar
        execute_button = tk.Button(left_frame, text="Ejecutar", command=self.ejecutar_codigo, bg="#61dafb")  
        execute_button.pack(pady=10)

        # Marco derecho (para escribir código)
        right_frame = tk.Frame(main_frame, padx=10, pady=10, bg="#282c34") 
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Área de texto para números de línea
        self.linenumbers = tk.Text(right_frame, width=4, padx=5, bg="#282c34", fg="#61dafb", bd=0, wrap=tk.NONE)
        self.linenumbers.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto 
        self.code_text = tk.Text(right_frame, wrap=tk.WORD, bg="#1e1e1e", fg="white", insertbackground="white")
        self.code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Barra de desplazamiento 
        y_scroll_bar = tk.Scrollbar(right_frame, command=self.on_scroll)
        y_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.code_text.config(yscrollcommand=y_scroll_bar.set)

        # Ruta del archivo actual
        self.file_path = None

       
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
        # Obtener el código 
        codigo = self.code_text.get(1.0, tk.END)
        
        print("Código a ejecutar:")
        print(codigo)

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
