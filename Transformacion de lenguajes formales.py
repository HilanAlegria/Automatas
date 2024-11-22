import tkinter as tk
from tkinter import ttk

class TransformadorDeLenguaje:
    def __init__(self, reglas_de_conversion):
        self.reglas_de_conversion = reglas_de_conversion

    def transformar_cadena(self, cadena):
        cadena_transformada = ""
        for caracter in cadena:
            if caracter in self.reglas_de_conversion:
                cadena_transformada += self.reglas_de_conversion[caracter]
            else:
                cadena_transformada += caracter
        return cadena_transformada

# Configuración de las reglas de conversión
reglas = { 'a': 'x',  'b': 'y',  'c': 'z',  'd': 'w',  'e': 'v',  'f': 'u',  'g': 't',  'h': 's'}  # Puedes modificar estas reglas según lo necesites
transformador = TransformadorDeLenguaje(reglas)

# Función para manejar la transformación y mostrar el resultado en la interfaz
def transformar_y_mostrar():
    cadena_entrada = entrada.get()
    resultado = transformador.transformar_cadena(cadena_entrada)
    salida.config(text=f"Resultado: {resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Transformador de Lenguaje")
ventana.resizable(True, True)
ventana.geometry("400x200")  
# Tamaño de la ventana

# Configurar tipo de letra
font_label = ("Helvetica", 12, "bold")
font_entry = ("Helvetica", 12)
font_result = ("Helvetica", 14, "italic")

# Campo de entrada
ttk.Label(ventana, text="Introduce la cadena de entrada:").pack(pady=5)
entrada = ttk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón para realizar la transformación
boton = ttk.Button(ventana, text="Transformar", command=transformar_y_mostrar)
boton.pack(pady=5)

# Etiqueta para mostrar el resultado
salida = ttk.Label(ventana, text="")
salida.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

