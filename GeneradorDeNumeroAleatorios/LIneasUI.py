import customtkinter as ctk
from tkinter import messagebox


global opcion


cajero1 = []
minutos1 = []

cajero2 = []
minutos2 = [] 

cajero3 = []
minutos3 = []

llegada = []
temp_llegada = []

def CargaLigera():
    minutos_d = [10, 15, 20, 25]
    probs_d = [20, 40, 30, 10]
    for i in range(len(minutos_d)):
        llegada.append(probs_d[i])
        temp_llegada.append(minutos_d[i])

    minutos_serv = [1, 2, 3]
    probs_serv = [60, 30, 10] 

    for i in range(len(minutos_serv)):
        cajero1.append(probs_serv[i]) 
        minutos1.append(minutos_serv[i])

    for i in range(len(minutos_serv)):
        cajero2.append(probs_serv[i]) 
        minutos2.append(minutos_serv[i])

    for i in range(len(minutos_serv)):
        cajero3.append(probs_serv[i]) 
        minutos3.append(minutos_serv[i])

def CargaNormal():
    minutos_A = [10, 11, 12, 13, 14, 15]
    probs_A = [10, 15, 25, 25, 10, 15] 
    for i in range(len(minutos_A)):
        cajero1.append(probs_A[i]) 
        minutos1.append(minutos_A[i])

    minutos_B = [2, 3, 4, 5]
    probs_B = [10, 20, 20, 50] 
    for i in range(len(minutos_B)):
        cajero2.append(probs_B[i]) 
        minutos2.append(minutos_B[i])

    minutos_C = [6, 7, 8, 9, 10]
    probs_C = [10, 20, 20, 40, 10]
    for i in range(len(minutos_C)):
        cajero3.append(probs_C[i]) 
        minutos3.append(minutos_C[i])

    minutos_d = [1, 2, 3, 4, 5, 6]
    probs_d = [10, 15, 25, 25, 10, 15] 
    for i in range(len(minutos_d)):
        llegada.append(probs_d[i])
        temp_llegada.append(minutos_d[i])

def CargaSaturada():
    minutos_d = [4, 1, 2, 3]
    probs_d = [20, 50, 20, 10] 
    for i in range(len(minutos_d)):
        llegada.append(probs_d[i])
        temp_llegada.append(minutos_d[i])

    minutos_A = [10, 15, 20, 25]
    probs_A = [15, 35, 40, 10] 
    for i in range(len(minutos_A)):
        cajero1.append(probs_A[i]) 
        minutos1.append(minutos_A[i])

    minutos_B = [8, 10, 12, 14]
    probs_B = [10, 30, 40, 20] 
    for i in range(len(minutos_B)):
        cajero2.append(probs_B[i]) 
        minutos2.append(minutos_B[i])

    minutos_C = [12, 13, 14, 15, 16]
    probs_C = [10, 20, 40, 20, 10]
    for i in range(len(minutos_C)):
        cajero3.append(probs_C[i]) 
        minutos3.append(minutos_C[i])


def aleatoreo(indice):
    ruta_archivo = "Aleatorios.txt"
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
            
            if 0 <= indice < len(lineas):
                return float(lineas[indice])
            else:
                print(f"Error: El índice {indice} está fuera de rango.")
                return None
                
    except FileNotFoundError:
        print("Error: No se encontró el archivo Aleatorios.txt")
        return None

from tkinter import ttk
import tkinter as tk
import customtkinter as ctk

def vaciar_datos():
    listas = [cajero1, minutos1, cajero2, minutos2, cajero3, minutos3, llegada, temp_llegada]
    for lista in listas:
        lista.clear()

