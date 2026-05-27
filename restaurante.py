import random
import math
import customtkinter as ctk
from tkinter import ttk
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk



# flojo_diario = [60, 100, 160, 200, 240]
# flujo_siario_prob = [10, 25, 40, 20, 5]

# grupo = [2, 4, 6, 7, 8]
# grupo_prob = [10, 40, 30, 15, 5]

# tem_preparacion = [5, 10, 20, 30]
# tem_preparacion_prob = [20, 55, 15, 10]

# consumo = [1, 2, 3]
# condumo_prob = [20, 60, 20]

# suministro = [1, 2, 4, 5]
# suministro_prob = [60, 25, 10, 5]

# even_rh = ["nada", "renuncia", "despedido", "renunacia multiple"]
# even_rh_prob = [92, 3, 4, 1]

# Evento_Ale_prob = [80, 10, 5, 5]
# Evento_Ale = ["Nada", "Merma o accidente menor", "Falla en equipo", "Devolucion de platillo"]

# hora_critica = [0, 1]
# hora_critica_prob = [90, 10]

# porcen_ora_critica = [30, 40, 50]
# porcen_ora_critica_prob = [40, 30, 30]

# categorai_platillos = [[70, 20, 10], [60, 25, 15], [50, 30, 20]]
# categorai_platillos_prob = [60, 30, 10]



# # otros datos
# platillos_disponibles = ["normal", "caro", "exotico"]
# platilllosEmpesamos = [400, 200, 40]

# cantidadMinimaDeStock = [200, 70, 10]
# cantidadDelStockmaxiom = [400, 300, 50]

# platillos_lista = platilllosEmpesamos[:]
# ganancias_por_platillo = [150, 600, 900]
# ganancias_netas = [100, 300, 350]

# cantidad_de_mesas = 2
# cantidad_de_cosineros = 8
# sueldo_cosineros = 15000
# horas_habiles = 8
# personal = 10
# sueldo_personal = 8000

# pago_servicios = 2000

