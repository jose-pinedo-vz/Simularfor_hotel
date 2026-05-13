
#* Ya funciona la seleccion, actualizacion, agregacion y borar filas de la tablas de probabilidades 

from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from CTkTable import CTkTable

# Configuración de estilo
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Recepcion:
    
    def __init__(self):
        self.Interfaz = ctk.CTk()
        
        self.Interfaz.title("Interfaz --- Recepcion")
        
        self.Cargar_datos() 
        self.Calculos_probAcu_rang()
        
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
        
        self.Tablas_Editables()      
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Tercera pestaña
        
        self.Monte_carlo = self.tabview.tab("MONTE CARLO")
        
        #Titulo 
        
        self.Titulo_frame_der = CTkLabel(self.Monte_carlo, text= "MONTE CARLO", font= ("Arial", 30 ))
        self.Titulo_frame_der.pack(pady=10, padx=10)
        
        #Boton de simular
        
        self.btn_generar = CTkButton(self.Monte_carlo, text= "simular", font= ("Arial", 25) , command= self.Creacion_tabla)
        self.btn_generar.pack(pady=10)
        
        
        # Para que la tabla no se salga de la pantalla
        
        self.scroll_frame = CTkScrollableFrame(self.Monte_carlo)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Tabla = None
        
        self.Interfaz.update() 
        
        # try: 
        #     self.principal.state("zoomed")
        # except: 
        #     self.principal.attributes("-zoomed", True)
        
        
        self.Interfaz.state("zoomed") #windows
        # self.Interfaz.attributes('-zoomed', True) #Linux
        
        self.Interfaz.mainloop()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def Cargar_datos(self):
        
        #Tabla 1 
        self.Personas_dias = [
            ["10 - 15", 0.15],
            ["16 - 25", 0.35],
            ["26 - 40", 0.3],
            ["31 - 60", 0.2]
        ]

        #Tabla 2
        self.Tipos_atencion = [
            ["2 - 5", 0.3],
            ["6 - 10", 0.40],
            ["11 - 15", 0.2],
            ["16 - 20", 0.1]
        ]

        #Tabla 3
        self.recepcionistas_dias = [
            ["1", 0.1],
            ["2", 0.25],
            ["3", 0.45],
            ["4", 0.2]
        ]

        #Tabla 4
        self.Cantidad_abandonos = [
            ["No", 0.76],
            ["< 10 ", 0.12],
            ["11 a 20", 0.08],
            ["> 21", 0.04]
        ]

        #Tabla 5
        self.tiempo_espera_cola = [
            ["0", 0.36],
            ["5", 0.28],
            ["10", 0.2],
            ["15", 0.12],
            ["20", 0.04]
        ]

        #Tabla 6
        self.tipo_solicitud = [
            ["Check - in", 0.4],
            ["Check - out", 0.25],
            ["Consulta / Informacion", 0.2],
            ["Solicitud Especial", 0.15]
        ]

        #Tabla 7
        self.grupos_personas = [
            ["1", 0.3],
            ["2", 0.45],
            ["3 a 4", 0.2],
            ["5 o mas", 0.05]
        ]

        #Tabla 8 (agregar otra columna antes)
        self.tipos_habitaciones = [
            ["Sencilla", "1200",  0.5],
            ["Doble", "2000",  0.35],
            ["Suite", "3500",  0.15],
        ]

        #Tabla 9
        self.Costos_brutos = [
            ["Salarios", 0.4],
            ["Agua y luz", 0.25],
            ["Mantenimieto", 0.2],
            ["Total", 0.15]
        ]
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def Calculos_probAcu_rang(self):
        
        #Tabla 1 (completa)
        
        Probabilidad_acumulada_1 = 0.0
        self.Tabla_1_e_d = []
        
        for val_1, prob_1 in self.Personas_dias:
            
            inicio_1 = Probabilidad_acumulada_1
            
            Probabilidad_acumulada_1 = round(Probabilidad_acumulada_1 + prob_1, 4)
            
            rango_1 = str(round(inicio_1, 4)) + " - " + str(round(Probabilidad_acumulada_1, 4))
            
            self.Tabla_1_e_d.append([val_1, prob_1, Probabilidad_acumulada_1, rango_1])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 2 (completa)
        
        Probabilidad_acumulada_2 = 0.0
        self.Tabla_2_e_d = []
        
        for val_2, prob_2 in self.Tipos_atencion:
            
            inicio_2 = Probabilidad_acumulada_2
            
            Probabilidad_acumulada_2 = round(Probabilidad_acumulada_2 + prob_2, 4)
            
            rango_2 = str(round(inicio_2, 4)) + " - " + str(round(Probabilidad_acumulada_2, 4))
            
            self.Tabla_2_e_d.append([val_2, prob_2, Probabilidad_acumulada_2, rango_2])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 3 (completa)
        
        Probabilidad_acumulada_3 = 0.0
        self.Tabla_3_e_d = []
        
        for val_3, prob_3 in self.recepcionistas_dias:
            
            inicio_3 = Probabilidad_acumulada_3
            
            Probabilidad_acumulada_3 = round(Probabilidad_acumulada_3 + prob_3, 4)
            
            rango_3 = str(round(inicio_3, 4)) + " - " + str(round(Probabilidad_acumulada_3, 4))
            
            self.Tabla_3_e_d.append([val_3, prob_3, Probabilidad_acumulada_3, rango_3])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 4 (completa)
        
        Probabilidad_acumulada_4 = 0.0
        self.Tabla_4_e_d = []
        
        for val_4, prob_4 in self.Cantidad_abandonos:
            
            inicio_4 = Probabilidad_acumulada_4
            
            Probabilidad_acumulada_4 = round(Probabilidad_acumulada_4 + prob_4, 4)
            
            rango_4 = str(round(inicio_4, 4)) + " - " + str(round(Probabilidad_acumulada_4, 4))
            
            self.Tabla_4_e_d.append([val_4, prob_4, Probabilidad_acumulada_4, rango_4])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 5 (completa)
        
        Probabilidad_acumulada_5 = 0.0
        self.Tabla_5_e_d = []
        
        for val_5, prob_5 in self.tiempo_espera_cola:
            
            inicio_5 = Probabilidad_acumulada_5
            
            Probabilidad_acumulada_5 = round(Probabilidad_acumulada_5 + prob_5, 4)
            
            rango_5 = str(round(inicio_5, 4)) + " - " + str(round(Probabilidad_acumulada_5, 4))
            
            self.Tabla_5_e_d.append([val_5, prob_5, Probabilidad_acumulada_5, rango_5])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 6 (completa)
        
        Probabilidad_acumulada_6 = 0.0
        self.Tabla_6_e_d = []
        
        for val_6, prob_6 in self.tipo_solicitud:
            
            inicio_6 = Probabilidad_acumulada_6
            
            Probabilidad_acumulada_6 = round(Probabilidad_acumulada_6 + prob_6, 4)
            
            rango_6 = str(round(inicio_6, 4)) + " - " + str(round(Probabilidad_acumulada_6, 4))
            
            self.Tabla_6_e_d.append([val_6, prob_6, Probabilidad_acumulada_6, rango_6])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 7 (completa)
        
        Probabilidad_acumulada_7 = 0.0
        self.Tabla_7_e_d = []
        
        for val_7, prob_7 in self.grupos_personas:
            
            inicio_7 = Probabilidad_acumulada_7
            
            Probabilidad_acumulada_7 = round(Probabilidad_acumulada_7 + prob_7, 4)
            
            rango_7 = str(round(inicio_7, 4)) + " - " + str(round(Probabilidad_acumulada_7, 4))
            
            self.Tabla_7_e_d.append([val_7, prob_7, Probabilidad_acumulada_7, rango_7])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 8 (completa)
        
        Probabilidad_acumulada_8 = 0.0
        self.Tabla_8_e_d = []
        
        for val_8, precio_8 ,prob_8 in self.tipos_habitaciones:
            
            inicio_8 = Probabilidad_acumulada_8
            
            Probabilidad_acumulada_8 = round(Probabilidad_acumulada_8 + prob_8, 4)
            
            rango_8 = str(round(inicio_8, 4)) + " - " + str(round(Probabilidad_acumulada_8, 4))
            
            self.Tabla_8_e_d.append([val_8, precio_8, prob_8, Probabilidad_acumulada_8, rango_8])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 9 (completa)
        
        Probabilidad_acumulada_9 = 0.0
        self.Tabla_9_e_d = []
        
        for val_9, prob_9 in self.Costos_brutos:
            
            inicio_9 = Probabilidad_acumulada_9
            
            Probabilidad_acumulada_9 = round(Probabilidad_acumulada_9 + prob_9, 4)
            
            rango_9 = str(round(inicio_9, 4)) + " - " + str(round(Probabilidad_acumulada_9, 4))
            
            self.Tabla_9_e_d.append([val_9, prob_9, Probabilidad_acumulada_9, rango_9])
            
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
    def Tablas_Editables(self):
        
        tablas = self.tabview.tab("TABLAS EDITABLES")
        
        self.frame_sup = CTkFrame(tablas, width=200, height= 200, corner_radius=10)
        self.frame_sup.pack(fill="both", pady=20, padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #cuadro de texto
        
        self.Valor = CTkEntry(self.frame_sup, placeholder_text= "Valor", width= 130)
        self.Valor.pack(side="left", padx=10)
        
        #se deja sin pack para mostarlo despues (SOLO CUANDO ESTA SELECCIONADA LA TABLA 8)
        self.Precio = CTkEntry(self.frame_sup, placeholder_text="Precio", width=130)
        
        self.Probabilidad = CTkEntry(self.frame_sup, placeholder_text= "Probabilidad", width= 130)
        self.Probabilidad.pack(side="left", padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.btn_Actualizar = CTkButton(self.frame_sup, text= "actualizar", font= ("Arial", 20), command= self.Actualizar_datos)
        self.btn_Actualizar.pack(side="left", padx=10)
        
        self.btn_Añadir = CTkButton(self.frame_sup, text= "añadir", font= ("Arial", 20), fg_color= "green", command= self.Añadir_fila)
        self.btn_Añadir.pack(side="left", padx=10)
        
        self.btn_Eliminar = CTkButton(self.frame_sup, text= "eliminar", font= ("Arial", 20), fg_color= "red", command= self.Eliminar_fila)
        self.btn_Eliminar.pack(side="left", padx=10)
        
        
        self.scroll_frame = CTkScrollableFrame(tablas)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 1 (personas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Personas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        
        self.Tabla_1_e = CTkTable(
            self.scroll_frame,
            values= encabezado_1 + self.Tabla_1_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_1
        )
        self.Tabla_1_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 2 (tipos de atencion)
        
        # Encabezado
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de atencion", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        self.Tabla_2_e = CTkTable(
            self.scroll_frame,
            values= encabezado_2 + self.Tabla_2_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_2
        )
        self.Tabla_2_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 3 (recepcionistas por dia)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Recepcionistas por dia", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        self.Tabla_3_e = CTkTable(
            self.scroll_frame,
            values= encabezado_3 + self.Tabla_3_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_3
        )
        self.Tabla_3_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 4 (cantidad de abandonos)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Cantidad de abandonos", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        self.Tabla_4_e = CTkTable(
            self.scroll_frame,
            values= encabezado_4 + self.Tabla_4_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_4
        )
        self.Tabla_4_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 5 (tiempo de espera en la cola)
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de espera en cola", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        self.Tabla_5_e = CTkTable(
            self.scroll_frame,
            values= encabezado_5 + self.Tabla_5_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_5
        )
        self.Tabla_5_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 6 (tipo de solicitud)
        
        # Encabezado
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_6 = CTkLabel(self.scroll_frame, text= "Tipo de solicitud", font= ("Arial", 20 ))
        self.Titulo_t_6.pack(pady=10, padx=10)
        
        self.Tabla_6_e = CTkTable(
            self.scroll_frame,
            values= encabezado_6 + self.Tabla_6_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_6
        )
        self.Tabla_6_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 7 (Grupo de personas)
        
        # Encabezado
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_7 = CTkLabel(self.scroll_frame, text= "Grupo de personas", font= ("Arial", 20 ))
        self.Titulo_t_7.pack(pady=10, padx=10)
        
        self.Tabla_7_e = CTkTable(
            self.scroll_frame,
            values= encabezado_7 + self.Tabla_7_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_7
        )
        self.Tabla_7_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 8 (tipo de habitaciones)
        
        # Encabezado
        encabezado_8 = [["Tipos", "Precio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_8 = CTkLabel(self.scroll_frame, text= "Tipo de habitaciones", font= ("Arial", 20 ))
        self.Titulo_t_8.pack(pady=10, padx=10)
        
        self.Tabla_8_e = CTkTable(
            self.scroll_frame,
            values= encabezado_8 + self.Tabla_8_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_8
        )
        self.Tabla_8_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #tabla 9 (costos brutos)
        
        # Encabezado
        encabezado_9 = [["Concepto", "Costos Diarios", "Costos Mesuales"]]
        
        #titulo
        self.Titulo_t_9 = CTkLabel(self.scroll_frame, text= "Costos Brutos", font= ("Arial", 20 ))
        self.Titulo_t_9.pack(pady=10, padx=10)
        
        self.Tabla_9_e = CTkTable(
            self.scroll_frame,
            values= encabezado_9 + self.Tabla_9_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_9
        )
        self.Tabla_9_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def Seleccionar_tabla_1(self, data):
        self.tabla_activa = self.Tabla_1_e
        self.lista_datos_activa = self.Personas_dias
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_2(self, data):
        self.tabla_activa = self.Tabla_2_e
        self.lista_datos_activa = self.Tipos_atencion
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_3(self, data):
        self.tabla_activa = self.Tabla_3_e
        self.lista_datos_activa = self.recepcionistas_dias
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_4(self, data):
        self.tabla_activa = self.Tabla_4_e
        self.lista_datos_activa = self.Cantidad_abandonos
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_5(self, data):
        self.tabla_activa = self.Tabla_5_e
        self.lista_datos_activa = self.tiempo_espera_cola
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
        
        
    def Seleccionar_tabla_6(self, data):
        self.tabla_activa = self.Tabla_6_e
        self.lista_datos_activa = self.tipo_solicitud
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_7(self, data):
        self.tabla_activa = self.Tabla_7_e
        self.lista_datos_activa = self.grupos_personas
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_8(self, data):
        self.tabla_activa = self.Tabla_8_e
        self.lista_datos_activa = self.tipos_habitaciones
        
        #se muestra el entry
        self.Precio.pack(side="left", padx=10, after=self.Valor)
        self.Seleccionar_fila(data)
    
    
    def Seleccionar_tabla_9(self, data):
        self.tabla_activa = self.Tabla_9_e
        self.lista_datos_activa = self.Costos_brutos
        
        #ocultamos el entry
        self.Precio.pack_forget()
        self.Seleccionar_fila(data)
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Seleccionar_fila(self, data):
        self.indice_selec = data['row']
        
        if self.indice_selec > 0:
            valores_fila = self.tabla_activa.get_row(self.indice_selec)
            
            self.Valor.delete(0, "end")
            self.Valor.insert(0, valores_fila[0])
            
            if self.tabla_activa == self.Tabla_8_e:
                self.Precio.delete(0, "end")
                self.Precio.insert(0, valores_fila[1])
                self.Probabilidad.delete(0, "end")
                self.Probabilidad.insert(0, valores_fila[2])
                
            else:
                self.Probabilidad.delete(0, "end")
                self.Probabilidad.insert(0, valores_fila[1])
            
            
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    
    def Verificar_probabilidad(self):
        self.suma_total = 0
        
        if self.lista_datos_activa:
            
            for fila in self.lista_datos_activa:
            
                if self.tabla_activa == self.Tabla_8_e:
                    self.suma_total +=  float(fila[2])
                
                else:
                    self.suma_total +=  float(fila[1])
        
        self.suma_total = round(self.suma_total, 2)
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
    def Actualizar_datos(self):
        
        # cosas para la tabla 8 y para la normal 
        if self.lista_datos_activa is None or self.indice_selec <= 0:
            
            messagebox.showwarning("ATENCION", "Primero seleccione una fila de una tabla")
            return
        
        
        if self.tabla_activa == self.Tabla_8_e:
        
            new_val = self.Valor.get()
            new_precio = int(self.Precio.get())
            new_prob = float(self.Probabilidad.get())

            new_suma = 0.0

            for i in range(len(self.lista_datos_activa)):

                if i == self.indice_selec - 1:
                    new_suma +=  new_prob
                    
                else: 
                    new_suma += float(self.lista_datos_activa[i][2])
                    
            new_suma = round(new_suma, 2)

            if new_suma > 1.0:
                messagebox.showerror("ERROR", F"La suma de las probabilidades debe de ser de 1, tu tienes {new_suma}")
                return
            
            
            self.lista_datos_activa[self.indice_selec - 1] = [new_val, new_precio, new_prob]
            
            self.Actualizar_tabla()
        
            messagebox.showinfo("EXITO", "Datos actualizados correctamente")
            
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
        
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_8 = [["Tipos", "Precio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_9 = [["Concepto", "Costos Diarios", "Costos Mesuales"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        datos_completos_7 = encabezado_7 + self.Tabla_7_e_d
        datos_completos_8 = encabezado_8 + self.Tabla_8_e_d
        datos_completos_9 = encabezado_9 + self.Tabla_9_e_d
        
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
        
        
        
        self.tabla_activa = None
        self.lista_datos_activa = None
        self.indice_selec = -1
        
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
    def Añadir_fila(self):
        if self.lista_datos_activa is None:
            
            messagebox.showwarning("ATENCION", "Primero seleccione una tabla")
            return
        
        
        try:
            
            new_val = self.Valor.get()
            new_prob = float(self.Probabilidad.get())
            
            self.Verificar_probabilidad()
            
            suma_futura = round(self.suma_total + new_prob, 2)
            
            if suma_futura > 1.0:
                messagebox.showerror("ERROR", F"La suma de las probabilidades debe de ser de 1, tu tienes {suma_futura}")
                return
            
            
            if self.tabla_activa == self.Tabla_8_e:
                new_precio = self.Precio.get()
                self.lista_datos_activa.append([new_val, new_precio, new_prob])
                
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
        
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_8 = [["Tipos", "Precio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        encabezado_9 = [["Concepto", "Costos Diarios", "Costos Mesuales"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        datos_completos_7 = encabezado_7 + self.Tabla_7_e_d
        datos_completos_8 = encabezado_8 + self.Tabla_8_e_d
        datos_completos_9 = encabezado_9 + self.Tabla_9_e_d
        
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
                
                self.Actualizar_tabla()
                
                self.Valor.delete(0, "end")
                self.Probabilidad.delete(0, "end")
                self.indice_selec = -1
                
                messagebox.showinfo("EXITO", "Fila eliminada correctamente")
                
            except Exception as e:
                messagebox.showerror("ERROR", f"No se pudo eliminar: {e}")
                
                
#-------------------------------------------------------------------------------------------------------------------------------------------------


# Tabla de monte carlo
    
    
    
    def Creacion_tabla(self):
        
        
        try:
            
            filas_predeterminadas = 10
            # filas_predeterminadas = int(self.prueba_1.get())
            
        except Exception:
                messagebox.showerror("INVALIDACION","Datos invalidos", parent= self.Interfaz)
                return False
            
        if self.Tabla:
            self.Tabla.destroy()
        
        encabezados = [["Dias", "Aleatorio\npersonas", "Personas\npor dia", "Aleatorio\ngrupo", "Personas\npor grupo", "Grupos atendidos", "Aleatorio\nhabitacion", "Precio", "Aleatorio\nservicio", "Servicio", "Aleatorio\nrecepcio-\nnistas", "Recepcio-\nnistas", "Aleatorio\natencion", "Atencion", "Aleatorio\nespera\nen cola", "Espera\nen cola", "Aleatorio\nabandono", "Abandono", "Ingresos\nbrutos", "Costo diario", "Ganan-\ncia\nneta"]]
        
        for i in range(filas_predeterminadas):
            fila_vacia = [str(i+1)] + [""] * 20
            encabezados.append(fila_vacia)
            
        #crear la tabla nueva
        
        self.Tabla = CTkTable(
            master = self.scroll_frame, 
            row = filas_predeterminadas + 1, 
            column= 21, 
            values= encabezados,
            width = 100,
            justify = "center",
            wraplength = 100
        )
        
        #mostrar tabla
        self.Tabla.pack(expand=True, fill="both", padx=10, pady=10)
        
Recepcion()