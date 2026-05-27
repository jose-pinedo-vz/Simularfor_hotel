import customtkinter as ctk
import random

from tkinter import messagebox
from pathlib import Path

def AbrirArchivo(numeros):
    print("llega al modulo de insercion")

    # Ruta del archivo .py actual
    ruta_script = Path(__file__)

    # Carpeta donde está el script
    carpeta = Path(__file__).resolve().parent

    # Abrir un archivo en la misma carpeta que el script
    archivo = carpeta / "Aleatorios.txt"
    print(numeros)

    with open(archivo, "a+") as f:
        for num in numeros:
            num=float(num)
            f.write(str(round(num,5))+"\n")

def PruebaDeFreeuencais(lista: list, divisor) -> bool:
    contante = ""

    lisat2 = lista[:]
    num = divisor
    contanteDeLIsta = ""

    contante += (f"Frecuecia esperada {len(lista) / num} \n")
    valor_k = num
    contante += (f"los intervalos son de {1 / num} \n \n")
    lista_de_intervalos = []
    valor = 0
    while valor <= 1:
        lista_de_intervalos.append(valor)
        valor += 1 / num

    contante += (f"lista de intervalos:  {lista_de_intervalos} \n")

    lisat2.sort()

    lista_auxiliar = []
    superLIsta = []

    for i in range(len(lista_de_intervalos) - 1):
        lista_auxiliar = []
        for num in lisat2:
            if num > lista_de_intervalos[i] and num < lista_de_intervalos[i + 1]:
                lista_auxiliar.append(num)
        superLIsta.append(lista_auxiliar)


    contanteDeLIsta += f"-- lista de valores separados -- \n"
    for lisa in superLIsta:
        contanteDeLIsta += "Elementos de la lista: \n"
        for i in range(len(lisa)):
            contanteDeLIsta += f"{lisa[i]}\n"

        contanteDeLIsta += f"Cantidad de elementos (FO): {len(lisa)} \n\n"

    frecuencia_esperada = len(lista) / len(superLIsta) 
    
    acumulador = 0
    contante += "Formula =  la suma de: (FO - FE) ** 2 / FE \n\n"
    for i in range(len(superLIsta)):
        ListaExtraida = superLIsta[i]
        fo = len(ListaExtraida) 
        contante += f"({frecuencia_esperada} - {fo}) ** 2 / {frecuencia_esperada} = "
        operacion = (frecuencia_esperada - fo) ** 2
        operacion = operacion / frecuencia_esperada
        
        contante += f" {operacion} \n"
        acumulador += operacion

    ventana_dialogo = ctk.CTkInputDialog(
        text=f"Introduce el número de xi considerando un valor de k = {valor_k - 1} :",
        title="Configuración Chi-Cuadrada"
    )

    xi = float(ventana_dialogo.get_input())

    contante += f"\nResultado de la formula: {acumulador} > {xi} "
    if acumulador < xi:
        contante += ("\nSe haceptan los aleatoresos")
        AbrirArchivo(lista)
    else:
        contante += ("\nNo hace hacepta")

    return contante, contanteDeLIsta


class frecuacual:
    def __init__(self, lista):
        ventanita = ctk.CTkToplevel()
        ventanita.geometry("1000x700")
        ventanita.title("Método de Comprobación Frecuencial")

        try: ventanita.state('zoomed')
        except: ventanita.attributes('-zoomed', True)

        self.titulo_lista = ctk.CTkLabel(ventanita, text="Lista de Aleatorios:", font=("Arial", 14, "bold"))
        self.titulo_lista.place(relx=0.05, rely=0.05)

        self.txt_lista = ctk.CTkTextbox(ventanita, width=250, height=550, font=("Consolas", 12))
        self.txt_lista.place(relx=0.05, rely=0.1)
        
        texto_lista = "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.txt_lista.insert("0.0", texto_lista)
        self.txt_lista.configure(state="disabled") 

        self.txt_lista2 = ctk.CTkTextbox(ventanita, width=450, height=75, font=("Consolas", 12))
        self.txt_lista2.place(relx=0.15, rely=0.20)

        texto_lista2 = f"Tamaño de la lista (N): {len(lista)}"
        self.txt_lista2.insert("0.0", texto_lista2)
        self.txt_lista2.configure(state="disabled") 

        self.txt_lista3 = ctk.CTkTextbox(ventanita, width=200, height=75, font=("Consolas", 13))
        self.txt_lista3.place(relx=0.15, rely=0.30)
        self.txt_lista3.insert("0.0", "Inserte n: ")
        self.txt_lista3.configure(state="disabled") 

        self.entry = ctk.CTkEntry(ventanita, width=250, height=75,)    
        self.entry.place(relx=0.23, rely=0.30)

        self.titulo_res = ctk.CTkLabel(ventanita, text="Resultados de la Prueba:", font=("Arial", 14, "bold"))
        self.titulo_res.place(relx=0.5, rely=0.01)

        self.txt_resultados = ctk.CTkTextbox(ventanita, width=1200, height=1000, font=("Consolas", 13))
        self.txt_resultados.place(relx=0.35, rely=0.1)

        self.titulo_res2 = ctk.CTkLabel(ventanita, text="Separacion de elmetenos:", font=("Arial", 14, "bold"))
        self.titulo_res2.place(relx=0.75, rely=0.01)

        self.txt_resultados2 = ctk.CTkTextbox(ventanita, width=600, height=1000, font=("Consolas", 13))
        self.txt_resultados2.place(relx=0.75, rely=0.1)


        def ejecutar_prueba():
            self.txt_resultados.configure(state="normal") 
            self.txt_resultados.delete("0.0", "end")

            var = int(self.entry.get())

            if len(lista) % var != 0:
                messagebox.showwarning("Atención", "El valor de n debe ser divisor de N")
                return
            
            constante, contante2 = PruebaDeFreeuencais(lista, var)
            
            self.txt_resultados.insert("0.0", f"{constante}")
            self.txt_resultados2.insert("0.0", f"{contante2}")

        self.boton = ctk.CTkButton(ventanita, text="Ejecutar Prueba Chi-Cuadrada", command=lambda: ejecutar_prueba())
        self.boton.place(relx=0.15, rely=0.15)

        ventanita.mainloop()



# lista  = [
#     0.889, 0.532, 0.209, 0.191, 0.775, 0.751, 0.787,
#     0.184, 0.253, 0.890, 0.796, 0.422, 0.468, 0.860,
#     0.703, 0.357, 0.892, 0.726, 0.220, 0.158, 0.022
# ]

# obj = frecuacual(lista)