class mostrar_Tablasa():
    def __init__(self, diccionario_resumen, diccionario, diccionario2, concluciones, insidencaisDelDiario, insidencias_rh_diccionario, GananciasTotales_lista, gastosTotales_lista, lista_meses, ganancias_mensuales, personas_mensuales, lista_eventos, lisat_provavilidad, lista_provavilidad_acumulada, lista_rango):
        self.lista_mesea = lista_meses
        self.ganancias_mensuales = ganancias_mensuales
        self.personas_mensuales = personas_mensuales

        self.diccionario_resumen = diccionario_resumen
        self.diccionario = diccionario
        self.diccionario2 = diccionario2
        self.insidencias_del_diario = insidencaisDelDiario
        self.insidencias_rh_diccionario = insidencias_rh_diccionario
        self.GananciasTotales_lista = GananciasTotales_lista
        self.gastosTotales_lista = gastosTotales_lista


        self.lista_eventos = lista_eventos
        self.lisat_provavilidad = lisat_provavilidad
        self.lista_provavilidad_acumulada = lista_provavilidad_acumulada
        self.lista_rango = lista_rango

        self.ventana_tablas = ctk.CTkToplevel()
        self.ventana_tablas.title("RESULTADOS")


        try:
            self.ventana_tablas.state("zoomed")
        except:
            self.ventana_tablas.attributes("-zoomed", True)

        fm_General = ctk.CTkScrollableFrame(self.ventana_tablas, border_width=10, border_color="#5D4037", orientation="vertical",
            fg_color="#D7CCC8")
        fm_General.pack(fill="both", expand=True, padx=10, pady=10)

        label_titulo = ctk.CTkLabel(fm_General,
                                    text="RESULTADOS DE LA SIMULACIÓN",
                                    font=("Arial", 24, "bold"),
                                    text_color="#3E2723")
        label_titulo.pack(pady=20)

        label_titulo = ctk.CTkLabel(fm_General,
                                    text="CLIENTES",
                                    font=("Arial", 24, "bold"),
                                    text_color="#3E2723")
        label_titulo.pack(pady=20)


        style = ttk.Style()

        style.configure("Treeview",
            background="#2B2B2B",
            foreground="#3E2723",
            fieldbackground="#2B2B2B",
            rowheight=35,
            borderwidth=0,
            font=("Arial", 9)
        )

        style.configure("Treeview.Heading",
            background="#3E2723",
            foreground="white",
            relief="flat",
            font=("Arial", 9, "bold")
        )

        style.map("Treeview", background=[("selected", "#1A1A1D")])

        label_t0_5 = ctk.CTkLabel(fm_General, text="RESUMEN", font=("Arial", 22, "bold"),text_color="#3E2723")
        label_t0_5.pack(pady=(20, 5))

        self.frame0_5 = ctk.CTkScrollableFrame(fm_General, border_width=2, height=400, border_color="#1A1A1D", fg_color="#2B2B2B", orientation="horizontal")
        self.frame0_5.pack(fill="both", expand=True, padx=20, pady=10)


        print("Resumen diccionario")
        print(self.diccionario_resumen)

        columnas_tabla0_5 = [
            "Día",
            "Total de personas atendidas",
            "Total de platillos cocinados",
            "Cantidad de minutos cocinados",
            "Ocio por cocinero",
            "¿Hubo hora crítica?",
            "Ganancias brutas",
            "Gastos de insumos"
        ]
        self.tabla0_5 = ttk.Treeview(self.frame0_5, columns=columnas_tabla0_5, show="headings")

        for col in columnas_tabla0_5:
            self.tabla0_5.heading(col, text=col.upper())
            self.tabla0_5.column(col, width=250, anchor="center")

        self.tabla0_5.pack(fill="both", expand=True)


        # correjir

        for i, d in enumerate(self.diccionario_resumen):
            valores = []
            for col in columnas_tabla0_5:
                dato = d.get(col)
                valores.append(dato)

            if i % 2 == 0:
                tag = "par"
            else:
               tag = "impar"
            self.tabla0_5.insert("", "end", values=valores, tags=(tag,))



        # label_t2 = ctk.CTkLabel(fm_General, text="RESULTADOS DE PLATILLOS", font=("Arial", 22, "bold"), text_color="#3E2723")
        # label_t2.pack(pady=(25, 5))

        label_t1 = ctk.CTkLabel(fm_General, text="RESULTADOS GENERALES", font=("Arial", 22, "bold"),text_color="#3E2723")
        label_t1.pack(pady=(20, 5))

        self.frame1 = ctk.CTkScrollableFrame(fm_General, border_width=2, height=400, border_color="#1A1A1D", fg_color="#2B2B2B", orientation="horizontal")
        self.frame1.pack(fill="both", expand=True, padx=20, pady=10)

        columnas_tabla1 = [
            "Día", "Mes", "Aleatorio Personas", "Personas en el día", "Aleatorio Grupos", "Personas por grupo",
            "Cantidad de mesas", "Mesas ocupadas por hora", "Personas perdidas",
            "Personas atendidas", "Aleatorio Crítica", "¿Hubo hora crítica?", "Porcentaje de hora crítica",
            "Perdidas en hora pico", "Personas atendidas en total", "Aleatorio Evento",
            "Evento del día", "Evento del personal", "Aleatorio RH", "Encargo a proveedores",
            "Platillos encargados", "Ingresos", "Egresos", "Total"
        ]

        self.tabla = ttk.Treeview(self.frame1, columns=columnas_tabla1, show="headings")

        for col in columnas_tabla1:
            self.tabla.heading(col, text=col.upper())
            self.tabla.column(col, width=250, anchor="center")

        self.tabla.pack(fill="both", expand=True)


        # correjir

        for i, d in enumerate(self.diccionario):
            valores = []
            for col in columnas_tabla1:
                dato = d.get(col)
                valores.append(dato)

            if i % 2 == 0:
                tag = "par"
            else:
               tag = "impar"
            self.tabla.insert("", "end", values=valores, tags=(tag,))



        label_t2 = ctk.CTkLabel(fm_General, text="RESULTADOS DE PLATILLOS", font=("Arial", 22, "bold"), text_color="#3E2723")
        label_t2.pack(pady=(25, 5))

        self.frame2 = ctk.CTkScrollableFrame(fm_General, border_width=2, height=400, border_color="#1A1A1D", fg_color="#2B2B2B", orientation="horizontal")
        self.frame2.pack(fill="both", expand=True, padx=20, pady=10)

        columnas_tabla2 = [
            "Día", "Platillos Iniciales", "Estado de encargo", "Aleatorio Platillos",
            "Promedio de platillos por persona", "Total de platillos vendidos", "Aleatorio Tiempo",
            "Tiempo de cocina por platillo", "Minutos cocinados totales", "Minutos por cocinero",
            "Tiempo de ocio por cocinero", "Aleatorio Distribución", "Distribución de los platillos",
            "Platillos a cocinar", "Platillos rechazados", "Ganancias brutas", "Gastos de insumos"
        ]

        self.tabla2 = ttk.Treeview(self.frame2, columns=columnas_tabla2, show="headings")
        for col in columnas_tabla2:
            self.tabla2.heading(col, text=col.upper())
            self.tabla2.column(col, width=250, anchor="center")

        self.tabla2.pack(fill="both", expand=True)

        for i, d2 in enumerate(self.diccionario2):
            valores2 = []
            for col in columnas_tabla2:
                dato = d2.get(col)
                valores2.append(dato)

            if i % 2 == 0:
                tag = "par"
            else:
               tag = "impar"
            self.tabla2.insert("", "end", values=valores2, tags=(tag,))


        label_t3 = ctk.CTkLabel(fm_General, text="CONCLUCIONES", font=("Arial", 22, "bold"), text_color="#3E2723")
        label_t3.pack(pady=(25, 5))

        self.frame3 = ctk.CTkFrame(fm_General, fg_color="#D7CCC8", border_width=2, border_color="#1A1A1D")
        self.frame3.pack(fill="x", padx=20, pady=10)
        # tamanio de las letras
        #
        style = ttk.Style()
        style.configure("TablaConceptos.Treeview",
            font=("Arial", 12),
            background="#D7CCC8",
            foreground="black",
            fieldbackground="#D7CCC8",
            rowheight=50
        )

        columnas_tabla3 = ["Concepto", "Valor Final"]
        self.tabla3 = ttk.Treeview(self.frame3, columns=columnas_tabla3, show="headings", height=30, style="TablaConceptos.Treeview")


        # correjir

        self.tabla3.heading("Concepto", text="CONCEPTO")
        self.tabla3.heading("Valor Final", text="VALOR FINAL")

        self.tabla3.column("Concepto", width=200, anchor="w")
        self.tabla3.column("Valor Final", width=200, anchor="center", stretch=True)

        self.tabla3.pack(fill="both", expand=True, padx=5, pady=5)


        # correjir
        for t in [self.tabla, self.tabla2, self.tabla3, self.tabla0_5]:
            t.tag_configure("par", background="#D7CCC8")
            t.tag_configure("impar", background="#FFFFFF") #


        for i in self.tabla3.get_children():
            self.tabla3.delete(i)


        for k, v in concluciones.items():
            if isinstance(v, (int, float)):
                v = f"{v:.2f}"

            self.tabla3.insert("", "end", values=(k, v))

        self.tabla3.pack(fill="both", expand=True)


        self.frame4 = ctk.CTkFrame(fm_General, fg_color="#D7CCC8", border_width=2, border_color="#1A1A1D")
        self.frame4.pack(fill="x", padx=20, pady=10)

        self.insidencia = ctk.CTkButton(self.frame4, text="Grafica de insidencias", command=lambda: self.GraficaInsidencais())
        self.insidencia.grid(row=0, column=0, pady=20, padx=10)

        self.insidenciaRh = ctk.CTkButton(self.frame4, text="Grafica de insidencias de Rh", command=lambda: self.GraficaEventosEh())
        self.insidenciaRh.grid(row=0, column=1, pady=20, padx=10)

        self.insidenciaRh = ctk.CTkButton(self.frame4, text="Comportamiento de gastos y ganancias", command=lambda: self.GraficarGanancias())
        self.insidenciaRh.grid(row=0, column=2, pady=20, padx=10)

        self.graficarpersoans = ctk.CTkButton(self.frame4, text="Compararcion de personas por mes", command=lambda: self.graficas_personas_meses())
        self.graficarpersoans.grid(row=0,column=3,padx=20,pady=20)

        self.gafracarGanancias=ctk.CTkButton(self.frame4, text="Comparacion de ganacias por mes", command=lambda: self.graficar_ganancias_meses())
        self.gafracarGanancias.grid(row=0,column=4,padx=20,pady=20)



        # mostrar valores basicos de la simulacion -----------------------------------------------------------
        self.frame5 = ctk.CTkFrame(fm_General, fg_color="#D7CCC8", border_width=2, border_color="#1A1A1D")
        self.frame5.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(self.frame5, text="Flujo de personas por dia:", font=("Arial", 15, "bold"), text_color="#3E2723").pack(padx=10,pady=10)

        columnas_tabla = ["Evento", "Provavilidad", "Provavilidad acumulada", "rango"]
        self.tabla4 = ttk.Treeview(self.frame5, columns=columnas_tabla, show="headings", height=5, style="TablaConceptos.Treeview")

        for col in columnas_tabla:
            self.tabla4.heading(col, text=col.upper())
            self.tabla4.column(col, width=250, anchor="center")

        self.tabla4.pack(fill="both", expand=True, padx=10,pady=10)

        evento = self.lista_eventos[0]
        prob = self.lisat_provavilidad[0]
        rango = self.lista_rango[0]

        rango2 = []
        for i in range(1, len(rango)):
            rango2.append(f"{rango[i-1]} - {rango[i]}")

        for i in range(len(evento)):
            self.tabla4.insert("", "end", values=(evento[i], prob[i], rango[i + 1], rango2[i]))


        # 2 -------------------

        ctk.CTkLabel(self.frame5, text="Promedio de grupo:", font=("Arial", 15, "bold"), text_color="#3E2723").pack(padx=10,pady=10)

        columnas_tabla = ["Evento", "Provavilidad", "Provavilidad acumulada", "rango"]
        self.tabla5 = ttk.Treeview(self.frame5, columns=columnas_tabla, show="headings", height=5, style="TablaConceptos.Treeview")

        for col in columnas_tabla:
            self.tabla5.heading(col, text=col.upper())
            self.tabla5.column(col, width=250, anchor="center")

        self.tabla5.pack(fill="both", expand=True, padx=10,pady=10)

        evento = self.lista_eventos[1]
        prob = self.lisat_provavilidad[1]
        rango = self.lista_rango[1]

        rango2 = []
        for i in range(1, len(rango)):
            rango2.append(f"{rango[i-1]} - {rango[i]}")

        for i in range(len(evento)):
            self.tabla5.insert("", "end", values=(evento[i], prob[i], rango[i + 1], rango2[i]))


        # 3 -------------------

        ctk.CTkLabel(self.frame5, text="Preparacion platillo:", font=("Arial", 15, "bold"), text_color="#3E2723").pack(padx=10,pady=10)

        columnas_tabla = ["Evento", "Provavilidad", "Provavilidad acumulada", "rango"]
        self.tabla6 = ttk.Treeview(self.frame5, columns=columnas_tabla, show="headings", height=5, style="TablaConceptos.Treeview")

        for col in columnas_tabla:
            self.tabla6.heading(col, text=col.upper())
            self.tabla6.column(col, width=250, anchor="center")

        self.tabla6.pack(fill="both", expand=True, padx=10,pady=10)

        evento = self.lista_eventos[2]
        prob = self.lisat_provavilidad[2]
        rango = self.lista_rango[2]

        rango2 = []
        for i in range(1, len(rango)):
            rango2.append(f"{rango[i-1]} - {rango[i]}")

        try:
            for i in range(len(evento)):
                self.tabla6.insert("", "end", values=(evento[i], prob[i], rango[i + 1], rango2[i]))
        except:
            pass

        # mas ===============
        self.tablas_automatizadas = []
        listaTitulos = ["1", "2", "3", "Consumo por persona", "Suministro (Dias)", "Prob evento de RH:", "Evento aleatorios:", "Horas criticas:", "Hay hora critica:", "Porcentaje de platillos:"]
        for i in range(3, 10):
            ctk.CTkLabel(self.frame5, text=listaTitulos[i], font=("Arial", 15, "bold"), text_color="#3E2723").pack(padx=10, pady=10)

            columnas_tabla = ["Evento", "Provavilidad", "Provavilidad acumulada", "rango"]

            tabla_temporal = ttk.Treeview(self.frame5, columns=columnas_tabla, show="headings", height=5, style="TablaConceptos.Treeview")

            for col in columnas_tabla:
                tabla_temporal.heading(col, text=col.upper())
                tabla_temporal.column(col, width=250, anchor="center")

            tabla_temporal.pack(fill="both", expand=True, padx=10, pady=10)

            evento = self.lista_eventos[i]
            prob = self.lisat_provavilidad[i]
            rango = self.lista_rango[i]
            
            rango2 = [f"{rango[j-1]} - {rango[j]}" for j in range(1, len(rango))]

            for j in range(len(evento)):
                tabla_temporal.insert("", "end", values=(evento[j], prob[j], rango[j + 1], rango2[j]))


            self.tablas_automatizadas.append(tabla_temporal)




    def GraficaInsidencais(self):
        # print(self.insidencias_del_diario)
        x = []
        y = []
        for xi, yi in self.insidencias_del_diario.items():
            x.append(f"{xi} ({yi})")
            y.append(yi)

        # print(x)
        # print(y)
        plt.bar(x, y)
        plt.suptitle("Registro de insidencias")
        plt.tight_layout()
        plt.show()

    def GraficaEventosEh(self):
        # insidencias_rh_diccionario

        x = []
        y = []
        for xi, yi in self.insidencias_rh_diccionario.items():
            x.append(f"{xi} ({yi})")
            y.append(yi)

        plt.bar(x, y)
        plt.suptitle("Registro de insidencias en el personal")
        plt.tight_layout()
        plt.show()
    def GraficarGanancias(self):

        lisat_dias = list(range(1, len(self.GananciasTotales_lista) + 1))

        plt.plot(lisat_dias, self.GananciasTotales_lista, 'g-', label="Ganancias", linewidth=2)
        plt.plot(lisat_dias, self.gastosTotales_lista, 'r-', label="Costos", linewidth=2)
        plt.xticks(lisat_dias)

        plt.title("Ganancias vs Costos")
        plt.xlabel("Día")
        plt.ylabel("Efectivo ($)")
        plt.legend()
        plt.grid(True, linestyle='--')

        plt.tight_layout()
        plt.show()
    
    def graficas_personas_meses(self):
        # self.lista_mesea = lista_meses
        # self.ganancias_mensuales = ganancias_mensuales
        # self.personas_mensuales = personas_mensuales

        plt.bar(self.lista_mesea, self.personas_mensuales)
        plt.suptitle("Registro de personas por mes")
        plt.tight_layout()
        plt.show()

    def graficar_ganancias_meses(self):
        gananciasnetas = round(sum(self.ganancias_mensuales), 2)
        plt.bar(self.lista_mesea,self.ganancias_mensuales)
        plt.suptitle(f"Registro de ganancias por mes {gananciasnetas}")
        plt.tight_layout()
        plt.show()



        self.ventana_tablas.mainloop()


