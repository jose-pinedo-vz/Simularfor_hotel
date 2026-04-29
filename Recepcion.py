
#! Interfaz sin funcionamiento 

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
        
        #Titulo (frame der)
        
        self.Titulo_frame_der = CTkLabel(self.Frame_Der, text= "MONTE CARLO", font= ("Arial", 30 ))
        
        self.Titulo_frame_der.pack(pady=10, padx=10)
        
        
        #Tabla
        
        # Para que la tabla no se salga de la pantalla
        self.scroll_frame = CTkScrollableFrame(self.Frame_Der)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        #---------------------------------------------------------
        
        self.Tabla = None
        
        self.Interfaz.update() 
        self.Interfaz.state("zoomed") #windows
        # self.Interfaz.attributes('-zoomed', True) #Linux
        
        self.Interfaz.mainloop()
        
        #---------------------------------------------------------
        
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