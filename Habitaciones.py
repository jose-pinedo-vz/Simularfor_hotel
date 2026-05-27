'''3 corridas: estresar, Equilibrado y donde aya mucho oseo
Calcular probabilidades. por ejemplo, que probabilidadd hay de que una habitación este disponible cierto dia
ADEMAS VER QUE ME ESTA CONTESTANTO ESA SIMULACIÓN ¿Que preguntas me contesta esta simulación que estoy haciendo?'''
# Cuantas habitaciones ocupo para que todos se usen
# Probabilidad de que una habitacion este disponible cierto dia
# Cual es la habitacion o las habitaciones mas usadas
# Esta simulacion me debe de dar opciones, para la toma de desiciones

"""Se pretende simular: cada uno de los procesos que queremos simular en cada modulo"""

#AGREGAR 5 INSUMOS MINIMO, PARA GENERAR COSTOS


import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox
import random
import os
import math
from GeneraRandom import aleatorio

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Habitaciones:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Habitaciones")
        self.ventana.configure(fg_color=COLOR_FONDO)
        ancho=self.ventana.winfo_screenwidth()
        alto=self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")

        # DATOS
        self.datos_llegadas=[[0, 0.29],
                             [1, 0.30],
                             [2, 0.20],
                             [3, 0.21]]

        self.datos_tipo=[["Individual", 0.40],
                         ["Doble", 0.40],
                         ["Suite", 0.20]]

        self.datos_estancia=[[1, 0.25],
                             [2, 0.35],
                             [3, 0.25],
                             [4, 0.15]]
        
        self.datos_mantenimiento=[[0, 0.75, 0],
                                  [1, 0.20, 500],
                                  [2, 0.05, 1200]]
        
        self.datos_daños=[["Sin daños", 0.75, 0],
                          ["Sábana dañada", 0.10, 300],
                          ["Toalla dañada", 0.08, 150],
                          ["TV dañada", 0.04, 400],
                          ["Foco", 0.03, 100]]
        
        self.datos_limpieza_individual=[[20, 0.20],
                                        [30, 0.50],
                                        [40, 0.30]]

        self.datos_limpieza_doble=[[30, 0.30],
                                   [45, 0.40],
                                   [60, 0.30]]

        self.datos_limpieza_suite=[[60, 0.20],
                                   [90, 0.50],
                                   [120, 0.30]]
        
        self.datos_personas=[[1, 0.35],
                             [2, 0.40],
                             [3, 0.15],
                             [4, 0.07],
                             [5, 0.03]]
        
        self.datos_decision=[["Aceptar superior", 0.30],
                               ["Dividir grupo", 0.25],
                               ["Esperar", 0.10],
                               ["Cancelar", 0.35]]
                                
        self.reiniciar_llegadas=False
        self.reiniciar_tipo=False
        self.reiniciar_estancia=False
        self.reiniciar_mantenimiento=False
        self.reiniciar_daños=False
        self.reiniciar_limpieza_individual=False
        self.reiniciar_limpieza_doble=False
        self.reiniciar_limpieza_suite=False
        self.reiniciar_personas=False
        self.reiniciar_decision=False

       # SCROLL
        self.frame_scroll=ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # TITULO
        titulo=ctk.CTkLabel(self.frame_scroll, text="Simulación de habitaciones", text_color=COLOR_TEXTO, font=("Arial", 28, "bold", "italic"))
        titulo.pack(pady=20)

        # FRAME PRINCIPAL DATOS
        self.frame_datos=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry=180
        alto_entry=40


        self.frame_hotel=ctk.CTkFrame(self.frame_datos)
        self.frame_hotel.pack(fill="x", padx=15, pady=15)
        titulo_hotel=ctk.CTkLabel(self.frame_hotel, text="CONFIGURACIÓN DEL HOTEL", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_hotel.grid(row=0, column=0, columnspan=3, pady=15)

        ctk.CTkLabel(self.frame_hotel, text="Habitaciones individuales:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=(20, 5))
        self.entry_individuales=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_individuales.grid(row=3, column=0, padx=20, pady=(0, 20))
        self.entry_individuales.insert(0, "10")

        ctk.CTkLabel(self.frame_hotel, text="Habitaciones dobles:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=1, padx=20, pady=(20, 5))
        self.entry_dobles=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_dobles.grid(row=3, column=1, padx=20, pady=(0, 20))
        self.entry_dobles.insert(0, "8")

        ctk.CTkLabel(self.frame_hotel, text="Habitaciones suite:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=2, padx=20, pady=(20, 5))
        self.entry_suites=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_suites.grid(row=3, column=2, padx=20, pady=(0, 20))
        self.entry_suites.insert(0, "5")

        ctk.CTkLabel(self.frame_hotel, text="Capacidad Individual:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=0, padx=20, pady=(10,5))
        self.entry_cap_individual=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_cap_individual.grid(row=5, column=0, padx=20, pady=(0,20))
        self.entry_cap_individual.insert(0, "1")

        ctk.CTkLabel(self.frame_hotel, text="Capacidad Doble:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=1, padx=20, pady=(10,5))
        self.entry_cap_doble=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_cap_doble.grid(row=5, column=1, padx=20, pady=(0,20))
        self.entry_cap_doble.insert(0, "2")

        ctk.CTkLabel(self.frame_hotel, text="Capacidad Suite:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=2, padx=20, pady=(10,5))
        self.entry_cap_suite=ctk.CTkEntry(self.frame_hotel, width=ancho_entry, height=alto_entry)
        self.entry_cap_suite.grid(row=5, column=2, padx=20, pady=(0,20))
        self.entry_cap_suite.insert(0, "5")
        

        self.frame_precios=ctk.CTkFrame(self.frame_datos)
        self.frame_precios.pack(fill="x", padx=15, pady=15)
        titulo_precios=ctk.CTkLabel(self.frame_precios, text="PRECIOS DE HABITACIONES", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_precios.grid(row=0, column=0, columnspan=3, pady=15)

        # PRECIOS
        ctk.CTkLabel(self.frame_precios, text="Precio Individual:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=0, padx=20, pady=(10, 5))
        self.entry_precio_individual=ctk.CTkEntry(self.frame_precios, width=ancho_entry, height=alto_entry)
        self.entry_precio_individual.grid(row=5, column=0, padx=20, pady=(0, 20))
        self.entry_precio_individual.insert(0, "500")

        ctk.CTkLabel(self.frame_precios, text="Precio Doble:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=1, padx=20, pady=(10, 5))
        self.entry_precio_doble=ctk.CTkEntry(self.frame_precios, width=ancho_entry, height=alto_entry)
        self.entry_precio_doble.grid(row=5, column=1, padx=20, pady=(0, 20))
        self.entry_precio_doble.insert(0, "800")

        ctk.CTkLabel(self.frame_precios, text="Precio Suite:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=2, padx=20, pady=(10, 5))
        self.entry_precio_suite=ctk.CTkEntry(self.frame_precios, width=ancho_entry, height=alto_entry)
        self.entry_precio_suite.grid(row=5, column=2, padx=20, pady=(0, 20))
        self.entry_precio_suite.insert(0, "1500")


        self.frame_operacion=ctk.CTkFrame(self.frame_datos)
        self.frame_operacion.pack(fill="x", padx=15, pady=15)
        titulo_operacion=ctk.CTkLabel(self.frame_operacion, text="OPERACIÓN Y COSTOS", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_operacion.grid(row=0, column=0, columnspan=3, pady=15)

        ctk.CTkLabel(self.frame_operacion, text="Costo operativo diario:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=0, padx=20, pady=(10, 5))
        self.entry_operativo=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_operativo.grid(row=3, column=0, padx=20, pady=(0, 20))
        self.entry_operativo.insert(0, "500")

        ctk.CTkLabel(self.frame_operacion, text="Limpieza Individual:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=1, padx=20, pady=(10,5))
        self.entry_limpieza_individual=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_limpieza_individual.grid(row=3, column=1, padx=20, pady=(0,20))
        self.entry_limpieza_individual.insert(0, "80")

        ctk.CTkLabel(self.frame_operacion, text="Limpieza Doble:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=2, padx=20, pady=(10,5))
        self.entry_limpieza_doble=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_limpieza_doble.grid(row=3, column=2, padx=20, pady=(0,20))
        self.entry_limpieza_doble.insert(0, "120")

        ctk.CTkLabel(self.frame_operacion, text="Limpieza Suite:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=3, padx=20, pady=(10,5))
        self.entry_limpieza_suite=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_limpieza_suite.grid(row=3, column=3, padx=20, pady=(0,20))
        self.entry_limpieza_suite.insert(0, "200")

        ctk.CTkLabel(self.frame_operacion, text="Días a simular:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=2, column=4, padx=20, pady=(10, 5))
        self.entry_dias=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_dias.grid(row=3, column=4, padx=20, pady=(0, 20))
        self.entry_dias.insert(0, "20")

        ctk.CTkLabel(self.frame_operacion, text="Personal de limpieza:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=4, column=0, padx=20, pady=(10,5))
        self.entry_personal_limpieza=ctk.CTkEntry(self.frame_operacion, width=ancho_entry, height=alto_entry)
        self.entry_personal_limpieza.grid(row=5, column=0, padx=20, pady=(0,20))
        self.entry_personal_limpieza.insert(0, "4")


        self.frame_insumos=ctk.CTkFrame(self.frame_datos)
        self.frame_insumos.pack(fill="x", padx=15, pady=15)
        titulo_insumos=ctk.CTkLabel(self.frame_insumos, text="INSUMOS POR CLIENTE", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_insumos.grid(row=0, column=0, columnspan=3, pady=15)

        ctk.CTkLabel(self.frame_insumos, text="Jabón:", text_color=COLOR_TEXTO).grid(row=1, column=0, padx=20, pady=10)
        self.entry_jabon=ctk.CTkEntry(self.frame_insumos, width=ancho_entry, height=alto_entry)
        self.entry_jabon.grid(row=2, column=0, padx=20, pady=(0, 20))
        self.entry_jabon.insert(0, "15")

        ctk.CTkLabel(self.frame_insumos, text="Shampoo:", text_color=COLOR_TEXTO).grid(row=1, column=1, padx=20, pady=10)
        self.entry_shampoo=ctk.CTkEntry(self.frame_insumos, width=ancho_entry, height=alto_entry)
        self.entry_shampoo.grid(row=2, column=1, padx=20, pady=(0, 20))
        self.entry_shampoo.insert(0, "30")

        ctk.CTkLabel(self.frame_insumos, text="Papel higiénico:", text_color=COLOR_TEXTO).grid(row=1, column=2, padx=20, pady=10)
        self.entry_papel=ctk.CTkEntry(self.frame_insumos, width=ancho_entry, height=alto_entry)
        self.entry_papel.grid(row=2, column=2, padx=20, pady=(0, 20))
        self.entry_papel.insert(0, "10")

        ctk.CTkLabel(self.frame_insumos, text="Toallas:", text_color=COLOR_TEXTO).grid(row=1, column=3, padx=20, pady=10)
        self.entry_toallas=ctk.CTkEntry(self.frame_insumos, width=ancho_entry, height=alto_entry)
        self.entry_toallas.grid(row=2, column=3, padx=20, pady=(0, 20))
        self.entry_toallas.insert(0, "50")

        ctk.CTkLabel(self.frame_insumos, text="Agua:", text_color=COLOR_TEXTO).grid(row=1, column=4, padx=20, pady=10)
        self.entry_agua=ctk.CTkEntry(self.frame_insumos, width=ancho_entry, height=alto_entry)
        self.entry_agua.grid(row=2, column=4, padx=20, pady=(0, 20))
        self.entry_agua.insert(0, "10")


        # BOTON SIMULAR
        self.frame_simular=ctk.CTkFrame(self.frame_scroll)
        self.frame_simular.pack(fill="x", padx=20, pady=20)
        self.btn_simular=ctk.CTkButton(self.frame_simular, text="SIMULAR HOTEL", width=300, height=50, fg_color="#D6C49E", text_color="#000000", font=("Arial", 18, "bold"), command=self.simular)
        self.btn_simular.pack(pady=20)

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_ingresos=ctk.CTkLabel(self.frame_kpis, text="Ingresos Totales: $0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_costos=ctk.CTkLabel(self.frame_kpis, text="Costos Totales: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_costos.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ganancias=ctk.CTkLabel(self.frame_kpis, text="Ganancia Neta: $0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_ganancias.grid(row=0, column=2, padx=40, pady=30)

        # BOTONES
        self.frame_botones=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_botones.pack(fill="x", padx=20, pady=20)

        botones=[("Limpiar", self.limpiar),
                 ("Sistema estresado", self.sistema_estresado),
                 ("Sistema equilibrado", self.sistema_equilibrado),
                 ("Siatema con oseo", self.sistema_oseo)]
        
        for i, (texto, comando) in enumerate(botones):
            boton=ctk.CTkButton(self.frame_botones, text=texto, width=180, height=40, fg_color="#FFBF42", text_color="#000000", command=comando)
            boton.grid(row=0, column=i, padx=20, pady=30)

        # FRAME PROBABILIDADES
        self.frame_probabilidades=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_probabilidades.pack(fill="x", padx=20, pady=20)

        titulo_prob=ctk.CTkLabel(self.frame_probabilidades, text="TABLAS DE PROBABILIDAD", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
        titulo_prob.pack(pady=20)

        self.contenedor=ctk.CTkFrame(self.frame_probabilidades, fg_color="transparent")
        self.contenedor.pack(padx=20, pady=20)

        self.crear_tabla("Llegadas por día", "Clientes", self.datos_llegadas, 0)

        self.crear_tabla("Llegadas en grupo", "Personas", self.datos_personas, 1)

        self.crear_tabla("Tipo de habitación", "Tipo", self.datos_tipo, 2)

        self.crear_tabla("Duración de estancia", "Noches", self.datos_estancia, 3)

        self.crear_tabla("Decisión del cliente", "Decisión", self.datos_decision, 4)

        self.crear_tabla("Daños en habitación", "Daño", self.datos_daños, 5)

        self.crear_tabla("Mantenimiento extra", "Dias fuera", self.datos_mantenimiento, 6)

        self.crear_tabla("Tiempo limpieza Individual", "Minutos I", self.datos_limpieza_individual, 7)

        self.crear_tabla("Tiempo limpieza Doble", "Minutos D", self.datos_limpieza_doble, 8)

        self.crear_tabla("Tiempo limpieza Suite", "Minutos S", self.datos_limpieza_suite, 9)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        self.ventana.mainloop()

    def limpiar(self):
        self.entry_individuales.delete(0, "end")
        self.entry_dobles.delete(0, "end")
        self.entry_suites.delete(0, "end")
        self.entry_operativo.delete(0, "end")
        self.entry_limpieza_individual.delete(0, "end")
        self.entry_limpieza_doble.delete(0, "end")
        self.entry_limpieza_suite.delete(0, "end")
        self.entry_dias.delete(0, "end")
        self.entry_precio_individual.delete(0, "end")
        self.entry_precio_doble.delete(0, "end")
        self.entry_precio_suite.delete(0, "end")

        self.lbl_ingresos.configure(text="Ingresos Totales: $0")

        self.lbl_costos.configure(text="Costos Totales: $0")

        self.lbl_ganancias.configure(text="Ganancia Neta: $0")

        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        messagebox.showinfo("Correcto", "Datos limpiados")

    def sistema_estresado(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "5")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "3")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "2")

        self.entry_operativo.delete(0, "end")
        self.entry_operativo.insert(0, "200")

        self.entry_limpieza_individual.delete(0, "end")
        self.entry_limpieza_individual.insert(0, "50")

        self.entry_limpieza_doble.delete(0, "end")
        self.entry_limpieza_doble.insert(0, "80")

        self.entry_limpieza_suite.delete(0, "end")
        self.entry_limpieza_suite.insert(0, "120")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "10")

        self.entry_precio_individual.delete(0, "end")
        self.entry_precio_individual.insert(0, "400")

        self.entry_precio_doble.delete(0, "end")
        self.entry_precio_doble.insert(0, "700")

        self.entry_precio_suite.delete(0, "end")
        self.entry_precio_suite.insert(0, "1200")
    
    def sistema_equilibrado(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "10")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "8")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "5")

        self.entry_operativo.delete(0, "end")
        self.entry_operativo.insert(0, "400")

        self.entry_limpieza_individual.delete(0, "end")
        self.entry_limpieza_individual.insert(0, "100")

        self.entry_limpieza_doble.delete(0, "end")
        self.entry_limpieza_doble.insert(0, "150")

        self.entry_limpieza_suite.delete(0, "end")
        self.entry_limpieza_suite.insert(0, "200")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "20")

        self.entry_precio_individual.delete(0, "end")
        self.entry_precio_individual.insert(0, "500")

        self.entry_precio_doble.delete(0, "end")
        self.entry_precio_doble.insert(0, "800")

        self.entry_precio_suite.delete(0, "end")
        self.entry_precio_suite.insert(0, "1500")
    
    def sistema_oseo(self):
        self.entry_individuales.delete(0, "end")
        self.entry_individuales.insert(0, "25")

        self.entry_dobles.delete(0, "end")
        self.entry_dobles.insert(0, "20")

        self.entry_suites.delete(0, "end")
        self.entry_suites.insert(0, "10")

        self.entry_operativo.delete(0, "end")
        self.entry_operativo.insert(0, "600")

        self.entry_limpieza_individual.delete(0, "end")
        self.entry_limpieza_individual.insert(0, "120")

        self.entry_limpieza_doble.delete(0, "end")
        self.entry_limpieza_doble.insert(0, "200")

        self.entry_limpieza_suite.delete(0, "end")
        self.entry_limpieza_suite.insert(0, "250")

        self.entry_dias.delete(0, "end")
        self.entry_dias.insert(0, "50")

        self.entry_precio_individual.delete(0, "end")
        self.entry_precio_individual.insert(0, "900")

        self.entry_precio_doble.delete(0, "end")
        self.entry_precio_doble.insert(0, "1800")

        self.entry_precio_suite.delete(0, "end")
        self.entry_precio_suite.insert(0, "3500")

    # CREAR TABLAS
    def crear_tabla(self, titulo, encabezado, datos, fila):
        frame=ctk.CTkFrame(self.contenedor)
        frame.grid(row=fila, column=0, padx=20, pady=20)

        ctk.CTkLabel(frame, text=titulo, text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
        entrada1=ctk.CTkEntry(frame, width=150, placeholder_text=encabezado)
        entrada1.pack(pady=5)
        entrada2=ctk.CTkEntry(frame, width=150, placeholder_text="Probabilidad")
        entrada2.pack(pady=5)

        if encabezado=="Daño" or encabezado=="Dias fuera":
            entrada3=ctk.CTkEntry(frame, width=150, placeholder_text="Costo")
            entrada3.pack(pady=5)

        if encabezado=="Daño" or encabezado=="Dias fuera":
            boton=ctk.CTkButton(frame, text="Agregar", command=lambda: self.agregar_daño(entrada1, entrada2, entrada3, datos, frame))

        else:
            boton=ctk.CTkButton(frame, text="Agregar", command=lambda: self.agregar_dato(entrada1, entrada2, datos, encabezado, frame))

        boton.pack(pady=10)

        tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
        tabla.pack(padx=10, pady=10)

        if encabezado=="Clientes":
            self.tabla_llegadas=tabla

        elif encabezado=="Tipo":
            self.tabla_tipo=tabla

        elif encabezado=="Noches":
            self.tabla_estancia=tabla

        elif encabezado=="Dias fuera":
            self.tabla_mantenimiento=tabla

        elif encabezado=="Daño":
            self.tabla_daños=tabla

        elif encabezado=="Personas":
            self.tabla_personas=tabla

        elif encabezado=="Decisión":
            self.tabla_decision=tabla

        elif encabezado=="Minutos I":
            self.tabla_limpieza_individual=tabla

        elif encabezado=="Minutos D":
            self.tabla_limpieza_doble=tabla

        elif encabezado=="Minutos S":
            self.tabla_limpieza_suite=tabla

    # CALCULAR TABLA
    def calcular_tabla(self, datos, encabezado):
        if encabezado=="Daño" or encabezado=="Dias fuera":
            tabla=[[encabezado, "Probabilidad", "Prob. Acumulada", "Rango", "Costo"]]

        else:
            tabla=[[encabezado, "Probabilidad", "Prob. Acumulada", "Rango"]]

        acumulada=0
        for i, fila in enumerate(datos):
            valor=fila[0]
            prob=fila[1]
            inicio=acumulada
            acumulada+=prob

            if i==0:
                rango=(f"0.0000 - {acumulada:.4f}")
            else:
                rango=(f"{inicio + 0.0001:.4f} - {acumulada:.4f}")

            if encabezado=="Daño" or encabezado=="Dias fuera":
                costo=fila[2]
                tabla.append([valor, f"{prob:.4f}", f"{acumulada:.4f}", rango, f"${costo}"])

            else:
                tabla.append([valor, f"{prob:.4f}", f"{acumulada:.4f}", rango])

        return tabla

    # AGREGAR DATOS
    def agregar_dato(self, entrada1, entrada2, datos, encabezado, frame):
        try:
            valor=entrada1.get().strip()
            prob=entrada2.get().strip()

            if valor=="" or prob=="":
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            prob=float(prob)
            if prob<=0 or prob>1:
                messagebox.showerror("Error", "Probabilidad inválida")
                return

            try:
                valor=int(valor)
            except:
                pass

            suma=0
            for fila in datos:
                suma=suma + fila[1]

            suma=round(suma, 4)
            if suma==1:
                if encabezado=="Clientes":
                    if self.reiniciar_llegadas==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_llegadas=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_llegadas=False

                elif encabezado=="Tipo":
                    if self.reiniciar_tipo==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_tipo=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_tipo=False

                elif encabezado=="Noches":
                    if self.reiniciar_estancia==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_estancia=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_estancia=False

                elif encabezado=="Daño":
                    if self.reiniciar_daños==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_daños=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_daños=False

                elif encabezado=="Personas":
                    if self.reiniciar_personas==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_personas=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_personas=False

                elif encabezado=="Decisión":
                    if self.reiniciar_decision==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_decision=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_decision=False

                else:
                    if self.reiniciar_mantenimiento==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                        self.reiniciar_mantenimiento=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_mantenimiento=False

            for fila in datos:
                if fila[0]==valor:
                    messagebox.showerror("Error", "Ese valor ya existe")
                    return

            datos.append([valor, prob])

            nueva_suma=0
            for fila in datos:
                nueva_suma=nueva_suma + fila[1]
            nueva_suma=round(nueva_suma, 4)

            if nueva_suma>1:
                datos.pop()
                messagebox.showerror("Error", "La suma de probabilidades no puede superar 1")
                return

            try:
                datos.sort()
            except:
                pass

            if encabezado=="Clientes":
                self.tabla_llegadas.destroy()

            elif encabezado=="Tipo":
                self.tabla_tipo.destroy()

            elif encabezado=="Noches":
                self.tabla_estancia.destroy()

            elif encabezado=="Costo":
                self.tabla_mantenimiento.destroy()

            elif encabezado=="Daño":
                self.tabla_daños.destroy()

            elif encabezado=="Personas":
                self.tabla_personas.destroy()

            elif encabezado=="Decisión":
                self.tabla_decision.destroy()

            elif encabezado=="Minutos I":
                self.tabla_limpieza_individual.destroy()

            elif encabezado=="Minutos D":
                self.tabla_limpieza_doble.destroy()

            elif encabezado=="Minutos S":
                self.tabla_limpieza_suite.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Clientes":
                self.tabla_llegadas=nueva_tabla

            elif encabezado=="Tipo":
                self.tabla_tipo=nueva_tabla

            elif encabezado=="Noches":
                self.tabla_estancia=nueva_tabla

            elif encabezado=="Costo":
                self.tabla_mantenimiento=nueva_tabla

            elif encabezado=="Daño":
                self.tabla_daños=nueva_tabla

            elif encabezado=="Personas":
                self.tabla_personas=nueva_tabla

            elif encabezado=="Decisión":
                self.tabla_decision=nueva_tabla

            elif encabezado=="Minutos I":
                self.tabla_limpieza_individual=nueva_tabla

            elif encabezado=="Minutos D":
                self.tabla_limpieza_doble=nueva_tabla

            elif encabezado=="Minutos S":
                self.tabla_limpieza_suite=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")

            if nueva_suma==1:
                messagebox.showinfo("Correcto", "La tabla ya suma 1")

        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def agregar_daño(self, entrada1, entrada2, entrada3, datos, frame):
        try:
            daño=entrada1.get().strip()
            prob=float(entrada2.get().strip())
            costo=float(entrada3.get().strip())

            if daño=="":
                messagebox.showerror("Error", "Daño vacío")
                return

            suma=0
            for fila in datos:
                suma+=fila[1]

            suma=round(suma, 4)

            if suma==1:
                if self.reiniciar_daños==False:
                    messagebox.showwarning("Advertencia", "La tabla ya suma 1\nSi agregas otro dato se reiniciará")
                    self.reiniciar_daños=True
                    return

                else:
                    datos.clear()
                    self.reiniciar_daños=False

            for fila in datos:
                if fila[0]==daño:
                    messagebox.showerror("Error", "Ese daño ya existe")
                    return

            datos.append([daño, prob, costo])

            nueva_suma=0
            for fila in datos:
                nueva_suma+=fila[1]

            nueva_suma=round(nueva_suma, 4)

            if nueva_suma>1:
                datos.pop()
                messagebox.showerror("Error", "La suma de probabilidades no puede superar 1")
                return

            self.tabla_daños.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, "Daño"))
            nueva_tabla.pack(padx=10, pady=10)

            self.tabla_daños=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")
            entrada3.delete(0, "end")

            if nueva_suma==1:
                messagebox.showinfo("Correcto", "La tabla ya suma 1")

        except:
            messagebox.showerror("Error", "Datos inválidos")
    
    # CREAR HOTEL
    def crear_hotel(self):
        try:
            individuales=int(self.entry_individuales.get())
            dobles=int(self.entry_dobles.get())
            suites=int(self.entry_suites.get())

            if individuales < 0 or dobles < 0 or suites < 0:
                messagebox.showerror("Error", "Las habitaciones no pueden ser negativas")
                return False

            if individuales + dobles + suites == 0:
                messagebox.showerror("Error", "Debe existir al menos una habitación")
                return False
            
            if self.entry_cap_individual.get().strip()=="":
                messagebox.showerror("Error", "Capacidad individual vacía")
                return False

            if self.entry_cap_doble.get().strip()=="":
                messagebox.showerror("Error", "Capacidad doble vacía")
                return False

            if self.entry_cap_suite.get().strip()=="":
                messagebox.showerror("Error", "Capacidad suite vacía")
                return False

            self.capacidad={"Individual": int(self.entry_cap_individual.get()),
                            "Doble": int(self.entry_cap_doble.get()),
                            "Suite": int(self.entry_cap_suite.get())}

            self.habitaciones_individuales={}
            self.habitaciones_dobles={}
            self.habitaciones_suite={}

            #INDIVIDUALES
            for i in range(1, individuales + 1):
                nombre="I" + str(i)
                self.habitaciones_individuales[nombre]={"ocupada_hasta":0,
                                                        "limpieza_hasta":0,
                                                        "mantenimiento_hasta":0}

            #DOBLES
            for i in range(1, dobles + 1):
                nombre="D" + str(i)
                self.habitaciones_dobles[nombre]={"ocupada_hasta":0,
                                                  "limpieza_hasta":0,
                                                  "mantenimiento_hasta":0}

            #SUITES
            for i in range(1, suites + 1):
                nombre="S" + str(i)
                self.habitaciones_suite[nombre]={"ocupada_hasta":0,
                                                 "limpieza_hasta":0,
                                                 "mantenimiento_hasta":0}

            #CLIENTES
            self.clientes=[]

            #USO DE HABITACIONES
            self.uso_habitaciones={}

            return True

        except:
            messagebox.showerror("Error", "No se pudo crear el hotel")

    #ASIGNAR HABITACIÓN
    def asignar_habitacion(self, tipo, dia_actual, noches):
        # INDIVIDUALES
        if tipo=="Individual":
            for habitacion in self.habitaciones_individuales:
                datos=self.habitaciones_individuales[habitacion]
                if (datos["ocupada_hasta"] <= dia_actual and datos["limpieza_hasta"] <= dia_actual and datos["mantenimiento_hasta"] <= dia_actual):
                    datos["ocupada_hasta"]=dia_actual + noches
                    return habitacion

        # DOBLES
        elif tipo=="Doble":
            for habitacion in self.habitaciones_dobles:
                datos=self.habitaciones_dobles[habitacion]
                if (datos["ocupada_hasta"] <= dia_actual and datos["limpieza_hasta"] <= dia_actual and datos["mantenimiento_hasta"] <= dia_actual):
                    datos["ocupada_hasta"]=dia_actual + noches
                    return habitacion

        # SUITES
        elif tipo=="Suite":
            for habitacion in self.habitaciones_suite:
                datos=self.habitaciones_suite[habitacion]
                if (datos["ocupada_hasta"] <= dia_actual and datos["limpieza_hasta"] <= dia_actual and datos["mantenimiento_hasta"] <= dia_actual):
                    datos["ocupada_hasta"]=dia_actual + noches
                    return habitacion

        return None

    #LIBERAR HABITACIONES
    def liberar_habitaciones(self, dia_actual):
        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            datos=self.habitaciones_individuales[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                datos["ocupada_hasta"]=0
            if datos["limpieza_hasta"]<=dia_actual:
                datos["limpieza_hasta"]=0
            if datos["mantenimiento_hasta"]<=dia_actual:
                datos["mantenimiento_hasta"]=0

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            datos=self.habitaciones_dobles[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                datos["ocupada_hasta"]=0
            if datos["limpieza_hasta"]<=dia_actual:
                datos["limpieza_hasta"]=0
            if datos["mantenimiento_hasta"]<=dia_actual:
                datos["mantenimiento_hasta"]=0

        # SUITES
        for habitacion in self.habitaciones_suite:
            datos=self.habitaciones_suite[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                datos["ocupada_hasta"]=0
            if datos["limpieza_hasta"]<=dia_actual:
                datos["limpieza_hasta"]=0
            if datos["mantenimiento_hasta"]<=dia_actual:
                datos["mantenimiento_hasta"]=0

    # CONTAR OCUPADAS
    def contar_ocupadas(self, dia_actual):
        ocupadas_individual=0
        ocupadas_dobles=0
        ocupadas_suite=0

        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            datos=self.habitaciones_individuales[habitacion]
            if datos["ocupada_hasta"]>dia_actual:
                ocupadas_individual=ocupadas_individual + 1

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            datos=self.habitaciones_dobles[habitacion]
            if datos["ocupada_hasta"]>dia_actual:
                ocupadas_dobles=ocupadas_dobles + 1

        # SUITES
        for habitacion in self.habitaciones_suite:
            datos=self.habitaciones_suite[habitacion]
            if datos["ocupada_hasta"]>dia_actual:
                ocupadas_suite=ocupadas_suite + 1

        return ocupadas_individual, ocupadas_dobles, ocupadas_suite

    # CONTAR DISPONIBLES
    def contar_disponibles(self, dia_actual):
        disponibles_individual=0
        disponibles_dobles=0
        disponibles_suite=0

        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            datos=self.habitaciones_individuales[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                disponibles_individual=disponibles_individual + 1

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            datos=self.habitaciones_dobles[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                disponibles_dobles=disponibles_dobles + 1

        # SUITES
        for habitacion in self.habitaciones_suite:
            datos=self.habitaciones_suite[habitacion]
            if datos["ocupada_hasta"]<=dia_actual:
                disponibles_suite=disponibles_suite + 1

        return disponibles_individual, disponibles_dobles, disponibles_suite
    
    # CONTAR SALIDAS
    def contar_salidas(self, dia_actual):
        salidas=0

        # INDIVIDUALES
        for habitacion in self.habitaciones_individuales:
            datos=self.habitaciones_individuales[habitacion]
            if datos["ocupada_hasta"]==dia_actual:
                salidas=salidas + 1

        # DOBLES
        for habitacion in self.habitaciones_dobles:
            datos=self.habitaciones_dobles[habitacion]
            if datos["ocupada_hasta"]==dia_actual:
                salidas=salidas + 1
                
        # SUITES
        for habitacion in self.habitaciones_suite:
            datos=self.habitaciones_suite[habitacion]
            if datos["ocupada_hasta"]==dia_actual:
                salidas=salidas + 1
        return salidas
        
    # BUSCAR RESULTADO
    def buscar_resultado(self, numero, datos):
        acumulada = 0
        for fila in datos:
            valor = fila[0]
            probabilidad = fila[1]
            acumulada += probabilidad
            if numero <= acumulada:
                return valor
            
    # VALIDAR TABLAS
    def validar_tablas(self):
        suma_llegadas=0
        for fila in self.datos_llegadas:
            suma_llegadas+=fila[1]

        suma_tipo=0
        for fila in self.datos_tipo:
            suma_tipo+=fila[1]
        
        suma_estancia=0
        for fila in self.datos_estancia:
            suma_estancia+=fila[1]

        suma_mantenimiento=0
        for fila in self.datos_mantenimiento:
            suma_mantenimiento+=fila[1]

        suma_personas=0
        for fila in self.datos_personas:
            suma_personas+=fila[1]

        suma_decision=0
        for fila in self.datos_decision:
            suma_decision+=fila[1]

        suma_limpieza_i=0
        for fila in self.datos_limpieza_individual:
            suma_limpieza_i+=fila[1]

        suma_limpieza_d=0
        for fila in self.datos_limpieza_doble:
            suma_limpieza_d+=fila[1]

        suma_limpieza_s=0
        for fila in self.datos_limpieza_suite:
            suma_limpieza_s+=fila[1]

        suma_daños=0
        for fila in self.datos_daños:
            suma_daños+=fila[1]

        suma_llegadas=round(suma_llegadas, 4)
        suma_tipo=round(suma_tipo, 4)
        suma_estancia=round(suma_estancia, 4)
        suma_mantenimiento=round(suma_mantenimiento, 4)
        suma_personas=round(suma_personas, 4)
        suma_decision=round(suma_decision, 4)
        suma_limpieza_i=round(suma_limpieza_i, 4)
        suma_limpieza_d=round(suma_limpieza_d, 4)
        suma_limpieza_s=round(suma_limpieza_s, 4)
        suma_daños=round(suma_daños, 4)

        if suma_llegadas!=1:
            messagebox.showerror("Error", "La tabla de llegadas debe sumar 1")
            return False

        if suma_tipo!=1:
            messagebox.showerror("Error", "La tabla de tipos debe sumar 1")
            return False

        if suma_estancia!=1:
            messagebox.showerror("Error", "La tabla de estancia debe sumar 1")
            return False
        
        if suma_mantenimiento!=1:
            messagebox.showerror("Error", "La tabla de mantenimiento debe sumar 1")
            return False
        
        if suma_personas!=1:
            messagebox.showerror("Error", "Tabla personas debe sumar 1")
            return False
        
        if suma_decision!=1:
            messagebox.showerror("Error", "Tabla de desicion debe sumar 1")
            return False
        
        if suma_limpieza_i!=1:
            messagebox.showerror("Error", "Tabla de tiempo limpieza individual debe sumar 1")
            return False
        
        if suma_limpieza_d!=1:
            messagebox.showerror("Error", "Tabla de tiempo limpieza doble debe sumar 1")
            return False
        
        if suma_limpieza_s!=1:
            messagebox.showerror("Error", "Tabla de tiempo de limpieza suite debe sumar 1")
            return False
        
        if suma_daños!=1:
            messagebox.showerror("Error", "Tabla de daños debe sumar 1")
            return False

        return True
    
    def obtener_temporada(self, dia):
        ciclo=dia % 30
        if ciclo==0:
            ciclo=30

        #TEMPORADA BAJA
        if ciclo>=1 and ciclo<=10:
            return "Baja", {"factor_llegadas": 0.7,
                            "factor_precio": 0.8}

        #TEMPORADA MEDIA
        elif ciclo>=11 and ciclo<=20:
            return "Media", {"factor_llegadas": 1.0,
                             "factor_precio": 1.0}

        # TEMPORADA ALTA
        else:
            return "Alta", {"factor_llegadas": 1.5,
                            "factor_precio": 1.4}

    # SIMULACIÓN
    def simular(self):
        try:
            # VALIDAR TABLAS
            if self.validar_tablas()==False:
                return

            # CREAR HOTEL
            if self.crear_hotel()==False:
                return

            # ENTRADAS
            dias=int(self.entry_dias.get())
            costo_operativo=float(self.entry_operativo.get())
            limpieza_individual=float(self.entry_limpieza_individual.get())
            limpieza_doble=float(self.entry_limpieza_doble.get())
            limpieza_suite=float(self.entry_limpieza_suite.get())
            personal=int(self.entry_personal_limpieza.get())
            
            if dias<=0:
                messagebox.showerror("Error", "Los días deben ser mayores a 0")
                return

            if costo_operativo<0 or limpieza_individual<0 or limpieza_doble<0 or limpieza_suite<0:
                messagebox.showerror("Error", "Los costos no pueden ser negativos")
                return
            if personal<=0:
                messagebox.showerror("Error", "El personal debe ser mayor a 0")
                return

            # PRECIOS
            precio_individual=float(self.entry_precio_individual.get())
            precio_doble=float(self.entry_precio_doble.get())
            precio_suite=float(self.entry_precio_suite.get())

            costo_jabon=float(self.entry_jabon.get())
            costo_shampoo=float(self.entry_shampoo.get())
            costo_papel=float(self.entry_papel.get())
            costo_toallas=float(self.entry_toallas.get())
            costo_agua=float(self.entry_agua.get())

            if precio_individual<=0 or precio_doble<=0 or precio_suite<=0:
                messagebox.showerror("Error", "Los precios deben ser mayores a 0")
                return

            precios={"Individual":precio_individual,
                     "Doble":precio_doble,
                     "Suite":precio_suite}


            indice=random.randint(1, 9000)
            print("indice", indice)
            # TABLAS
            tabla_llegadas=[["Día", "Temporada", "Aleatorio", "Llegadas"]]

            tabla_clientes=[["Día", "Cliente", "Aleatorio personas", "Personas", "Aleatorio Tipo", "Tipo", "Habitación", "Estado", "Aleatorio Estancia", "Noches", "Salida"]]
            
            tabla_ocupacion=[["Día", "Ocupadas I", "Ocupadas D", "Ocupadas S", "Disponibles I", "Disponibles D", "Disponibles S", "% Ocupación"]]

            tabla_costos=[["Día", "Salidas", "Costo Limpieza", "Costo Daños", "Aleatorio Mantenimiento", "Mantenimiento Extra", "Costo Total"]]

            tabla_finanzas=[["Día", "Ingresos", "Costos", "Ganancia"]]

            tabla_resumen=[["Indicador", "Valor"]]

            tabla_analisis=[["Sección", "Análisis"]]

            ingresos_totales=0
            costos_totales=0
            ganancias_totales=0

            clientes_totales=0
            clientes_rechazados=0

            cliente_global=1

            total_habitaciones=(len(self.habitaciones_individuales) + len(self.habitaciones_dobles) + len(self.habitaciones_suite))

            suma_ocupacion=0
            habitaciones_disponibles_totales=0
            demanda_tipos = {"Individual":0,
                             "Doble":0,
                             "Suite":0}
            
            suma_disponibles_i=0
            suma_disponibles_d=0
            suma_disponibles_s=0
            
            ocupacion_i_total=0
            ocupacion_d_total=0
            ocupacion_s_total=0

            tiempo_limpieza_total=0

            detalles_daños={}

            # DÍAS
            for dia in range(1, dias + 1):
                # SALIDAS
                salidas=self.contar_salidas(dia)

                # COSTO LIMPIEZA
                costo_limpieza=0
                costo_daños=0

                detalles_daños[dia]=[]
                for cliente in self.clientes:
                    if cliente["Salida"]==dia:
                        habitacion=cliente["Habitacion"]
                        if habitacion.startswith("I"):
                            alea_tiempo=aleatorio(indice)
                            indice+=1
                            tiempo=self.buscar_resultado(alea_tiempo, self.datos_limpieza_individual)

                        elif habitacion.startswith("D"):
                            alea_tiempo=aleatorio(indice)
                            indice+=1
                            tiempo=self.buscar_resultado(alea_tiempo, self.datos_limpieza_doble)

                        else:
                            alea_tiempo=aleatorio(indice)
                            indice+=1
                            tiempo=self.buscar_resultado(alea_tiempo, self.datos_limpieza_suite)

                        tiempo_limpieza_total+=tiempo

                        # MINUTOS A DÍAS
                        dias_limpieza=tiempo / (personal * 480)
                        if tiempo>(personal * 480):
                            dias_limpieza=math.ceil(dias_limpieza)
                        else:
                            dias_limpieza=0

                        # BLOQUEAR HABITACIÓN POR LIMPIEZA
                        if habitacion.startswith("I"):
                            self.habitaciones_individuales[habitacion]["limpieza_hasta"]=dia + dias_limpieza

                        elif habitacion.startswith("D"):
                            self.habitaciones_dobles[habitacion]["limpieza_hasta"]=dia + dias_limpieza

                        elif habitacion.startswith("S"):
                            self.habitaciones_suite[habitacion]["limpieza_hasta"]=dia + dias_limpieza

                        #DAÑOS EN CADA SALIDA
                        alea_daño=aleatorio(indice)
                        indice+=1
                        daño=self.buscar_resultado(alea_daño, self.datos_daños)
                        costo_daño_individual=0
                        for fila in self.datos_daños:
                            if fila[0]==daño:
                                costo_daño_individual=fila[2]
                        detalles_daños[dia].append([round(alea_daño,4), daño, costo_daño_individual])
                        
                        for fila in self.datos_daños:
                            if fila[0]==daño:
                                costo_daños+=fila[2]

                        habitacion=cliente["Habitacion"]
                        if habitacion.startswith("I"):
                            costo_limpieza+=limpieza_individual
                        elif habitacion.startswith("D"):
                            costo_limpieza+=limpieza_doble
                        elif habitacion.startswith("S"):
                            costo_limpieza+=limpieza_suite

                # LIBERAR HABITACIONES
                self.liberar_habitaciones(dia)

                # ALEATORIO LLEGADAS
                alea_llegadas=aleatorio(indice)

                indice=indice + 1

                # LLEGADAS
                llegadas=self.buscar_resultado(alea_llegadas, self.datos_llegadas)
                temporada, datos_temporada = self.obtener_temporada(dia)
                factor_llegadas=datos_temporada["factor_llegadas"]
                llegadas=round(llegadas * factor_llegadas)
                if llegadas<0:
                    llegadas=0

                tabla_llegadas.append([dia, temporada, alea_llegadas, llegadas])

                                      
                ingresos_dia=0
                costo_insumos_dia=0
                # CLIENTES
                for cliente in range(1, llegadas + 1):
                    clientes_totales=clientes_totales + 1

                    # ALEATORIO TIPO
                    alea_tipo=aleatorio(indice)
                    indice=indice + 1
                    tipo=self.buscar_resultado(alea_tipo, self.datos_tipo)
                    demanda_tipos[tipo] += 1

                    alea_personas=aleatorio(indice)
                    indice=indice + 1
                    personas=self.buscar_resultado(alea_personas, self.datos_personas)

                    # VALIDAR CAPACIDAD
                    if personas>self.capacidad[tipo]:
                        if tipo=="Individual":
                            tipo="Doble"
                            if personas > self.capacidad[tipo]:
                                tipo="Suite"
                        elif tipo=="Doble":
                            tipo="Suite"

                    # ALEATORIO ESTANCIA
                    alea_estancia=aleatorio(indice)
                    indice=indice + 1
                    noches=self.buscar_resultado(alea_estancia, self.datos_estancia)

                    # ASIGNAR HABITACIÓN
                    habitacion=self.asignar_habitacion(tipo, dia, noches)
                    if habitacion==None:
                        alea_decision=aleatorio(indice)
                        indice+=1
                        decision=self.buscar_resultado(alea_decision, self.datos_decision)

                        if decision=="Aceptar superior":
                            if tipo=="Individual":
                                tipo_superior="Doble"

                            elif tipo=="Doble":
                                tipo_superior="Suite"

                            else:
                                tipo_superior=None

                            if tipo_superior!=None:
                                habitacion=self.asignar_habitacion(tipo_superior, dia, noches)

                                if habitacion!=None:
                                    tipo=tipo_superior

                        if habitacion==None:
                            habitacion="-"

                    # SI HAY HABITACIÓN
                    if habitacion!="-":
                        if habitacion not in self.uso_habitaciones:
                            self.uso_habitaciones[habitacion]=0

                        self.uso_habitaciones[habitacion] += 1

                        costo_insumos_cliente=costo_jabon + costo_shampoo + costo_papel + costo_toallas + costo_agua
                        costo_insumos_cliente *= personas * noches
                        costo_insumos_dia += costo_insumos_cliente

                        estado="Aceptado"
                        salida=dia + noches
                        factor_precio=datos_temporada["factor_precio"]
                        precio_temporada=precios[tipo] * factor_precio
                        ingreso=precio_temporada * noches
                        ingresos_dia=ingresos_dia + ingreso
                        self.clientes.append({"Cliente":cliente_global,
                                              "Habitacion":habitacion,
                                              "Entrada":dia,
                                              "Salida":salida,
                                              "Personas":personas,
                                              "Tipo":tipo,
                                              "Noches":noches})

                    else:
                        estado="Rechazado"
                        salida="-"
                        ingreso=0
                        clientes_rechazados=clientes_rechazados + 1

                    # TABLA CLIENTES
                    if salida=="-":
                        texto_salida="-"
                    else:
                        texto_salida="Día " + str(salida)

                    tabla_clientes.append([dia, cliente_global, alea_personas ,personas, alea_tipo, tipo, habitacion, estado, alea_estancia, noches, texto_salida])
                    cliente_global=cliente_global + 1

                # MANTENIMIENTO
                alea_mantenimiento=aleatorio(indice)
                indice+=1

                dias_fuera=self.buscar_resultado(alea_mantenimiento, self.datos_mantenimiento)

                costo_mantenimiento=0
                for fila in self.datos_mantenimiento:
                    if fila[0]==dias_fuera:
                        costo_mantenimiento=fila[2]
                        break

                # SI OCURRE MANTENIMIENTO
                if dias_fuera>0:
                    habitaciones_disponibles=[]
                    # INDIVIDUALES
                    for numero, datos in self.habitaciones_individuales.items():
                        if (datos["ocupada"]==False and dia>=datos["limpieza_hasta"] and dia>=datos["mantenimiento_hasta"]):
                            habitaciones_disponibles.append(("Individual", numero, datos))

                    # DOBLES
                    for numero, datos in self.habitaciones_dobles.items():
                        if (datos["ocupada"]==False and dia>=datos["limpieza_hasta"] and dia>=datos["mantenimiento_hasta"]):
                            habitaciones_disponibles.append(("Doble", numero, datos))

                    # SUITES
                    for numero, datos in self.habitaciones_suite.items():
                        if (datos["ocupada"]==False and dia>=datos["limpieza_hasta"] and dia>=datos["mantenimiento_hasta"]):
                            habitaciones_disponibles.append(("Suite", numero, datos))

                    # ELEGIR HABITACIÓN
                    if len(habitaciones_disponibles)>0:

                        tipo, numero, datos=random.choice(habitaciones_disponibles)
                        datos["mantenimiento_hasta"]=dia + dias_fuera
        
                # COSTOS
                costo_total=(costo_limpieza + costo_operativo + costo_mantenimiento + costo_daños + costo_insumos_dia)

                # GANANCIA
                ganancia=ingresos_dia - costo_total
                ingresos_totales=ingresos_totales + ingresos_dia
                costos_totales+=costo_total
                ganancias_totales=ganancias_totales + ganancia

                # OCUPADAS
                ocupadas_individual, ocupadas_dobles, ocupadas_suite=self.contar_ocupadas(dia)
                ocupacion_i_total += ocupadas_individual
                ocupacion_d_total += ocupadas_dobles
                ocupacion_s_total += ocupadas_suite

                # DISPONIBLES
                disponibles_individual, disponibles_dobles, disponibles_suite=self.contar_disponibles(dia)
                suma_disponibles_i+=disponibles_individual
                suma_disponibles_d+=disponibles_dobles
                suma_disponibles_s+=disponibles_suite
                habitaciones_disponibles_totales+=(disponibles_individual + disponibles_dobles + disponibles_suite)

                # TOTAL OCUPADAS
                total_ocupadas=(ocupadas_individual + ocupadas_dobles + ocupadas_suite)

                # PORCENTAJE
                porcentaje_ocupacion=(total_ocupadas/total_habitaciones) * 100

                suma_ocupacion=(suma_ocupacion + porcentaje_ocupacion)

                # TABLA OCUPACIÓN
                tabla_ocupacion.append([dia, ocupadas_individual, ocupadas_dobles, ocupadas_suite, disponibles_individual, disponibles_dobles, disponibles_suite, f"{porcentaje_ocupacion:.2f}%"])

                # TABLA COSTOS
                tabla_costos.append([dia, salidas, f"${costo_limpieza:,.2f}", f"${costo_daños:,.2f}", alea_mantenimiento, f"${costo_mantenimiento:,.2f}", f"${costo_total:,.2f}"])
                
                # TABLA FINANZAS
                tabla_finanzas.append([dia, f"${ingresos_dia:,.2f}", f"${costo_total:,.2f}", f"${ganancia:,.2f}"])

            # PROMEDIO OCUPACIÓN
            promedio_ocupacion=suma_ocupacion / dias
            
            if len(self.uso_habitaciones)>0:
                habitacion_mas_usada=max(self.uso_habitaciones, key=self.uso_habitaciones.get)
                uso_maximo=self.uso_habitaciones[habitacion_mas_usada]

            else:
                habitacion_mas_usada="Ninguna"
                uso_maximo=0

            #DISPONIBILIDAD GENERAL
            probabilidad_disponibilidad=(habitaciones_disponibles_totales /(total_habitaciones * dias)) * 100

            #DISPONIBILIDAD INDIVIDUAL
            if len(self.habitaciones_individuales)>0:
                probabilidad_individual=(suma_disponibles_i / (len(self.habitaciones_individuales) * dias)) * 100
            else:
                probabilidad_individual=0
            #DISPONIBILIDAD DOBLE
            if len(self.habitaciones_dobles)>0:
                probabilidad_doble=(suma_disponibles_d / (len(self.habitaciones_dobles) * dias)) * 100
            else:
                probabilidad_doble=0
            #DISPONIBILIDAD SUITE
            if len(self.habitaciones_suite)>0:
                probabilidad_suite=(suma_disponibles_s / (len(self.habitaciones_suite) * dias)) * 100
            else:
                probabilidad_suite=0

            #OCUPACIÓN INDIVIDUAL
            if len(self.habitaciones_individuales)>0:
                porcentaje_i=(ocupacion_i_total / (len(self.habitaciones_individuales) * dias)) * 100
            else:
                porcentaje_i=0
            #OCUPACIÓN DOBLE
            if len(self.habitaciones_dobles)>0:
                porcentaje_d=(ocupacion_d_total / (len(self.habitaciones_dobles) * dias)) * 100
            else:
                porcentaje_d=0
            #OCUPACIÓN SUITE
            if len(self.habitaciones_suite)>0:
                porcentaje_s=(ocupacion_s_total / (len(self.habitaciones_suite) * dias)) * 100
            else:
                porcentaje_s=0

            # TABLA RESUMEN
            tabla_resumen.append(["Clientes Totales", clientes_totales])
            tabla_resumen.append(["Clientes Rechazados", clientes_rechazados])
            tabla_resumen.append(["Ocupación Promedio", f"{promedio_ocupacion:.4f}%"])
            tabla_resumen.append(["Ingresos Totales", f"${ingresos_totales:,.4f}"])
            tabla_resumen.append(["Costos Totales", f"${costos_totales:,.4f}"])
            tabla_resumen.append(["Ganancia Total", f"${ganancias_totales:,.4f}"])
            tabla_resumen.append(["Habitación más usada", f"{habitacion_mas_usada} ({uso_maximo} veces)"])
            tabla_resumen.append(["Probabilidad disponibilidad general", f"{probabilidad_disponibilidad:.2f}%"])
            tabla_resumen.append(["Disponibilidad Individual", f"{probabilidad_individual:.2f}%"])
            tabla_resumen.append(["Disponibilidad Doble", f"{probabilidad_doble:.2f}%"])
            tabla_resumen.append(["Disponibilidad Suite", f"{probabilidad_suite:.2f}%"])
            tabla_resumen.append(["Demanda Individual", demanda_tipos["Individual"]])
            tabla_resumen.append(["Demanda Doble", demanda_tipos["Doble"]])
            tabla_resumen.append(["Demanda Suite", demanda_tipos["Suite"]])
            tabla_resumen.append(["Uso Individual", f"{porcentaje_i:.2f}%"])
            tabla_resumen.append(["Uso Doble", f"{porcentaje_d:.2f}%"])
            tabla_resumen.append(["Uso Suite", f"{porcentaje_s:.2f}%"])

            #LIMPIEZA
            capacidad_limpieza=personal * 480 * dias
            if tiempo_limpieza_total > capacidad_limpieza:
                tabla_analisis.append(["Limpieza", "El personal de limpieza es insuficiente."])

            elif tiempo_limpieza_total > capacidad_limpieza * 0.8:
                tabla_analisis.append(["Limpieza", "El personal trabaja cerca de su límite."])

            else:
                tabla_analisis.append(["Limpieza", "La capacidad de limpieza es adecuada."])

            #SATURACIÓN
            if promedio_ocupacion>85:
                tabla_analisis.append(["Saturación", "El hotel está muy saturado. Se recomienda ampliar habitaciones."])

            elif promedio_ocupacion>=60 and promedio_ocupacion<=85:
                tabla_analisis.append(["Saturación", "El hotel trabaja en un rango equilibrado."])

            else:
                tabla_analisis.append(["Saturación", "Existe mucho ocio en habitaciones. Se recomienda reducir capacidad o aumentar publicidad."])

            #CLIENTES RECHAZADOS
            porcentaje_rechazo=(clientes_rechazados/clientes_totales)*100
            if porcentaje_rechazo>25:
                tabla_analisis.append(["Rechazos", "El porcentaje de rechazo es alto."])

            elif porcentaje_rechazo>10:
                tabla_analisis.append(["Rechazos", "Existen rechazos moderados."])

            else:
                tabla_analisis.append(["Rechazos", "El nivel de rechazo es bajo."])

            #GANANCIAS
            if ganancias_totales<0:
                tabla_analisis.append(["Ganancias", "El hotel esta operando con perdidas"])

            elif ganancias_totales<ingresos_totales * 0.15:
                tabla_analisis.append(["Ganancias", "La ganancia es baja respecto a los ingresos"])

            else:
                tabla_analisis.append(["Ganancias", "La operacion del hotel es rentable"])

            #DISPONIBILIDAD
            if probabilidad_disponibilidad<15:
                tabla_analisis.append(["Disponibilidad general", "La disponibilidad es critica"])

            elif probabilidad_disponibilidad>70:
                tabla_analisis.append(["Disponibilidad general", "Hay exceso de habitaciones sin uso"])

            #DISPONIBILIDAD INDIVIDUAL
            if porcentaje_i>90:
                tabla_analisis.append(["Individuales", "Las habitaciones individuales presentan saturación alta. Se recomienda ampliar disponibilidad."])

            elif porcentaje_i>=60:
                tabla_analisis.append(["Individuales", "Las habitaciones individuales trabajan en un rango equilibrado."])

            else:
                tabla_analisis.append(["Individuales", "Las habitaciones individuales tienen baja ocupación."])

            #DISPONIBILIDAD DOBLE
            if porcentaje_d>90:
                tabla_analisis.append(["Dobles", "Las habitaciones dobles presentan alta demanda y posible saturación."])

            elif porcentaje_d>=60:
                tabla_analisis.append(["Dobles", "Las habitaciones dobles trabajan en equilibrio."])

            else:
                tabla_analisis.append(["Dobles", "Las habitaciones dobles presentan baja utilización."])

            #DISPONIBILIDAD SUITE
            if porcentaje_s > 90:
                tabla_analisis.append(["Suites", "Las suites presentan alta ocupación."])

            elif porcentaje_s >= 60:
                tabla_analisis.append(["Suites", "Las suites mantienen una ocupación estable."])

            else:
                tabla_analisis.append(["Suites", "Las suites tienen baja demanda."])

            #DEMANDAS
            if demanda_tipos["Doble"]>demanda_tipos["Individual"] and porcentaje_d>85:
                tabla_analisis.append(["Demanda", "La mayor presión del sistema se concentra en habitaciones dobles."])

            if demanda_tipos["Suite"]<demanda_tipos["Individual"] and porcentaje_s<40:
                tabla_analisis.append(["Demanda","Las suites presentan baja demanda respecto a otros tipos."])
                
            # KPIS
            self.lbl_ingresos.configure(text=f"Ingresos Totales: ${ingresos_totales:,.2f}")

            self.lbl_costos.configure(text=f"Costos Totales: ${costos_totales:,.2f}")

            self.lbl_ganancias.configure(text=f"Ganancia Neta: ${ganancias_totales:,.2f}")

            # LIMPIAR FRAME
            for widget in self.frame_resultados.winfo_children():
                widget.destroy()

            # TÍTULO
            titulo=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
            titulo.pack(pady=20)

            # TABS
            self.tabs=ctk.CTkTabview(self.frame_resultados, width=1400, height=900)
            self.tabs.pack(fill="both", expand=True, padx=20, pady=20)

            # CREAR TABS
            self.tabs.add("Llegadas")
            self.tabs.add("Clientes")
            self.tabs.add("Ocupación")
            self.tabs.add("Costos")
            self.tabs.add("Finanzas")
            self.tabs.add("Resumen")
            self.tabs.add("Análisis")

            # TABLA LLEGADAS
            ctk.CTkLabel(self.tabs.tab("Llegadas"), text="LLEGADAS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            self.tabla_llegadas_resultado=CTkTable(self.tabs.tab("Llegadas"), values=tabla_llegadas)
            self.tabla_llegadas_resultado.pack(pady=10)

            # TABLA CLIENTES
            ctk.CTkLabel(self.tabs.tab("Clientes"), text="CLIENTES", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_clientes=ctk.CTkScrollableFrame(self.tabs.tab("Clientes"), orientation="horizontal", width=1200, height=600)
            frame_clientes.pack(fill="both", expand=True, padx=20,pady=10)
            self.tabla_clientes=CTkTable(frame_clientes, values=tabla_clientes)
            self.tabla_clientes.pack(padx=10, pady=10)

            # TABLA OCUPACIÓN
            ctk.CTkLabel(self.tabs.tab("Ocupación"), text="OCUPACIÓN", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_ocupacion=ctk.CTkScrollableFrame(self.tabs.tab("Ocupación"), orientation="horizontal", width=1200, height=500)
            frame_ocupacion.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_ocupacion=CTkTable(frame_ocupacion, values=tabla_ocupacion)
            self.tabla_ocupacion.pack(padx=10, pady=10)

            # TABLA COSTOS
            self.fila_costos_seleccionada=None
            ctk.CTkLabel(self.tabs.tab("Costos"), text="COSTOS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_costos=ctk.CTkScrollableFrame(self.tabs.tab("Costos"), orientation="horizontal", width=1200, height=500)
            frame_costos.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_costos=CTkTable(frame_costos, values=tabla_costos, command=self.seleccionar_fila_costos)
            self.tabla_costos.pack(padx=10, pady=10)

            boton_ver_daños=ctk.CTkButton(self.tabs.tab("Costos"), text="Ver daños del día seleccionado", command=lambda: self.ver_daños_dia(detalles_daños))
            boton_ver_daños.pack(pady=10)

            # TABLA FINANZAS
            ctk.CTkLabel(self.tabs.tab("Finanzas"), text="FINANZAS", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_finanzas=ctk.CTkScrollableFrame(self.tabs.tab("Finanzas"), orientation="horizontal", width=1200, height=500)
            frame_finanzas.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_finanzas=CTkTable(frame_finanzas, values=tabla_finanzas)
            self.tabla_finanzas.pack(padx=10, pady=10)

            # TABLA RESUMEN
            ctk.CTkLabel(self.tabs.tab("Resumen"), text="RESUMEN GENERAL", text_color=COLOR_TEXTO,font=("Arial", 18, "bold")).pack(pady=10)
            frame_resumen=ctk.CTkScrollableFrame(self.tabs.tab("Resumen"), orientation="horizontal", width=1000, height=500)
            frame_resumen.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_resumen=CTkTable(frame_resumen, values=tabla_resumen)
            self.tabla_resumen.pack(padx=10, pady=10)

            # TABLA ANALISIS
            ctk.CTkLabel(self.tabs.tab("Análisis"), text="ANÁLISIS DEL SISTEMA", text_color=COLOR_TEXTO, font=("Arial", 18, "bold")).pack(pady=10)
            frame_analisis=ctk.CTkScrollableFrame(self.tabs.tab("Análisis"), orientation="horizontal", width=1000, height=500)
            frame_analisis.pack(fill="both", expand=True, padx=20, pady=10)
            self.tabla_analisis=CTkTable(frame_analisis, values=tabla_analisis)
            self.tabla_analisis.pack(padx=10, pady=10)

            # MENSAJE
            messagebox.showinfo("Correcto", "Simulación realizada")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def seleccionar_fila_costos(self, datos):
        fila=datos["row"]
        if fila==0:
            return
        self.fila_costos_seleccionada=fila

    def ver_daños_dia(self, detalles_daños):
        if self.fila_costos_seleccionada is None:
            messagebox.showwarning("Aviso", "Seleccione un día en la tabla de costos")
            return

        fila=self.fila_costos_seleccionada
        dia=int(self.tabla_costos.get_row(fila)[0])

        ventana=ctk.CTkToplevel(self.ventana)
        ventana.title(f"Daños del día {dia}")
        ventana.geometry("400x300")
        titulo=ctk.CTkLabel(ventana, text=f"DETALLE DE DAÑOS - DÍA {dia}", font=("Arial", 20, "bold"))
        titulo.pack(pady=20)

        datos=[["Aleatorio Daño", "Daño", "Costo"]]

        if len(detalles_daños[dia])==0:
            datos.append(["-", "Sin daños", "$0"])

        else:
            for detalle in detalles_daños[dia]:
                datos.append([detalle[0], detalle[1], f"${detalle[2]:,.2f}"])

        tabla=CTkTable(ventana, values=datos)
        tabla.pack(expand=True, fill="both", padx=20, pady=20)




Habitaciones()