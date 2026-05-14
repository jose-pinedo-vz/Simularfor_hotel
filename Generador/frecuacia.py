import customtkinter as ctk
import random

from tkinter import messagebox
from pathlib import Path

def AbrirArchivo(numeros):

    # Ruta del archivo .py actual
    ruta_script = Path(__file__)

    # Carpeta donde está el script
    carpeta = Path(__file__).resolve().parent

    # Abrir un archivo en la misma carpeta que el script
    archivo = carpeta / "aleatorios.txt"

    with open(archivo, "a+") as f:
        
        f.write("\n")
        for num in numeros:
            num=round(num,5)
            f.write(str(num)+"\n")

def PruebaDeFreeuencais(lista: list, divisor) -> bool:
    contante = ""

    lisat2 = lista[:]
    num = divisor
    contanteDeLIsta = ""

    contante += (f"Frecuecia esperada {len(lista) / num} \n")
    Fe = len(lista) / num
    valor_k = num
    contante += (f"los intervalos son de {1 / num} \n \n")
    lista_de_intervalos = []
    valor = 0
    while valor <= 1:
        lista_de_intervalos.append(round(valor, 2))
        valor += 1 / num

    contante += (f"lista de intervalos:  {lista_de_intervalos} \n\n")

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
        contante += f"Freceuncia esperada {Fe} - frecuecnai observada {len(lisa)}\n"
        for i in range(len(lisa)):
            contanteDeLIsta += f"{lisa[i]}\n"

        contanteDeLIsta += f"Cantidad de elementos (FO): {len(lisa)} \n\n"

    frecuencia_esperada = len(lista) / len(superLIsta) 
    
    acumulador = 0
    contante += "\nFormula =  la suma de: (FO - FE) ** 2 / FE \n\n"
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

    contante += f"\nResultado de la formula: {acumulador} < {xi}\nCon un valor de significancia del 5% "
    if acumulador < xi:
        contante += ("\nSe haceptan los aleatorios")
        AbrirArchivo(lista)
    else:
        contante += ("\nNo hace aceptan")

    return contante, contanteDeLIsta


class frecuacual:
    def __init__(self, lista):
        ventanita = ctk.CTkToplevel()
        ventanita.geometry("1200x800")
        ventanita.title("Método de Comprobación Frecuencial")

        try: ventanita.state('zoomed')
        except: ventanita.attributes('-zoomed', True)

        ventanita.grid_columnconfigure((0, 1, 2), weight=1)
        ventanita.grid_rowconfigure(1, weight=1) 

        frame_superior = ctk.CTkFrame(ventanita, fg_color="transparent")
        frame_superior.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        
        self.titulo_lista = ctk.CTkLabel(frame_superior, text="Lista de Aleatorios:", font=("Arial", 12, "bold"))
        self.titulo_lista.grid(row=0, column=0, padx=5, sticky="w")
        
        self.txt_lista = ctk.CTkTextbox(frame_superior, width=250, height=500, font=("Consolas", 11))
        self.txt_lista.grid(row=1, column=0, padx=5, pady=5)
        texto_lista = "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.txt_lista.insert("0.0", texto_lista)
        self.txt_lista.configure(state="disabled")

        frame_info = ctk.CTkFrame(frame_superior, fg_color="transparent")
        frame_info.grid(row=1, column=1, padx=20)

        self.txt_lista2 = ctk.CTkTextbox(frame_info, width=600, height=40, font=("Consolas", 12))
        self.txt_lista2.pack(pady=5)
        self.txt_lista2.insert("0.0", f"Tamaño de la lista (N): {len(lista)}")
        self.txt_lista2.configure(state="disabled")

        self.txt_lista3 = ctk.CTkTextbox(frame_info, width=300, height=100, font=("Consolas", 12))
        self.txt_lista3.pack(side="left", padx=5)
        self.txt_lista3.insert("0.0", "Inserte n: ")
        self.txt_lista3.configure(state="disabled")

        self.entry = ctk.CTkEntry(frame_info, width=300, height=100)    
        self.entry.pack(side="left", padx=5)

        def ejecutar_prueba():
            try:
                self.txt_resultados.configure(state="normal") 
                self.txt_resultados.delete("0.0", "end")
                self.txt_resultados2.configure(state="normal") 
                self.txt_resultados2.delete("0.0", "end")

                var = int(self.entry.get())
                if len(lista) % var != 0:
                    from tkinter import messagebox
                    messagebox.showwarning("Atención", "El valor de n debe ser divisor de N")
                    return
                
                constante, contante2 = PruebaDeFreeuencais(lista, var)
                
                self.txt_resultados.insert("0.0", f"{constante}")
                self.txt_resultados2.insert("0.0", f"{contante2}")
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Datos inválidos: {e}")

        self.boton = ctk.CTkButton(frame_superior, text="Ejecutar prueba de frecuencias", 
                                   command=ejecutar_prueba, height=50)
        self.boton.grid(row=1, column=2, padx=10)

        ventanita.grid_columnconfigure((0, 1, 2), weight=1)
        ventanita.grid_rowconfigure((0, 1, 2), weight=0)
        ventanita.grid_rowconfigure(3, weight=1) 

        ctk.CTkLabel(ventanita, text="Prosedimiento", font=("Arial", 13, "bold")).grid(row=2, column=0, columnspan=2, pady=(10, 0))
        ctk.CTkLabel(ventanita, text="Distribucion de elemetnos:", font=("Arial", 13, "bold")).grid(row=2, column=2, pady=(10, 0))

        self.txt_resultados = ctk.CTkTextbox(ventanita, font=("Consolas", 13))
        self.txt_resultados.grid(row=3, column=0, columnspan=2, padx=15, pady=(5, 15), sticky="nsew")

        self.txt_resultados2 = ctk.CTkTextbox(ventanita, font=("Consolas", 13))
        self.txt_resultados2.grid(row=3, column=2, padx=15, pady=(5, 15), sticky="nsew")




# lista  = [
#     0.889, 0.532, 0.209, 0.191, 0.775, 0.751, 0.787,
#     0.184, 0.253, 0.890, 0.796, 0.422, 0.468, 0.860,
#     0.703, 0.357, 0.892, 0.726, 0.220, 0.158, 0.022
# ]

# obj = frecuacual(lista)