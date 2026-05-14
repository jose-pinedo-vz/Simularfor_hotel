import random 
from numpy import * 
import numpy as np 
import tkinter as tk
from tkinter import scrolledtext, messagebox

class PruebaHuecos():
    def __init__(self, lista_numeros=None):
        self.lista_numeros = lista_numeros
    
    def Ventana(self, lista):
        self.lista_numeros = lista
        self.ventana = tk.Tk()
        self.ventana.title("PRUEBA DE HUECOS")
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        self.ventana.configure(bg="#1A1A1A")
        self.ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
        self.ventana.resizable(False, False)
        
        tk.Label(self.ventana, text=f"Numeros disponibles: {len(lista)}", bg="#1A1A1A", fg="white", font=("Arial", 12, "bold")).place(relx=0.5, rely=0.03, anchor='center')
        
        tk.Label(self.ventana, text="alpha (intervalo menor):", bg="#1A1A1A", fg="white", font=("Arial", 11)).place(relx=0.35, rely=0.12, anchor='center')
        self.entry_alpha = tk.Entry(self.ventana, width=15)
        self.entry_alpha.place(relx=0.55, rely=0.12, anchor='center')

        tk.Label(self.ventana, text="beta (intervalo mayor):", bg="#1A1A1A", fg="white", font=("Arial", 11)).place(relx=0.35, rely=0.18, anchor='center')
        self.entry_beta = tk.Entry(self.ventana, width=15)
        self.entry_beta.place(relx=0.55, rely=0.18, anchor='center')

        tk.Button(self.ventana, text="Ejecutar", command=self.procedimiento, width=15).place(relx=0.88, rely=0.12, anchor='center')

        self.txt_resultados = scrolledtext.ScrolledText(
            self.ventana, font=("Courier", 10), bg="black", fg="blue"
        )
        self.txt_resultados.place(relx=0.5, rely=0.6, relwidth=0.95, relheight=0.75, anchor='center')
        
        self.ventana.mainloop()
    
    def print(self, texto):
        self.txt_resultados.insert(tk.END, str(texto) + "\n")
        self.txt_resultados.see(tk.END)
    
    def guardar_numeros_en_archivo(self):
        ruta_archivo = "aleatorios.txt"
        try:
            with open(ruta_archivo, "w") as archivo:
                for numero in self.lista_numeros:
                    archivo.write(f"{numero}\n")
            self.print(f"\n¡Numeros guardados exitosamente en {ruta_archivo}!")
            messagebox.showinfo("Exito", f"Se guardaron {len(self.lista_numeros)} numeros en {ruta_archivo}")
        except Exception as e:
            self.print(f"\nError al guardar el archivo: {e}")
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    def procedimiento(self):
        self.txt_resultados.delete(1.0, tk.END)
        
        if self.lista_numeros is None or len(self.lista_numeros) == 0:
            self.print("Error: No hay numeros para evaluar")
            return
        
        n = len(self.lista_numeros)

        try:
            alpha = float(self.entry_alpha.get())
            betha = float(self.entry_beta.get())
        except:
            self.print("Error en los datos de entrada")
            return
        
        if alpha >= betha:
            self.print("Error: alpha debe ser menor que beta")
            return

        arre = np.zeros(n)
        
        for i in range(n):
            arre[i] = self.lista_numeros[i]
        
        self.print("="*50)
        self.print("PRUEBA DE HUECOS")
        self.print("="*50)
        self.print(f"Cantidad de numeros evaluados: {n}")
        self.print("")
        self.print("Numeros a evaluar:")
        self.print(arre)

        huecos = []
        conta = 0
        for j in range(n):
            if alpha < arre[j] < betha:
                huecos.append(conta)
                conta = 0
            else: 
                conta += 1

        self.print("")
        self.print("Huecos encontrados:")
        self.print(huecos)

        p = betha - alpha

        observadas = {}
        for hueco in huecos:
            if hueco in observadas:
                observadas[hueco] += 1
            else:
                observadas[hueco] = 1

        self.print("")
        self.print("Frecuencia observada:")
        self.print(observadas)

        N = len(huecos)
        esperadas = {}
        for k in observadas:
            prob = (1-p)**k * p
            esperadas[k] = N * prob

        self.print("")
        self.print("Frecuencia esperada:")
        self.print(esperadas)

        self.print("")
        self.print("Pi (probabilidades):")
        for k in observadas:
            prob = (1-p)**k * p
            self.print(f"k={k}: {prob}")

        x2 = {}
        for k in observadas:
            o = observadas[k]
            e = esperadas[k]
            if e > 0:
                x2[k] = (o - e)**2 / e
            else:
                x2[k] = 0

        total = sum(list(x2.values()))
        
        tabla_valores_criticos = {
            1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070,
            6: 12.592, 7: 14.067, 8: 15.507, 9: 16.919, 10: 18.307,
            11: 19.675, 12: 21.026, 13: 22.362, 14: 23.685, 15: 24.996,
            16: 26.296, 17: 27.587, 18: 28.869, 19: 30.144, 20: 31.410
        }

        grados_libertad = len(observadas) - 1

        self.print("")
        self.print("="*50)
        self.print("RESULTADO PRUEBA DE HUECOS")
        self.print("="*50)
        self.print(f"Estadistico: {total}")
        self.print(f"Grados de libertad: {grados_libertad}")
        self.print(f"Alpha: {alpha}")
        self.print(f"Beta: {betha}")
        self.print(f"p (beta - alpha): {p}")

        if grados_libertad in tabla_valores_criticos:
            valor_critico = tabla_valores_criticos[grados_libertad]
            self.print(f"Valor critico (tabla): {valor_critico}")

            self.print("")
            if total < valor_critico:
                self.print("CONCLUSION: Se ACEPTA H0")
                self.print("Guardando numeros en el archivo")
                self.guardar_numeros_en_archivo()
            else:
                self.print("CONCLUSION: Se RECHAZA H0")
                self.print("NO se guardaron los numeros en aleatorios.txt.")
        
            self.print(".")
        else:

            self.print(".")