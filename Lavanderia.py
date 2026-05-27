

#! restriccion para que no se pueda poner mas de 1 en probabilidad
#! tablas con detalles (mostrar aleatorio y dato exacto)

#! numeros del archivo de jose

from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox, Canvas, Scrollbar
from CTkTable import CTkTable
import random

# Configuración de estilo
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

import GeneraRandom 


class Lavanderia:
    
    def __init__(self):
        
        self.Interfaz = ctk.CTk()
        self.Interfaz.title("Interfaz --- Lavanderia")
        
        self.Cargar_datos() 
        self.Calculos_probAcu_rang() 
        self.contador = 1
                

        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Variables a usar
        
        self.Tabla_1_e = None
        self.Tabla_2_e = None
        self.Tabla_3_e = None
        self.Tabla_4_e = None
        self.Tabla_5_e = None
        self.Tabla_6_e = None
        self.Tabla_7_e = None
        self.Tabla_8_e = None
        self.Tabla_9_e = None
        self.Tabla_10_e = None
        self.Tabla_11_e = None
        self.Tabla_12_e = None
        
        self.Tabla_1_e_det = None
        self.Tabla_2_e_det = None
        self.Tabla_3_e_det = None
        self.Tabla_4_e_det = None
        self.Tabla_5_e_det = None
        self.Tabla_6_e_det = None
        self.Tabla_7_e_det = None
        self.Tabla_8_e_det = None
        self.Tabla_9_e_det = None
        self.Tabla_10_e_det = None
        self.Tabla_11_e_det = None
        self.Tabla_12_e_det = None
        
        self.L_tabla_1 = []
        self.L_tabla_2 = []
        self.L_tabla_3 = []
        self.L_tabla_4 = []
        self.L_tabla_5 = []
        self.L_tabla_6 = []
        self.L_tabla_7 = []
        self.L_tabla_8 = []
        
        self.horas_trabajadas_por_dia = []
        
        self.Total_insumos = 0
        
        self.piezas_jabon = []
        self.piezas_suavitel = []
        self.piezas_desmanchador = []
        self.piezas_bolsas = []
        self.piezas_ganchos = []
        
        
        self.maquinas_descompuestas = []
        
        self.tabla_activa = None
        self.indice_selec = -1
        self.lista_datos_activa = None
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Comportamiento de las filas y columnas de la interfaz
        
        self.Interfaz.grid_columnconfigure(1, weight=1)
        self.Interfaz.grid_rowconfigure(0, weight=1)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #FRAME DERECHO (SOLO PARA MOSTRAR LOS DATOS)
        
        self.Frame_Der = CTkFrame(self.Interfaz, width=200, corner_radius=10)
        self.Frame_Der.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Tabview (sirve para tener vistas de pestañas en una misma interfaz)
        
        self.tabview = CTkTabview(self.Frame_Der, corner_radius= 30, width=1900, height= 300)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)
        
        #botones dentro del tabview
        
        self.tabview.add("TABLAS EDITABLES")
        self.tabview.add("MONTE CARLO")
        self.tabview.add("DETALLES")
        
        
        self.Tablas_Editables() 
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Tercera pestaña 
        
        self.Monte_carlo = self.tabview.tab("MONTE CARLO")    
        
        #Titulo 
        
        self.Titulo_frame_der = CTkLabel(self.Monte_carlo, text= "MONTE CARLO", font= ("Arial", 30 ))
        self.Titulo_frame_der.pack(pady=10, padx=10)
        
        #Boton de simular

        self.btn_simular = CTkButton(self.Monte_carlo, text= "simular", font= ("Arial", 25), command= self.Creacion_tabla)
        self.btn_simular.pack(pady=10)
        
        #boton de borrar lo escrito  
        self.Limpiar = CTkButton(self.Monte_carlo, text= "     🗑️", font= ("Arial", 25), command= self.Limpiar)
        self.Limpiar.pack(padx=10)
        
        
        #caniidad de dias a simular
        self.cant_dias = CTkEntry(self.Monte_carlo, placeholder_text= "Cantidad de dias", width= 205, font= ("Arial", 25))
        self.cant_dias.pack(after= self.btn_simular , pady= 10)
        
        
        
        
        # self.tit_Limpiar = CTkLabel(self.frame_resultados, text= "Limpiar\ndatos", font= ("Arial", 20))
        # self.tit_Limpiar.grid(row=0, column=20, padx=10, pady=10)
        
        
        
        
        
        
        # Para que la tabla no se salga de la pantalla
        
        # self.scroll_frame = CTkScrollableFrame(self.Monte_carlo)
        # self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #scroll modificado 
        
        self.frame_new = CTkFrame(self.Monte_carlo)
        self.frame_new.pack(expand=True, fill="both", padx=10, pady=10)

        # Canvas para scroll horizontal
        self.canvas = Canvas(self.frame_new, bg="#2b2b2b", highlightthickness=0)
        
        
        self.scroll_hori = Scrollbar(self.frame_new, orient="horizontal", command= self.canvas.xview)
        
        
        
        self.scroll_verti = Scrollbar(self.frame_new, orient="vertical", command= self.canvas.yview)
        
        
        self.canvas.configure(xscrollcommand= self.scroll_hori.set, yscrollcommand=self.scroll_verti.set)
        
        
        self.scroll_verti.pack(side="right", fill="y")
        self.scroll_hori.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", expand=True, fill="both")
        
        
        self.scroll_frame = CTkFrame(self.canvas)
        self.canvas_ventana = self.canvas.create_window((0, 0), window= self.scroll_frame, anchor="nw")
        
        
        def on_configure(event):
            self.canvas.configure(scrollregion= self.canvas.bbox("all"))

        self.scroll_frame.bind("<Configure>", on_configure)
        
        
        
        #valores abajo de la tabla
        
        self.frame_resultados = CTkFrame(self.Monte_carlo)
        self.frame_resultados.pack(pady=20)
        
        
        
        #Cantidad de maquinas
        
        self.tit_cant_maquinas = CTkLabel(self.frame_resultados, text= "Cantidad de\nmaquinas", font= ("Arial", 15 ))
        self.tit_cant_maquinas.grid(row=0, column=0, padx=10, pady=10)
        
        self.cant_maquinas = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cant_maquinas.grid(row=1, column=0, padx=10, pady=10)
        
        
        
        
        #cantidad de insumos       (jabon, suavitel, desmanchador, bolsas, ganchos)
        
        self.tit_cant_jabon = CTkLabel(self.frame_resultados, text= 'Cantidad de\njabon "gr"', font= ("Arial", 15))
        self.tit_cant_jabon.grid(row=0, column=1, padx=10, pady=10)
        
        self.cant_jabon = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15))
        self.cant_jabon.grid(row=1, column=1, padx=10, pady=10)
        
        
        
        self.tit_cost_jabon = CTkLabel(self.frame_resultados, text= 'Costo jabon\n"pieza"', font= ("Arial", 15))
        self.tit_cost_jabon.grid(row=0, column=2, padx=10, pady=10)
        
        
        self.cost_jabon = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cost_jabon.grid(row=1, column=2, padx=10, pady=10)
        
        
        
        
        
        
        
        
        self.tit_cant_suavitel = CTkLabel(self.frame_resultados, text= 'Cantidad de\nsuavitel "ml"', font= ("Arial", 15))
        self.tit_cant_suavitel.grid(row=0, column=3, padx=10, pady=10)
        
        self.cant_suavitel = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15))
        self.cant_suavitel.grid(row=1, column=3, padx=10, pady=10)
        
        
        
        self.tit_cost_suavitel = CTkLabel(self.frame_resultados, text= 'Costo suavitel\n"pieza"', font= ("Arial", 15))
        self.tit_cost_suavitel.grid(row=0, column=4, padx=10, pady=10)
        
        self.cost_suavitel = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cost_suavitel.grid(row=1, column=4, padx=10, pady=10)
        
        
        
        
        
        
        
        

        self.tit_cant_desmanchador = CTkLabel(self.frame_resultados, text= 'Cantidad de\ndesmanchador "ml"', font= ("Arial", 15))
        self.tit_cant_desmanchador.grid(row=0, column=5, padx=10, pady=10)
        
        self.cant_desmanchador = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cant_desmanchador.grid(row=1, column=5, padx=10, pady=10)
        
        
        
        self.tit_cost_desmanchador = CTkLabel(self.frame_resultados, text= 'Costo desmanchador\n"pieza"', font= ("Arial", 15))
        self.tit_cost_desmanchador.grid(row=0, column=6, padx=10, pady=10)
        
        self.cost_desmanchador = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cost_desmanchador.grid(row=1, column=6, padx=10, pady=10)
        
        
        
        
        
        
        
        
        self.tit_cant_bolsas = CTkLabel(self.frame_resultados, text= "Cantidad de\nbolsas", font= ("Arial", 15))
        self.tit_cant_bolsas.grid(row=0, column=7, padx=10, pady=10)
        
        self.cant_bolsas = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15))
        self.cant_bolsas.grid(row=1, column=7, padx=10, pady=10)
        
        
        
        
        self.tit_cost_bolsas = CTkLabel(self.frame_resultados, text= 'Costo bolsas\n"pieza"', font= ("Arial", 15))
        self.tit_cost_bolsas.grid(row=0, column=8, padx=10, pady=10)
        
        self.cost_bolsas = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cost_bolsas.grid(row=1, column=8, padx=10, pady=10)
        
        
        
        
        
        
        
        self.tit_cant_ganchos = CTkLabel(self.frame_resultados, text= "Cantidad de\nganchos", font= ("Arial", 15))
        self.tit_cant_ganchos.grid(row=0, column=9, padx=10, pady=10)
        
        self.cant_ganchos = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.cant_ganchos.grid(row=1, column=9, padx=10, pady=10)
        
        
        self.tit_cost_ganchos = CTkLabel(self.frame_resultados, text= 'Costo ganchos\n"pieza"', font= ("Arial", 15))
        self.tit_cost_ganchos.grid(row=0, column=10, padx=10, pady=10)
        
        self.cost_ganchos = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15))
        self.cost_ganchos.grid(row=1, column=10, padx=10, pady=10)

        
        
        
        
        
        #costos diarios
        
        self.tit_costos_diarios = CTkLabel(self.frame_resultados, text= "Costos\ndiarios", font= ("Arial", 15))
        self.tit_costos_diarios.grid(row=0, column=11, padx=10, pady=10)
        
        self.costos_diarios = CTkEntry(self.frame_resultados, width= 130, font=("Arial", 15 ))
        self.costos_diarios.grid(row=1, column=11, padx=10, pady=10)
        
        
        
        
        #tercera pestaña 
        
        self.Detalles_monte_carlo = self.tabview.tab("DETALLES")
        
        #Titulo 
        
        self.Titulo_frame_der = CTkLabel(self.Detalles_monte_carlo, text= "DETALLES MONTE CARLO", font= ("Arial", 30 ))
        self.Titulo_frame_der.pack(pady=10, padx=10)    
        
        
        self.scroll_frame_det = CTkScrollableFrame(self.Detalles_monte_carlo)
        self.scroll_frame_det.pack(expand=True, fill="both", padx=10, pady=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Tabla = None
        self.resultados_tabla_3 = []
        self.resultados_tabla_5 = []
        
        self.Interfaz.update()
        
        
        
        try: 
            self.Interfaz.state("zoomed")
        except: 
            self.Interfaz.attributes("-zoomed", True)
        
        
        
        # self.Interfaz.state("zoomed") #windows
        # self.Interfaz.attributes('-zoomed', True) #Linux
        
        self.Interfaz.mainloop()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------

#Tablas de probabilidades

    
    def Cargar_datos(self):
        
        #Tabla 1
        self.Cargas_dias = [
            ["5 - 10", 0.2],
            ["11 - 20", 0.4],
            ["21 - 30", 0.3],
            ["31 - 40", 0.1]
        ]
        
        #Tabla 2
        self.Tipos_cargas = [
            ["Sabanas / Toallas", 0.75],
            ["Ropa de huesped", 0.2],
            ["Ropa del staff", 0.05]
        ]
        
        #Tabla 4
        # self.Numero_maquinas = [
        #     ["1", 0.15],
        #     ["2", 0.45],
        #     ["3", 0.3],
        #     ["4", 0.1]
        # ]
        
        #Tabla 3                               5
        self.Tiempo_ciclo = [
            [20, 0.35],
            [30, 0.4],
            [40, 0.2],
            [50, 0.05]
        ]
        
        #Tabla 4                             3
        self.Estado_maquinas = [
            ["Normal", 0.58],
            ["Retraso", 0.25],
            ["Falla", 0.12],
            ["Corte de luz / agua", 0.05]
        ]
        
        #Tabla 5
        self.dias_repacion = [
            ["2 - 3", 0.65],
            ["4 - 6", 0.25],
            ["7 - 15", 0.10]
        ]
        
        # self.Tabla_6_e_d = [
        #     ["Normal", 1],
        #     ["Retraso", 1.5],
        #     ["Falla", 0],
        #     ["Corte de luz / agua", 2]
        # ]
        
        #Tabla 6
        self.daño_ropa = [
            ["No", 0.95],
            ["Mancha", 0.03],
            ["Rotura", 0.015],
            ["Extravio", 0.005],
        ]
        
        #* no se usa
        self.Insumos =[
            ["Jabon"],
            ["Suavitel"],
            ["Desmanchador"],
            ["Bolsas"],
            ["Ganchos"]
        ]
        
        #Tabla 7
        self.Uso_insumo_jabon = [
            ["50 - 100", 0.35],
            ["101 - 180", 0.45],
            ["181 - 250", 0.20]
        ]
        
        #Tabla 8
        self.Uso_insumo_suavitel = [
            ["0", 0.25],
            ["30 - 60", 0.40],
            ["61 - 100", 0.25],
            ["101 - 150", 0.10],
        ]
        
        #Tabla 9
        self.Uso_insumo_desmanchador = [
            ["0", 0.60],
            ["20 - 40", 0.25],
            ["41 - 70", 0.10],
            ["71 - 120", 0.05],
        ]
        
        #Tabla 10
        self.Uso_insumo_bolsas = [
            ["0", 0.25],
            ["1", 0.50],
            ["2", 0.20],
            ["3", 0.05],
        ]
        
        #Tabla 11
        self.Uso_insumo_ganchos = [
            ["0", 0.45],
            ["1 - 3", 0.35],
            ["4 - 6", 0.15],
            ["7 - 10", 0.05],
        ]
        
        #Tabla 12
        self.Tabla_12_e_d = [
            ["Normal", 1],
            ["Retraso", 1.5],
            ["Falla", 0],
            ["Corte de luz / agua", 2]
        ]
        
        
        self.Tabla_13_e_d = [
            ["Jabon", 1000],
            ["Suavitel", 1000],
            ["Desmanchador", 1000]
        ]
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Calculos_probAcu_rang(self):
        
        #Tabla 1 (completa)
        
        Probabilidad_acumulada_1 = 0.0
        self.Tabla_1_e_d = []
        
        for val_1, prob_1 in self.Cargas_dias:
            
            inicio_1 = Probabilidad_acumulada_1
            
            Probabilidad_acumulada_1 = round(Probabilidad_acumulada_1 + prob_1, 4)
            
            rango_1 = str(round(inicio_1, 4)) + " - " + str(round(Probabilidad_acumulada_1, 4))
            
            self.Tabla_1_e_d.append([val_1, prob_1, Probabilidad_acumulada_1, rango_1])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 2 (completa)
        
        Probabilidad_acumulada_2 = 0.0
        self.Tabla_2_e_d = []
            
        for val_2, prob_2 in self.Tipos_cargas:
            
            inicio_2 = Probabilidad_acumulada_2
            
            Probabilidad_acumulada_2 = round(Probabilidad_acumulada_2 + prob_2, 4)
            
            rango_2 = str(round(inicio_2, 4)) + " - " + str(round(Probabilidad_acumulada_2, 4))
            
            self.Tabla_2_e_d.append([val_2, prob_2, Probabilidad_acumulada_2, rango_2])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 3 (completa)
        
        Probabilidad_acumulada_3 = 0.0
        self.Tabla_3_e_d = []
        
        # for val_3, prob_3 in self.Estado_maquinas:
        for val_3, prob_3 in self.Tiempo_ciclo:
            
            inicio_3 = Probabilidad_acumulada_3
            
            Probabilidad_acumulada_3 = round(Probabilidad_acumulada_3 + prob_3, 4)
            
            rango_3 = str(round(inicio_3, 4)) + " - " + str(round(Probabilidad_acumulada_3, 4))
            
            self.Tabla_3_e_d.append([val_3, prob_3, Probabilidad_acumulada_3, rango_3])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 4 (completa)
        
        Probabilidad_acumulada_4 = 0.0
        self.Tabla_4_e_d = []
        
        # for val_4, prob_4 in self.Numero_maquinas:
        for val_4, prob_4 in self.Estado_maquinas:
        
            
            inicio_4 = Probabilidad_acumulada_4
            
            Probabilidad_acumulada_4 = round(Probabilidad_acumulada_4 + prob_4, 4)
            
            rango_4 = str(round(inicio_4, 4)) + " - " + str(round(Probabilidad_acumulada_4, 4))
            
            self.Tabla_4_e_d.append([val_4, prob_4, Probabilidad_acumulada_4, rango_4])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 5 (completa)
        
        Probabilidad_acumulada_5 = 0.0
        self.Tabla_5_e_d = []
        
        # for val_5, prob_5 in self.Tiempo_ciclo:
        for val_5, prob_5 in self.dias_repacion:
        
            
            inicio_5 = Probabilidad_acumulada_5
            
            Probabilidad_acumulada_5 = round(Probabilidad_acumulada_5 + prob_5, 4)
            
            rango_5 = str(round(inicio_5, 4)) + " - " + str(round(Probabilidad_acumulada_5, 4))
            
            self.Tabla_5_e_d.append([val_5, prob_5, Probabilidad_acumulada_5, rango_5])
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 6 (completa)
        
        Probabilidad_acumulada_6 = 0.0
        self.Tabla_6_e_d = []
        
        for val_6, prob_6 in self.daño_ropa:
        
            
            inicio_6 = Probabilidad_acumulada_6
            
            Probabilidad_acumulada_6 = round(Probabilidad_acumulada_6 + prob_6, 4)
            
            rango_6 = str(round(inicio_6, 4)) + " - " + str(round(Probabilidad_acumulada_6, 4))
            
            self.Tabla_6_e_d.append([val_6, prob_6, Probabilidad_acumulada_6, rango_6])
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 7 (completa) 
        
        Probabilidad_acumulada_7 = 0.0
        self.Tabla_7_e_d = []
        
        for val_7, prob_7 in self.Uso_insumo_jabon:
        
            
            inicio_7 = Probabilidad_acumulada_7
            
            Probabilidad_acumulada_7 = round(Probabilidad_acumulada_7 + prob_7, 4)
            
            rango_7 = str(round(inicio_7, 4)) + " - " + str(round(Probabilidad_acumulada_7, 4))
            
            self.Tabla_7_e_d.append([val_7, prob_7, Probabilidad_acumulada_7, rango_7])
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 8 (completa)   
        
        Probabilidad_acumulada_8 = 0.0
        self.Tabla_8_e_d = []
        
        for val_8, prob_8 in self.Uso_insumo_suavitel:
        
            
            inicio_8 = Probabilidad_acumulada_8
            
            Probabilidad_acumulada_8 = round(Probabilidad_acumulada_8 + prob_8, 4)
            
            rango_8 = str(round(inicio_8, 4)) + " - " + str(round(Probabilidad_acumulada_8, 4))
            
            self.Tabla_8_e_d.append([val_8, prob_8, Probabilidad_acumulada_8, rango_8])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 9 (completa)   
        
        Probabilidad_acumulada_9 = 0.0
        self.Tabla_9_e_d = []
        
        for val_9, prob_9 in self.Uso_insumo_desmanchador:
        
            
            inicio_9 = Probabilidad_acumulada_9
            
            Probabilidad_acumulada_9 = round(Probabilidad_acumulada_9 + prob_9, 4)
            
            rango_9 = str(round(inicio_9, 4)) + " - " + str(round(Probabilidad_acumulada_9, 4))
            
            self.Tabla_9_e_d.append([val_9, prob_9, Probabilidad_acumulada_9, rango_9])
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 10 (completa)   
        
        Probabilidad_acumulada_10 = 0.0
        self.Tabla_10_e_d = []
        
        for val_10, prob_10 in self.Uso_insumo_bolsas:
        
            
            inicio_10 = Probabilidad_acumulada_10
            
            Probabilidad_acumulada_10 = round(Probabilidad_acumulada_10 + prob_10, 4)
            
            rango_10 = str(round(inicio_10, 4)) + " - " + str(round(Probabilidad_acumulada_10, 4))
            
            self.Tabla_10_e_d.append([val_10, prob_10, Probabilidad_acumulada_10, rango_10])
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 11 (completa)   
        
        Probabilidad_acumulada_11 = 0.0
        self.Tabla_11_e_d = []
        
        for val_11, prob_11 in self.Uso_insumo_ganchos:
        
            
            inicio_11 = Probabilidad_acumulada_11
            
            Probabilidad_acumulada_11 = round(Probabilidad_acumulada_11 + prob_11, 4)
            
            rango_11 = str(round(inicio_11, 4)) + " - " + str(round(Probabilidad_acumulada_11, 4))
            
            self.Tabla_11_e_d.append([val_11, prob_11, Probabilidad_acumulada_11, rango_11])
            
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Tablas_Editables(self):
        
        tablas = self.tabview.tab("TABLAS EDITABLES")
        
        self.frame_sup = CTkFrame(tablas, width=200, height= 200, corner_radius=10)
        self.frame_sup.pack(fill="both", pady=20, padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #cuadro de texto
        
        self.Valor = CTkEntry(self.frame_sup, placeholder_text= "Valor", width= 130)
        self.Valor.pack(side="left", padx=10)
        
        #se deja sin pack para mostarlo despues (SOLO CUANDO ESTA SELECCIONADA LA TABLA 12)
        self.Tiempo = CTkEntry(self.frame_sup, placeholder_text="Tiempo", width=130)
        
        
        #se deja sin pack para mostarlo despues (SOLO CUANDO ESTA SELECCIONADA LA TABLA 13)
        self.Conversion = CTkEntry(self.frame_sup, placeholder_text="Conversion", width=130)
        
        
        self.Probabilidad = CTkEntry(self.frame_sup, placeholder_text= "Probabilidad", width= 130)
        self.Probabilidad.pack(side="left", padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #botones
        
        self.btn_Actualizar = CTkButton(self.frame_sup, text= "actualizar", font= ("Arial", 20), command= self.Actualizar_datos)
        self.btn_Actualizar.pack(side="left", padx=10)
        
        self.btn_Añadir = CTkButton(self.frame_sup, text= "añadir", font= ("Arial", 20), fg_color= "green", command= self.Añadir_fila)
        self.btn_Añadir.pack(side="left", padx=10)
        
        self.btn_Eliminar = CTkButton(self.frame_sup, text= "eliminar", font= ("Arial", 20), fg_color= "red", command= self.Eliminar_fila)
        self.btn_Eliminar.pack(side="left", padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #para mostar las tablas
        
        self.scroll_frame = CTkScrollableFrame(tablas)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 1 (cargas por dia) 
        
        # Encabezado
        encabezado_1 = [["Cargas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Cargas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        
        self.Tabla_1_e = CTkTable(
            self.scroll_frame,
            values= encabezado_1 + self.Tabla_1_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_1
        )
        self.Tabla_1_e.pack(expand=True, fill="both", pady=(0, 50))
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 2 (Tipos de cargas)
        
        # Encabezado
        encabezado_2 = [["Tipo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de cargas", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        
        self.Tabla_2_e = CTkTable(
            self.scroll_frame,
            values= encabezado_2 + self.Tabla_2_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_2
        )
        self.Tabla_2_e.pack(expand=True, fill="both", pady=(0, 50))
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 3 (Tiempo de ciclo)
        
        # Encabezado
        encabezado_3 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Tiempo de ciclo", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        
        self.Tabla_3_e = CTkTable(
            self.scroll_frame,
            values= encabezado_3 + self.Tabla_3_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_3
        )
        # Tabla_3.pack(expand=True, fill="both")
        self.Tabla_3_e.pack(expand=True, fill="both", pady=(0, 50))
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 4 (Estado de las maquinas)
        
        # Encabezado
        encabezado_4 = [["Estado", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Estado de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        
        self.Tabla_4_e = CTkTable(
            self.scroll_frame,
            values= encabezado_4 + self.Tabla_4_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_4
        )
        self.Tabla_4_e.pack(expand=True, fill="both", pady=(0, 50))
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 5 (dias de repacion)
        
        # Encabezado
        encabezado_5 = [["Dias", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Dias de repacion de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        
        self.Tabla_5_e = CTkTable(
            self.scroll_frame,
            values= encabezado_5 + self.Tabla_5_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_5
        )
        self.Tabla_5_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Tabla 6 (daños de ropa) 
        
        # Encabezado
        encabezado_6 = [["Tipo de daños", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_6 = CTkLabel(self.scroll_frame, text= "Daños a la ropa", font= ("Arial", 20 ))
        self.Titulo_t_6.pack(pady=10, padx=10)
        
        self.Tabla_6_e = CTkTable(
            self.scroll_frame,
            values= encabezado_6 + self.Tabla_6_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_6
        )
        self.Tabla_6_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla de insumo jabon
        
        # Encabezado
        encabezado_7 = [["Cantidad (gramos)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_7 = CTkLabel(self.scroll_frame, text= "Consumo de jabon (gramos)", font= ("Arial", 20 ))
        self.Titulo_t_7.pack(pady=10, padx=10)
        
        self.Tabla_7_e = CTkTable(
            self.scroll_frame,
            values= encabezado_7 + self.Tabla_7_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_7
        )
        self.Tabla_7_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla de insumo suavitel
        
        # Encabezado
        encabezado_8 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_8 = CTkLabel(self.scroll_frame, text= "Consumo de suavitel  (ml)", font= ("Arial", 20 ))
        self.Titulo_t_8.pack(pady=10, padx=10)
        
        self.Tabla_8_e = CTkTable(
            self.scroll_frame,
            values= encabezado_8 + self.Tabla_8_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_8
        )
        self.Tabla_8_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Tabla de insumo desmanchador
        
        # Encabezado
        encabezado_9 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_9 = CTkLabel(self.scroll_frame, text= "Consumo de desmanchador (ml)", font= ("Arial", 20 ))
        self.Titulo_t_9.pack(pady=10, padx=10)
        
        self.Tabla_9_e = CTkTable(
            self.scroll_frame,
            values= encabezado_9 + self.Tabla_9_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_9
        )
        self.Tabla_9_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Tabla de insumo bolsas
        
        # Encabezado
        encabezado_10 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_10 = CTkLabel(self.scroll_frame, text= "Uso de bolsas (pieza)", font= ("Arial", 20 ))
        self.Titulo_t_10.pack(pady=10, padx=10)
        
        self.Tabla_10_e = CTkTable(
            self.scroll_frame,
            values= encabezado_10 + self.Tabla_10_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_10
        )
        self.Tabla_10_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla de insumo ganchos
        
        # Encabezado
        encabezado_11 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        self.Titulo_t_11 = CTkLabel(self.scroll_frame, text= "Uso de ganchos (pieza)", font= ("Arial", 20 ))
        self.Titulo_t_11.pack(pady=10, padx=10)
        
        self.Tabla_11_e = CTkTable(
            self.scroll_frame,
            values= encabezado_11 + self.Tabla_11_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_11
        )
        self.Tabla_11_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla de tiempo (que se multiplica)
        
        # Encabezado
        encabezado_12 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        
        self.Titulo_t_12 = CTkLabel(self.scroll_frame, text= "Tiempo de trabajo de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_12.pack(pady=10, padx=10)
        
        self.Tabla_12_e = CTkTable(
            self.scroll_frame,
            values= encabezado_12 + self.Tabla_12_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_12
        )
        self.Tabla_12_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla de piezas (ml o g  * 1000)
        
        # Encabezado
        encabezado_13 = [["Candidad (ml o g)", "Equivalente a una pieza"]]
        
        self.Titulo_t_13 = CTkLabel(self.scroll_frame, text= "Cantidad por pieza", font= ("Arial", 20 ))
        self.Titulo_t_13.pack(pady=10, padx=10)
        
        self.Tabla_13_e = CTkTable(
            self.scroll_frame,
            values= encabezado_13 + self.Tabla_13_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_13
        )
        self.Tabla_13_e.pack(expand=True, fill="both", pady=(0, 50))
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Seleccionar_tabla_1(self, data):
        self.tabla_activa = self.Tabla_1_e
        self.lista_datos_activa = self.Cargas_dias
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_2(self, data):
        self.tabla_activa = self.Tabla_2_e
        self.lista_datos_activa = self.Tipos_cargas
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_3(self, data):
        self.tabla_activa = self.Tabla_3_e
        # self.lista_datos_activa = self.Estado_maquinas
        self.lista_datos_activa = self.Tiempo_ciclo
        
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_4(self, data):
        self.tabla_activa = self.Tabla_4_e
        # self.lista_datos_activa = self.Numero_maquinas
        self.lista_datos_activa = self. Estado_maquinas
        
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_5(self, data):
        self.tabla_activa = self.Tabla_5_e
        # self.lista_datos_activa = self.Tiempo_ciclo
        self.lista_datos_activa = self.dias_repacion
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_6(self, data):
        self.tabla_activa = self.Tabla_6_e
        self.lista_datos_activa = self.daño_ropa
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_7(self, data):
        self.tabla_activa = self.Tabla_7_e
        self.lista_datos_activa = self.Uso_insumo_jabon
        
        
        # ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_8(self, data):
        self.tabla_activa = self.Tabla_8_e
        self.lista_datos_activa = self.Uso_insumo_suavitel
        
        
        # ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_9(self, data):
        self.tabla_activa = self.Tabla_9_e
        self.lista_datos_activa = self.Uso_insumo_desmanchador
        
        
        # ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_10(self, data):
        self.tabla_activa = self.Tabla_10_e
        self.lista_datos_activa = self.Uso_insumo_bolsas
        
        
        # ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_11(self, data):
        self.tabla_activa = self.Tabla_11_e
        self.lista_datos_activa = self.Uso_insumo_ganchos
        
        
        # ocultamos el entry
        self.Tiempo.pack_forget()
        self.Conversion.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_12(self, data): #8
        self.tabla_activa = self.Tabla_12_e
        self.lista_datos_activa = self.Tabla_12_e_d
        
        #ocultamos el entry
        self.Probabilidad.pack_forget()
        self.Conversion.pack_forget()
        
        #se mustra el entry
        self.Tiempo.pack(side= "left", padx= 10, after= self.Valor)
        self.Seleccionar_fila(data)
        
        
    def Seleccionar_tabla_13(self, data): 
        self.tabla_activa = self.Tabla_13_e
        self.lista_datos_activa = self.Tabla_13_e_d
        
        #ocultamos el entry
        self.Probabilidad.pack_forget()
        self.Tiempo.pack_forget()
        
        #se mustra el entry
        self.Conversion.pack(side= "left", padx= 10, after= self.Valor)
        self.Seleccionar_fila(data)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Seleccionar_fila(self, data):
        self.indice_selec = data['row']
        
        if self.indice_selec > 0:
            valores_fila = self.tabla_activa.get_row(self.indice_selec)
            
            self.Valor.delete(0, "end")    
            self.Valor.insert(0, valores_fila[0])  
            
            if self.tabla_activa == self.Tabla_12_e: 
                
                self.Tiempo.delete(0, "end")
                self.Tiempo.insert(0, valores_fila[1])
                
            elif self.tabla_activa == self.Tabla_13_e:
                self.Conversion.delete(0, "end")
                self.Conversion.insert(0, valores_fila[1])
            
            else:
                self.Probabilidad.delete(0, "end")    
                self.Probabilidad.insert(0, valores_fila[1])
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Verificar_probabilidad(self):
        self.suma_total = 0
        
        if self.lista_datos_activa:
            
            for fila in self.lista_datos_activa:
                
                if self.tabla_activa != self.Tabla_12_e and self.tabla_activa != self.Tabla_13_e:
                    self.suma_total += float(fila[1])
                
        self.suma_total = round(self.suma_total, 2)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Actualizar_datos(self):
        
        # cosas para la tabla 6 y para la normal 
        
        if self.lista_datos_activa is None or self.indice_selec <= 0:
            messagebox.showwarning("ATENCION", "Primero seleccione una fila de una tabla")
            return
        
        if self.tabla_activa == self.Tabla_12_e:
            
            new_val = self.Valor.get()
            new_tiempo = int(self.Tiempo.get())
            
            self.lista_datos_activa[self.indice_selec - 1] = [new_val, new_tiempo]
            
        elif self.tabla_activa == self.Tabla_13_e:
            
            new_val = self.Valor.get()
            new_conversion = int(self.Conversion.get())
            
            self.lista_datos_activa[self.indice_selec - 1] = [new_val, new_conversion]
            
        else:
            
            new_val = self.Valor.get()
            new_prob = float(self.Probabilidad.get())


            new_suma = 0.0

            for i in range(len(self.lista_datos_activa)):

                if i == self.indice_selec - 1:
                    new_suma +=  new_prob

                else: 
                    new_suma += float(self.lista_datos_activa[i][1])

            new_suma = round(new_suma, 2)


            if new_suma > 1.0:
                messagebox.showerror("ERROR", F"La suma de las probabilidades debe de ser de 1, tu tienes {new_suma}")
                return

            self.lista_datos_activa[self.indice_selec - 1] = [new_val, new_prob]

            self.Actualizar_tabla()

            messagebox.showinfo("EXITO", "Datos actualizados correctamente")

#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Actualizar_tabla(self):
        
        self.Calculos_probAcu_rang()
        
        encabezado_1 = [["Cargas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_2 = [["Tipo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_3 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_4 = [["Estado", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_5 = [["Dias", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_6 = [["Tipo de daños", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_7 = [["Cantidad (gramos)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_8 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_9 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_10 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_11 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_12 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        encabezado_13 = [["Candidad (ml o g)", "Equivalente a una pieza"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d 
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        datos_completos_7 = encabezado_7 + self.Tabla_7_e_d
        datos_completos_8 = encabezado_8 + self.Tabla_8_e_d
        datos_completos_9 = encabezado_9 + self.Tabla_9_e_d
        datos_completos_10 = encabezado_10 + self.Tabla_10_e_d
        datos_completos_11 = encabezado_11 + self.Tabla_11_e_d
        datos_completos_12 = encabezado_12 + self.Tabla_12_e_d
        datos_completos_13 = encabezado_13 + self.Tabla_13_e_d
        
        
        self.Tabla_1_e.configure(values=datos_completos_1)
        self.Tabla_1_e.update_values(datos_completos_1)
        
        
        self.Tabla_2_e.configure(values=datos_completos_2)
        self.Tabla_2_e.update_values(datos_completos_2)
        
        
        self.Tabla_3_e.configure(values=datos_completos_3)
        self.Tabla_3_e.update_values(datos_completos_3)
        
        
        self.Tabla_4_e.configure(values=datos_completos_4)
        self.Tabla_4_e.update_values(datos_completos_4)
        
        
        self.Tabla_5_e.configure(values=datos_completos_5)
        self.Tabla_5_e.update_values(datos_completos_5)
        
        
        self.Tabla_6_e.configure(values=datos_completos_6)
        self.Tabla_6_e.update_values(datos_completos_6)
        
        
        self.Tabla_7_e.configure(values=datos_completos_7)
        self.Tabla_7_e.update_values(datos_completos_7)
        
        
        self.Tabla_8_e.configure(values=datos_completos_8)
        self.Tabla_8_e.update_values(datos_completos_8)
        
        
        self.Tabla_9_e.configure(values=datos_completos_9)
        self.Tabla_9_e.update_values(datos_completos_9)
        
        
        self.Tabla_10_e.configure(values=datos_completos_10)
        self.Tabla_10_e.update_values(datos_completos_10)
        
        
        self.Tabla_11_e.configure(values=datos_completos_11)
        self.Tabla_11_e.update_values(datos_completos_11)
        
        
        self.Tabla_12_e.configure(values=datos_completos_12)
        self.Tabla_12_e.update_values(datos_completos_12)
        
        self.Tabla_13_e.configure(values=datos_completos_12)
        self.Tabla_13_e.update_values(datos_completos_12)
        
        
        self.tabla_activa = None
        self.lista_datos_activa = None
        self.indice_selec = -1
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Añadir_fila(self):
        
        if self.lista_datos_activa is None:
            
            messagebox.showwarning("ATENCION", "Primero seleccione una tabla")
            return
        
        
        new_val = self.Valor.get()
        new_prob = float(self.Probabilidad.get())
        
        
        try:
            
            self.Verificar_probabilidad()
            
            suma_futura = round(self.suma_total + new_prob, 2)
            
            if suma_futura > 1.0:
                messagebox.showerror("ERROR", F"La suma de las probabilidades debe de ser de 1, tu tienes {suma_futura}")
                return
            
            if self.tabla_activa == self.Tabla_12_e:
                new_tiempo = self.Tiempo.get()
                self.lista_datos_activa.append([new_val, new_tiempo])
                
            elif self.tabla_activa == self.Tabla_12_e:
                new_conversion = self.Conversion.get()
                self.lista_datos_activa.append([new_val, new_conversion])
            
            else:
                self.lista_datos_activa.append([new_val, new_prob])
            
            
            if self.tabla_activa == self.Tabla_1_e:
                self.Tabla_1_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_2_e:
                self.Tabla_2_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_3_e:
                self.Tabla_3_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_4_e:
                self.Tabla_4_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_5_e:
                self.Tabla_5_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_6_e:
                self.Tabla_6_e_d.append(self.lista_datos_activa[-1]) 
                
                
            elif self.tabla_activa == self.Tabla_7_e:
                self.Tabla_7_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_8_e:
                self.Tabla_8_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_9_e:
                self.Tabla_9_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_10_e:
                self.Tabla_10_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_11_e:
                self.Tabla_11_e_d.append(self.lista_datos_activa[-1])
                
                
            elif self.tabla_activa == self.Tabla_12_e:
                self.Tabla_12_e_d.append(self.lista_datos_activa[-1])
                
            elif self.tabla_activa == self.Tabla_13_e:
                self.Tabla_13_e_d.append(self.lista_datos_activa[-1])
                
                
            self.indice_selec = -1
            
            
            self.Actualizar_tabla_agregar_fila()
            
            self.Valor.delete(0, "end")
            self.Probabilidad.delete(0, "end")
            
            messagebox.showinfo("EXITO", "Fila añadida correctamente")
            
        except ValueError:
            messagebox.showerror("ERROR", "Datos invalidos", parent= self.Interfaz)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Actualizar_tabla_agregar_fila(self):
        
        self.Calculos_probAcu_rang()
        
        encabezado_1 = [["Cargas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_2 = [["Tipo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_3 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_4 = [["Estado", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_5 = [["Dias", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_6 = [["Tipo de daños", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_7 = [["Cantidad (gramos)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_8 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_9 = [["Cantidad (ml)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_10 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_11 = [["Cantidad (piezas)", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_12 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        encabezado_13 = [["Candidad (ml o g)", "Equivalente a una pieza"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d 
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        datos_completos_7 = encabezado_7 + self.Tabla_7_e_d
        datos_completos_8 = encabezado_8 + self.Tabla_8_e_d
        datos_completos_9 = encabezado_9 + self.Tabla_9_e_d
        datos_completos_10 = encabezado_10 + self.Tabla_10_e_d
        datos_completos_11 = encabezado_11 + self.Tabla_11_e_d
        datos_completos_12 = encabezado_12 + self.Tabla_12_e_d
        datos_completos_13 = encabezado_13 + self.Tabla_13_e_d
        
        
        if self.tabla_activa == self.Tabla_1_e:
            self.Tabla_1_e.add_row(datos_completos_1[-1])
            
            
        elif self.tabla_activa == self.Tabla_2_e:
            self.Tabla_2_e.add_row(datos_completos_2[-1])
            
            
        elif self.tabla_activa == self.Tabla_3_e:
            self.Tabla_3_e.add_row(datos_completos_3[-1])
            
            
        elif self.tabla_activa == self.Tabla_4_e:
            self.Tabla_4_e.add_row(datos_completos_4[-1])
            
            
        elif self.tabla_activa == self.Tabla_5_e:
            self.Tabla_5_e.add_row(datos_completos_5[-1])
            
            
        elif self.tabla_activa == self.Tabla_6_e:
            self.Tabla_6_e.add_row(datos_completos_6[-1])
            
            
        elif self.tabla_activa == self.Tabla_7_e:
            self.Tabla_7_e.add_row(datos_completos_7[-1])
            
            
        elif self.tabla_activa == self.Tabla_8_e:
            self.Tabla_8_e.add_row(datos_completos_8[-1])
            
            
        elif self.tabla_activa == self.Tabla_9_e:
            self.Tabla_9_e.add_row(datos_completos_9[-1])
            
            
        elif self.tabla_activa == self.Tabla_10_e:
            self.Tabla_10_e.add_row(datos_completos_10[-1])
            
            
        elif self.tabla_activa == self.Tabla_11_e:
            self.Tabla_11_e.add_row(datos_completos_11[-1])
            
            
        elif self.tabla_activa == self.Tabla_12_e:
            self.Tabla_12_e.add_row(datos_completos_12[-1])
            
            
        elif self.tabla_activa == self.Tabla_13_e:
            self.Tabla_13_e.add_row(datos_completos_13[-1])
        
        
        self.tabla_activa = None
        self.lista_datos_activa = None
        self.indice_selec = -1
        
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Eliminar_fila(self):
        
        if self.lista_datos_activa is None or self.indice_selec <= 0:
            messagebox.showwarning("ATENCION", "Primero seleccione una fila de una tabla")
            return
        
        confirmar = messagebox.askyesno("CONFIRMAR", "¿Estás seguro de que deseas eliminar esta fila?")
        
        if confirmar:
            try:
                
                if self.tabla_activa == self.Tabla_1_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_1_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_2_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_2_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_3_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_3_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_4_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_4_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_5_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_5_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_6_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_6_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_7_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_7_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_8_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_8_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_9_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_9_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_10_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_10_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_11_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_11_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_12_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_12_e.delete_row(indice_a_borrar)
                    
                    
                elif self.tabla_activa == self.Tabla_13_e:
                    indice_a_borrar = self.indice_selec - 1
                    self.lista_datos_activa.pop(indice_a_borrar)
                    self.Tabla_13_e.delete_row(indice_a_borrar)
                
                self.Actualizar_tabla()
                
                self.Valor.delete(0, "end")
                self.Probabilidad.delete(0, "end")
                self.indice_selec = -1
                
                messagebox.showinfo("EXITO", "Fila eliminada correctamente")
                
            except Exception as e:
                messagebox.showerror("ERROR", f"No se pudo eliminar: {e}")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------

#Tabla Principal (monte carlo)

    
    def Creacion_tabla(self):
        
        try:
            
            if not self.cant_dias.get():
                messagebox.showerror("ERROR", "Establesca los dias a simular")
                return
            
            if not self.cant_jabon.get() or not self.cost_jabon.get() or not self.cant_suavitel.get() or not self.cost_suavitel.get() or not self.cant_desmanchador.get() or not self.cost_desmanchador.get() or not self.cant_bolsas.get() or not self.cost_bolsas.get() or not self.cant_ganchos.get() or not self.cost_ganchos.get():
                messagebox.showerror("ERROR", "Establesca la cantidad y los costos de los insumos")
                return
            
            if not self.cant_maquinas.get():
                messagebox.showerror("ERROR", "Determine cuantas maquinas totales habra")
                return
                
            if not self.costos_diarios.get():
                messagebox.showerror("ERROR", "Ingresa los costos diarios")
                return
                
            
            self.filas_tabla_monte_carlo = int(self.cant_dias.get())
            
            self.cantidad_maquinas_total = int(self.cant_maquinas.get())
            
            
            
            self.val_cant_jabon = float(self.cant_jabon.get())
            self.val_cost_jabon = float(self.cost_jabon.get())
            
            self.val_cant_suavitel = float(self.cant_suavitel.get())
            self.val_cost_suavitel = float(self.cost_suavitel.get())
            
            self.val_cant_desmanchador = float(self.cant_desmanchador.get())
            self.val_cost_desmanchador = float(self.cost_desmanchador.get())
            
            self.val_cant_bolsas = float(self.cant_bolsas.get())
            self.val_cost_bolsas = float(self.cost_bolsas.get())
            
            self.val_cant_ganchos = float(self.cant_ganchos.get())
            self.val_cost_ganchos = float(self.cost_ganchos.get())
            
            
            
            self.val_costo_diaro = float(self.costos_diarios.get())
            
        except Exception as e:
                messagebox.showerror("INVALIDACION",F"Datos invalidos{e}", parent= self.Interfaz)
                return False
            
        if self.Tabla:
            self.Tabla.destroy()
            
        # encabezados = [["Dias", "Aleatorio\ncargas", "Rango de\nCargas", "Cargas\nExactas", "Aleatorio\ntipo de\ncargas", "Tipo de\ncargas","Aleatorio\nmaquinas", "Cantidad de\nmaquinas", "Aleatorio\ntiempo de\nciclo", "Tiempo de\nciclo", "Aleatorio\nestado\nmaquinas", "Estado\nmaquinas", "Tiempo"]]
        
        
        encabezados = [["Dias", "Aleatorio\ncargas", "Rango de\nCargas", "Cargas\nExactas", "Tipo de\ncarga mas\ndemandada", "Promedio\nciclo", "Cantidad de\nmaquinas\ncon fallas", "Promedio dias\nde reparacion", "Cantidad de\ndias de\nreparacion\ntotal", "Cantidad\nde ropa\ndañada", "Cantidad\nde jabon\nusado", "Cantidad\nde suavitel\nusado", "Cantidad de\ndesmanchador\nusado", "Cantidad\nde bolsas\nusadas", "Cantidad\nde ganchos\nusados","Candidad de\ninsumos usados", "Promedio de\ninsumos usados","Tiempo\ntotal de\ntrabajo de\nlas maquinas", "Costos", "Perdidas", "Ganancias"]]
        
        for i in range(self.filas_tabla_monte_carlo):
            fila_vacia = [str(i+1)] + [""] * 12
            encabezados.append(fila_vacia)
            
        #crear la tabla principal
        
        self.Tabla = CTkTable(
            master = self.scroll_frame, 
            row = self.filas_tabla_monte_carlo + 1, 
            column= len(encabezados[0]), #12 
            values= encabezados,
            width = 100,
            justify = "center",
            wraplength = 80
        )
        
        #mostrar tabla
        self.Tabla.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.Generacion_aleatorios()
    
    
    def Generacion_aleatorios(self):
        
        self.L_tabla_1 = []
        # self.L_tabla_2 = []
        # self.L_tabla_3 = []
        # self.L_tabla_4 = []
        # self.L_tabla_5 = []
        
        for _ in range(self.filas_tabla_monte_carlo):
            
            self.contador += 1
            ale_tabla_1 = round(GeneraRandom.aleatorio(self.contador), 4)

            # ale_tabla_2 = round(random.random(), 4)
            # ale_tabla_3 = round(random.random(), 4)
            # ale_tabla_4 = round(random.random(), 4)
            # ale_tabla_5 = round(random.random(), 4)
            
            
            self.L_tabla_1.append(ale_tabla_1)
            # self.L_tabla_2.append(ale_tabla_2)
            # self.L_tabla_3.append(ale_tabla_3)
            # self.L_tabla_4.append(ale_tabla_4)
            # self.L_tabla_5.append(ale_tabla_5)
            
            
            # Aleatorios 1  (cargas exactas)
            
            columna_tabla_1 = 1
            for indice_1 in range(len(self.L_tabla_1)):
                valor_1 = self.L_tabla_1[indice_1]
                
                self.Tabla.insert(indice_1 + 1, columna_tabla_1, valor_1)

        # print("Mostrar tabla")
        # print(self.L_tabla_1)
            
            
            # Aleatorios 2 (tipos de cargas)
            
            # columna_tabla_2 = 4
            # for indice_2 in range(len(self.L_tabla_2)):
            #     valor_2 = self.L_tabla_2[indice_2]
                
            #     self.Tabla.insert(indice_2 + 1, columna_tabla_2, valor_2)
            
            
            
            # Aleatorios 3 (estados de maquinas)
            
            # columna_tabla_3 = 10
            # for indice_3 in range(len(self.L_tabla_3)):
            #     valor_3 = self.L_tabla_3[indice_3]
                
            #     self.Tabla.insert(indice_3 + 1, columna_tabla_3, valor_3)
            
            
            
            # Aleatorios 4 (numero de maquinas)
            
            # columna_tabla_4 = 6
            # for indice_4 in range(len(self.L_tabla_4)):
            #     valor_4 = self.L_tabla_4[indice_4]
                
            #     self.Tabla.insert(indice_4 + 1, columna_tabla_4, valor_4)
            
            
            
            # Aleatorios 5 (tiempo de ciclo)
            
            # columna_tabla_5 = 8
            # for indice_5 in range(len(self.L_tabla_5)):
            #     valor_5 = self.L_tabla_5[indice_5]
                
            #     self.Tabla.insert(indice_5 + 1, columna_tabla_5, valor_5)
            
        self.Probabilidades_Cargas_dias()
    
    
    def Probabilidades_Cargas_dias(self):
        
        #comparar con los rangos
        
        resultados_tabla_1 = []
        self.resultados_cargas_exactos = []
        
        for ale in self.L_tabla_1:
            
            for fila in self.Tabla_1_e_d:
                
                str_rango = fila[-1]
                partes = str_rango.split(" - ")
                
                inf = float(partes[0].strip())
                sup = float(partes[1].strip())
                
                
                
                if ale > inf and ale <= sup:
                    
                    valor_correcto = fila[0]
                    
                    resultados_tabla_1.append(valor_correcto)
                    
                    
                    
                    
                    #Encontrar las cargas exactas
                    
                    parte_c_e = valor_correcto.split(" - ")
                    primero = int(parte_c_e[0].strip())
                    segundo = int(parte_c_e[1].strip())
                    
                    
                    res = random.randint(primero, segundo)
                    
                    
                    self.resultados_cargas_exactos.append(res)
                    
                    break
                
                
                
            # Cargas Dias
            
            columna_tabla_1 = 2
            for indice_1 in range(len(resultados_tabla_1)):
                valor_1 = resultados_tabla_1[indice_1]
                
                self.Tabla.insert(indice_1 + 1, columna_tabla_1, valor_1)
            
            
            #Cargas exactas 

            
            columna_tabla_1_1 = 3
            for indice_1_1 in range(len(self.resultados_cargas_exactos)):
                valor_1_1 = self.resultados_cargas_exactos[indice_1_1]
                
                self.Tabla.insert(indice_1_1 + 1, columna_tabla_1_1, valor_1_1)

        # genero las tablas de los recidentes, para la vediricacion de estos -----------------------------

        print(self.L_tabla_1)
        print(self.resultados_cargas_exactos)
        def llamarTablas():
            self.GenerarTlas(self.L_tabla_1, self.resultados_cargas_exactos)

        botonsito = ctk.CTkButton(self.scroll_frame_det, text="generar tablas residentes", command=lambda:llamarTablas())
        botonsito.pack(padx=20,pady=20)

        # --------------------------------------------------
            
            
        self.Tipo_cargas_moda()
    
    
    def Tipo_cargas_moda (self):
        
        self.resultados_cargas = []
        self.resultados_conteo_cargas = []
        
        self.mas_demandadas = []
        
        for cargas in self.resultados_cargas_exactos:
            total_cargas = 0
            cargas_dia = []
            
            while total_cargas < cargas:
                self.contador += 1

                
                ale = round(GeneraRandom.aleatorio(self.contador), 4)
                
                for fila in self.Tabla_2_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes [0].strip())
                    sup = float(partes [1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        
                        total_cargas += 1
                        
                        cargas_dia.append(valor_correcto)
                        
                        break
                        
                        
            self.resultados_cargas.append(cargas_dia)
            
            
            
            cant = []
            
            for fila in self.Tabla_2_e_d:
                cant.append(0)
                
                
            for carg in cargas_dia:
                
                for i in range(len(self.Tabla_2_e_d)):
                    
                    opcion = self.Tabla_2_e_d[i][0]
                    
                    if carg == opcion:
                        cant[i] += 1
                            
            self.resultados_conteo_cargas.append(cant)
            
            
            conteo = -1
            tipo_carga_moda = ""
            
            for tc in range(len(cant)):
                if cant[tc] > conteo:
                    conteo = cant[tc]
                    tipo_carga_moda = self.Tabla_2_e_d[tc][0]
                    
            self.mas_demandadas.append(tipo_carga_moda)
            
            
        columna_tipo_cargas_demandadas = 4
        for indice_2 in range(len(self.mas_demandadas)):
            valor_t_c = self.mas_demandadas[indice_2]
            
            self.Tabla.insert(indice_2 + 1, columna_tipo_cargas_demandadas, str(valor_t_c))
            
        
        self.Dato_tabla_3_det()
        
        
    def Dato_tabla_3_det(self):
        #promedio de tiempo de ciclo
        
        self.resultados_tiempo_ciclo = []
        self.resultados_conteo_tiempo_ciclo = []
        
        
        for cargas in self.resultados_cargas_exactos:
            
            tiempo_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = round(GeneraRandom.aleatorio(self.contador), 4)
                
                for fila in self.Tabla_3_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes [0].strip())
                    sup = float(partes [1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        tiempo_dia.append(valor_correcto)
                        
                        break
                    
            self.resultados_tiempo_ciclo.append(tiempo_dia)
            
            
            cant = []
            
            for fila in self.Tabla_3_e_d:
                cant.append(0)
                
            for tiempo_ciclo in tiempo_dia:
                
                for i in range(len(self.Tabla_3_e_d)):
                    
                    opcion = self.Tabla_3_e_d[i][0]
                    
                    if tiempo_ciclo == opcion:
                        cant[i] += 1
                        break
                    
            self.resultados_conteo_tiempo_ciclo.append(cant)
            
        # self.Tablas_Detalles()
        self.Dato_tabla_4_det()
    
    
    
    def acutalizar_maquinas_des(self):
        nuevas = []
        
        for dias_rest in self.maquinas_descompuestas:
            
            dias_rest -= 1
            
            if dias_rest > 0:
                nuevas.append(dias_rest)
        
        self.maquinas_descompuestas = nuevas
    
    
    def Dato_tabla_4_det(self):
        
        #estados de las maquinas
        
        #self.cantidad_maquinas_total = int(self.cant_maquinas.get())
        
        self.resultados_estado_maquinas = []
        self.resultados_conteo_estado_maquinas = []
        self.resultados_cant_fallas = []
        
        
        for cargas in self.resultados_cargas_exactos:
            
            self.acutalizar_maquinas_des()
            
            estado_dia = []
            
            for i in range(self.cantidad_maquinas_total):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                
                for fila in self.Tabla_4_e_d:
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes [0].strip())
                    sup = float(partes [1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        estado_dia.append(valor_correcto)
                        
                        break
                    
                    
            self.resultados_estado_maquinas.append(estado_dia)
            
            cant = []
            
            for fila in self.Tabla_4_e_d:
                cant.append(0)
                
            for estado in estado_dia:
                
                for i in range(len(self.Tabla_4_e_d)):
                    
                    opcion = self.Tabla_4_e_d[i][0]
                    
                    if estado == opcion:
                        cant[i] += 1
                        break
                    
            self.resultados_conteo_estado_maquinas.append(cant)
            
            
            #solo fallas en las maquinas
            
            total_maqu_fallas = 0
            
            for i in range(len(self.Tabla_4_e_d)):
                
                if self.Tabla_4_e_d[i][0] == "Falla":
                    
                    total_maqu_fallas = cant[i]
                    
                    break
                
            self.resultados_cant_fallas.append(total_maqu_fallas)
                
                
                
                
        columna_fallas_maquinas = 6
        for indice_4 in range(len(self.resultados_cant_fallas)):
            valor_4 = self.resultados_cant_fallas[indice_4]
            
            self.Tabla.insert(indice_4 + 1, columna_fallas_maquinas, str(valor_4))
        
        
        # self.Tablas_Detalles()
        self.Dato_tabla_5_det()
    
    
    def Dato_tabla_5_det(self):
        
        #promedio dias de reparacion
        
        self.resultados_dias_reparacion = []
        self.resultados_conteo_dias_reparacion = []
        
        self.resultados_total_reparacion = []
        self.resultados_promedio_reparacion = []
        
        for fallas in self.resultados_cant_fallas:
            
            reparaciones_dia = []
            
            for i in range(fallas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_5_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        #encontrar el tiempo exacto          
                        parte_t_e = valor_correcto.split(" - ")
                        primero = int(parte_t_e[0].strip())
                        segundo = int(parte_t_e[1].strip())
                        
                        res = random.randint(primero, segundo)
                        
                        reparaciones_dia.append(res)
                        
                        break
                    
                    
            self.resultados_dias_reparacion.append(reparaciones_dia)
            
            
            cant = []
            
            for fila in self.Tabla_5_e_d:
                cant.append(0)
                
                
            for dias in reparaciones_dia:
                
                for i in range(len(self.Tabla_5_e_d)):
                    
                    opcion = self.Tabla_5_e_d[i][0]
                    
                    
                    part = opcion.split(" - ")
                    
                    if len(part) == 2:
                        ini = int(part[0].strip())
                        fin = int(part[1].strip())
                        
                        if dias >= ini and dias <= fin :
                            cant[i] += 1
                            
                            break
                    else:
                        
                        valor = int(opcion)
                        
                        
                        if dias == valor:
                            cant[i] += 1
                            
                            break
                        
                    # if dias == opcion:
                        
                    #     cant[i] += 1
                        
                    #     break
                    
            self.resultados_conteo_dias_reparacion.append(cant)
            
            
            #total dias de repaciones
            
            total_dias = sum(reparaciones_dia)
            
            self.resultados_total_reparacion.append(total_dias)
            
            
            #promedio dias de repaciones
            if len(reparaciones_dia) > 0:
                
                promedio = round(total_dias / len(reparaciones_dia), 2)
                
            else:
                
                promedio = 0
                
                
            self.resultados_promedio_reparacion.append(promedio)
        
        
        # self.Tablas_Detalles()
        self.Dato_tabla_6_det()
    
    
    def Dato_tabla_6_det(self):
        
        #cantidad de daño a la ropa
        
        self.resultados_daños_ropa = []
        self.resultados_conteo_daños_ropa = []
        self.resultados_total_daños = []
        
        for cargas in self.resultados_cargas_exactos:
            
            daños_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                
                # ale = random.random()
                
                for fila in self.Tabla_6_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        daños_dia.append(valor_correcto)
                        
                        break
                    
                    
            self.resultados_daños_ropa.append(daños_dia)
            
            cant = []
            
            for fila in self.Tabla_6_e_d:
                cant.append(0)
                
            for daño in daños_dia:
                
                for i in range(len(self.Tabla_6_e_d)):
                    
                    opcion = self.Tabla_6_e_d[i][0]
                    
                    if daño == opcion:
                        
                        cant[i] += 1
                        
                        break
            
            self.resultados_conteo_daños_ropa.append(cant)
            
            total_ropa_dañada = 0
            
            for i in range(len(self.Tabla_6_e_d)):
                
                if self.Tabla_6_e_d[i][0] != "No":
                    
                    total_ropa_dañada += cant[i]
                    
                    
            self.resultados_total_daños.append(total_ropa_dañada)
        
        columna_cant_ropa_dañada = 9
        for indice_6 in range(len(self.resultados_total_daños)):
            valor_6 = self.resultados_total_daños[indice_6]
            
            self.Tabla.insert(indice_6 + 1, columna_cant_ropa_dañada, str(valor_6))
        
        # self.Tablas_Detalles()
        self.Dato_tabla_7_det()
    
    
    def Dato_tabla_7_det(self):
        
        self.resultados_jabon = []
        self.resultados_conteos_jabon = []
        
        for cargas in self.resultados_cargas_exactos:
            
            total_jabon_dia = 0
            
            jabon_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_7_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        part = valor_correcto.split(" - ")
                        
                        if len(part) == 2:
                            ini = int(part[0].strip())
                            fin = int(part[1].strip())
                            
                            valor_exacto = random.randint(ini, fin)
                            total_jabon_dia += valor_exacto
                            jabon_dia.append(valor_correcto)
                            
                        else:
                            valor_exacto = int(valor_correcto)
                            total_jabon_dia += valor_exacto
                            jabon_dia.append(valor_correcto)
                            
                            
                        break
                    
            self.resultados_jabon.append(total_jabon_dia)
            
            cant = []
            
            for fila in self.Tabla_7_e_d:
                cant.append(0)
                
            for cant_jabon in jabon_dia:
                
                for i in range(len(self.Tabla_7_e_d)):
                    
                    opcion = self.Tabla_7_e_d[i][0]
                    
                    if cant_jabon == opcion:
                        cant[i] += 1 
                        break
                    
            self.resultados_conteos_jabon.append(cant)
        
        self.Dato_tabla_8_det()
    
    
    def Dato_tabla_8_det(self):
        
        self.resultados_suavitel = []
        self.resultados_conteos_suavitel = []
        
        for cargas in self.resultados_cargas_exactos:
            
            total_suavitel_dia = 0
            
            suavitel_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_8_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        part = valor_correcto.split(" - ")
                        
                        if len(part) == 2:
                            ini = int(part[0].strip())
                            fin = int(part[1].strip())
                            
                            valor_exacto = random.randint(ini, fin)
                            total_suavitel_dia += valor_exacto
                            suavitel_dia.append(valor_correcto)
                            
                        else:
                            valor_exacto = int(valor_correcto)
                            total_suavitel_dia += valor_exacto
                            suavitel_dia.append(valor_correcto)
                            
                            
                        break
                    
            self.resultados_suavitel.append(total_suavitel_dia)
            
            cant = []
            
            for fila in self.Tabla_8_e_d:
                cant.append(0)
                
            for cant_suavitel in suavitel_dia:
                
                for i in range(len(self.Tabla_8_e_d)):
                    
                    opcion = self.Tabla_8_e_d[i][0]
                    
                    if cant_suavitel == opcion:
                        cant[i] += 1 
                        break
                    
            self.resultados_conteos_suavitel.append(cant)
            
        self.Dato_tabla_9_det()
    
    
    def Dato_tabla_9_det(self):
        
        self.resultados_desmanchador = []
        self.resultados_conteos_desmanchador = []
        
        for cargas in self.resultados_cargas_exactos:
            
            total_desmanchador_dia = 0
            
            desmanchador_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_9_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        part = valor_correcto.split(" - ")
                        
                        if len(part) == 2:
                            ini = int(part[0].strip())
                            fin = int(part[1].strip())
                            
                            valor_exacto = random.randint(ini, fin)
                            total_desmanchador_dia += valor_exacto
                            desmanchador_dia.append(valor_correcto)
                            
                        else:
                            valor_exacto = int(valor_correcto)
                            total_desmanchador_dia += valor_exacto
                            desmanchador_dia.append(valor_correcto)
                            
                        break
                    
            self.resultados_desmanchador.append(total_desmanchador_dia)
            
            cant = []
            
            for fila in self.Tabla_9_e_d:
                cant.append(0)
                
            for cant_desman in desmanchador_dia:
                
                for i in range(len(self.Tabla_9_e_d)):
                    
                    opcion = self.Tabla_9_e_d[i][0]
                    
                    if cant_desman == opcion:
                        cant[i] += 1
            
            self.resultados_conteos_desmanchador.append(cant)
            
        self.Dato_tabla_10_det()
    
    
    def Dato_tabla_10_det(self):
        
        self.resultados_bolsas = []
        self.resultados_conteos_bolsas = []
        
        for cargas in self.resultados_cargas_exactos:
            
            total_bolsas_dia = 0
            
            bolsas_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_10_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        part = valor_correcto.split(" - ")
                        
                        if len(part) == 2:
                            ini = int(part[0].strip())
                            fin = int(part[1].strip())
                            
                            valor_exacto = random.randint(ini, fin)
                            total_bolsas_dia += valor_exacto
                            bolsas_dia.append(valor_correcto)
                            
                        else:
                            valor_exacto = int(valor_correcto)
                            total_bolsas_dia += valor_exacto
                            bolsas_dia.append(valor_correcto)
                            
                            
                        break
                    
            self.resultados_bolsas.append(total_bolsas_dia)
            
            cant = []
            
            for fila in self.Tabla_10_e_d:
                cant.append(0)
                
            for cant_bolsas in bolsas_dia:
                
                for i in range(len(self.Tabla_10_e_d)):
                    
                    opcion = self.Tabla_10_e_d[i][0]
                    
                    if cant_bolsas == opcion:
                        cant[i] += 1
            
            self.resultados_conteos_bolsas.append(cant)
            
        self.Dato_tabla_11_det()
        # self.Tablas_Detalles()
        
    
    def Dato_tabla_11_det(self):
        
        self.resultados_ganchos = []
        self.resultados_conteos_ganchos = []
        
        for cargas in self.resultados_cargas_exactos:
            
            total_ganchos_dia = 0
            
            ganchos_dia = []
            
            for i in range(cargas):
                self.contador += 1
                ale = GeneraRandom.aleatorio(self.contador)
                # ale = random.random()
                
                for fila in self.Tabla_11_e_d:
                    
                    str_rango = fila[-1]
                    partes = str_rango.split(" - ")
                    
                    inf = float(partes[0].strip())
                    sup = float(partes[1].strip())
                    
                    if ale > inf and ale <= sup:
                        
                        valor_correcto = fila[0]
                        
                        part = valor_correcto.split(" - ")
                        
                        if len(part) == 2:
                            ini = int(part[0].strip())
                            fin = int(part[1].strip())
                            
                            valor_exacto = random.randint(ini, fin)
                            total_ganchos_dia += valor_exacto
                            ganchos_dia.append(valor_correcto)
                            
                        else:
                            valor_exacto = int(valor_correcto)
                            total_ganchos_dia += valor_exacto
                            ganchos_dia.append(valor_correcto)
                            
                            
                        break
                    
            self.resultados_ganchos.append(total_ganchos_dia)
            
            cant = []
            
            for fila in self.Tabla_11_e_d:
                cant.append(0)
                
            for cant_ganchos in ganchos_dia:
                
                for i in range(len(self.Tabla_11_e_d)):
                    
                    opcion = self.Tabla_11_e_d[i][0]
                    
                    if cant_ganchos == opcion:
                        cant[i] += 1
            
            self.resultados_conteos_ganchos.append(cant)
            
        self.Tablas_Detalles()
    
    
    def Costos_diarios (self):
        
        try:
            
            if not self.costos_diarios.get():
                messagebox.showerror("ERROR", "Ingresa los costos diarios")
                
                self.val_costos_diaros = float(self.costos_diarios.get())
                
        except ValueError:
            messagebox.showerror("ERROR", "Valor invalido")
    
    
    def Tablas_Detalles(self):
        
        #---------------------------------------------------------
        
        #tipos de cargas
        
        self.valores_enca_2 = ["Dias"]
        
        for val in self.Tabla_2_e_d:
            valores = val[0]
            self.valores_enca_2.append(valores)
        
        
        encabezado_2 = [self.valores_enca_2]
        
        
        self.Titulo_t_2_det = CTkLabel(self.scroll_frame_det, text= "Tipos de cargas", font= ("Arial", 30 ))
        self.Titulo_t_2_det.pack(pady=10, padx=10)
        
        self.Titulo_t_2_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_2_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteo_cargas)):
            fila_vacia = [str(i+1)]
            encabezado_2.append(fila_vacia)
        
        
        self.Tabla_2_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteo_cargas) + 1,
            column= len(self.valores_enca_2),
            values= encabezado_2,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_2_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_tipo_cargas_detalles()
        
        
        #---------------------------------------------------------
        
        
        #tiempo de ciclo 
        
        self.valores_enca_3 = ["Dias"]
        
        for val in self.Tabla_3_e_d:
            valores = val[0]
            self.valores_enca_3.append(valores)
        
        
        encabezado_3 = [self.valores_enca_3] 
        
        
        self.Titulo_t_3_det = CTkLabel(self.scroll_frame_det, text= "Tiempo de ciclo", font= ("Arial", 30 ))
        self.Titulo_t_3_det.pack(pady=10, padx=10)
        
        self.Titulo_t_3_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_3_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteo_tiempo_ciclo)):
            fila_vacia = [str(i+1)]
            encabezado_3.append(fila_vacia)
        
        
        self.Tabla_3_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteo_tiempo_ciclo) + 1,
            column= len(self.valores_enca_3),
            values= encabezado_3,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_3_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_tiempo_ciclo()
        
        #---------------------------------------------------------
        
        #cantidad de fallas
        
        self.valores_enca_4 = ["Dias"]
        
        for val in self.Tabla_4_e_d:
            valores = val[0]
            self.valores_enca_4.append(valores)
        
        
        encabezado_4 = [self.valores_enca_4] 
        
        
        self.Titulo_t_4_det = CTkLabel(self.scroll_frame_det, text= "Estado de las maquinas", font= ("Arial", 30 ))
        self.Titulo_t_4_det.pack(pady=10, padx=10)
        
        self.Titulo_t_4_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_4_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteo_estado_maquinas)):
            fila_vacia = [str(i+1)]
            encabezado_4.append(fila_vacia)
        
        
        self.Tabla_4_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteo_estado_maquinas) + 1,
            column= len(self.valores_enca_4),
            values= encabezado_4,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_4_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_fallas_maquinas()
        
        
        #---------------------------------------------------------
        
        #tiempo de raparacion
        
        self.valores_enca_5 = ["Dias"]
        
        for val in self.Tabla_5_e_d:
            valores = val[0]
            self.valores_enca_5.append(valores)
        
        
        encabezado_5 = [self.valores_enca_5] 
        
        
        self.Titulo_t_5_det = CTkLabel(self.scroll_frame_det, text= "Dias de reparacion", font= ("Arial", 30 ))
        self.Titulo_t_5_det.pack(pady=10, padx=10)
        
        self.Titulo_t_5_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_5_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteo_dias_reparacion)):
            fila_vacia = [str(i+1)]
            encabezado_5.append(fila_vacia)
        
        
        self.Tabla_5_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteo_dias_reparacion) + 1,
            column= len(self.valores_enca_5),
            values= encabezado_5,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_5_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_prom_tiempo_repacion()
        
        #---------------------------------------------------------
        
        #cantidad de daños
        
        self.valores_enca_6 = ["Dias"]
        
        for val in self.Tabla_6_e_d:
            valores = val[0]
            self.valores_enca_6.append(valores)
        
        
        encabezado_6 = [self.valores_enca_6] 
        
        
        self.Titulo_t_6_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de daños a la ropa", font= ("Arial", 30 ))
        self.Titulo_t_6_det.pack(pady=10, padx=10)
        
        self.Titulo_t_6_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_6_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteo_daños_ropa)):
            fila_vacia = [str(i+1)]
            encabezado_6.append(fila_vacia)
        
        
        self.Tabla_6_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteo_daños_ropa) + 1,
            column= len(self.valores_enca_6),
            values= encabezado_6,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_6_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_daños_ropa()
        
        
        #---------------------------------------------------------
        
        #cantidad de uso de jabon
        
        self.valores_enca_7 = ["Dias"]
        
        for val in self.Tabla_7_e_d:
            valores = val[0]
            self.valores_enca_7.append(valores)
        
        
        encabezado_7 = [self.valores_enca_7] 
        
        
        self.Titulo_t_7_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de uso del jabon", font= ("Arial", 30 ))
        self.Titulo_t_7_det.pack(pady=10, padx=10)
        
        self.Titulo_t_7_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_7_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteos_jabon)):
            fila_vacia = [str(i+1)]
            encabezado_7.append(fila_vacia)
        
        
        self.Tabla_7_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteos_jabon) + 1,
            column= len(self.valores_enca_7),
            values= encabezado_7,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_7_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_jabon()
        
        #---------------------------------------------------------
        
        #cantidad de uso de suavitel
        
        self.valores_enca_8 = ["Dias"]
        
        for val in self.Tabla_8_e_d:
            valores = val[0]
            self.valores_enca_8.append(valores)
        
        
        encabezado_8 = [self.valores_enca_8] 
        
        
        self.Titulo_t_8_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de uso del suavitel", font= ("Arial", 30 ))
        self.Titulo_t_8_det.pack(pady=10, padx=10)
        
        self.Titulo_t_8_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_8_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteos_suavitel)):
            fila_vacia = [str(i+1)]
            encabezado_8.append(fila_vacia)
        
        
        self.Tabla_8_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteos_suavitel) + 1,
            column= len(self.valores_enca_8),
            values= encabezado_8,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_8_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_suavitel()
        
        #---------------------------------------------------------
        
        #cantidad de uso de desmanchador
        
        self.valores_enca_9 = ["Dias"]
        
        for val in self.Tabla_9_e_d:
            valores = val[0]
            self.valores_enca_9.append(valores)
        
        
        encabezado_9 = [self.valores_enca_9] 
        
        
        self.Titulo_t_9_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de uso del desmanchador", font= ("Arial", 30 ))
        self.Titulo_t_9_det.pack(pady=10, padx=10)
        
        self.Titulo_t_9_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_9_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteos_desmanchador)):
            fila_vacia = [str(i+1)]
            encabezado_9.append(fila_vacia)
        
        
        self.Tabla_9_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteos_desmanchador) + 1,
            column= len(self.valores_enca_9),
            values= encabezado_9,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_9_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_desmanchador()
        
        #---------------------------------------------------------
        
        #cantidad de uso de bolsas
        
        self.valores_enca_10 = ["Dias"]
        
        for val in self.Tabla_10_e_d:
            valores = val[0]
            self.valores_enca_10.append(valores)
        
        
        encabezado_10 = [self.valores_enca_10] 
        
        
        self.Titulo_t_10_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de uso de las bolsas", font= ("Arial", 30 ))
        self.Titulo_t_10_det.pack(pady=10, padx=10)
        
        self.Titulo_t_10_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_10_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteos_bolsas)):
            fila_vacia = [str(i+1)]
            encabezado_10.append(fila_vacia)
        
        
        self.Tabla_10_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteos_bolsas) + 1,
            column= len(self.valores_enca_10),
            values= encabezado_10,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_10_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_bolsas()
        
        
        #---------------------------------------------------------
        
        #cantidad de uso de ganchos
        
        self.valores_enca_11 = ["Dias"]
        
        for val in self.Tabla_11_e_d:
            valores = val[0]
            self.valores_enca_11.append(valores)
        
        
        encabezado_11 = [self.valores_enca_11] 
        
        
        self.Titulo_t_11_det = CTkLabel(self.scroll_frame_det, text= "Cantidad de uso de ganchos", font= ("Arial", 30 ))
        self.Titulo_t_11_det.pack(pady=10, padx=10)
        
        self.Titulo_t_11_objetivo = CTkLabel(self.scroll_frame_det, text= "Cantidad de veces que salio el valor en un dia", font= ("Arial", 20))
        self.Titulo_t_11_objetivo.pack(pady=15, padx=10)
        
        
        for i in range(len(self.resultados_conteos_ganchos)):
            fila_vacia = [str(i+1)]
            encabezado_11.append(fila_vacia)
        
        
        self.Tabla_11_e_det = CTkTable(
            self.scroll_frame_det,
            row= len(self.resultados_conteos_ganchos) + 1,
            column= len(self.valores_enca_11),
            values= encabezado_11,
            justify = "center",
            header_color="#0a2e57"
        )
        
        
        self.Tabla_11_e_det.pack(expand=True, fill="both", pady=(0, 50))
        
        self.Tabla_ganchos()
        
        #---------------------------------------------------------
        
        
    def Tabla_tipo_cargas_detalles(self):
        fila_actual = 1
        
        for indice_2 in range(len(self.resultados_conteo_cargas)):
            valor_2 = self.resultados_conteo_cargas[indice_2]
            
            columna_actual = 1
            
            for num in valor_2:
                self.Tabla_2_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
            fila_actual += 1
        
        
    # def Tabla_tiempo_ciclo(self):
        
    #     fila_actual = 1
        
    #     self.horas_trabajadas_por_dia = []
        
    #     for indice_3 in range(len(self.resultados_conteo_tiempo_ciclo)):
    #         valor_3 = self.resultados_conteo_tiempo_ciclo[indice_3]
            
            
    #         columna_actual = 1
            
            
    #         for num in valor_3:
    #             self.Tabla_3_e_det.insert(fila_actual, columna_actual, str(num))
                
    #             columna_actual += 1
                
                
                
                
                
    #         minutos_totales_dia = 0
    #         cant_cargas_dia = 0
            
            
    #         for i in range(len(valor_3)):
    #             fila_ciclo = valor_3[i]
                
    #             cant_cargas_dia += fila_ciclo
                
    #             val_tiempo_dia = self.Tabla_3_e_d[i][0]

    #             minutos_totales_dia += fila_ciclo * val_tiempo_dia
                
    #             hora = round((minutos_totales_dia / 60), 2)
                
    #             texto_tiempo = str(minutos_totales_dia) + "min" + "\n" + str(hora) + "hrs"
                
                
    #         #promedio 
    #         if cant_cargas_dia > 0:
    #             promedio_total = round((minutos_totales_dia / cant_cargas_dia), 2)
                
    #         else:
    #             promedio_total = 0
                
            
            
    #         columna_prom_tiempo_ciclo = 5
    #         self.Tabla.insert(fila_actual, columna_prom_tiempo_ciclo, str(promedio_total))
            
    #         columna_tiempo_total_ciclo = 17
    #         self.Tabla.insert(fila_actual, columna_tiempo_total_ciclo, str(texto_tiempo))
            
    #         fila_actual += 1
        
    def Tabla_tiempo_ciclo(self):
        
        fila_actual = 1
        self.horas_trabajadas_por_dia = []
        
        for indice_3 in range(len(self.resultados_conteo_tiempo_ciclo)):
            valor_3 = self.resultados_conteo_tiempo_ciclo[indice_3]
            
            columna_actual = 1
            
            for num in valor_3:
                self.Tabla_3_e_det.insert(fila_actual, columna_actual, str(num))
                columna_actual += 1
                
            minutos_totales_dia = 0
            cant_cargas_dia = 0
            
            for i in range(len(valor_3)):
                fila_ciclo = valor_3[i]
                cant_cargas_dia += fila_ciclo
                
                val_tiempo_dia = self.Tabla_3_e_d[i][0]
                minutos_totales_dia += fila_ciclo * val_tiempo_dia
            
            
            
            #Multiplicar si es por 1, 1.5, 2 o 0
            estados_dia = self.resultados_estado_maquinas[indice_3]
            
            multiplicador_dia = 1.0
            
            for estado in estados_dia:
                
                if estado != "Normal":
                    
                    for fila_12 in self.Tabla_12_e_d:
                        nombre_estado = fila_12[0]
                        valor_multiplicador = fila_12[1]
                        
                        if estado == nombre_estado:
                            multiplicador_dia = float(valor_multiplicador)
                            break
                        
                    break 
            
            minutos_totales_dia = minutos_totales_dia * multiplicador_dia
            
            hora = round((minutos_totales_dia / 60), 2)
            texto_tiempo = str(int(minutos_totales_dia)) + "min" + "\n" + str(hora) + "hrs"
                
            if cant_cargas_dia > 0:
                promedio_total = round((minutos_totales_dia / cant_cargas_dia), 2)
            else:
                promedio_total = 0
                
            columna_prom_tiempo_ciclo = 5
            self.Tabla.insert(fila_actual, columna_prom_tiempo_ciclo, str(promedio_total))
            
            columna_tiempo_total_ciclo = 17
            self.Tabla.insert(fila_actual, columna_tiempo_total_ciclo, str(texto_tiempo))
            
            fila_actual += 1
        
    def Tabla_fallas_maquinas (self):
        
        fila_actual = 1
        
        for indice_4 in range(len(self.resultados_conteo_estado_maquinas)):
            valor_4 = self.resultados_conteo_estado_maquinas[indice_4]
            
            columna_actual = 1
            
            for num in valor_4:
                self.Tabla_4_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
            
            fila_actual += 1
        
        
    def Tabla_prom_tiempo_repacion(self):
        
        fila_actual = 1
        
        for indice_5 in range(len(self.resultados_conteo_dias_reparacion)):
            
            valor = self.resultados_conteo_dias_reparacion[indice_5]
            
            columna_actual = 1
            
            for num in valor:
                self.Tabla_5_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
            
            columna_promedio_tiempo = 7
            self.Tabla.insert(fila_actual, columna_promedio_tiempo, str(self.resultados_promedio_reparacion[indice_5]))
            
            
            columna_total_tiempo = 8
            self.Tabla.insert(fila_actual, columna_total_tiempo, str(self.resultados_total_reparacion[indice_5]))
            
            
            fila_actual += 1
        
        
    def Tabla_daños_ropa(self):
        
        fila_actual = 1
        
        for indice_6 in range(len(self.resultados_conteo_daños_ropa)):
            
            valor = self.resultados_conteo_daños_ropa[indice_6]
            
            columna_actual = 1
            
            for num in valor:
                
                self.Tabla_6_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
            fila_actual += 1
        
        
    def Tabla_jabon(self):
        
        fila_actual = 1
        
        pieza_jabon = self.Tabla_13_e_d[0][1]
        
        for indice_7 in range(len(self.resultados_conteos_jabon)):
            valor_7 = self.resultados_conteos_jabon[indice_7]
            
            columna_actual = 1
            
            for num in valor_7:
                self.Tabla_7_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
            jabon_del_dia = self.resultados_jabon[indice_7]
            
            pieza = round((jabon_del_dia / pieza_jabon), 2)
            
            # self.Total_insumos += pieza
            self.piezas_jabon.append(pieza)
            
            texto_jabon = str(jabon_del_dia) + " g" + " * " + str(pieza_jabon) + "\n" + str(pieza) + " pieza(s)"
            
            columna_jabon_total_dia = 10
            self.Tabla.insert(fila_actual, columna_jabon_total_dia, texto_jabon)
            
            fila_actual += 1
        
        
    def Tabla_suavitel(self):
        
        fila_actual = 1
        
        pieza_suavitel = self.Tabla_13_e_d[1][1]
        
        for indice_8 in range(len(self.resultados_conteos_suavitel)):
            valor_8 = self.resultados_conteos_suavitel[indice_8]
            
            columna_actual = 1
            
            for num in valor_8:
                self.Tabla_8_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
            
            suavitel_del_dia = self.resultados_suavitel[indice_8]
            
            pieza = round((suavitel_del_dia / pieza_suavitel), 2)
            
            # self.Total_insumos += pieza
            self.piezas_suavitel.append(pieza)
            
            texto_suavitel = str(suavitel_del_dia) + " ml" + " * " + str(pieza_suavitel) + "\n" + str(pieza) + " pieza(s)"
            
            columna_suavitel_total_dia = 11
            self.Tabla.insert(fila_actual, columna_suavitel_total_dia, texto_suavitel)
            
            fila_actual += 1
    
    
    def Tabla_desmanchador(self):
        
        fila_actual = 1
        
        pieza_desmanchador = self.Tabla_13_e_d[2][1]
        
        for indice_9 in range(len(self.resultados_conteos_desmanchador)):
            valor_9 = self.resultados_conteos_desmanchador[indice_9]
            
            columna_actual = 1
            
            for num in valor_9:
                self.Tabla_9_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
                
            desmanchador_del_dia = self.resultados_desmanchador[indice_9]
            
            pieza = round((desmanchador_del_dia / pieza_desmanchador), 2)
            
            # self.Total_insumos += pieza
            
            self.piezas_desmanchador.append(pieza)
            
            texto_desmanchador = str(desmanchador_del_dia) + " ml" + " * " + str(pieza_desmanchador) + "\n" + str(pieza) + " pieza(s)"
            
            columna_desmanchador_total_dia = 12
            self.Tabla.insert(fila_actual, columna_desmanchador_total_dia, texto_desmanchador)
            
            fila_actual += 1
    
    
    def Tabla_bolsas(self):
        
        fila_actual = 1
        
        for indice_10 in range(len(self.resultados_conteos_bolsas)):
            valor_10 = self.resultados_conteos_bolsas[indice_10]
            
            columna_actual = 1
            
            for num in valor_10:
                self.Tabla_10_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
                
            bolsas_del_dia = self.resultados_bolsas[indice_10]
            
            # self.Total_insumos += bolsas_del_dia
            
            self.piezas_bolsas.append(bolsas_del_dia)
            
            texto_bolsas = str(bolsas_del_dia) + " pieza(s)"
            
            columna_bolsas_total_dia = 13
            self.Tabla.insert(fila_actual, columna_bolsas_total_dia, texto_bolsas)
            
            fila_actual += 1
    
    
    def Tabla_ganchos(self):
        
        fila_actual = 1
        
        for indice_11 in range(len(self.resultados_conteos_ganchos)):
            valor_11 = self.resultados_conteos_ganchos[indice_11]
            
            columna_actual = 1
            
            for num in valor_11:
                self.Tabla_11_e_det.insert(fila_actual, columna_actual, str(num))
                
                columna_actual += 1
                
            ganchos_del_dia = self.resultados_ganchos[indice_11]
            
            # self.Total_insumos += ganchos_del_dia
            
            self.piezas_ganchos.append(ganchos_del_dia)
            
            
            texto_ganchos = str(ganchos_del_dia) + " pieza(s)"
            
            columna_ganchos_total_dia = 14
            self.Tabla.insert(fila_actual, columna_ganchos_total_dia, texto_ganchos)
            
            fila_actual += 1
            
        self.Tabla_insumos_totales()
    
    
    def Tabla_insumos_totales(self):
        
        fila_actual = 1
        
        for indice_13 in range(self.filas_tabla_monte_carlo):
            
            jabon_dia = self.piezas_jabon[indice_13] 
            suavitel_dia = self.piezas_suavitel[indice_13] 
            desmanchador_dia = self.piezas_desmanchador[indice_13] 
            bolsas_dia = self.piezas_bolsas[indice_13] 
            ganchos_dia = self.piezas_ganchos[indice_13] 
            
            total_dia = jabon_dia + suavitel_dia + desmanchador_dia + bolsas_dia + ganchos_dia
            
            if self.filas_tabla_monte_carlo > 0:
                promedio_dia = round((total_dia / 5), 2)
            
            else:
                promedio_dia = 0
            
            columna_total_insumos = 15
            self.Tabla.insert(fila_actual, columna_total_insumos, str(total_dia))
            
            columna_promedio_insumos = 16
            self.Tabla.insert(fila_actual, columna_promedio_insumos, str(promedio_dia))
            
            fila_actual += 1
            
        self.Tabla_costos_diarios()
    
    
    def Tabla_costos_diarios(self):
        
        for dia in range(self.filas_tabla_monte_carlo):
            
            #piezas
            
            cant_piezas_jabon = self.piezas_jabon[dia]
            cant_piezas_suavitel = self.piezas_suavitel[dia]
            cant_piezas_desmanchador = self.piezas_desmanchador[dia]
            cant_piezas_bolsas = self.piezas_bolsas[dia]  
            cant_piezas_ganchos = self.piezas_ganchos[dia]
            
            
            #cantida * precio
            
            gasto_jabon = cant_piezas_jabon * float(self.val_cost_jabon)
            gasto_suavitel = cant_piezas_suavitel * float(self.val_cost_suavitel)
            gasto_desmanchador = cant_piezas_desmanchador * float(self.val_cost_desmanchador)
            gasto_bolsas = cant_piezas_bolsas * float(self.val_cost_bolsas)
            gasto_ganchos = cant_piezas_ganchos * float(self.val_cost_ganchos)
            
            #insuimos al dia
            total_insumos_del_dia = gasto_jabon + gasto_suavitel + gasto_desmanchador + gasto_bolsas + gasto_ganchos
            
            #costos
            costo_total_del_dia = round(self.val_costo_diaro + total_insumos_del_dia, 2)
            
            columna_costos_diarios = 18
            self.Tabla.insert(dia + 1, columna_costos_diarios, str(costo_total_del_dia))
            
        self.Tabla_perdidas_diarios()
    
    
    def Tabla_perdidas_diarios(self):
        
        costo_prenda_dañada_extraviada = 150.0  
        costo_falla = 500.0  
        costo_retrasos = 200.0      
        
        fila_actual = 1
        
        
        for dia in range(self.filas_tabla_monte_carlo):
            
            cantidad_fallas = self.resultados_cant_fallas[dia]
            cantidad_daños_ropa = self.resultados_total_daños[dia]
            
            daño_rop = cantidad_daños_ropa * costo_prenda_dañada_extraviada
            
            perdida_reparacion = cantidad_fallas * costo_falla
            
            
            
            perdida_por_retraso = 0.0
            
            estados_dia = self.resultados_conteo_estado_maquinas[dia]
            
            
            # if cantidad_fallas == 0:
                
            estados_dia = self.resultados_conteo_estado_maquinas[dia]
                
            cant_normales = 0
            for i in range(len(self.Tabla_4_e_d)):
                if self.Tabla_4_e_d[i][0] == "Normal":
                    cant_normales = estados_dia[i]
                    break
                
                
            for i in range(len(self.Tabla_4_e_d)):
                nombre_estado = self.Tabla_4_e_d[i][0]
                cantidad_en_este_estado = estados_dia[i]
                
                
                # for i in range(len(self.Tabla_4_e_d)):

                #     nombre_estado = self.Tabla_4_e_d[i][0]
                #     cantidad_en_este_estado = estados_dia[i]
                
                if cantidad_en_este_estado > cant_normales:
                    if nombre_estado == "Retraso" or nombre_estado == "Corte de luz / agua":
                        
                        for fila_12 in self.Tabla_12_e_d:
                            nom_estado = fila_12[0]
                            valor_mult = fila_12[1]
                            
                            if nombre_estado == nom_estado:
                                perdida_por_retraso = costo_retrasos * float(valor_mult)
                                break
                        break
                        
            t_perdidas = daño_rop + perdida_reparacion + perdida_por_retraso
            total_perdidas = round(t_perdidas, 2)
            
            texto_perdidas = "$ " + str(total_perdidas)
            
            columna_perdidas_diarias = 19  
            self.Tabla.insert(fila_actual, columna_perdidas_diarias, texto_perdidas)
            
            fila_actual += 1
            
        
        self.Tabla_ganancia()
    
    
    def Tabla_ganancia(self):
        
        cobro_ropa_lav = 200.0  
        
        fila_actual = 1
        
        # pos_ropa_huesp = 1 
        
        
        for dia in range(self.filas_tabla_monte_carlo):
            
            
            cargas = self.resultados_conteo_cargas[dia][1]
            
            
            ingreso_clientes = cargas * cobro_ropa_lav
            ganancia = round(ingreso_clientes, 2)
            
            
            texto_ganancia = "$ " + str(ganancia)
            
            
            columna_ganancias = 20
            self.Tabla.insert(fila_actual, columna_ganancias, texto_ganancia)
            
            fila_actual += 1
    
    
    def Limpiar(self):
        self.cant_dias.delete(0, "end")
        self.cant_maquinas.delete(0, "end")
        self.cant_insumos.delete(0, "end")
        self.costos_diarios.delete(0, "end")
    
    
    def GenerarTlas(self, lista1: list, lista2: list) -> None:
        """
        el la primera lista es de aleatorios y la segunda es de los resultados
        """
        self.ventanaTlablas = ctk.CTkToplevel()
        self.ventanaTlablas.geometry("500x500")
        self.ventanaTlablas.title("Ver aleatorios")

        # self.ventanaTlablas.after(100, self.ventanaTlablas.lift)
        
        self.ventanaTlablas.grid_columnconfigure(0, weight=1)
        self.ventanaTlablas.grid_rowconfigure(1, weight=1)

        lbl_aleatorio = ctk.CTkLabel(self.ventanaTlablas, text="Aleatorio", font=("Arial", 14, "bold"))
        lbl_aleatorio.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        

        lbl_evento = ctk.CTkLabel(self.ventanaTlablas, text="Evento", font=("Arial", 14, "bold"))
        lbl_evento.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.ventanaTlablas.grid_columnconfigure(0, weight=1)
        self.ventanaTlablas.grid_columnconfigure(1, weight=1)


        frame_tabla = ctk.CTkScrollableFrame(self.ventanaTlablas)
        frame_tabla.grid(row=1, column=0, columnspan=2, padx=15, pady=(0, 15), sticky="nsew")
        

        frame_tabla.grid_columnconfigure(0, weight=1)
        frame_tabla.grid_columnconfigure(1, weight=1)

        for i, (aleatorio, evento) in enumerate(zip(lista1, lista2)):

            lbl_val1 = ctk.CTkLabel(frame_tabla, text=str(aleatorio), font=("Arial", 12))
            lbl_val1.grid(row=i, column=0, padx=5, pady=2, sticky="ew")

            lbl_val2 = ctk.CTkLabel(frame_tabla, text=str(evento), font=("Arial", 12))
            lbl_val2.grid(row=i, column=1, padx=5, pady=2, sticky="ew")


Lavanderia()