def creartabla(lista_datos, prom_ocio1, prom_ocio2, prom_ocio3, personasEnEspera):
    ventana_res = tk.Toplevel()
    ventana_res.title("Datos")
    try: ventana_res.state('zoomed')
    except: ventana_res.attributes('-zoomed', True)  # maximizada (en Linux usa: ventana_res.attributes("-zoomed", True))

    ctk.CTkLabel(ventana_res, text=f"""     Promedio de hocio del cajero 1: {prom_ocio1} minutos \n
                                    Promedio de hocio del cajero 1: {prom_ocio2} minutos \n
                                    Promedio de hocio del cajero 1: {prom_ocio3} minutos \n 
                                    Cantidad de personas que tubieron que esperar en fila {personasEnEspera}""", text_color="black").pack(fill="both", padx=10, pady=10)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    font=("Courier New", 12),
                    rowheight=45,
                    background="#ffffff",
                    foreground="#000000",
                    fieldbackground="#ffffff")
    style.configure("Treeview.Heading",
                    font=("Courier New", 12, "bold"),
                    background="#2c3e50",
                    foreground="#ffffff",
                    relief="flat",
                    padding=6)
    style.map("Treeview",
              background=[("selected", "#2980b9")],
              foreground=[("selected", "#ffffff")])
    style.map("Treeview.Heading",
              background=[("active", "#34495e")])

    columnas = ("it", "llegada", "ini1","tarda1", "fin1", "ini2", "tarda2", "fin2", "ini3","tarda3", "fin3", "ocio", "Espera")
    encabezados = ["It", "Llegada", "Inicai C1", "tarda", "Fin C1", "Inicia C2", "tarda", "Fin C2", "Inicia C3","tarda", "Fin C3", "ocio", "Espera"]

    frame = tk.Frame(ventana_res)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tabla = ttk.Treeview(frame, columns=columnas, show="headings")

    for col, enc in zip(columnas, encabezados):
        tabla.heading(col, text=enc)
        tabla.column(col, anchor="center", stretch=True)

    for i, d in enumerate(lista_datos):
        valores = (
            d.get("Iteracion",            "--"),
            d.get("llegada del clietne",  "--"),
            d.get("empiesa el cajero 1",  "--"),
            d.get("tiempo de tarsanza 1",  "--"),
            d.get("terminacajero 1",      "--"),
            d.get("empiesa el cajero 2",  "--"),
            d.get("tiempo de tarsanza 2",  "--"),
            d.get("terminacajero 2",      "--"),
            d.get("empiesa el cajero 3",  "--"),
            d.get("tiempo de tarsanza 3",  "--"),
            d.get("terminacajero 3",      "--"),
            d.get("tiempo de ocio",      "--") ,
            d.get("espera",      "--") 

        )
        tag = "par" if i % 2 == 0 else "impar"
        tabla.insert("", "end", values=valores, tags=(tag,))

    tabla.tag_configure("par",   background="#eaf4fb")
    tabla.tag_configure("impar", background="#ffffff")

    scroll_y = ttk.Scrollbar(frame, orient="vertical",   command=tabla.yview)
    scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=tabla.xview)
    tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.pack(side="right",  fill="y")
    scroll_x.pack(side="bottom", fill="x")
    tabla.pack(side="left", fill="both", expand=True)



def validar(lista) -> bool:
    if sum(lista) == 100:
        return True
    else:
        return False
    
def transformarListas(lista) -> list:
    for i in range(len(lista)):
        lista[i] = lista[i] / 100
    print(lista)
    return lista

def rangos(lista) -> list:
    lista_acumulada = [0]
    for i in range(len(lista)):
        nuevo_valor = lista_acumulada[-1] + lista[i]
        lista_acumulada.append(round(nuevo_valor, 3))
    return lista_acumulada