def CargarMedios():
    global flojo_diario, flujo_siario_prob, grupo, grupo_prob, tem_preparacion, tem_preparacion_prob, consumo, condumo_prob, suministro, \
        suministro_prob, even_rh, even_rh_prob, Evento_Ale_prob, Evento_Ale, hora_critica, hora_critica_prob, porcen_ora_critica, \
        porcen_ora_critica_prob, categorai_platillos, categorai_platillos_prob, platillos_disponibles, cantidadMinimaDeStock, cantidadDelStockmaxiom, platilllosEmpesamos, Listamultiplciadores


    flojo_diario = [60, 100, 160, 200, 240]
    flujo_siario_prob = [10, 25, 40, 20, 5]

    grupo = [2, 4, 6, 7, 8]
    grupo_prob = [10, 40, 30, 15, 5]

    tem_preparacion = [5, 10, 20, 30]
    tem_preparacion_prob = [20, 55, 15, 10]

    consumo = [1, 2, 3]
    condumo_prob = [20, 60, 20]

    suministro = [1, 2, 3, 4]
    suministro_prob = [60, 30, 5, 5]

    even_rh = ["nada", "renuncia", "despedido", "multiple"]
    even_rh_prob = [92, 3, 4, 1]

    Evento_Ale_prob = [80, 10, 5, 5]
    Evento_Ale = ["Nada", "Merma o accidente menor", "Falla en equipo", "Devolucion de platillo"]

    hora_critica = [0, 1]
    hora_critica_prob = [90, 10]

    porcen_ora_critica = [30, 40, 50]
    porcen_ora_critica_prob = [40, 30, 30]

    categorai_platillos = [[70, 20, 10], [60, 25, 15], [50, 30, 20]]
    categorai_platillos_prob = [60, 30, 10]

    platillos_disponibles = ["normal", "caro", "exotico"]
    platilllosEmpesamos = [600, 400, 100]

    cantidadMinimaDeStock = [400, 130, 40]
    cantidadDelStockmaxiom = platilllosEmpesamos[:]

    global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios, platillos_lista, \
        ganancias_por_platillo, ganancias_netas, penalisacino_por_personas_perdidas, penalisacion_por_platillos_perdidos

    platillos_lista = platilllosEmpesamos[:]
    ganancias_por_platillo = [50, 150, 300]
    ganancias_netas = [20, 50, 100]

    cantidad_de_mesas = 15
    cantidad_de_cosineros = 8
    sueldo_cosineros = 15000
    horas_habiles = 8
    personal = 10
    sueldo_personal = 8000

    pago_servicios = 2000

    penalisacino_por_personas_perdidas = 100
    penalisacion_por_platillos_perdidos = 50

    # print("Si carga")


    Listamultiplciadores = [1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1]


def validar(lista) -> bool:
    # print(lista)
    if sum(lista) == 100:
        return True
    else:
        return False

def transformarListas(lista) -> list:
    for i in range(len(lista)):
        lista[i] = lista[i] / 100
    return lista

def rangos(lista) -> list:
    lista_acumulada = [0]
    for i in range(len(lista)):
        nuevo_valor = lista_acumulada[-1] + lista[i]
        lista_acumulada.append(round(nuevo_valor, 3))
    return lista_acumulada

contador = 0
import GeneraRandom
def provavilidar(lista1, lista2):
    global contador
    contador += 1
    rand = GeneraRandom.aleatorio(contador)
    for i in range(len(lista2) - 1):
        if lista2[i] <= rand < lista2[i+1]:
            return lista1[i], rand

