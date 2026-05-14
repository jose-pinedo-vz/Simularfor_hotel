# PruebaEstKolmogorov.py
from numpy import *
import numpy as np
import math
import customtkinter as ctk

class PruebaKolmogorov:
    def __init__(self):
        pass
    
    def Ventana(self, lista):
        self.lista_numeros = lista
        self.ventana = ctk.CTkToplevel()
        self.ventana.title("PRUEBA DE KOLMOGOROV")
        self.ventana.geometry("900x700")
        self.ventana.configure(bg="#1A1A1A")
        
        frame_principal = ctk.CTkFrame(self.ventana)
        frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        label_info = ctk.CTkLabel(frame_principal, text=f"Numeros disponibles: {len(lista)}", font=("Arial", 14, "bold"))
        label_info.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        label_alpha = ctk.CTkLabel(frame_principal, text="Valor de Alpha (0.01 a 0.20):")
        label_alpha.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_alpha = ctk.CTkEntry(frame_principal, width=150)
        self.entry_alpha.insert(0, "0.05")
        self.entry_alpha.grid(row=1, column=1, padx=10, pady=10)
        
        self.boton = ctk.CTkButton(frame_principal, text="Ejecutar Prueba", command=self.procedimiento)
        self.boton.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
        
        self.txt_resultados = ctk.CTkTextbox(frame_principal, width=800, height=450, font=("Courier", 11))
        self.txt_resultados.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.ventana.grab_set()
        self.ventana.wait_window()
        return self.resultado_final
    
    def print(self, texto):
        self.txt_resultados.insert("end", str(texto) + "\n")
        self.txt_resultados.see("end")
    
    def obtener_valor_critico(self, alpha):
        if alpha <= 0.01:
            return 1.628
        elif alpha <= 0.025:
            return 1.48
        elif alpha <= 0.05:
            return 1.358
        elif alpha <= 0.10:
            return 1.224
        else:
            return math.sqrt(-0.5 * math.log(alpha / 2))
    
    def procedimiento(self):
        N = len(self.lista_numeros)
        
        try:
            alpha = float(self.entry_alpha.get())
        except:
            self.print("Error: ingresa un numero valido para alpha")
            return
        
        if alpha <= 0 or alpha >= 1:
            self.print("Error: alpha debe estar entre 0 y 1")
            return
        
        if N == 0:
            self.print("Error: No hay numeros para evaluar")
            return
        
        listan = []
        aleanum = np.zeros(N)
        
        for i in range(1, N+1):
            listan.append(i)
        
        for i in range(N):
            aleanum[i] = self.lista_numeros[i]
        
        self.print("="*50)
        self.print("PRUEBA DE KOLMOGOROV - SMIRNOV")
        self.print("="*50)
        self.print(f"Cantidad de numeros a evaluar: {N}")
        self.print("")
        self.print("Numeros aleatorios a evaluar:")
        self.print(aleanum)
        
        for i in range(N):
            for j in range(0, N-i-1):
                if aleanum[j] > aleanum[j+1]:
                    aleanum[j], aleanum[j+1] = aleanum[j+1], aleanum[j]
        
        self.print("")
        self.print("Numeros ordenados:")
        self.print(aleanum)
        
        fn = []
        for i in listan:
            fn.append(i / N)
        
        self.print("")
        self.print("fn (i/N):")
        self.print(fn)
        
        valor_critico = self.obtener_valor_critico(alpha)
        daN = valor_critico / math.sqrt(N)
        
        diferencias = []
        for i in range(1, N+1):
            Fn = i / N
            xi = aleanum[i-1]
            diferencia = abs(Fn - xi)
            diferencias.append(diferencia)
        
        DN = max(diferencias)
        
        self.print("")
        self.print("="*50)
        self.print("RESULTADOS:")
        self.print("="*50)
        self.print(f"Alpha ingresado: {alpha}")
        self.print(f"Valor critico usado: {valor_critico}")
        self.print(f"daN (valor critico / sqrt(N)): {daN}")
        self.print(f"DN (maxima diferencia): {DN}")
        self.print("")
        self.print("CONDICIONAL: Se acepta H0 si DN < daN")
        self.print("")
        
        if DN < daN:
            self.print("RESULTADO: Se acepta H0")
            archivo = open("aleatorios.txt", "a+")
            for num in aleanum:
                archivo.write(str(num) + "\n")
            archivo.close()
            self.resultado_final = True
            self.print("NUMEROS GUARDADOS EN EL ARCHIVO")
        else:
            self.print("RESULTADO: No se acepta H0")
            self.print("NUMEROS NO APTOS")
            self.resultado_final = False