def validaciones(cantit) -> None:
    print(cajero1) 
    print(minutos1)

    print(cajero2)
    print(minutos2)

    print(cajero3) 
    print(minutos3)

    print(llegada) 
    print(temp_llegada) 

    print("se ejecuta la 1`")
    if validar(cajero1) and validar(cajero2) and validar(cajero3) and validar(cajero1):
        pass
    else:
        messagebox.showerror("Error en los datos", "revise que las provavilidades cuadren")
        return
        

    # validar que los datos sean consistentes
    if len(cajero1) != len(minutos1):
        messagebox.showerror("Error en los datos", "revise los datos")
        return

    if len(cajero2) != len(minutos2):
        messagebox.showerror("Error en los datos", "revise los datos")
        return
    
    if len(cajero3) != len(minutos3):
        messagebox.showerror("Error en los datos", "revise los datos")
        return
    
    if len(llegada) != len(temp_llegada):
        messagebox.showerror("Error en los datos", "revise los datos")
        return

    transformarListas(cajero1)
    transformarListas(cajero2)
    transformarListas(cajero3)
    transformarListas(llegada)


    rango_cajero1 = rangos(cajero1)
    rango_cajero2 = rangos(cajero2)
    rango_cajero3 = rangos(cajero3)
    rango_llegada = rangos(llegada)

    # simulacion como tal
    hora_cajero1 = 0
    hora_cajero2 = 0
    hora_cajero3 = 0
    hora_llegada = 0

    ocio_c1 = []
    ocio_c2 = [] 
    ocio_c3 = []

    listaDeDiccionarios = []
    contador = 0

    personasEnEspera = 0
    for _ in range(cantit):
        m_hora_1 = "--"
        m_hora_cajero1 = "--"
        m_hora_2 = "--"
        m_hora_cajero2 = "--"
        m_hora_3 = "--"
        m_hora_cajero3 = "--"
        temp1 = "--"
        temp2 = "--"
        temp3 = "--"

        tiempoDeOcio = 0
        tiempodDeEspera = 0

        contador += 1
        rand = aleatoreo(contador)
        obc = 0
        for i in range(1, len(rango_llegada)):
            if rand >= rango_llegada[i - 1] and rand < rango_llegada[i]:
                obc = i - 1

        hora_llegada += temp_llegada[obc]

        if hora_llegada >= hora_cajero1:
            # print("lo atiende cajero 1")
            contador += 1
            rand = aleatoreo(contador)
            obc = 0
            for i in range(1, len(rango_cajero1)):
                if rand >= rango_cajero1[i - 1] and rand < rango_cajero1[i]:
                    obc = i - 1
            hora = minutos1[obc]
            temp1 = hora
            # print(f"el cajero uno se tarda {hora} minutos en atenderlo")

            ocio_c1.append(hora_llegada - hora_cajero1)
            tiempoDeOcio = hora_llegada - hora_cajero1

            # print(f"tiempode ocio del primer elemento {hora_llegada - hora_cajero1}")
            hora_cajero1 = (hora_llegada) + hora
            # print(f"el cajero se desocupa a las {hora_cajero1}")
            m_hora_1 = hora_llegada
            m_hora_cajero1 = hora_cajero1
            

        elif hora_llegada >= hora_cajero2:
            # print("lo atiende cajero 2")
            contador += 1
            rand = aleatoreo(contador)
            obc = 0
            for i in range(1, len(rango_cajero2)):
                if rand >= rango_cajero2[i - 1] and rand < rango_cajero2[i]:
                    obc = i - 1
            hora = minutos2[obc]
            temp2 = hora

            # print(f"el cajero dos se tarda {hora} minutos en atenderlo")
            ocio_c2.append(hora_llegada - hora_cajero2)
            tiempoDeOcio = hora_llegada - hora_cajero2

            # print(f"tiempode ocio del segundo elemento {hora_llegada - hora_cajero2}")
            hora_cajero2 = (hora_llegada) + hora
            # print(f"el cajero se desocupa a las {hora_cajero2}")

            m_hora_2 = hora_llegada
            m_hora_cajero2 = hora_cajero2

        elif hora_llegada >= hora_cajero3:
            # print("lo atiende cajero 3")
            contador += 1
            rand = aleatoreo(contador)
            obc = 0
            for i in range(1, len(rango_cajero3)):
                if rand >= rango_cajero3[i - 1] and rand < rango_cajero3[i]:
                    obc = i - 1
            hora = minutos3[obc]
            temp3 = hora
            # print(f"el cajero 3 se tarda {hora} minutos en atenderlo")
            ocio_c3.append(hora_llegada - hora_cajero3)
            tiempoDeOcio = hora_llegada - hora_cajero3
            # print(f"tiempode ocio del tercer elemento {hora_llegada - hora_cajero3}")
            hora_cajero3 = (hora_llegada) + hora
            # print(f"el cajero se desocupa a las {hora_cajero3}")

            m_hora_3 = hora_llegada
            m_hora_cajero3 = hora_cajero3


        else:
            personasEnEspera += 1

            if hora_cajero1 <= hora_cajero2 and hora_cajero1 <= hora_cajero3:

                m_hora_1 = hora_cajero1
                contador += 1
                rand = aleatoreo(contador)
                obc = 0
                for i in range(1, len(rango_cajero1)):
                    if rand >= rango_cajero1[i - 1] and rand < rango_cajero1[i]:
                        obc = i - 1
                hora = minutos1[obc]
                hora_cajero1 = hora_cajero1 + hora
                # --- ASIGNACIÓN PARA TABLA ---
                temp1 = hora
                m_hora_cajero1 = hora_cajero1
                tiempodDeEspera = abs(hora_llegada - m_hora_1) 


            elif hora_cajero2 <= hora_cajero1 and hora_cajero2 <= hora_cajero3:
                m_hora_2 = hora_cajero2
                contador += 1
                rand = aleatoreo(contador)
                obc = 0
                for i in range(1, len(rango_cajero2)):
                    if rand >= rango_cajero2[i - 1] and rand < rango_cajero2[i]:
                        obc = i - 1
                hora = minutos2[obc]
                hora_cajero2 = hora_cajero2 + hora
                # --- ASIGNACIÓN PARA TABLA ---
                temp2 = hora

                m_hora_cajero2 = hora_cajero2
                tiempodDeEspera = abs(hora_llegada - m_hora_2)


            elif hora_cajero3 <= hora_cajero1 and hora_cajero3 <= hora_cajero2:
                m_hora_3 = hora_cajero3
                contador += 1
                rand = aleatoreo(contador)
                obc = 0
                for i in range(1, len(rango_cajero3)):
                    if rand >= rango_cajero3[i - 1] and rand < rango_cajero3[i]:
                        obc = i - 1
                hora = minutos3[obc]
                hora_cajero3 = hora_cajero3 + hora
                # --- ASIGNACIÓN PARA TABLA ---
                temp3 = hora
                m_hora_cajero3 = hora_cajero3
                tiempodDeEspera = abs(hora_llegada - m_hora_3)


        diccionario = {
                "Iteracion": _,
                "llegada del clietne": hora_llegada,
                "empiesa el cajero 1": m_hora_1,
                "tiempo de tarsanza 1": temp1,
                "terminacajero 1": m_hora_cajero1,
                "empiesa el cajero 2": m_hora_2,
                "tiempo de tarsanza 2": temp2,
                "terminacajero 2": m_hora_cajero2,
                "empiesa el cajero 3": m_hora_3,
                "tiempo de tarsanza 3": temp3,
                "terminacajero 3": m_hora_cajero3,
                "tiempo de ocio": tiempoDeOcio,
                "espera": tiempodDeEspera
        }
        
        listaDeDiccionarios.append(diccionario)


    # personasEnEspera
    try:
        prom_ocio1= {sum(ocio_c1) / len(ocio_c1)}
        prom_ocio2= {sum(ocio_c2) / len(ocio_c2)}
        prom_ocio3= {sum(ocio_c3) / len(ocio_c3)}
    except:
        prom_ocio1 = 0
        prom_ocio2 = 0
        prom_ocio3 = 0

        
    # print(listaDeDiccionarios)
    creartabla(listaDeDiccionarios, prom_ocio1, prom_ocio2, prom_ocio3, personasEnEspera)

    