def validaciones(Dias_a_Simular) -> float:
    # validar si las provavilidades son correctas
    global flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob, categorai_platillos_prob
    global suministro_prob, even_rh_prob, Evento_Ale_prob, porcen_ora_critica_prob, hora_critica_prob
    global flojo_diario

    # CargarMedios()

    lista_eventos = []
    lisat_provavilidad = []
    lista_provavilidad_acumulada = []
    lista_rango = []

    listas_a_validar = [
        flujo_siario_prob, grupo_prob, tem_preparacion_prob, condumo_prob,
        suministro_prob, even_rh_prob, Evento_Ale_prob,
        porcen_ora_critica_prob, hora_critica_prob, categorai_platillos_prob
    ]

    lisat_provavilidad.append(flujo_siario_prob)
    lisat_provavilidad.append(grupo_prob)
    lisat_provavilidad.append(tem_preparacion_prob)
    lisat_provavilidad.append(condumo_prob)
    lisat_provavilidad.append(suministro_prob)
    lisat_provavilidad.append(even_rh_prob)
    lisat_provavilidad.append(Evento_Ale_prob)
    lisat_provavilidad.append(porcen_ora_critica_prob)
    lisat_provavilidad.append(hora_critica_prob)
    lisat_provavilidad.append(categorai_platillos_prob)





    for p in listas_a_validar:
        if not validar(p):
            print(f"Error: Una de las listas de probabilidad no suma 100%")
            return False


    if len(flojo_diario) != len(flujo_siario_prob):
        print("Error en los datos 1")
        return

    if len(grupo) != len(grupo_prob):
        print("Error en los datos 2")
        return

    if len(tem_preparacion) != len(tem_preparacion_prob):
        print("Error en los datos 3")
        return

    if len(consumo) != len(condumo_prob):
        print("Error en los datos 4")
        return

    if len(suministro) != len(suministro_prob):
        print("Error en los datos 5")
        return

    if len(even_rh) != len(even_rh_prob):
        print("Error en los datos 6")
        return

    if len(Evento_Ale) != len(Evento_Ale_prob):
        print("Error en los datos 7")
        return

    if len(porcen_ora_critica) != len(porcen_ora_critica_prob):
        print("Error en los datos 8")
        return


    if len(hora_critica) != len(hora_critica_prob):
        print("Error en los datos 9")
        return

    if len(categorai_platillos) != len(categorai_platillos_prob):
        print("Error en los datos 10")
        return
    
    lista_eventos.append(flojo_diario)
    lista_eventos.append(grupo)
    lista_eventos.append(tem_preparacion)
    lista_eventos.append(consumo)
    lista_eventos.append(suministro)
    lista_eventos.append(even_rh)
    lista_eventos.append(Evento_Ale)
    lista_eventos.append(porcen_ora_critica)
    lista_eventos.append(hora_critica)
    lista_eventos.append(categorai_platillos)


    # paso la lista a decimal
    transformarListas(flujo_siario_prob)
    transformarListas(grupo_prob)
    transformarListas(tem_preparacion_prob)
    transformarListas(condumo_prob)
    transformarListas(suministro_prob)
    transformarListas(even_rh_prob)
    transformarListas(Evento_Ale_prob)
    transformarListas(porcen_ora_critica_prob)
    transformarListas(hora_critica_prob)
    transformarListas(categorai_platillos_prob)

    lista_provavilidad_acumulada.append(flujo_siario_prob)
    lista_provavilidad_acumulada.append(grupo_prob)
    lista_provavilidad_acumulada.append(tem_preparacion_prob)
    lista_provavilidad_acumulada.append(condumo_prob)
    lista_provavilidad_acumulada.append(suministro_prob)
    lista_provavilidad_acumulada.append(even_rh_prob)
    lista_provavilidad_acumulada.append(Evento_Ale_prob)
    lista_provavilidad_acumulada.append(porcen_ora_critica_prob)
    lista_provavilidad_acumulada.append(hora_critica_prob)
    lista_provavilidad_acumulada.append(categorai_platillos_prob)


    # creo los rangos
    flujo_siario_prob = rangos(flujo_siario_prob)
    grupo_prob = rangos(grupo_prob)
    tem_preparacion_prob = rangos(tem_preparacion_prob)
    condumo_prob = rangos(condumo_prob)
    suministro_prob = rangos(suministro_prob)
    even_rh_prob = rangos(even_rh_prob)
    Evento_Ale_prob = rangos(Evento_Ale_prob)
    porcen_ora_critica_prob = rangos(porcen_ora_critica_prob)
    hora_critica_prob = rangos(hora_critica_prob)
    categorai_platillos_prob = rangos(categorai_platillos_prob)


    lista_rango.append(flujo_siario_prob)
    lista_rango.append(grupo_prob)
    lista_rango.append(tem_preparacion_prob)
    lista_rango.append(condumo_prob)
    lista_rango.append(suministro_prob)
    lista_rango.append(even_rh_prob)
    lista_rango.append(Evento_Ale_prob)
    lista_rango.append(porcen_ora_critica_prob)
    lista_rango.append(hora_critica_prob)
    lista_rango.append(categorai_platillos_prob)

    print("los datos estan correctos")

    # platillos con los que empesamos
    platillos_encargados = []
    estado_encarga = 0
    lleganAlimentos = 0

    diasDeENcarga = []
    platillosDeEncarga = []
    # global flojo_diario
    flojo_diario_auxilia = flojo_diario[:]
    inicio_fin_semana = 5

    listaDiccionarios1 = []
    listaDiccionarios2 = []

    SumaTotal = 0
    GastosTotal = 0

    ganancias_totales = 0
    gastos_totales = 0

    lista_de_platillos_vendidos = []
    dias_simulados = 0
    lista_de_maximas_apariciones = []
    clientes_totales_perdidos = 0
    platillos_perdidos_totales = 0
    personas_totales_de_llegada = 0

    insidencaisDelDiario = []
    insidencaisDelDiarioRh = []

    GananciasTotales_lista = []
    gastosTotales_lista = []
    diccionario_resumen = []

    lista_promedio_personas_por_grupo = []
    lista_promedio_de_hocio_por_cocinero = []

    dias_del_anio = 0

    lista_meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    rangos_meses = [
        (1, 31),   
        (32, 59),   
        (60, 90),   
        (91, 120),  
        (121, 151), 
        (152, 181), 
        (182, 212), 
        (213, 243), 
        (244, 273), 
        (274, 304), 
        (305, 334), 
        (335, 365)  
    ]

    ganancias_mensuales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    personas_mensuales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    personas_por_mes = 0
    ganancias_por_mes = 0
    mes_antorios = "Enero"
    contador_de_meses=0



    for _ in range(Dias_a_Simular):
        print("dia: ", _ + 1)

        dias_del_anio += 1
        if dias_del_anio == 366:
            dias_del_anio = 1

        mes_actual = ""

        

        
        for indice, (inicio, fin) in enumerate(rangos_meses):
            if inicio <= dias_del_anio and dias_del_anio <= fin:
                multiplicador = Listamultiplciadores[indice]

        
        print("el multiplicador es de  1")

        

        


        flojo_diario = flojo_diario_auxilia[:]
        if inicio_fin_semana <= (_ + 1) and (_ + 1) <= inicio_fin_semana + 2:
            print("Fin de semana")
            for i in range(len(flojo_diario)):
                flojo_diario[i] = flojo_diario[i] * 1.20

        if (_ + 1) > inicio_fin_semana + 2:
            print("Final del fin de semana")
            inicio_fin_semana += 7

        personas, random_1 = provavilidar(flojo_diario,  flujo_siario_prob)
        personas = int(personas)
        personas = multiplicador * personas
        personas_totales_en_el_dia = personas
        print("canditad de personas en el dia: ", personas)
        personas_totales_de_llegada += personas
        print("Platillos con lo que se inicia: ", platillos_lista)

        estado_de_la_encarga_mostrar = ""

        if _ in diasDeENcarga:
            estado_de_la_encarga_mostrar = "llego mercancia"
            for idx, dia_pedido in enumerate(diasDeENcarga):
                if _ == dia_pedido:
                    pedido = platillosDeEncarga[idx]
                    for cat in range(len(platillos_lista)):
                        platillos_lista[cat] += pedido[cat]
            estado_encarga = 0
            print("Cantidad de platillos: ", platillos_lista)

        else:
            estado_de_la_encarga_mostrar = "No llego mercancia"

        platillos_de_inicio_a_mostrar = platillos_lista[:]

        grupo_Porcent, rnadom_2 = provavilidar(grupo, grupo_prob)
        print(f"promedio de personas por grupo: {grupo_Porcent}")
        print(f"mesas totales por hora: {cantidad_de_mesas} ")
        mesas_ocupadas = math.ceil(personas / grupo_Porcent / horas_habiles)
        print(f"mesas ocupadas por hora {mesas_ocupadas}")

        personas_perdidas = 0
        if mesas_ocupadas > cantidad_de_mesas:
            personas_perdidas = (mesas_ocupadas - cantidad_de_mesas) * grupo_Porcent * horas_habiles
            personas = personas - personas_perdidas
            print("personas perdidas ", personas_perdidas)
            print("personas atendidas ", personas)

            clientes_totales_perdidos += personas_perdidas

        # print("Fin del dia")
        criticas, random8 = provavilidar(hora_critica, hora_critica_prob)
        existencia_de_hora_critica = ""
        personas_perdidas_pico = 0
        porncentaje_de_personas_en_hora_pico = ""
        if criticas == 1:
            print("ubo una hora crítica")
            existencia_de_hora_critica = "Si"
            porcentaje, random10 = provavilidar(porcen_ora_critica, porcen_ora_critica_prob)
            porncentaje_de_personas_en_hora_pico = f"{porcentaje}%"

            # total de personas
            personas_pico = int(personas * (porcentaje / 100))

            print(f"{porcentaje} pociento de personas llegaron en una hora")
            print(f"personas en pico: {personas_pico}")

            mesas_pico = math.ceil(personas_pico / grupo_Porcent)

            if mesas_pico > cantidad_de_mesas:
                exceso_mesas = mesas_pico - cantidad_de_mesas

                personas_perdidas_pico = exceso_mesas * grupo_Porcent

                print(f"personas perdidas por hora crítica {personas_perdidas_pico}")
                clientes_totales_perdidos += personas_perdidas_pico

                personas -= personas_perdidas_pico
                personas = max(0, personas)
            else:
                print("NO ser perdio gente")
        else:
            existencia_de_hora_critica = "No"

        platillos_por_persona, random_3 = provavilidar(consumo, condumo_prob)
        print(f"el promedio de platos por persona fue de: {platillos_por_persona}")

        total_de_platillos = platillos_por_persona * personas
        print(f"fueron un total de {total_de_platillos} platillos")

        temp_cosina_promedio, random_4 = provavilidar(tem_preparacion, tem_preparacion_prob)
        print(f"tiempo promedio de preparacion de los platillos: {temp_cosina_promedio}")

        horas_cosina_totales = temp_cosina_promedio * total_de_platillos
        print(f"Total de minutos cosinando: {horas_cosina_totales}")

        minutos_por_cocinero = horas_cosina_totales / cantidad_de_cosineros
        print(f"cada mesero devera de trabajar {minutos_por_cocinero} minutos al dia")

        distribucion_platillos, random_5 = provavilidar(categorai_platillos, categorai_platillos_prob)
        print(f"distribucion de los platillos {distribucion_platillos}")

        platillos_totales_sumatoria = []
        for i in range(len(distribucion_platillos)):
            print(f"de la categoria {i + 1} son {math.ceil(total_de_platillos * (distribucion_platillos[i]/100))}")
            platillos_totales_sumatoria.append(math.ceil(total_de_platillos * (distribucion_platillos[i]/100)))

        print(f"Lista platillos totales: {platillos_totales_sumatoria}")

        indice_maximo = max(range(len(platillos_totales_sumatoria)), key=platillos_totales_sumatoria.__getitem__)

        lista_de_maximas_apariciones.append(indice_maximo)

        # print(platillos_totales_sumatoria)

        platillosRechasados = 0
        ganancias_totales_dia = 0
        ganancias_netas_dia = 0
        ventas_reales_insumos = 0

        for i in range(len(distribucion_platillos)):
            demanda_especifica = int(round(total_de_platillos * (distribucion_platillos[i] / 100)))

            if platillos_lista[i] >= demanda_especifica:
                vendido = demanda_especifica
                platillos_lista[i] = int(platillos_lista[i] - vendido)
            else:
                vendido = platillos_lista[i]
                # el math.vell redondea hcia arri
                rechasados_esta_cat = math.ceil(demanda_especifica - vendido)
                platillosRechasados += rechasados_esta_cat
                platillos_lista[i] = 0

            ganancias_totales_dia += vendido * ganancias_por_platillo[i]
            ganancias_netas_dia += vendido * ganancias_netas[i]

        ganancias = ganancias_totales_dia
        ganancias_netas_final = ganancias_netas_dia
        gastos_insumos = ganancias - ganancias_netas_final


        print(f"platillos rechazados: {platillosRechasados}")

        platillos_perdidos_totales += platillosRechasados

        Platillos_vendidos_totales = sum(platillos_totales_sumatoria) - platillosRechasados

        print(f"Platillos vendidos totales: {Platillos_vendidos_totales}")

        lista_de_platillos_vendidos.append(Platillos_vendidos_totales)

        print(f"ganancias de platillos {ganancias_netas}")
        print(f"ganancias netas final {ganancias_netas_final}")
        print(f"ganancias netas final {gastos_insumos}")

        # ganancias = 0
        # for i in range(len(distribucion_platillos)):
        #     # print(f"platillos {i} =  {ganancias_por_platillo[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
        #     ganancias += ganancias_por_platillo[i] * total_de_platillos * (distribucion_platillos[i]/100)

        # print("ganancais totales: ", ganancias)

        # gastos = ganancias

        # ganancias = 0
        # for i in range(len(distribucion_platillos)):
        #     # print(f"platillos {i} =  {ganancias_netas[i] * (total_de_platillos * (distribucion_platillos[i]/100))}")
        #     ganancias += ganancias_netas[i] * total_de_platillos * (distribucion_platillos[i]/100)

        # print("ganancais netas (utilidades): ", ganancias)

        # ganancias = ganancias
        # gastos = gastos - ganancias
        # print(f"Gastos totales de los platillos {gastos}")

        # evento aleatiorio
        eventoProb, random_6 = provavilidar(Evento_Ale, Evento_Ale_prob)
        insidencaisDelDiario.append(eventoProb)
        print("Evento catastrofico del dia? ", eventoProb)
        # event rh
        eventoRH, random_9 = provavilidar(even_rh, even_rh_prob)
        insidencaisDelDiarioRh.append(eventoRH)
        print("Eventos con el personal: ", eventoRH)
        pedido_del_dia_para_diccionario = []
        encarga_provedroes = ""
        for i in range(len(distribucion_platillos)):
            if platillos_lista[i] <= cantidadMinimaDeStock[i] and estado_encarga == 0:
                tiempo_de_llegada, random_7 = provavilidar(suministro, suministro_prob)
                print("se encargan alimentos y se tardan en llegar: ", tiempo_de_llegada, " dias")
                encarga_provedroes = f"Dias: {tiempo_de_llegada}"

                lleganAlimentos = _ + tiempo_de_llegada
                for j in range(len(distribucion_platillos)):
                    platillos_encargados.append(cantidadDelStockmaxiom[j] - platillos_lista[j])

                print(f"se encargo mercancia y llega en {lleganAlimentos} dias")
                diasDeENcarga.append(lleganAlimentos)
                print(f"cantidad de alimentos encargados {platillos_encargados}")
                platillosDeEncarga.append(platillos_encargados)
                pedido_del_dia_para_diccionario = platillos_encargados[:]
                platillos_encargados = []

                estado_encarga = 1
                break
            else:
                if estado_encarga == 0:
                    encarga_provedroes = "No se encargo"
                    pedido_del_dia_para_diccionario = []

        print("platillos restandes del dia: ", platillos_lista)

        print("Final dia ", _ + 1)
        print(f"ganancias {ganancias}")
        SumaTotal = ganancias

        costo_cocineros = (sueldo_cosineros / 30) * cantidad_de_cosineros
        costo_personal = (sueldo_personal / 30) * personal
        costo_servicios = pago_servicios / 30

        total_fijos = costo_cocineros + costo_personal + costo_servicios
        total_fijos = round(total_fijos, 2)
        print(f"gastos: {total_fijos}")
        GastosTotal = total_fijos + gastos_insumos
        print(f"gastos totales: {GastosTotal}")

        print(f"ganancias netas = {ganancias - GastosTotal}")
        Ganancias_totales = ganancias - GastosTotal


        ganancias_totales += ganancias
        gastos_totales += GastosTotal

        dias_simulados += 1

        lista_promedio_personas_por_grupo.append(grupo_Porcent)
        lista_promedio_de_hocio_por_cocinero.append(round((horas_habiles - (minutos_por_cocinero / 60)), 2))



        for indice, (inicio, fin) in enumerate(rangos_meses):
            if inicio <= dias_del_anio and dias_del_anio <= fin:
                mes_actual = lista_meses[indice]
                ganancias_mensuales[indice]+=round(Ganancias_totales, 2)
                personas_mensuales[indice]+=personas


        # lista
        diccionario = {
            "Día": _ + 1,
            "Mes": mes_actual,
            "Aleatorio Personas": random_1,
            "Personas en el día": personas_totales_en_el_dia,
            "Aleatorio Grupos": rnadom_2,
            "Personas por grupo": grupo_Porcent,
            "Cantidad de mesas": cantidad_de_mesas,
            "Mesas ocupadas por hora": mesas_ocupadas,
            "Personas perdidas": personas_perdidas,
            "Personas atendidas": personas_totales_en_el_dia - personas_perdidas,
            "Aleatorio Crítica": random8,
            "¿Hubo hora crítica?": existencia_de_hora_critica,
            "Porcentaje de hora crítica": porncentaje_de_personas_en_hora_pico,
            "Perdidas en hora pico": personas_perdidas_pico,
            "Personas atendidas en total": personas,
            "Aleatorio Evento": random_6,
            "Evento del día": eventoProb,
            "Evento del personal": eventoRH,
            "Aleatorio RH": random_9,
            "Encargo a proveedores": encarga_provedroes,
            "Platillos encargados": pedido_del_dia_para_diccionario,
            "Ingresos": ganancias,
            "Egresos": GastosTotal,
            "Total": round(Ganancias_totales, 2)
        }

        diccionario2 = {
            "Día": _ + 1,
            "Platillos Iniciales": platillos_de_inicio_a_mostrar,
            "Estado de encargo": estado_de_la_encarga_mostrar,
            "Aleatorio Platillos": random_3,
            "Promedio de platillos por persona": platillos_por_persona,
            "Total de platillos vendidos": total_de_platillos,
            "Aleatorio Tiempo": random_4,
            "Tiempo de cocina por platillo": temp_cosina_promedio,
            "Minutos cocinados totales": horas_cosina_totales,
            "Minutos por cocinero": minutos_por_cocinero,
            "Tiempo de ocio por cocinero": f"{round((horas_habiles - (minutos_por_cocinero / 60)), 2)} h",
            "Aleatorio Distribución": random_5,
            "Distribución de los platillos": distribucion_platillos,
            "Platillos a cocinar": platillos_totales_sumatoria,
            "Platillos rechazados": platillosRechasados,
            "Ganancias brutas": ganancias,
            "Gastos de insumos": gastos_insumos
        }

        diccionario0_5 = {
            "Día": _ + 1,
            "Total de personas atendidas": personas,
            "Total de platillos cocinados": sum(platillos_totales_sumatoria) - platillosRechasados,
            "Cantidad de minutos cocinados": minutos_por_cocinero,
            "Ocio por cocinero": round((horas_habiles - (minutos_por_cocinero / 60)), 2),
            "¿Hubo hora crítica?": existencia_de_hora_critica,
            "Ganancias brutas": ganancias,
            "Gastos de insumos": gastos_insumos
        }

        listaDiccionarios1.append(diccionario)
        listaDiccionarios2.append(diccionario2)
        diccionario_resumen.append(diccionario0_5)

        GananciasTotales_lista.append(ganancias)
        gastosTotales_lista.append(GastosTotal)



        



    platillo_mas_consumido = lista_de_maximas_apariciones

    conteo = {}
    for n in lista_de_maximas_apariciones:
        conteo[n] = conteo.get(n, 0) + 1

    platillo_mas_consumido = max(conteo, key=conteo.get)

    eficienciaCosina =  round(((personas_totales_de_llegada - clientes_totales_perdidos) / personas_totales_de_llegada) * 100, 2)

    # calculo de empleados ideales
    ocio_promedio_cocinero = sum(lista_promedio_de_hocio_por_cocinero) / len(lista_promedio_de_hocio_por_cocinero)
    horas_reales_cocinadas = cantidad_de_cosineros * (horas_habiles - ocio_promedio_cocinero)
    empleados_ideales = math.ceil(horas_reales_cocinadas / horas_habiles)


    #penalisaciones
    penalisacionPersonas = clientes_totales_perdidos * penalisacino_por_personas_perdidas
    penalisacionPlatillos = platillos_perdidos_totales * penalisacion_por_platillos_perdidos

    # calcular mes con mas trafico de personas

    maxPersonas = personas_mensuales[0]
    mes = "Enero"
    for i in range(1, len(personas_mensuales)):
        if personas_mensuales[i] > maxPersonas:
            maxPersonas = personas_mensuales[i]
            mes = lista_meses[i]

    maxPersonas2 = personas_mensuales[0]
    mes2 = "Enero"
    for i in range(1, len(personas_mensuales)):
        if personas_mensuales[i] < maxPersonas2:
            maxPersonas2 = personas_mensuales[i]
            mes2 = lista_meses[i]

    MaxGanancias = ganancias_mensuales[0]
    mes3 = "Enero"
    for i in range(1, len(ganancias_mensuales)):
        if ganancias_mensuales[i] > MaxGanancias:
            MaxGanancias = ganancias_mensuales[i]
            mes = lista_meses[i]

    concluciones = {
        "Días simulados: ": dias_simulados,
        "Promedio de platillos por día: ": (sum(lista_de_platillos_vendidos) / len(lista_de_platillos_vendidos)),
        "Platillo más consumido: ": platillos_disponibles[platillo_mas_consumido],
        "Personas totales atendidas: ": personas_totales_de_llegada,
        "Promedio de personas por dia: ": (personas_totales_de_llegada) / dias_simulados,
        "Promedio de personas en los grupos: ": (sum(lista_promedio_personas_por_grupo) / len(lista_promedio_personas_por_grupo)),
        "Personas perdidas o rechazadas: ": clientes_totales_perdidos,
        "Penalisacion por personas: ": penalisacionPersonas,
        "Eficiencia de la cocina: ": f"{eficienciaCosina}%",
        "Platillos perdidos: ": platillos_perdidos_totales,
        "Penalisacion por platillos: ": penalisacionPlatillos,
        "Ocio promedio por cocinero: ": (sum(lista_promedio_de_hocio_por_cocinero) / len(lista_promedio_de_hocio_por_cocinero)),
        "Cantidad idea de empleados: ": empleados_ideales,
        "Mes con mas clientes": f"{mes} con {maxPersonas} personas",
        "Mes con menos clientes": f"{mes2} con {maxPersonas2} personas",
        "Mes con mas ganancias:": f"{mes3} con {MaxGanancias} personas",
        "Inversión total: ": gastos_totales,
        "Ganancias brutas: ": ganancias_totales,
        "Utilidad neta: ": ganancias_totales - gastos_totales - penalisacionPlatillos - penalisacionPersonas
    }


    # print("DIccionario 1 \n")
    # print(listaDiccionarios1)
    # print("Diccionario 2 \n")
    # print(listaDiccionarios2)

    # insidenticas


    print("insidencias")
    insidencias_diccionario = {}

    for insidencia in Evento_Ale:
        cantidad = insidencaisDelDiario.count(insidencia)
        insidencias_diccionario[insidencia] = cantidad
    # print(insidencias_diccionario)
    insidencias_rh_diccionario = {}
    for rh in even_rh:
        cantidad = insidencaisDelDiarioRh.count(rh)
        insidencias_rh_diccionario[rh] = cantidad

    print("Evento rh")
    print(insidencias_rh_diccionario)

    print(lista_meses)
    print(ganancias_mensuales)
    print(personas_mensuales)

    # lista_eventos = []
    # lisat_provavilidad = []
    # lista_provavilidad_acumulada = []
    # lista_rango = []


    mostrar_Tablasa(diccionario_resumen, listaDiccionarios1, listaDiccionarios2, concluciones, insidencias_diccionario, insidencias_rh_diccionario, GananciasTotales_lista, gastosTotales_lista, lista_meses, ganancias_mensuales, personas_mensuales, lista_eventos, lisat_provavilidad, lista_provavilidad_acumulada, lista_rango)


    


    



    CargarMedios()

