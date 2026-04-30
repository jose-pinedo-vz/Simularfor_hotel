
#! Interfaz sin funcionamiento, por el momento  

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
        
        # self.Interfaz.geometry("1500x800")
        
        # try: self.principal.state("zoomed")
        # except: self.principal.attributes("-zoomed", True)
        
        
        self.Interfaz.grid_columnconfigure(1, weight=1)
        self.Interfaz.grid_rowconfigure(0, weight=1)
        
        
        #---------------------------------------------------------
        
        #FRAME DERECHO (SOLO PARA MOSTRAR LOS DATOS)
        
        self.Frame_Der = CTkFrame(self.Interfaz, width=200, corner_radius=10)
        self.Frame_Der.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        
        #---------------------------------------------------------
        
        
        #Tabview (sirve para tener vistas de pestañas en una misma interfaz)
        
        self.tabview = CTkTabview(self.Frame_Der, corner_radius= 30, width=1900, height= 300)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)
        
        #botones dentro del tabview
        
        self.tabview.add("TABLAS PREDEFINIDAS")
        self.tabview.add("TABLAS EDITABLES")
        self.tabview.add("MONTE CARLO")
        
        self.Tablas_Predefinidas()  
        self.Tablas_Editables()      
        
        
        # titulo de la segunda pestaña
        
        self.Monte_carlo = self.tabview.tab("MONTE CARLO")
        
        
        #Titulo 
        
        self.Titulo_frame_der = CTkLabel(self.Monte_carlo, text= "MONTE CARLO", font= ("Arial", 30 ))
        self.Titulo_frame_der.pack(pady=10, padx=10)
        
        
        #Boton de simular
        
        self.btn_generar = CTkButton(self.Monte_carlo, text= "simular", font= ("Arial", 25) , command= self.Creacion_tabla)
        self.btn_generar.pack(pady=10)
        
        
        #Tabla
        
        # Para que la tabla no se salga de la pantalla
        
        self.scroll_frame = CTkScrollableFrame(self.Monte_carlo)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #---------------------------------------------------------
        
        self.Tabla = None
        
        self.Interfaz.update() 
        self.Interfaz.state("zoomed") #windows
        # self.Interfaz.attributes('-zoomed', True) #Linux
        
        self.Interfaz.mainloop()
        
        #---------------------------------------------------------
        
    def Tablas_Predefinidas(self):
        
        tablas_pre = self.tabview.tab("TABLAS PREDEFINIDAS")
        
        self.scroll_frame = CTkScrollableFrame(tablas_pre)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        
        #tabla 1 (personas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Personas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        
        Tabla_1 = CTkTable(
            self.scroll_frame,
            values= encabezado_1,
            header_color="#0a2e57"
        )
        # Tabla_1.pack(expand=True, fill="both")
        Tabla_1.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_1 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_1 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_1 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_1 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_1.add_row(values= fila_t_1_1)
        Tabla_1.add_row(values= fila_t_2_1)
        Tabla_1.add_row(values= fila_t_3_1)
        Tabla_1.add_row(values= fila_t_4_1)
        
        
        #tabla 2 (tipos de atencion)
        
        # Encabezado
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de atencion", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        Tabla_2 = CTkTable(
            self.scroll_frame,
            values= encabezado_2,
            header_color="#0a2e57"
        )
        # Tabla_2.pack(expand=True, fill="both")
        Tabla_2.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_2 = ["2 - 5", "0.3", "0.3", "0 - 0.3"]
        fila_t_2_2 = ["6 - 10", "0.40", "0.7", "0.301 - 0.7"]
        fila_t_3_2 = ["11 - 15", "0.2", "0.9", "0.701 - 0.9"]
        fila_t_4_2 = ["16 - 20", "0.1", "1", "0.901 - 1"]
        
        Tabla_2.add_row(values= fila_t_1_2)
        Tabla_2.add_row(values= fila_t_2_2)
        Tabla_2.add_row(values= fila_t_3_2)
        Tabla_2.add_row(values= fila_t_4_2)
        
        
        #tabla 3 (recepcionistas por dia)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Recepcionistas por dia", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        Tabla_3 = CTkTable(
            self.scroll_frame,
            values= encabezado_3,
            header_color="#0a2e57"
        )
        # Tabla_3.pack(expand=True, fill="both")
        Tabla_3.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_3 = ["1", "0.1", "0.1", "0 - 0.1"]
        fila_t_2_3 = ["2", "0.25", "0.35", "0.101 - 0.35"]
        fila_t_3_3 = ["3", "0.45", "0.8", "0.3501 - 0.80"]
        fila_t_4_3 = ["4", "0.2", "1", "0.8001 - 1"]
        
        Tabla_3.add_row(values= fila_t_1_3)
        Tabla_3.add_row(values= fila_t_2_3)
        Tabla_3.add_row(values= fila_t_3_3)
        Tabla_3.add_row(values= fila_t_4_3)
        
        #tabla 4 (cantidad de abandonos)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Cantidad de abandonos", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        Tabla_4 = CTkTable(
            self.scroll_frame,
            values= encabezado_4,
            header_color="#0a2e57"
        )
        # Tabla_4.pack(expand=True, fill="both")
        Tabla_4.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_4 = ["No", "0.76", "0.76", "0 - 0.76"]
        fila_t_2_4 = ["< 10", "0.12", "0.50", "0.7601 - 0.88"]
        fila_t_3_4 = ["11 a 20", "0.08", "0.8", "0.8801 - 0.96"]
        fila_t_4_4 = ["> 21", "0.04", "1", "0.9601 - 1"]
        
        Tabla_4.add_row(values= fila_t_1_4)
        Tabla_4.add_row(values= fila_t_2_4)
        Tabla_4.add_row(values= fila_t_3_4)
        Tabla_4.add_row(values= fila_t_4_4)
        
        #tabla 5 (tiempo de espera en la cola)
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de espera en cola", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        Tabla_5 = CTkTable(
            self.scroll_frame,
            values= encabezado_5,
            header_color="#0a2e57"
        )
        # Tabla_5.pack(expand=True, fill="both")
        Tabla_5.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_5 = ["0", "0.36", "0.36", "0 - 0.36"]
        fila_t_2_5 = ["5", "0.28", "0.64", "0.3601 - 0.64"]
        fila_t_3_5 = ["10", "0.2", "0.84", "0.6401 - 0.84"]
        fila_t_4_5 = ["15", "0.12", "0.96", "0.8401 - 0.96"]
        fila_t_5_5 = ["20", "0.04", "1", "0.9601 - 1"]
        
        Tabla_5.add_row(values= fila_t_1_5)
        Tabla_5.add_row(values= fila_t_2_5)
        Tabla_5.add_row(values= fila_t_3_5)
        Tabla_5.add_row(values= fila_t_4_5)
        Tabla_5.add_row(values= fila_t_5_5)
        
        #tabla 6 (tipo de solicitud)
        
        # Encabezado
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_6 = CTkLabel(self.scroll_frame, text= "Tipo de solicitud", font= ("Arial", 20 ))
        self.Titulo_t_6.pack(pady=10, padx=10)
        
        Tabla_6 = CTkTable(
            self.scroll_frame,
            values= encabezado_6,
            header_color="#0a2e57"
        )
        # Tabla_6.pack(expand=True, fill="both")
        Tabla_6.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_6 = ["Check - in", "0.4", "0.4", "0 - 0.4"]
        fila_t_2_6 = ["Check - out", "0.25", "0.65", "0.401 - 0.65"]
        fila_t_3_6 = ["Consulta / Informacion", "0.2", "0.85", "0.6501 - 0.85"]
        fila_t_4_6 = ["Solicitud Especial", "0.15", "1", "0.8501 - 1"]
        
        Tabla_6.add_row(values= fila_t_1_6)
        Tabla_6.add_row(values= fila_t_2_6)
        Tabla_6.add_row(values= fila_t_3_6)
        Tabla_6.add_row(values= fila_t_4_6)
        
        #tabla 7 (Grupo de personas)
        
        # Encabezado
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_7 = CTkLabel(self.scroll_frame, text= "Grupo de personas", font= ("Arial", 20 ))
        self.Titulo_t_7.pack(pady=10, padx=10)
        
        Tabla_7 = CTkTable(
            self.scroll_frame,
            values= encabezado_7,
            header_color="#0a2e57"
        )
        # Tabla_7.pack(expand=True, fill="both")
        Tabla_7.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_7 = ["1", "0.3", "0.3", "0 - 0.3"]
        fila_t_2_7 = ["2", "0.45", "0.75", "0.301 - 0.75"]
        fila_t_3_7 = ["3 a 4", "0.2", "0.95", "0.7501 - 0.95"]
        fila_t_4_7 = ["5 o mas", "0.05", "1", "0.9501 - 1"]
        
        Tabla_7.add_row(values= fila_t_1_7)
        Tabla_7.add_row(values= fila_t_2_7)
        Tabla_7.add_row(values= fila_t_3_7)
        Tabla_7.add_row(values= fila_t_4_7)
        
        #tabla 8 (tipo de habitaciones)
        
        # Encabezado
        encabezado_8 = [["Tipos", "Precio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_8 = CTkLabel(self.scroll_frame, text= "Tipo de habitaciones", font= ("Arial", 20 ))
        self.Titulo_t_8.pack(pady=10, padx=10)
        
        Tabla_8 = CTkTable(
            self.scroll_frame,
            values= encabezado_8,
            header_color="#0a2e57"
        )
        # Tabla_8.pack(expand=True, fill="both")
        Tabla_8.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_8 = ["Sencilla", "1200", "0.5", "0.5", "0 - 0.5"]
        fila_t_2_8 = ["Doble", "2000", "0.35", "0.85", "0.501 - 0.85"]
        fila_t_3_8 = ["Suite", "3500", "0.15", "1", "0.8501 - 1"]
        
        Tabla_8.add_row(values= fila_t_1_8)
        Tabla_8.add_row(values= fila_t_2_8)
        Tabla_8.add_row(values= fila_t_3_8)
        
        #tabla 9 (costos brutos)
        
        # Encabezado
        encabezado_9 = [["Concepto", "Costos Diarios", "Costos Mesuales"]]
        
        #titulo
        self.Titulo_t_9 = CTkLabel(self.scroll_frame, text= "Costos Brutos", font= ("Arial", 20 ))
        self.Titulo_t_9.pack(pady=10, padx=10)
        
        Tabla_9 = CTkTable(
            self.scroll_frame,
            values= encabezado_9,
            header_color="#0a2e57"
        )
        # Tabla_9.pack(expand=True, fill="both")
        Tabla_9.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_9 = ["Salarios", "800", "24000"]
        fila_t_2_9 = ["Agua y luz", "300", "9000"]
        fila_t_3_9 = ["Mantenimieto", "200", "6000"]
        fila_t_4_9 = ["", "", ""]
        fila_t_5_9 = ["Total", "1300", "39000"]
        
        Tabla_9.add_row(values= fila_t_1_9)
        Tabla_9.add_row(values= fila_t_2_9)
        Tabla_9.add_row(values= fila_t_3_9)
        Tabla_9.add_row(values= fila_t_4_9)
        Tabla_9.add_row(values= fila_t_5_9)
        
    def Tablas_Editables(self):
        
        tablas = self.tabview.tab("TABLAS EDITABLES")
        
        
        #---------------------------------------------------------
        
        self.frame_sup = CTkFrame(tablas, width=200, height= 200, corner_radius=10)
        self.frame_sup.pack(fill="both", pady=20, padx=10)
        
        
        
        self.Valor = CTkEntry(self.frame_sup, placeholder_text= "Valor", width= 130)
        self.Valor.pack(side="left", padx=10)
        
        self.Probabilidad = CTkEntry(self.frame_sup, placeholder_text= "Probabilidad", width= 130)
        self.Probabilidad.pack(side="left", padx=10)
        
        self.btn_Actualizar = CTkButton(self.frame_sup, text= "actualizar", font= ("Arial", 20))# , command= self.actualizar_datos)
        self.btn_Actualizar.pack(side="left", padx=10)
        
        
        
        self.scroll_frame = CTkScrollableFrame(tablas)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        #---------------------------------------------------------
        
        #tabla 1 (personas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Personas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        
        Tabla_1 = CTkTable(
            self.scroll_frame,
            values= encabezado_1,
            header_color="#0a2e57"
        )
        # Tabla_1.pack(expand=True, fill="both")
        Tabla_1.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_1 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_1 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_1 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_1 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_1.add_row(values= fila_t_1_1)
        Tabla_1.add_row(values= fila_t_2_1)
        Tabla_1.add_row(values= fila_t_3_1)
        Tabla_1.add_row(values= fila_t_4_1)
        
        
        #tabla 2 (tipos de atencion)
        
        # Encabezado
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de atencion", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        Tabla_2 = CTkTable(
            self.scroll_frame,
            values= encabezado_2,
            header_color="#0a2e57"
        )
        # Tabla_2.pack(expand=True, fill="both")
        Tabla_2.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_2 = ["2 - 5", "0.3", "0.3", "0 - 0.3"]
        fila_t_2_2 = ["6 - 10", "0.40", "0.7", "0.301 - 0.7"]
        fila_t_3_2 = ["11 - 15", "0.2", "0.9", "0.701 - 0.9"]
        fila_t_4_2 = ["16 - 20", "0.1", "1", "0.901 - 1"]
        
        Tabla_2.add_row(values= fila_t_1_2)
        Tabla_2.add_row(values= fila_t_2_2)
        Tabla_2.add_row(values= fila_t_3_2)
        Tabla_2.add_row(values= fila_t_4_2)
        
        
        #tabla 3 (recepcionistas por dia)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Recepcionistas por dia", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        Tabla_3 = CTkTable(
            self.scroll_frame,
            values= encabezado_3,
            header_color="#0a2e57"
        )
        # Tabla_3.pack(expand=True, fill="both")
        Tabla_3.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_3 = ["1", "0.1", "0.1", "0 - 0.1"]
        fila_t_2_3 = ["2", "0.25", "0.35", "0.101 - 0.35"]
        fila_t_3_3 = ["3", "0.45", "0.8", "0.3501 - 0.80"]
        fila_t_4_3 = ["4", "0.2", "1", "0.8001 - 1"]
        
        Tabla_3.add_row(values= fila_t_1_3)
        Tabla_3.add_row(values= fila_t_2_3)
        Tabla_3.add_row(values= fila_t_3_3)
        Tabla_3.add_row(values= fila_t_4_3)
        
        #tabla 4 (cantidad de abandonos)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Cantidad de abandonos", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        Tabla_4 = CTkTable(
            self.scroll_frame,
            values= encabezado_4,
            header_color="#0a2e57"
        )
        # Tabla_4.pack(expand=True, fill="both")
        Tabla_4.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_4 = ["No", "0.76", "0.76", "0 - 0.76"]
        fila_t_2_4 = ["< 10", "0.12", "0.50", "0.7601 - 0.88"]
        fila_t_3_4 = ["11 a 20", "0.08", "0.8", "0.8801 - 0.96"]
        fila_t_4_4 = ["> 21", "0.04", "1", "0.9601 - 1"]
        
        Tabla_4.add_row(values= fila_t_1_4)
        Tabla_4.add_row(values= fila_t_2_4)
        Tabla_4.add_row(values= fila_t_3_4)
        Tabla_4.add_row(values= fila_t_4_4)
        
        #tabla 5 (tiempo de espera en la cola)
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de espera en cola", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        Tabla_5 = CTkTable(
            self.scroll_frame,
            values= encabezado_5,
            header_color="#0a2e57"
        )
        # Tabla_5.pack(expand=True, fill="both")
        Tabla_5.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_5 = ["0", "0.36", "0.36", "0 - 0.36"]
        fila_t_2_5 = ["5", "0.28", "0.64", "0.3601 - 0.64"]
        fila_t_3_5 = ["10", "0.2", "0.84", "0.6401 - 0.84"]
        fila_t_4_5 = ["15", "0.12", "0.96", "0.8401 - 0.96"]
        fila_t_5_5 = ["20", "0.04", "1", "0.9601 - 1"]
        
        Tabla_5.add_row(values= fila_t_1_5)
        Tabla_5.add_row(values= fila_t_2_5)
        Tabla_5.add_row(values= fila_t_3_5)
        Tabla_5.add_row(values= fila_t_4_5)
        Tabla_5.add_row(values= fila_t_5_5)
        
        #tabla 6 (tipo de solicitud)
        
        # Encabezado
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_6 = CTkLabel(self.scroll_frame, text= "Tipo de solicitud", font= ("Arial", 20 ))
        self.Titulo_t_6.pack(pady=10, padx=10)
        
        Tabla_6 = CTkTable(
            self.scroll_frame,
            values= encabezado_6,
            header_color="#0a2e57"
        )
        # Tabla_6.pack(expand=True, fill="both")
        Tabla_6.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_6 = ["Check - in", "0.4", "0.4", "0 - 0.4"]
        fila_t_2_6 = ["Check - out", "0.25", "0.65", "0.401 - 0.65"]
        fila_t_3_6 = ["Consulta / Informacion", "0.2", "0.85", "0.6501 - 0.85"]
        fila_t_4_6 = ["Solicitud Especial", "0.15", "1", "0.8501 - 1"]
        
        Tabla_6.add_row(values= fila_t_1_6)
        Tabla_6.add_row(values= fila_t_2_6)
        Tabla_6.add_row(values= fila_t_3_6)
        Tabla_6.add_row(values= fila_t_4_6)
        
        #tabla 7 (Grupo de personas)
        
        # Encabezado
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_7 = CTkLabel(self.scroll_frame, text= "Grupo de personas", font= ("Arial", 20 ))
        self.Titulo_t_7.pack(pady=10, padx=10)
        
        Tabla_7 = CTkTable(
            self.scroll_frame,
            values= encabezado_7,
            header_color="#0a2e57"
        )
        # Tabla_7.pack(expand=True, fill="both")
        Tabla_7.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_7 = ["1", "0.3", "0.3", "0 - 0.3"]
        fila_t_2_7 = ["2", "0.45", "0.75", "0.301 - 0.75"]
        fila_t_3_7 = ["3 a 4", "0.2", "0.95", "0.7501 - 0.95"]
        fila_t_4_7 = ["5 o mas", "0.05", "1", "0.9501 - 1"]
        
        Tabla_7.add_row(values= fila_t_1_7)
        Tabla_7.add_row(values= fila_t_2_7)
        Tabla_7.add_row(values= fila_t_3_7)
        Tabla_7.add_row(values= fila_t_4_7)
        
        #tabla 8 (tipo de habitaciones)
        
        # Encabezado
        encabezado_8 = [["Tipos", "Precio", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_8 = CTkLabel(self.scroll_frame, text= "Tipo de habitaciones", font= ("Arial", 20 ))
        self.Titulo_t_8.pack(pady=10, padx=10)
        
        Tabla_8 = CTkTable(
            self.scroll_frame,
            values= encabezado_8,
            header_color="#0a2e57"
        )
        # Tabla_8.pack(expand=True, fill="both")
        Tabla_8.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_8 = ["Sencilla", "1200", "0.5", "0.5", "0 - 0.5"]
        fila_t_2_8 = ["Doble", "2000", "0.35", "0.85", "0.501 - 0.85"]
        fila_t_3_8 = ["Suite", "3500", "0.15", "1", "0.8501 - 1"]
        
        Tabla_8.add_row(values= fila_t_1_8)
        Tabla_8.add_row(values= fila_t_2_8)
        Tabla_8.add_row(values= fila_t_3_8)
        
        #tabla 9 (costos brutos)
        
        # Encabezado
        encabezado_9 = [["Concepto", "Costos Diarios", "Costos Mesuales"]]
        
        #titulo
        self.Titulo_t_9 = CTkLabel(self.scroll_frame, text= "Costos Brutos", font= ("Arial", 20 ))
        self.Titulo_t_9.pack(pady=10, padx=10)
        
        Tabla_9 = CTkTable(
            self.scroll_frame,
            values= encabezado_9,
            header_color="#0a2e57"
        )
        # Tabla_9.pack(expand=True, fill="both")
        Tabla_9.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_9 = ["Salarios", "800", "24000"]
        fila_t_2_9 = ["Agua y luz", "300", "9000"]
        fila_t_3_9 = ["Mantenimieto", "200", "6000"]
        fila_t_4_9 = ["", "", ""]
        fila_t_5_9 = ["Total", "1300", "39000"]
        
        Tabla_9.add_row(values= fila_t_1_9)
        Tabla_9.add_row(values= fila_t_2_9)
        Tabla_9.add_row(values= fila_t_3_9)
        Tabla_9.add_row(values= fila_t_4_9)
        Tabla_9.add_row(values= fila_t_5_9)
        
    def Creacion_tabla(self):
        
        #obtener los datos para hacer la tabla
        
        # if not self.prueba_1.get() or not self.prueba_2.get() or not self.prueba_3.get() or not self.prueba_4.get():
        #     messagebox.showwarning("CAMPOS","Complete los campos vacios", parent= self.Interfaz)
        #     return False
        
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