#----------------------------------------------------------------------------------------------------------

def validaciones2(cantit) -> None:
    print("se ejecuata la 2")
    if validar(cajero1) and validar(cajero2) and validar(cajero3) and validar(cajero1):
        pass
    else:
        messagebox.showerror("Error en los datos", "revise que las provavilidades cuadren")
        return
        

    # validar que los datos sean consistentes
    if len(cajero1) != len(minutos1):
        messagebox.showerror("Error en los datos", "revise los datos")
        return

    if len(cajero2) != len(minutos2):
        messagebox.showerror("Error en los datos", "revise los datos")
        return
    
    if len(cajero3) != len(minutos3):
        messagebox.showerror("Error en los datos", "revise los datos")
        return
    
    if len(llegada) != len(temp_llegada):
        messagebox.showerror("Error en los datos", "revise los datos")
        return

    transformarListas(cajero1)
    transformarListas(cajero2)
    transformarListas(cajero3)
    transformarListas(llegada)


    rango_cajero1 = rangos(cajero1)
    rango_cajero2 = rangos(cajero2)
    rango_cajero3 = rangos(cajero3)
    rango_llegada = rangos(llegada)

    # simulacion como tal
    hora_cajero1 = 0
    hora_cajero2 = 0
    hora_cajero3 = 0
    hora_llegada = 0

    ocio_c1 = []
    ocio_c2 = [] 
    ocio_c3 = []

    listaDeDiccionarios = []

    personasEnEspera = 0
    contador = 0

    cont = 0

    for _ in range(cantit):
        contador += 1
        print(contador)

        m_hora_1 = "--"
        m_hora_cajero1 = "--"
        m_hora_2 = "--"
        m_hora_cajero2 = "--"
        m_hora_3 = "--"
        m_hora_cajero3 = "--"
        temp1 = "--"
        temp2 = "--"
        temp3 = "--"

        tiempoDeOcio = 0
        tiempodDeEspera = 0

        cont += 1
        rand = aleatoreo(cont)
        obc = 0
        for i in range(1, len(rango_llegada)):
            if rand >= rango_llegada[i - 1] and rand < rango_llegada[i]:
                obc = i - 1

        hora_llegada += temp_llegada[obc]

        if contador == 1:
            cont += 1
            rand = aleatoreo(cont)
            obc = 0
            for i in range(1, len(rango_cajero1)):
                if rand >= rango_cajero1[i - 1] and rand < rango_cajero1[i]:
                    obc = i - 1
            hora = minutos1[obc]
            temp1 = hora

            # Si el cliente llega despues de que el cajero se desocupó:
            if hora_llegada >= hora_cajero1:
                m_hora_1 = hora_llegada          
                tiempoDeOcio = hora_llegada - hora_cajero1
                tiempodDeEspera = 0            
            
            #i el cliente llega antes de se desocupe
            else:
                m_hora_1 = hora_cajero1       
                tiempoDeOcio = 0                 
                tiempodDeEspera = hora_cajero1 - hora_llegada 

            ocio_c1.append(tiempoDeOcio)
            hora_cajero1 = m_hora_1 + hora      
            m_hora_cajero1 = hora_cajero1
            

        elif contador == 2:
            cont += 1
            rand = aleatoreo(cont)
            obc = 0
            for i in range(1, len(rango_cajero2)):
                if rand >= rango_cajero2[i - 1] and rand < rango_cajero2[i]:
                    obc = i - 1
            hora = minutos2[obc]
            temp2 = hora
            if hora_llegada >= hora_cajero2:
                m_hora_2 = hora_llegada          
                tiempoDeOcio = hora_llegada - hora_cajero2
                tiempodDeEspera = 0            
            
            else:
                m_hora_2 = hora_cajero2      
                tiempoDeOcio = 0                 
                tiempodDeEspera = hora_cajero2 - hora_llegada 

            ocio_c2.append(tiempoDeOcio)
            hora_cajero2 = m_hora_2 + hora      
            m_hora_cajero2 = hora_cajero2
            

        elif contador == 3:
            cont += 1
            rand = aleatoreo(cont)
            obc = 0
            for i in range(1, len(rango_cajero3)):
                if rand >= rango_cajero3[i - 1] and rand < rango_cajero3[i]:
                    obc = i - 1
            hora = minutos3[obc]
            temp3 = hora
            if hora_llegada >= hora_cajero3:
                m_hora_3 = hora_llegada          
                tiempoDeOcio = hora_llegada - hora_cajero3
                tiempodDeEspera = 0            
            
            else:
                m_hora_3 = hora_cajero3         
                tiempodDeEspera = hora_cajero3 - hora_llegada 

            ocio_c3.append(tiempoDeOcio)
            hora_cajero3 = m_hora_3 + hora      
            m_hora_cajero3 = hora_cajero3

            contador = 0
            
        diccionario = {
                "Iteracion": _,
                "llegada del clietne": hora_llegada,
                "empiesa el cajero 1": m_hora_1,
                "tiempo de tarsanza 1": temp1,
                "terminacajero 1": m_hora_cajero1,
                "empiesa el cajero 2": m_hora_2,
                "tiempo de tarsanza 2": temp2,
                "terminacajero 2": m_hora_cajero2,
                "empiesa el cajero 3": m_hora_3,
                "tiempo de tarsanza 3": temp3,
                "terminacajero 3": m_hora_cajero3,
                "tiempo de ocio": tiempoDeOcio,
                "espera": tiempodDeEspera
        }
        
        listaDeDiccionarios.append(diccionario)


    # personasEnEspera
    try:
        prom_ocio1= {sum(ocio_c1) / len(ocio_c1)}
        prom_ocio2= {sum(ocio_c2) / len(ocio_c2)}
        prom_ocio3= {sum(ocio_c3) / len(ocio_c3)}
    except:
        prom_ocio1 = 0
        prom_ocio2 = 0
        prom_ocio3 = 0
        
    print(listaDeDiccionarios)
    creartabla(listaDeDiccionarios, prom_ocio1, prom_ocio2, prom_ocio3, personasEnEspera)
    
    

