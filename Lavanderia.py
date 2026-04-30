
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
        
        
        #tabla 1 (cargas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Cargas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        Tabla_1 = CTkTable(
            self.scroll_frame,
            values= encabezado_1,
            header_color="#0a2e57"
        )
        # Tabla_1.pack(expand=True, fill="both")
        Tabla_1.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_1 = ["5 - 10", "0.2", "0.2", "0 - 0.2"]
        fila_t_2_1 = ["11 - 20", "0.4", "0.6", "0.2001 - 0.60"]
        fila_t_3_1 = ["21 - 30", "0.3", "0.9", "0.601 - 0.9"]
        fila_t_4_1 = ["31 - 40", "0.1", "1", "0.9001 - 1"]
        
        Tabla_1.add_row(values= fila_t_1_1)
        Tabla_1.add_row(values= fila_t_2_1)
        Tabla_1.add_row(values= fila_t_3_1)
        Tabla_1.add_row(values= fila_t_4_1)
        
        
        #tabla 2 (Tipos de cargas)
        
        # Encabezado
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de cargas", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        Tabla_2 = CTkTable(
            self.scroll_frame,
            values= encabezado_2,
            header_color="#0a2e57"
        )
        # Tabla_2.pack(expand=True, fill="both")
        Tabla_2.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_2 = ["Sabanas / Toallas", "0.6", "0.6", "0 - 0.6"]
        fila_t_2_2 = ["Ropa de huesped", "0.3", "0.9", "0.6001 - 0.9"]
        fila_t_3_2 = ["Ropa del staff", "0.1", "1", "0.901 - 1"]
        
        Tabla_2.add_row(values= fila_t_1_2)
        Tabla_2.add_row(values= fila_t_2_2)
        Tabla_2.add_row(values= fila_t_3_2)
        
        
        #tabla 3 (Estado de las maquinas)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Estado de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        Tabla_3 = CTkTable(
            self.scroll_frame,
            values= encabezado_3,
            header_color="#0a2e57"
        )
        # Tabla_3.pack(expand=True, fill="both")
        Tabla_3.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_3 = ["Normal", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_3 = ["Retraso", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_3 = ["Falla", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_3 = ["Corte de luz / agua", "0.2", "1", "0.801 - 1"]
        
        Tabla_3.add_row(values= fila_t_1_3)
        Tabla_3.add_row(values= fila_t_2_3)
        Tabla_3.add_row(values= fila_t_3_3)
        Tabla_3.add_row(values= fila_t_4_3)
        
        #tabla 4 (Numero de maquinas)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Numero de maquinas", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        Tabla_4 = CTkTable(
            self.scroll_frame,
            values= encabezado_4,
            header_color="#0a2e57"
        )
        # Tabla_4.pack(expand=True, fill="both")
        Tabla_4.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_4 = ["1", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_4 = ["2", "0.45", "0.6", "0.1501 - 0.60"]
        fila_t_3_4 = ["3", "0.3", "0.9", "0.601 - 0.9"]
        fila_t_4_4 = ["4", "0.1", "1", "0.901 - 1"]
        
        Tabla_4.add_row(values= fila_t_1_4)
        Tabla_4.add_row(values= fila_t_2_4)
        Tabla_4.add_row(values= fila_t_3_4)
        Tabla_4.add_row(values= fila_t_4_4)
        
        #tabla 5 (Tiempo de ciclo "lavado, secado y doblado"
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de ciclo lavado, secado y doblado", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        Tabla_5 = CTkTable(
            self.scroll_frame,
            values= encabezado_5,
            header_color="#0a2e57"
        )
        # Tabla_5.pack(expand=True, fill="both")
        Tabla_5.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_5 = ["20", "0.35", "0.35", "0 - 0.35"]
        fila_t_2_5 = ["30", "0.4", "0.75", "0.3501 - 0.75"]
        fila_t_3_5 = ["40", "0.2", "0.95", "0.7501 - 0.95"]
        fila_t_4_5 = ["50", "0.05", "1", "0.9501 - 1"]
        
        Tabla_5.add_row(values= fila_t_1_5)
        Tabla_5.add_row(values= fila_t_2_5)
        Tabla_5.add_row(values= fila_t_3_5)
        Tabla_5.add_row(values= fila_t_4_5)
        
    def Tablas_Editables(self):
        
        tablas = self.tabview.tab("TABLAS EDITABLES")
        
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
        
        #tabla 1 (cargas por dia)
        
        # Encabezado
        encabezado_1 = [["Personas", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_1 = CTkLabel(self.scroll_frame, text= "Cargas por dia", font= ("Arial", 20 ))
        self.Titulo_t_1.pack(pady=10, padx=10)
        
        Tabla_1 = CTkTable(
            self.scroll_frame,
            values= encabezado_1,
            header_color="#0a2e57"
        )
        # Tabla_1.pack(expand=True, fill="both")
        Tabla_1.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_1 = ["5 - 10", "0.2", "0.2", "0 - 0.2"]
        fila_t_2_1 = ["11 - 20", "0.4", "0.6", "0.2001 - 0.60"]
        fila_t_3_1 = ["21 - 30", "0.3", "0.9", "0.601 - 0.9"]
        fila_t_4_1 = ["31 - 40", "0.1", "1", "0.9001 - 1"]
        
        Tabla_1.add_row(values= fila_t_1_1)
        Tabla_1.add_row(values= fila_t_2_1)
        Tabla_1.add_row(values= fila_t_3_1)
        Tabla_1.add_row(values= fila_t_4_1)
        
        
        #tabla 2 (Tipos de cargas)
        
        # Encabezado
        encabezado_2 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_2 = CTkLabel(self.scroll_frame, text= "Tipos de cargas", font= ("Arial", 20 ))
        self.Titulo_t_2.pack(pady=10, padx=10)
        
        Tabla_2 = CTkTable(
            self.scroll_frame,
            values= encabezado_2,
            header_color="#0a2e57"
        )
        # Tabla_2.pack(expand=True, fill="both")
        Tabla_2.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_2 = ["Sabanas / Toallas", "0.6", "0.6", "0 - 0.6"]
        fila_t_2_2 = ["Ropa de huesped", "0.3", "0.9", "0.6001 - 0.9"]
        fila_t_3_2 = ["Ropa del staff", "0.1", "1", "0.901 - 1"]
        
        Tabla_2.add_row(values= fila_t_1_2)
        Tabla_2.add_row(values= fila_t_2_2)
        Tabla_2.add_row(values= fila_t_3_2)
        
        
        #tabla 3 (Estado de las maquinas)
        
        # Encabezado
        encabezado_3 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Estado de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_3.pack(pady=10, padx=10)
        
        Tabla_3 = CTkTable(
            self.scroll_frame,
            values= encabezado_3,
            header_color="#0a2e57"
        )
        # Tabla_3.pack(expand=True, fill="both")
        Tabla_3.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_3 = ["Normal", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_3 = ["Retraso", "0.35", "0.50", "0.1501 - 0.50"]
        fila_t_3_3 = ["Falla", "0.3", "0.8", "0.501 - 0.8"]
        fila_t_4_3 = ["Corte de luz / agua", "0.2", "1", "0.801 - 1"]
        
        Tabla_3.add_row(values= fila_t_1_3)
        Tabla_3.add_row(values= fila_t_2_3)
        Tabla_3.add_row(values= fila_t_3_3)
        Tabla_3.add_row(values= fila_t_4_3)
        
        #tabla 4 (Numero de maquinas)
        
        # Encabezado
        encabezado_4 = [["Abandonos", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Numero de maquinas", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        Tabla_4 = CTkTable(
            self.scroll_frame,
            values= encabezado_4,
            header_color="#0a2e57"
        )
        # Tabla_4.pack(expand=True, fill="both")
        Tabla_4.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_4 = ["1", "0.15", "0.15", "0 - 0.15"]
        fila_t_2_4 = ["2", "0.45", "0.6", "0.1501 - 0.60"]
        fila_t_3_4 = ["3", "0.3", "0.9", "0.601 - 0.9"]
        fila_t_4_4 = ["4", "0.1", "1", "0.901 - 1"]
        
        Tabla_4.add_row(values= fila_t_1_4)
        Tabla_4.add_row(values= fila_t_2_4)
        Tabla_4.add_row(values= fila_t_3_4)
        Tabla_4.add_row(values= fila_t_4_4)
        
        #tabla 5 (Tiempo de ciclo "lavado, secado y doblado"
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de ciclo lavado, secado y doblado", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        Tabla_5 = CTkTable(
            self.scroll_frame,
            values= encabezado_5,
            header_color="#0a2e57"
        )
        # Tabla_5.pack(expand=True, fill="both")
        Tabla_5.pack(expand=True, fill="both", pady=(0, 50))
        
        fila_t_1_5 = ["20", "0.35", "0.35", "0 - 0.35"]
        fila_t_2_5 = ["30", "0.4", "0.75", "0.3501 - 0.75"]
        fila_t_3_5 = ["40", "0.2", "0.95", "0.7501 - 0.95"]
        fila_t_4_5 = ["50", "0.05", "1", "0.9501 - 1"]
        
        Tabla_5.add_row(values= fila_t_1_5)
        Tabla_5.add_row(values= fila_t_2_5)
        Tabla_5.add_row(values= fila_t_3_5)
        Tabla_5.add_row(values= fila_t_4_5)
        
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