# validaciones(50)





class cocina:
    def __init__(self):
        CargarMedios()
        self.ventana = ctk.CTkToplevel()
        self.ventana.title("COSINA - RESTAURANTE")

        try: self.ventana.state("zoomed")
        except: self.ventana.attributes("-zoomed", True)

        color_fondo = "#D7CCC8"          # Gris oscuro para los Frames internos
        color_hover = "#5D4037"          # Fondo principal (el negro de la imagen)
        color_texto = "#3E2723"          # Blanco puro para visibilidad
        color_Extra = "#FFA726"          # Naranja para los botones (como en la imagen)
        color_contorno_azul = "#1A1A1D"


        self.ventana.configure(fg_color=color_hover)

        self.frame_scroll = ctk.CTkScrollableFrame(
            self.ventana,
            fg_color=color_hover
        )
        self.frame_scroll.pack(fill="both", expand=True, padx=10, pady=8)


        ancho_entry = 148
        alto_entry = 36
        ancho_txt = 138
        alto_txt = 180
        pad_col = 6
        pad_row = 4


        self.datosFijos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosFijos.pack(pady=10, padx=10, fill="x")

        label1 = ctk.CTkLabel(self.datosFijos, text="Cantidad de cocineros:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label1.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.CantidadDeCosineros = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.CantidadDeCosineros.grid(row=1, column=0, padx=pad_col, pady=(2, 10))

        label2 = ctk.CTkLabel(self.datosFijos, text="Mesas disponibles:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label2.grid(row=0, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.cantidadDeMesas = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.cantidadDeMesas.grid(row=1, column=1, padx=pad_col, pady=(2, 10))

        label3 = ctk.CTkLabel(self.datosFijos, text="Horas laborales:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label3.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Horaslaborales = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.Horaslaborales.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label4 = ctk.CTkLabel(self.datosFijos, text="Cantidad de personal extra:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label4.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.personal = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.personal.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label5 = ctk.CTkLabel(self.datosFijos, text="Sueldo cocineros / mes:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label5.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.SueldoCosinero = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.SueldoCosinero.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label6 = ctk.CTkLabel(self.datosFijos, text="Sueldo resto del personal:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label6.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.sueldoPersonal = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.sueldoPersonal.grid(row=1, column=5, padx=pad_col, pady=(2, 10))

        label7 = ctk.CTkLabel(self.datosFijos, text="Pago total servicios mensuales:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label7.grid(row=0, column=6, padx=pad_col, pady=(10, 2), sticky="ew")

        self.pagoServicios = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.pagoServicios.grid(row=1, column=6, padx=pad_col, pady=(2, 10))

        label71 = ctk.CTkLabel(self.datosFijos, text="dias a simular", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label71.grid(row=0, column=7, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Dias_simular = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.Dias_simular.grid(row=1, column=7, padx=pad_col, pady=(2, 10))

        label72 = ctk.CTkLabel(self.datosFijos, text="Penalisacin por personas", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label72.grid(row=2, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.penalisacion_personas= ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.penalisacion_personas.grid(row=3, column=0, padx=pad_col, pady=(2, 10))

        label72 = ctk.CTkLabel(self.datosFijos, text="Penalisacin por platillos", font=("Arial", 13), text_color=color_texto, wraplength=ancho_entry)
        label72.grid(row=2, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.penalisacion_platillos = ctk.CTkEntry(self.datosFijos, font=("Arial", 13), width=ancho_entry, height=alto_entry)
        self.penalisacion_platillos.grid(row=3, column=1, padx=pad_col, pady=(2, 10))


        self.datosPlatillos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosPlatillos.pack(pady=10, padx=10, fill="x")

        label8 = ctk.CTkLabel(self.datosPlatillos, text="Platillos disponibles:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label8.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.nombreplatillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.nombreplatillos.grid(row=1, column=0, padx=pad_col, pady=(2, 10))


        label10 = ctk.CTkLabel(self.datosPlatillos, text="Porcentaje de platillos:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label10.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Text_categorai_platillos = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.Text_categorai_platillos.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label11 = ctk.CTkLabel(self.datosPlatillos, text="Prob de porcentaje:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label11.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.Text_categorai_platillos_prob = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.Text_categorai_platillos_prob.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label12 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad inicial de Stock:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label12.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.txt_cantidadStock = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.txt_cantidadStock.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label13 = ctk.CTkLabel(self.datosPlatillos, text="Cantidad mínima de Stock:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label13.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.txt_cantidadStock_min = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.txt_cantidadStock_min.grid(row=1, column=5, padx=pad_col, pady=(2, 10))

        label14 = ctk.CTkLabel(self.datosPlatillos, text="Costo del platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label14.grid(row=0, column=6, padx=pad_col, pady=(10, 2), sticky="ew")

        self.texr_costoDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.texr_costoDelPlatillo.grid(row=1, column=6, padx=pad_col, pady=(2, 10))

        label15 = ctk.CTkLabel(self.datosPlatillos, text="Ganancia del platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label15.grid(row=0, column=7, padx=pad_col, pady=(10, 2), sticky="ew")

        self.texr_gananciaDelPlatillo = ctk.CTkTextbox(self.datosPlatillos, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.texr_gananciaDelPlatillo.grid(row=1, column=7, padx=pad_col, pady=(2, 10))


        self.datosBariables = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosBariables.pack(pady=10, padx=10, fill="x")

        label16 = ctk.CTkLabel(self.datosBariables, text="Flujo de personas por dia:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label16.grid(row=0, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_FlujodePersonasPorDia = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_FlujodePersonasPorDia.grid(row=1, column=0, padx=pad_col, pady=(2, 10))

        label17 = ctk.CTkLabel(self.datosBariables, text="Prob flujo de personas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label17.grid(row=0, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_FlujodePersonasPorDia_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_FlujodePersonasPorDia_prob.grid(row=1, column=1, padx=pad_col, pady=(2, 10))

        label18 = ctk.CTkLabel(self.datosBariables, text="Promedio de grupo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label18.grid(row=0, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_TamaniodelGrupo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_TamaniodelGrupo.grid(row=1, column=2, padx=pad_col, pady=(2, 10))

        label19 = ctk.CTkLabel(self.datosBariables, text="Prob promedio de grupo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label19.grid(row=0, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_TamaniodelGrupoprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_TamaniodelGrupoprob.grid(row=1, column=3, padx=pad_col, pady=(2, 10))

        label20 = ctk.CTkLabel(self.datosBariables, text="Preparacion platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label20.grid(row=0, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.tex_preapracion_platillo = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.tex_preapracion_platillo.grid(row=1, column=4, padx=pad_col, pady=(2, 10))

        label21 = ctk.CTkLabel(self.datosBariables, text="Prob preparacion platillo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label21.grid(row=0, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.tex_preapracion_platillo_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.tex_preapracion_platillo_prob.grid(row=1, column=5, padx=pad_col, pady=(2, 10))



        label22 = ctk.CTkLabel(self.datosBariables, text="Consumo por persona:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label22.grid(row=2, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_consumoPorPersona = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_consumoPorPersona.grid(row=3, column=0, padx=pad_col, pady=(2, 10))

        label23 = ctk.CTkLabel(self.datosBariables, text="Prob consumo:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label23.grid(row=2, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_comsumoPorPersona_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_comsumoPorPersona_prob.grid(row=3, column=1, padx=pad_col, pady=(2, 10))

        label24 = ctk.CTkLabel(self.datosBariables, text="Suministro:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label24.grid(row=2, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_suministro = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_suministro.grid(row=3, column=2, padx=pad_col, pady=(2, 10))

        label25 = ctk.CTkLabel(self.datosBariables, text="Prob suministro:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label25.grid(row=2, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_suministroProb = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_suministroProb.grid(row=3, column=3, padx=pad_col, pady=(2, 10))

        label26 = ctk.CTkLabel(self.datosBariables, text="Evento de RH:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label26.grid(row=2, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoRh = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoRh.grid(row=3, column=4, padx=pad_col, pady=(2, 10))

        label76 = ctk.CTkLabel(self.datosBariables, text="Evento de RH:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label76.grid(row=2, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_penalisacionRh = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_penalisacionRh.grid(row=3, column=4, padx=pad_col, pady=(2, 10))

        label27 = ctk.CTkLabel(self.datosBariables, text="Prob evento de RH:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label27.grid(row=2, column=5, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoRh_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoRh_prob.grid(row=3, column=5, padx=pad_col, pady=(2, 10))


        label28 = ctk.CTkLabel(self.datosBariables, text="Evento aleatorios:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label28.grid(row=4, column=0, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoAle = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoAle.grid(row=5, column=0, padx=pad_col, pady=(2, 10))

        label29 = ctk.CTkLabel(self.datosBariables, text="Prob evento aleatorios:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label29.grid(row=4, column=1, padx=pad_col, pady=(10, 2), sticky="ew")

        self.text_eventoAle_prob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.text_eventoAle_prob.grid(row=5, column=1, padx=pad_col, pady=(2, 10))

        label30 = ctk.CTkLabel(self.datosBariables, text="Horas criticas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label30.grid(row=4, column=2, padx=pad_col, pady=(10, 2), sticky="ew")

        self.textHorasCriticas = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.textHorasCriticas.grid(row=5, column=2, padx=pad_col, pady=(2, 10))

        label31 = ctk.CTkLabel(self.datosBariables, text="Prob horas criticas:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label31.grid(row=4, column=3, padx=pad_col, pady=(10, 2), sticky="ew")

        self.textHorasCriticasprob = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.textHorasCriticasprob.grid(row=5, column=3, padx=pad_col, pady=(2, 10))


        label32 = ctk.CTkLabel(self.datosBariables, text="Hay hora critica:", font=("Arial", 13), text_color=color_texto, wraplength=ancho_txt)
        label32.grid(row=4, column=4, padx=pad_col, pady=(10, 2), sticky="ew")

        self.texHayhoracritica = ctk.CTkTextbox(self.datosBariables, font=("Arial", 13), width=ancho_txt, height=alto_txt)
        self.texHayhoracritica.grid(row=5, column=4, padx=pad_col, pady=(2, 10))

        self.datosmeses = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.datosmeses.pack(pady=10, padx=10, fill="x")

        lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


        for i, mes in enumerate(lista_meses):
            ctk.CTkLabel(self.datosmeses, text=f"{mes}", text_color=color_texto).grid(row=i,column=0,padx=20,pady=20)



        self.ent_enero = ctk.CTkEntry(self.datosmeses)
        self.ent_enero.grid(row=0,column=1,padx=20,pady=20)
        self.ent_febredo = ctk.CTkEntry(self.datosmeses)
        self.ent_febredo.grid(row=1,column=1,padx=20,pady=20)
        self.ent_marzo= ctk.CTkEntry(self.datosmeses)
        self.ent_marzo.grid(row=2,column=1,padx=20,pady=20)
        self.ent_abril = ctk.CTkEntry(self.datosmeses)
        self.ent_abril.grid(row=3,column=1,padx=20,pady=20)
        self.ent_mayo = ctk.CTkEntry(self.datosmeses)
        self.ent_mayo.grid(row=4,column=1,padx=20,pady=20)
        self.ent_junio = ctk.CTkEntry(self.datosmeses)
        self.ent_junio.grid(row=5,column=1,padx=20,pady=20)
        self.ent_julio = ctk.CTkEntry(self.datosmeses)
        self.ent_julio.grid(row=6,column=1,padx=20,pady=20)
        self.ent_agosto = ctk.CTkEntry(self.datosmeses)
        self.ent_agosto.grid(row=7,column=1,padx=20,pady=20)
        self.ent_septiembre = ctk.CTkEntry(self.datosmeses)
        self.ent_septiembre.grid(row=8,column=1,padx=20,pady=20)
        self.ent_ocutubre = ctk.CTkEntry(self.datosmeses)
        self.ent_ocutubre.grid(row=9,column=1,padx=20,pady=20)
        self.ent_Nobiembre = ctk.CTkEntry(self.datosmeses)
        self.ent_Nobiembre.grid(row=10,column=1,padx=20,pady=20)
        self.ent_Dicimebre= ctk.CTkEntry(self.datosmeses)
        self.ent_Dicimebre.grid(row=11,column=1,padx=20,pady=20)




        self.Botonsitos = ctk.CTkFrame(
            self.frame_scroll,
            fg_color=color_fondo,
            border_width=2,
            border_color=color_contorno_azul
        )
        self.Botonsitos.pack(pady=10, padx=10, fill="x")

        ancho_btn = 200
        alto_btn  = 55

        self.cargar = ctk.CTkButton(
            self.Botonsitos, text="Cargar elementos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.extraervalores()
        )
        self.cargar.grid(row=0, column=0, padx=20, pady=20)

        self.Baciar = ctk.CTkButton(
            self.Botonsitos, text="Vaciar",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.Bacias()
        )
        self.Baciar.grid(row=0, column=1, padx=20, pady=20)

        self.bj = ctk.CTkButton(
            self.Botonsitos, text="Valores bajos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.piloto()
        )
        self.bj.grid(row=0, column=2, padx=20, pady=20)

        self.at = ctk.CTkButton(
            self.Botonsitos, text="Valores altos",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold")
        )
        self.at.grid(row=0, column=3, padx=20, pady=20)

        self.md = ctk.CTkButton(
            self.Botonsitos, text="Valores medios",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.cargarValoresmedios()
        )
        self.md.grid(row=0, column=4, padx=20, pady=20)

        self.disparar = ctk.CTkButton(
            self.Botonsitos, text="Simular",
            width=ancho_btn, height=alto_btn,
            fg_color=color_Extra, hover_color=color_hover,
            text_color=color_texto, font=("Arial", 14, "bold"),
            command=lambda: self.piloto()
        )
        self.disparar.grid(row=0, column=6, padx=20, pady=20)

        self.cargarElementosEninterface()

    def cargarElementosEninterface(self):
        # primera parte
        self.CantidadDeCosineros.delete(0, "end")
        self.CantidadDeCosineros.insert(0, str(cantidad_de_cosineros))

        self.cantidadDeMesas.delete(0, "end")
        self.cantidadDeMesas.insert(0, str(cantidad_de_mesas))

        self.Horaslaborales.delete(0, "end")
        self.Horaslaborales.insert(0, str(horas_habiles))

        self.personal.delete(0, "end")
        self.personal.insert(0, str(personal))

        self.sueldoPersonal.delete(0, "end")
        self.sueldoPersonal.insert(0, str(sueldo_personal))

        self.SueldoCosinero.delete(0, "end")
        self.SueldoCosinero.insert(0, str(sueldo_cosineros))

        self.pagoServicios.delete(0, "end")
        self.pagoServicios.insert(0, str(pago_servicios))

        # penalisacino_por_personas_perdidas = 100
        # penalisacion_por_platillos_perdidos = 50

        self.penalisacion_personas.delete(0, "end")
        self.penalisacion_personas.insert(0, str(penalisacino_por_personas_perdidas))

        self.penalisacion_platillos.delete(0, "end")
        self.penalisacion_platillos.insert(0, str(penalisacion_por_platillos_perdidos))


        # parte 2
        self.nombreplatillos.delete("1.0", "end")
        print("Experimentos: ", platillos_disponibles)
        for platillo in platillos_disponibles:
            self.nombreplatillos.insert("end", str(platillo) + "\n")


        self.Text_categorai_platillos.delete("1.0", "end")
        for lista in categorai_platillos:
            for elemento in lista:
                self.Text_categorai_platillos.insert("end", str(elemento) + " ")
            self.Text_categorai_platillos.insert("end", "\n")


        self.Text_categorai_platillos_prob.delete("1.0", "end")
        for elemento in categorai_platillos_prob:
            self.Text_categorai_platillos_prob.insert("end", str(elemento) + "\n")

        self.txt_cantidadStock.delete("1.0", "end")
        for elemento in platillos_lista:
            self.txt_cantidadStock.insert("end", str(elemento) + "\n")

        self.txt_cantidadStock_min.delete("1.0", "end")
        for elemento in cantidadMinimaDeStock:
            self.txt_cantidadStock_min.insert("end", str(elemento) + "\n")

        self.texr_costoDelPlatillo.delete("1.0", "end")
        for elemento in ganancias_por_platillo:
            self.texr_costoDelPlatillo.insert("end", str(elemento) + "\n")

        self.texr_gananciaDelPlatillo.delete("1.0", "end")
        for elemento in ganancias_netas:
            self.texr_gananciaDelPlatillo.insert("end", str(elemento) + "\n")


        # parte 3
        self.text_FlujodePersonasPorDia.delete("1.0", "end")
        for elemento in flojo_diario:
            self.text_FlujodePersonasPorDia.insert("end", str(elemento) + "\n")

        self.text_FlujodePersonasPorDia_prob.delete("1.0", "end")
        for elemento in flujo_siario_prob:
            self.text_FlujodePersonasPorDia_prob.insert("end", str(elemento) + "\n")

        self.text_TamaniodelGrupo.delete("1.0", "end")
        for elemento in grupo:
            self.text_TamaniodelGrupo.insert("end", str(elemento) + "\n")

        self.text_TamaniodelGrupoprob.delete("1.0", "end")
        for elemento in grupo_prob:
            self.text_TamaniodelGrupoprob.insert("end", str(elemento) + "\n")

        self.tex_preapracion_platillo.delete("1.0", "end")
        for elemento in tem_preparacion:
            self.tex_preapracion_platillo.insert("end", str(elemento) + "\n")

        self.tex_preapracion_platillo_prob.delete("1.0", "end")
        for elemento in tem_preparacion_prob:
            self.tex_preapracion_platillo_prob.insert("end", str(elemento) + "\n")

        self.text_consumoPorPersona.delete("1.0", "end")
        for elemento in consumo:
            self.text_consumoPorPersona.insert("end", str(elemento) + "\n")

        self.text_comsumoPorPersona_prob.delete("1.0", "end")
        for elemento in condumo_prob:
            self.text_comsumoPorPersona_prob.insert("end", str(elemento) + "\n")

        self.text_suministro.delete("1.0", "end")
        for elemento in suministro:
            self.text_suministro.insert("end", str(elemento) + "\n")

        self.text_suministroProb.delete("1.0", "end")
        for elemento in suministro_prob:
            self.text_suministroProb.insert("end", str(elemento) + "\n")

        self.text_eventoRh.delete("1.0", "end")
        for elemento in even_rh:
            self.text_eventoRh.insert("end", str(elemento) + "\n")

        self.text_eventoRh_prob.delete("1.0", "end")
        for elemento in even_rh_prob:
            self.text_eventoRh_prob.insert("end", str(elemento) + "\n")

        self.text_eventoAle.delete("1.0", "end")
        for elemento in Evento_Ale:
            self.text_eventoAle.insert("end", str(elemento) + "\n")

        self.text_eventoAle_prob.delete("1.0", "end")
        for elemento in Evento_Ale_prob:
            self.text_eventoAle_prob.insert("end", str(elemento) + "\n")

        self.textHorasCriticas.delete("1.0", "end")
        for elemento in porcen_ora_critica:
            self.textHorasCriticas.insert("end", str(elemento) + "\n")

        self.textHorasCriticasprob.delete("1.0", "end")
        for elemento in porcen_ora_critica_prob:
            self.textHorasCriticasprob.insert("end", str(elemento) + "\n")


        # texto_crudo = self.texHayhoracritica.get("1.0", "end")
        # hora_critica_prob = [int(x) for x in texto_crudo.split()]

        self.texHayhoracritica.delete("1.0", "end")
        for elemento in hora_critica_prob:
            self.texHayhoracritica.insert("end", str(elemento) + "\n")


        self.ent_enero.delete(0, "end")
        self.ent_febredo.delete(0, "end")
        self.ent_marzo.delete(0, "end")
        self.ent_abril.delete(0, "end")
        self.ent_mayo.delete(0, "end")
        self.ent_junio.delete(0, "end")
        self.ent_julio.delete(0, "end")
        self.ent_agosto.delete(0, "end")
        self.ent_septiembre.delete(0, "end")
        self.ent_ocutubre.delete(0, "end")
        self.ent_Nobiembre.delete(0, "end")
        self.ent_Dicimebre.delete(0, "end")

        global Listamultiplciadores

        self.ent_enero.insert(0, Listamultiplciadores[0])
        self.ent_febredo.insert(0, Listamultiplciadores[1])
        self.ent_marzo.insert(0, Listamultiplciadores[2])
        self.ent_abril.insert(0, Listamultiplciadores[3])
        self.ent_mayo.insert(0, Listamultiplciadores[4])
        self.ent_junio.insert(0, Listamultiplciadores[5])
        self.ent_julio.insert(0, Listamultiplciadores[6])
        self.ent_agosto.insert(0, Listamultiplciadores[7])
        self.ent_septiembre.insert(0, Listamultiplciadores[8])
        self.ent_ocutubre.insert(0, Listamultiplciadores[9])
        self.ent_Nobiembre.insert(0, Listamultiplciadores[10])
        self.ent_Dicimebre.insert(0, Listamultiplciadores[11])



        # Listamultiplciadores 

    def extraervalores(self):
        # print("Si llega")

        global flojo_diario, flujo_siario_prob, grupo, grupo_prob, tem_preparacion, tem_preparacion_prob, consumo, condumo_prob, suministro, \
            suministro_prob, even_rh, even_rh_prob, Evento_Ale_prob, Evento_Ale, hora_critica, hora_critica_prob, porcen_ora_critica, \
            porcen_ora_critica_prob, categorai_platillos, categorai_platillos_prob, platillos_disponibles, cantidadMinimaDeStock, cantidadDelStockmaxiom, \
            penalisacino_por_personas_perdidas, penalisacion_por_platillos_perdidos, Listamultiplciadores
    
        penalisacino_por_personas_perdidas = float(self.penalisacion_personas.get())
        penalisacion_por_platillos_perdidos = float(self.penalisacion_platillos.get())

        # self.penalisacion_personas.delete(0, "end")
        # self.penalisacion_personas.insert(0, str(penalisacino_por_personas_perdidas))

        # self.penalisacion_platillos.delete(0, "end")
        # self.penalisacion_platillos.insert(0, str(penalisacion_por_platillos_perdidos))


        texto_crudo = self.text_FlujodePersonasPorDia.get("1.0", "end")
        flojo_diario = [float(x) for x in texto_crudo.split()]

        texto_crudo = self.text_FlujodePersonasPorDia_prob.get("1.0", "end")
        flujo_siario_prob = [float(x) for x in texto_crudo.split()]

        # texto_crudo = self.text_comsumoPorPersona_prob.get("1.0", "end")
        # flujo_siario_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_TamaniodelGrupo.get("1.0", "end")
        grupo = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_TamaniodelGrupoprob.get("1.0", "end")
        grupo_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.tex_preapracion_platillo.get("1.0", "end")
        tem_preparacion = [int(x) for x in texto_crudo.split()]

        #pulir
        #
        texto_crudo = self.tex_preapracion_platillo_prob.get("1.0", "end")
        tem_preparacion_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_consumoPorPersona.get("1.0", "end")
        consumo = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_comsumoPorPersona_prob.get("1.0", "end")
        condumo_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.text_suministro.get("1.0", "end")
        suministro = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_suministroProb.get("1.0", "end")
        suministro_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_eventoRh.get("1.0", "end")
        even_rh = [x for x in texto_crudo.split()]

        texto_crudo = self.text_eventoRh_prob.get("1.0", "end")
        even_rh_prob = [float(x) for x in texto_crudo.split()]


        # error
        texto_crudo = self.text_eventoAle_prob.get("1.0", "end-1c")
        Evento_Ale_prob = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.text_eventoAle.get("1.0", "end-1c")
        Evento_Ale = [x.strip() for x in texto_crudo.splitlines() if x.strip()]



        texto_crudo = self.textHorasCriticas.get("1.0", "end")
        porcen_ora_critica = [int(x) for x in texto_crudo.split()]

        # error textHorasCriticasprob
        texto_crudo = self.textHorasCriticasprob.get("1.0", "end")
        porcen_ora_critica_prob = [int(x) for x in texto_crudo.split()]


        # texto_crudo = self..get("1.0", "end")
        # porcen_ora_critica = [int(x) for x in texto_crudo.split()]

        # texto_crudo = self.tex_preapracion_platillo_prob.get("1.0", "end")
        # porcen_ora_critica_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.Text_categorai_platillos.get("1.0", "end").strip()

        categorai_platillos = []

        for linea in texto_crudo.split('\n'):
            if linea.strip():
                fila = [int(x) for x in linea.split()]
                categorai_platillos.append(fila)


        texto_crudo = self.Text_categorai_platillos_prob.get("1.0", "end")
        categorai_platillos_prob = [int(x) for x in texto_crudo.split()]


        texto_crudo = self.nombreplatillos.get("1.0", "end")
        platillos_disponibles = [x for x in texto_crudo.split()]

        texto_crudo = self.txt_cantidadStock.get("1.0", "end")
        platilllosEmpesamos = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.txt_cantidadStock_min.get("1.0", "end")
        cantidadMinimaDeStock = [int(x) for x in texto_crudo.split()]

        texto_crudo = self.txt_cantidadStock.get("1.0", "end")
        cantidadDelStockmaxiom = platilllosEmpesamos[:]

        # texHayhoracritica

        texto_crudo = self.texHayhoracritica.get("1.0", "end")
        hora_critica_prob = [int(x) for x in texto_crudo.split()]

        global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios, platillos_lista, \
            ganancias_por_platillo, ganancias_netas, Listamultiplciadores

        platillos_lista = platilllosEmpesamos[:]


        texto_crudo = self.texr_costoDelPlatillo.get("1.0", "end")
        ganancias_por_platillo = [float(x) for x in texto_crudo.split()]

        texto_crudo = self.texr_gananciaDelPlatillo.get("1.0", "end")
        ganancias_netas = [float(x) for x in texto_crudo.split()]


        cantidad_de_mesas = int(self.cantidadDeMesas.get())
        cantidad_de_cosineros = int(self.CantidadDeCosineros.get())
        sueldo_cosineros = float(self.SueldoCosinero.get())
        horas_habiles = int(self.Horaslaborales.get())
        personal = int(self.personal.get())
        sueldo_personal = float(self.sueldoPersonal.get())

        pago_servicios = float(self.pagoServicios.get())



        Listamultiplciadores[0] = float(self.ent_enero.get())
        Listamultiplciadores[1] = float(self.ent_febredo.get())
        Listamultiplciadores[2] = float(self.ent_marzo.get())
        Listamultiplciadores[3]= float(self.ent_abril.get())
        Listamultiplciadores[4]=float(self.ent_mayo.get())
        Listamultiplciadores[5]=float(self.ent_junio.get())
        Listamultiplciadores[6]=float(self.ent_julio.get())
        Listamultiplciadores[7]=float(self.ent_agosto.get())
        Listamultiplciadores[8]=float(self.ent_septiembre.get())
        Listamultiplciadores[9]=float(self.ent_ocutubre.get())
        Listamultiplciadores[10]=float(self.ent_Nobiembre.get())
        Listamultiplciadores[11]=float(self.ent_Dicimebre.get())


        Listamultiplciadores

        print("Todo salio bien")

        self.cargarElementosEninterface()


        # aniadir hora critica

    def Bacias(self):
        hora_critica_prob.clear()
        flojo_diario.clear()
        flujo_siario_prob.clear()

        grupo.clear()
        grupo_prob.clear()

        tem_preparacion.clear()
        tem_preparacion_prob.clear()

        consumo.clear()
        condumo_prob.clear()

        suministro.clear()
        suministro_prob.clear()

        even_rh.clear()
        even_rh_prob.clear()

        Evento_Ale_prob.clear()
        Evento_Ale.clear()

        hora_critica.clear()
        hora_critica_prob.clear()

        porcen_ora_critica.clear()
        porcen_ora_critica_prob.clear()

        categorai_platillos.clear()
        categorai_platillos_prob.clear()

        # otros datos
        platillos_disponibles.clear()
        platilllosEmpesamos.clear()

        cantidadMinimaDeStock.clear()
        cantidadDelStockmaxiom.clear()

        platillos_lista.clear()
        ganancias_por_platillo.clear()
        ganancias_netas.clear()

        Listamultiplciadores.clear()

        global cantidad_de_mesas, cantidad_de_cosineros, sueldo_cosineros, horas_habiles, personal, sueldo_personal, pago_servicios

        cantidad_de_mesas = 0
        cantidad_de_cosineros = 0
        sueldo_cosineros = 0
        horas_habiles = 0
        personal = 0
        sueldo_personal = 0
        pago_servicios = 0

        self.cargarElementosEninterface()

    def cargarValoresmedios(self):
        CargarMedios()

        print("Si carga")

        self.cargarElementosEninterface()

    def piloto(self):
        dias = int(self.Dias_simular.get())
        validaciones(dias)




if __name__ == "__main__":
    app = cocina()
    app.ventana.mainloop()