# -----------------------------------------------------------------------------------------------------



class ventana:
    def __init__(self):
        self.opcion = 0
        self.ui = ctk.CTkToplevel()
        self.ui.title = ("Lineas de espera")
        self.ui.geometry("1900x1000")

        self.ui.grid_columnconfigure(1, weight=1)
        self.ui.grid_rowconfigure(0, weight=1)

        # izquierda
        self.costado = ctk.CTkFrame(self.ui, width=200, corner_radius=0)
        self.costado.grid(row=0, column=0, sticky="nsew")

        self.label_titulo = ctk.CTkLabel(self.costado, text="Panel de Control", font=("Arial", 16, "bold"))
        self.label_titulo.pack(padx=20, pady=20)

        self.linea1 = ctk.CTkButton(self.costado, text="Banco 1", font=("Arail", 16, "bold"),
                                    command=lambda: self.ecenario1_amedias())
        self.linea1.pack(padx=20, pady=20)
        
        self.linea2 = ctk.CTkButton(self.costado, text="Banco 2", font=("Arail", 16, "bold"),
                                    command=lambda: self.ecenario2())
        self.linea2.pack(padx=20, pady=20)

        #derecah
        self.frame_datos = ctk.CTkFrame(self.ui, fg_color="transparent")
        self.frame_datos.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.ui.mainloop()

    def ecenario2(self):
        print("entre a la 2")
        self.opcion = 2
        self.ecenario1()

    def ecenario1_amedias(self):
        print("entra a la 1")
        self.opcion = 1
        self.ecenario1()
        

    def limpiar_frame_derecho(self):
        for widget in self.frame_datos.winfo_children():
            widget.destroy()

    def ecenario1(self):
        self.limpiar_frame_derecho()

        ctk.CTkLabel(self.frame_datos, text="Entrada de Datos Del Ecenario 1", 
                            font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=6, padx=10, pady=20, sticky="w")

        ctk.CTkLabel(self.frame_datos, text="| provavilidad C1| ", font=("Arial", 16, "bold")).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.frame_datos, text="| minutos C1| ", font=("Arial", 16, "bold")).grid(row=1, column=1, padx=5, pady=5)

        # Cajero 2
        ctk.CTkLabel(self.frame_datos, text="| provavilidad C2| ", font=("Arial", 16, "bold")).grid(row=1, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.frame_datos, text="| minutos C2 |", font=("Arial", 16, "bold")).grid(row=1, column=3, padx=5, pady=5)

        # Cajero 3
        ctk.CTkLabel(self.frame_datos, text="| provavilidad C3 |", font=("Arial", 16, "bold")).grid(row=1, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.frame_datos, text="| minutos C3| ", font=("Arial", 16, "bold")).grid(row=1, column=5, padx=5, pady=5)
        
        # labels de la colupna 3
        self.c_p1 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_p1.grid(row=2, column=0, padx=5, pady=5)
        self.c_m1 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_m1.grid(row=2, column=1, padx=5, pady=5)

        self.c_p2 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_p2.grid(row=2, column=2, padx=5, pady=5)
        self.c_m2 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_m2.grid(row=2, column=3, padx=5, pady=5)

        self.c_p3 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_p3.grid(row=2, column=4, padx=5, pady=5)
        self.c_m3 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.c_m3.grid(row=2, column=5, padx=5, pady=5)

        #entris
        self.en_c_p1 = ctk.CTkEntry(self.frame_datos)
        self.en_c_p1.grid(row=3, column=0, padx=5, pady=5)
        self.en_c_m1 = ctk.CTkEntry(self.frame_datos)
        self.en_c_m1.grid(row=3, column=1, padx=5, pady=5)

        self.en_c_p2 = ctk.CTkEntry(self.frame_datos)
        self.en_c_p2.grid(row=3, column=2, padx=5, pady=5)
        self.en_c_m2 = ctk.CTkEntry(self.frame_datos)
        self.en_c_m2.grid(row=3, column=3, padx=5, pady=5)

        self.en_c_p3 = ctk.CTkEntry(self.frame_datos)
        self.en_c_p3.grid(row=3, column=4, padx=5, pady=5)
        self.en_c_m3 = ctk.CTkEntry(self.frame_datos)
        self.en_c_m3.grid(row=3, column=5, padx=5, pady=5)

        # botones de la colupna 5
        self.btn_c_p1 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                    command=lambda: self.llenarC1())
        self.btn_c_p1.grid(row=4, column=0, padx=5, pady=5)
        self.btn_c_m1 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                    command=lambda: self.llenarC1())
        self.btn_c_m1.grid(row=4, column=1, padx=5, pady=5)


        self.btn_c_p2 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                    command=lambda: self.llenarC2())
        self.btn_c_p2.grid(row=4, column=2, padx=5, pady=5)
        self.btn_c_m2 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                   command=lambda: self.llenarC2())
        self.btn_c_m2.grid(row=4, column=3, padx=5, pady=5)


        self.btn_c_p3 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                    command=lambda: self.llenarC3())
        self.btn_c_p3.grid(row=4, column=4, padx=5, pady=5)
        self.btn_c_m3 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                   command=lambda: self.llenarC3())
        self.btn_c_m3.grid(row=4, column=5, padx=5, pady=5)

        # ultima parte la parte de las llegadas
        ctk.CTkLabel(self.frame_datos, text="| provavilidad llegadas| ", font=("Arial", 16, "bold")).grid(row=5, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.frame_datos, text="| minutos |", font=("Arial", 16, "bold")).grid(row=5, column=1, padx=5, pady=5)

        self.llegadas = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.llegadas.grid(row=6, column=0, padx=5, pady=5)
        self.llegadas_m1 = ctk.CTkLabel(self.frame_datos, width=150, height=250, fg_color="gray20", text="")
        self.llegadas_m1.grid(row=6, column=1, padx=5, pady=5)

        self.en_llegadas = ctk.CTkEntry(self.frame_datos)
        self.en_llegadas.grid(row=7, column=0, padx=5, pady=5)
        self.en_llegadas2 = ctk.CTkEntry(self.frame_datos)
        self.en_llegadas2.grid(row=7, column=1, padx=5, pady=5)

        self.btn_llegadas = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                    command=lambda: self.llenar_llegadas())
        self.btn_llegadas.grid(row=8, column=0, padx=5, pady=5)
        self.btn_llegada2 = ctk.CTkButton(self.frame_datos, text="Agregar", font=("Arail", 16, "bold"),
                                   command=lambda: self.llenar_llegadas())
        self.btn_llegada2.grid(row=8, column=1, padx=5, pady=5)

        self.CantidadIteraciones = ctk.CTkEntry(self.frame_datos, placeholder_text="iteraciones")
        self.CantidadIteraciones.grid(row=6, column=3, padx=5, pady=5)


        self.btn_simular = ctk.CTkButton(self.frame_datos, text="simular", font=("Arail", 16, "bold"),
                                    command=lambda: self.simular())
        self.btn_simular.grid(row=8, column=3, padx=5, pady=5)

        self.brn_Normal = ctk.CTkButton(self.frame_datos, text="Carga normal", font=("Arail", 16, "bold"),
                                    command=lambda: self.Normalitos())
        self.brn_Normal.grid(row=7, column=4, padx=5, pady=5)

        self.brn_Lenta = ctk.CTkButton(self.frame_datos, text="Carga lenta", font=("Arail", 16, "bold"),
                                    command=lambda: self.lentos())
        self.brn_Lenta.grid(row=8, column=4, padx=5, pady=5)

        self.brn_saturada = ctk.CTkButton(self.frame_datos, text="Carga saturada", font=("Arail", 16, "bold"),
                                    command=lambda: self.rapido())
        self.brn_saturada.grid(row=6, column=4, padx=5, pady=5)

        self.Baciar = ctk.CTkButton(self.frame_datos, text="Baciar", font=("Arail", 16, "bold"),
                                    command=lambda: self.bacio())
        self.Baciar.grid(row=6, column=5, padx=5, pady=5)




    def llenarC1(self) -> None:
        try:
            raw_prov = self.en_c_p1.get().replace(',', ' ').split()
            raw_min = self.en_c_m1.get().replace(',', ' ').split()

            provavilidad_lista = [float(x) for x in raw_prov]
            minuto_lista = [int(x) for x in raw_min] 

            cajero1.extend(provavilidad_lista) 
            minutos1.extend(minuto_lista)

            self.c_p1.configure(text="\n".join(map(str, cajero1)))
            self.c_m1.configure(text="\n".join(map(str, minutos1)))
            self.en_c_p1.delete(0, "end")
            self.en_c_m1.delete(0, "end")
        except:
            messagebox.showerror("Error de Datos", "revise que sean numero enterios o flotantes")

    def llenarC2(self) -> None:
        try:
            raw_prov = self.en_c_p2.get().replace(',', ' ').split()
            raw_min = self.en_c_m2.get().replace(',', ' ').split()

            provavilidad_lista = [float(x) for x in raw_prov]
            minuto_lista = [int(x) for x in raw_min] 

            cajero2.extend(provavilidad_lista) 
            minutos2.extend(minuto_lista)

            self.c_p2.configure(text="\n".join(map(str, cajero2)))
            self.c_m2.configure(text="\n".join(map(str, minutos2)))
            self.en_c_p2.delete(0, "end")
            self.en_c_m2.delete(0, "end")
        except:
            messagebox.showerror("Error de Datos", "revise que sean numero enterios o flotantes")

    def llenarC3(self) -> None:
        try:
            raw_prov = self.en_c_p3.get().replace(',', ' ').split()
            raw_min = self.en_c_m3.get().replace(',', ' ').split()

            provavilidad_lista = [float(x) for x in raw_prov]
            minuto_lista = [int(x) for x in raw_min] 

            cajero3.extend(provavilidad_lista) 
            minutos3.extend(minuto_lista)

            self.c_p3.configure(text="\n".join(map(str, cajero3)))
            self.c_m3.configure(text="\n".join(map(str, minutos3)))
            self.en_c_p3.delete(0, "end")
            self.en_c_m3.delete(0, "end")
        except:
            messagebox.showerror("Error de Datos", "revise que sean numero enterios o flotantes")

    
    def llenar_llegadas(self) -> None:
        try:
            raw_prov = self.en_llegadas.get().replace(',', ' ').split()
            raw_min = self.en_llegadas2.get().replace(',', ' ').split()

            provavilidad_lista = [float(x) for x in raw_prov]
            minuto_lista = [int(x) for x in raw_min] 

            llegada.extend(provavilidad_lista) 
            temp_llegada.extend(minuto_lista)

            self.llegadas.configure(text="\n".join(map(str, llegada)))
            self.llegadas_m1.configure(text="\n".join(map(str, temp_llegada)))
            self.en_llegadas.delete(0, "end")
            self.en_llegadas2.delete(0, "end")
        except:
            messagebox.showerror("Error de Datos", "revise que sean numero enterios o flotantes")

    def Normalitos(self):
        CargaNormal()

        self.c_p1.configure(text="\n".join(map(str, cajero1)))
        self.c_m1.configure(text="\n".join(map(str, minutos1)))
        self.en_c_p1.delete(0, "end")
        self.en_c_m1.delete(0, "end")

        self.c_p2.configure(text="\n".join(map(str, cajero2)))
        self.c_m2.configure(text="\n".join(map(str, minutos2)))
        self.en_c_p2.delete(0, "end")
        self.en_c_m2.delete(0, "end")


        self.c_p3.configure(text="\n".join(map(str, cajero3)))
        self.c_m3.configure(text="\n".join(map(str, minutos3)))
        self.en_c_p3.delete(0, "end")
        self.en_c_m3.delete(0, "end")


        self.llegadas.configure(text="\n".join(map(str, llegada)))
        self.llegadas_m1.configure(text="\n".join(map(str, temp_llegada)))
        self.en_llegadas.delete(0, "end")
        self.en_llegadas2.delete(0, "end")

    def lentos(self):
        CargaLigera()

        self.c_p1.configure(text="\n".join(map(str, cajero1)))
        self.c_m1.configure(text="\n".join(map(str, minutos1)))
        self.en_c_p1.delete(0, "end")
        self.en_c_m1.delete(0, "end")

        self.c_p2.configure(text="\n".join(map(str, cajero2)))
        self.c_m2.configure(text="\n".join(map(str, minutos2)))
        self.en_c_p2.delete(0, "end")
        self.en_c_m2.delete(0, "end")


        self.c_p3.configure(text="\n".join(map(str, cajero3)))
        self.c_m3.configure(text="\n".join(map(str, minutos3)))
        self.en_c_p3.delete(0, "end")
        self.en_c_m3.delete(0, "end")


        self.llegadas.configure(text="\n".join(map(str, llegada)))
        self.llegadas_m1.configure(text="\n".join(map(str, temp_llegada)))
        self.en_llegadas.delete(0, "end")
        self.en_llegadas2.delete(0, "end")

        

    def rapido(self):
        CargaSaturada()
        
        self.c_p1.configure(text="\n".join(map(str, cajero1)))
        self.c_m1.configure(text="\n".join(map(str, minutos1)))
        self.en_c_p1.delete(0, "end")
        self.en_c_m1.delete(0, "end")

        self.c_p2.configure(text="\n".join(map(str, cajero2)))
        self.c_m2.configure(text="\n".join(map(str, minutos2)))
        self.en_c_p2.delete(0, "end")
        self.en_c_m2.delete(0, "end")


        self.c_p3.configure(text="\n".join(map(str, cajero3)))
        self.c_m3.configure(text="\n".join(map(str, minutos3)))
        self.en_c_p3.delete(0, "end")
        self.en_c_m3.delete(0, "end")


        self.llegadas.configure(text="\n".join(map(str, llegada)))
        self.llegadas_m1.configure(text="\n".join(map(str, temp_llegada)))
        self.en_llegadas.delete(0, "end")
        self.en_llegadas2.delete(0, "end")

    def bacio(self):
        vaciar_datos()

        self.c_p1.configure(text="\n".join(map(str, cajero1)))
        self.c_m1.configure(text="\n".join(map(str, minutos1)))
        self.en_c_p1.delete(0, "end")
        self.en_c_m1.delete(0, "end")

        self.c_p2.configure(text="\n".join(map(str, cajero2)))
        self.c_m2.configure(text="\n".join(map(str, minutos2)))
        self.en_c_p2.delete(0, "end")
        self.en_c_m2.delete(0, "end")


        self.c_p3.configure(text="\n".join(map(str, cajero3)))
        self.c_m3.configure(text="\n".join(map(str, minutos3)))
        self.en_c_p3.delete(0, "end")
        self.en_c_m3.delete(0, "end")


        self.llegadas.configure(text="\n".join(map(str, llegada)))
        self.llegadas_m1.configure(text="\n".join(map(str, temp_llegada)))
        self.en_llegadas.delete(0, "end")
        self.en_llegadas2.delete(0, "end")

    def simular(self):
        print("se llego el momento de la simulacion")   
        cantit = int(self.CantidadIteraciones.get())

        print(cajero1) 
        print(minutos1)

        print(cajero2)
        print(minutos2)

        print(cajero3) 
        print(minutos3)

        print(llegada) 
        print(temp_llegada) 

        print(self.opcion)
        if self.opcion == 1:
            validaciones(cantit)
            vaciar_datos()
        elif self.opcion == 2:
            validaciones2(cantit)
            vaciar_datos()



