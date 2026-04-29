
#! Interfaz sin funcionamiento 

from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from CTkTable import CTkTable

# Configuración de estilo
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class Lavanderia:
    
    def __init__(self):
        self.Interfaz = ctk.CTk()
        
        self.Interfaz.title("Interfaz --- Lavanderia")
        
        # self.Interfaz.geometry("1500x800")
        
        # try: self.principal.state("zoomed")
        # except: self.principal.attributes("-zoomed", True)
        
        
        self.Interfaz.grid_columnconfigure(1, weight=1)
        self.Interfaz.grid_rowconfigure(0, weight=1)
        
        #---------------------------------------------------------
        
        #PANEL IZQUIERDO (Solo para pedir los datos)
        self.Frame_izq = CTkFrame(self.Interfaz, width=200, corner_radius=10)
        self.Frame_izq.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        
        #Titulo (frame izq)
        self.Titulo_frame_izq = CTkLabel(self.Frame_izq, text= "DATOS", font= ("Arial", 25 ))
        self.Titulo_frame_izq.pack(pady=20, padx=10)
        
        #Cuadros de texto
        
        self.prueba_1 = CTkEntry(self.Frame_izq, placeholder_text="Dias", width= 130)
        self.prueba_1.pack(pady=20, padx=10)
        
        self.prueba_2 = CTkEntry(self.Frame_izq, placeholder_text="Dato 2", width= 130)
        self.prueba_2.pack(pady=20, padx=10)
        
        self.prueba_3 = CTkEntry(self.Frame_izq, placeholder_text="Dato 3", width= 130)
        self.prueba_3.pack(pady=20, padx=10)
        
        self.prueba_4 = CTkEntry(self.Frame_izq, placeholder_text="Dato 4", width= 130)
        self.prueba_4.pack(pady=20, padx=10)
        
        self.prueba_5 = CTkEntry(self.Frame_izq, placeholder_text="Dato 5", width= 130)
        self.prueba_5.pack(pady=20, padx=10)
        
        self.prueba_6 = CTkEntry(self.Frame_izq, placeholder_text="Dato 6", width= 130)
        self.prueba_6.pack(pady=20, padx=10)
        
        #Boton de simular
        
        self.btn_generar = CTkButton(self.Frame_izq, text= "simular", font= ("Arial", 25) , command= self.Creacion_tabla)
        self.btn_generar.pack(pady=10)
        
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
        self.tabview.add("MONTE CARLO")
        
        self.Tablas()        
        
        
        # titulo de la segunda pestaña
        
        self.Monte_carlo = self.tabview.tab("MONTE CARLO")    
        
        #Titulo 
        
        self.Titulo_frame_der = CTkLabel(self.Monte_carlo, text= "MONTE CARLO", font= ("Arial", 30 ))
        
        self.Titulo_frame_der.pack(pady=10, padx=10)
        
        
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
        
    def Tablas(self):
        
        tablas = self.tabview.tab("TABLAS PREDEFINIDAS")
        
        self.scroll_frame = CTkScrollableFrame(tablas)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        
        #tabla 1 (personas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
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
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_2 = CTkTable(
            self.scroll_frame,
            values= encabezado_2,
            header_color="#0a2e57"
        )
        # Tabla_2.pack(expand=True, fill="both")
        Tabla_2.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_2 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_2 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_2 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_2 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_2.add_row(values= fila_t_1_2)
        Tabla_2.add_row(values= fila_t_2_2)
        Tabla_2.add_row(values= fila_t_3_2)
        Tabla_2.add_row(values= fila_t_4_2)
        
        
        #tabla 3 (recepcionistas por dia)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_3 = CTkTable(
            self.scroll_frame,
            values= encabezado_3,
            header_color="#0a2e57"
        )
        # Tabla_3.pack(expand=True, fill="both")
        Tabla_3.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_3 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_3 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_3 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_3 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_3.add_row(values= fila_t_1_3)
        Tabla_3.add_row(values= fila_t_2_3)
        Tabla_3.add_row(values= fila_t_3_3)
        Tabla_3.add_row(values= fila_t_4_3)
        
        #tabla 4 (cantidad de abandonos)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_4 = CTkTable(
            self.scroll_frame,
            values= encabezado_4,
            header_color="#0a2e57"
        )
        # Tabla_4.pack(expand=True, fill="both")
        Tabla_4.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_4 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_4 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_4 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_4 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_4.add_row(values= fila_t_1_4)
        Tabla_4.add_row(values= fila_t_2_4)
        Tabla_4.add_row(values= fila_t_3_4)
        Tabla_4.add_row(values= fila_t_4_4)
        
        #tabla 5 (tiempo de espera en la cola)
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_5 = CTkTable(
            self.scroll_frame,
            values= encabezado_5,
            header_color="#0a2e57"
        )
        # Tabla_5.pack(expand=True, fill="both")
        Tabla_5.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_5 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_5 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_5 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_5 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_5.add_row(values= fila_t_1_5)
        Tabla_5.add_row(values= fila_t_2_5)
        Tabla_5.add_row(values= fila_t_3_5)
        Tabla_5.add_row(values= fila_t_4_5)
        
        #tabla 6 (tipo de solicitud)
        
        # Encabezado
        encabezado_6 = [["Tipo de\nservicio", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_6 = CTkTable(
            self.scroll_frame,
            values= encabezado_6,
            header_color="#0a2e57"
        )
        # Tabla_6.pack(expand=True, fill="both")
        Tabla_6.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_6 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_6 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_6 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_6 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_6.add_row(values= fila_t_1_6)
        Tabla_6.add_row(values= fila_t_2_6)
        Tabla_6.add_row(values= fila_t_3_6)
        Tabla_6.add_row(values= fila_t_4_6)
        
        #tabla 7 (Grupo de personas)
        
        # Encabezado
        encabezado_7 = [["Personas", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_7 = CTkTable(
            self.scroll_frame,
            values= encabezado_7,
            header_color="#0a2e57"
        )
        # Tabla_7.pack(expand=True, fill="both")
        Tabla_7.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_7 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_7 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_7 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_7 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_7.add_row(values= fila_t_1_7)
        Tabla_7.add_row(values= fila_t_2_7)
        Tabla_7.add_row(values= fila_t_3_7)
        Tabla_7.add_row(values= fila_t_4_7)
        
        #tabla 8 (tipo de habitaciones)
        
        # Encabezado
        encabezado_8 = [["Tipos", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_8 = CTkTable(
            self.scroll_frame,
            values= encabezado_8,
            header_color="#0a2e57"
        )
        # Tabla_8.pack(expand=True, fill="both")
        Tabla_8.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_8 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_8 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_8 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_8 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_8.add_row(values= fila_t_1_8)
        Tabla_8.add_row(values= fila_t_2_8)
        Tabla_8.add_row(values= fila_t_3_8)
        Tabla_8.add_row(values= fila_t_4_8)
        
        #tabla 9 (costos brutos)
        
        # Encabezado
        encabezado_9 = [["Concepto", "Probabilidad", "Probabilidad\nacumulada", "Rango"]]
        
        Tabla_9 = CTkTable(
            self.scroll_frame,
            values= encabezado_9,
            header_color="#0a2e57"
        )
        # Tabla_9.pack(expand=True, fill="both")
        Tabla_9.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_9 = ["10 - 15", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_9 = ["16 - 25", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_9 = ["26 - 40", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_9 = ["21 - 60", "0.2", "1", "0.801 - 1"]
        
        Tabla_9.add_row(values= fila_t_1_9)
        Tabla_9.add_row(values= fila_t_2_9)
        Tabla_9.add_row(values= fila_t_3_9)
        Tabla_9.add_row(values= fila_t_4_9)
        
    def Creacion_tabla(self):
        
        #obtener los datos para hacer la tabla
        
        # if not self.prueba_1.get() or not self.prueba_2.get() or not self.prueba_3.get() or not self.prueba_4.get():
        #     messagebox.showwarning("CAMPOS","Complete los campos vacios", parent= self.Interfaz)
        #     return False
        
        try:
            
            # filas_predeterminadas = 10
            filas_predeterminadas = int(self.prueba_1.get())
            
        except Exception:
                messagebox.showerror("INVALIDACION","Datos invalidos", parent= self.Interfaz)
                return False
            
        if self.Tabla:
            self.Tabla.destroy()
        
        encabezados = [["Dias", "Aleatorio\ncargas", "Cargas", "Aleatorio\ntipo de\ncargas", "Aleatorio\nmaquinas", "Cantidad de\nmaquinas", "Aleatorio\ntiempo de\nciclo", "Tiempo de\nciclo", "Aleatorio\nestado\nmaquinas", "Estado\nmaquinas", "Tiempo"]]
        
        for i in range(filas_predeterminadas):
            fila_vacia = [str(i+1)] + [""] * 11
            encabezados.append(fila_vacia)
            
        #crear la tabla nueva
        
        self.Tabla = CTkTable(
            master = self.scroll_frame, 
            row = filas_predeterminadas + 1, 
            column= 11, 
            values= encabezados,
            width = 100,
            justify = "center",
            wraplength = 100
        )
        
        #mostrar tabla
        self.Tabla.pack(expand=True, fill="both", padx=10, pady=10)
        
Lavanderia()