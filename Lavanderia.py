
#* Ya muestra los valores en la tabla (falta cheacar que si se actualizan los datos, si se muestren correctamente. Adeamas faltaria poner un bloqueo si la probabilidad no llega a 1)

from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from CTkTable import CTkTable
import random

# Configuración de estilo
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")


class Lavanderia:
    
    def __init__(self):
        
        self.Interfaz = ctk.CTk()
        self.Interfaz.title("Interfaz --- Lavanderia")
        
        self.Cargar_datos() 
        self.Calculos_probAcu_rang() 
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Variables a usar
        
        self.Tabla_1_e = None
        self.Tabla_2_e = None
        self.Tabla_3_e = None
        self.Tabla_4_e = None
        self.Tabla_5_e = None
        
        self.L_tabla_1 = []
        self.L_tabla_2 = []
        self.L_tabla_3 = []
        self.L_tabla_4 = []
        self.L_tabla_5 = []
        
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

        self.btn_simular = CTkButton(self.Monte_carlo, text= "simular", font= ("Arial", 25), command= self.Creacion_tabla)
        self.btn_simular.pack(pady=10)
        
        # Para que la tabla no se salga de la pantalla
        
        self.scroll_frame = CTkScrollableFrame(self.Monte_carlo)
        self.scroll_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.Tabla = None
        self.resultados_tabla_3 = []
        self.resultados_tabla_5 = []
        
        self.Interfaz.update()
        
        
        
        # try: 
        #     self.principal.state("zoomed")
        # except: 
        #     self.principal.attributes("-zoomed", True)
        
        
        
        self.Interfaz.state("zoomed") #windows
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
            ["Sabanas / Toallas", 0.6],
            ["Ropa de huesped", 0.3],
            ["Ropa del staff", 0.1]
        ]
        
        #Tabla 3
        self.Estado_maquinas = [
            ["Normal", 0.58],
            ["Retraso", 0.25],
            ["Falla", 0.12],
            ["Corte de luz / agua", 0.05]
        ]
        
        #Tabla 4
        self.Numero_maquinas = [
            ["1", 0.15],
            ["2", 0.45],
            ["3", 0.3],
            ["4", 0.1]
        ]
        
        #Tabla 5
        self.Tiempo_ciclo = [
            ["20", 0.35],
            ["30", 0.4],
            ["40", 0.2],
            ["50", 0.05]
        ]
        
        self.Tabla_6_e_d = [
            ["Normal", 1],
            ["Retraso", 1.5],
            ["Falla", 0],
            ["Corte de luz / agua", 2]
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
        
        for val_3, prob_3 in self.Estado_maquinas:
            
            inicio_3 = Probabilidad_acumulada_3
            
            Probabilidad_acumulada_3 = round(Probabilidad_acumulada_3 + prob_3, 4)
            
            rango_3 = str(round(inicio_3, 4)) + " - " + str(round(Probabilidad_acumulada_3, 4))
            
            self.Tabla_3_e_d.append([val_3, prob_3, Probabilidad_acumulada_3, rango_3])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 4 (completa)
        
        Probabilidad_acumulada_4 = 0.0
        self.Tabla_4_e_d = []
        
        for val_4, prob_4 in self.Numero_maquinas:
            
            inicio_4 = Probabilidad_acumulada_4
            
            Probabilidad_acumulada_4 = round(Probabilidad_acumulada_4 + prob_4, 4)
            
            rango_4 = str(round(inicio_4, 4)) + " - " + str(round(Probabilidad_acumulada_4, 4))
            
            self.Tabla_4_e_d.append([val_4, prob_4, Probabilidad_acumulada_4, rango_4])
            
            
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        #Tabla 5 (completa)
        
        Probabilidad_acumulada_5 = 0.0
        self.Tabla_5_e_d = []
        
        for val_5, prob_5 in self.Tiempo_ciclo:
            
            inicio_5 = Probabilidad_acumulada_5
            
            Probabilidad_acumulada_5 = round(Probabilidad_acumulada_5 + prob_5, 4)
            
            rango_5 = str(round(inicio_5, 4)) + " - " + str(round(Probabilidad_acumulada_5, 4))
            
            self.Tabla_5_e_d.append([val_5, prob_5, Probabilidad_acumulada_5, rango_5])
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Tablas_Editables(self):
        
        tablas = self.tabview.tab("TABLAS EDITABLES")
        
        self.frame_sup = CTkFrame(tablas, width=200, height= 200, corner_radius=10)
        self.frame_sup.pack(fill="both", pady=20, padx=10)
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #cuadro de texto
        
        self.Valor = CTkEntry(self.frame_sup, placeholder_text= "Valor", width= 130)
        self.Valor.pack(side="left", padx=10)
        
        #se deja sin pack para mostarlo despues (SOLO CUANDO ESTA SELECCIONADA LA TABLA 6)
        self.Tiempo = CTkEntry(self.frame_sup, placeholder_text="Tiempo", width=130)
        
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
        
        #tabla 3 (Estado de las maquinas)
        
        # Encabezado
        encabezado_3 = [["Estado", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_3 = CTkLabel(self.scroll_frame, text= "Estado de las maquinas", font= ("Arial", 20 ))
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
        
        #tabla 4 (Numero de maquinas)
        
        # Encabezado
        encabezado_4 = [["Cantidad", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_4 = CTkLabel(self.scroll_frame, text= "Numero de maquinas", font= ("Arial", 20 ))
        self.Titulo_t_4.pack(pady=10, padx=10)
        
        
        self.Tabla_4_e = CTkTable(
            self.scroll_frame,
            values= encabezado_4 + self.Tabla_4_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_4
        )
        self.Tabla_4_e.pack(expand=True, fill="both", pady=(0, 50))
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #tabla 5 (Tiempo de ciclo "lavado, secado y doblado"
        
        # Encabezado
        encabezado_5 = [["Tiempo", "Probabilidad", "Probabilidad acumulada", "Rango"]]
        
        #titulo
        self.Titulo_t_5 = CTkLabel(self.scroll_frame, text= "Tiempo de ciclo lavado, secado y doblado", font= ("Arial", 20 ))
        self.Titulo_t_5.pack(pady=10, padx=10)
        
        
        self.Tabla_5_e = CTkTable(
            self.scroll_frame,
            values= encabezado_5 + self.Tabla_5_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_5
        )
        self.Tabla_5_e.pack(expand=True, fill="both", pady=(0, 50))
        
        
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        
        #Tabla de tiempo 
        
        # Encabezado
        encabezado_6 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        
        self.Titulo_t_6 = CTkLabel(self.scroll_frame, text= "Tiempo total de trabajo de las maquinas", font= ("Arial", 20 ))
        self.Titulo_t_6.pack(pady=10, padx=10)
        
        self.Tabla_6_e = CTkTable(
            self.scroll_frame,
            values= encabezado_6 + self.Tabla_6_e_d,
            header_color="#0a2e57",
            command=self.Seleccionar_tabla_6
        )
        self.Tabla_6_e.pack(expand=True, fill="both", pady=(0, 50))
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Seleccionar_tabla_1(self, data):
        self.tabla_activa = self.Tabla_1_e
        self.lista_datos_activa = self.Cargas_dias
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_2(self, data):
        self.tabla_activa = self.Tabla_2_e
        self.lista_datos_activa = self.Tipos_cargas
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_3(self, data):
        self.tabla_activa = self.Tabla_3_e
        self.lista_datos_activa = self.Estado_maquinas
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_4(self, data):
        self.tabla_activa = self.Tabla_4_e
        self.lista_datos_activa = self.Numero_maquinas
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_5(self, data):
        self.tabla_activa = self.Tabla_5_e
        self.lista_datos_activa = self.Tiempo_ciclo
        
        #ocultamos el entry
        self.Tiempo.pack_forget()
        self.Probabilidad.pack(side="left", padx=10, after= self.Valor)
        self.Seleccionar_fila(data)
        
    def Seleccionar_tabla_6(self, data):
        self.tabla_activa = self.Tabla_6_e
        self.lista_datos_activa = self.Tabla_6_e_d
        
        #ocultamos el entry
        self.Probabilidad.pack_forget()
        
        #se mustra el entry
        self.Tiempo.pack(side= "left", padx= 10, after= self.Valor)
        self.Seleccionar_fila(data)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Seleccionar_fila(self, data):
        self.indice_selec = data['row']
        
        if self.indice_selec > 0:
            valores_fila = self.tabla_activa.get_row(self.indice_selec)
            
            self.Valor.delete(0, "end")    
            self.Valor.insert(0, valores_fila[0])  
            
            if self.tabla_activa == self.Tabla_6_e:
                
                self.Tiempo.delete(0, "end")
                self.Tiempo.insert(0, valores_fila[1])
            
            else:
                self.Probabilidad.delete(0, "end")    
                self.Probabilidad.insert(0, valores_fila[1])
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Verificar_probabilidad(self):
        self.suma_total = 0
        
        if self.lista_datos_activa:
            
            for fila in self.lista_datos_activa:
                
                if self.tabla_activa != self.Tabla_6_e:
                    self.suma_total += float(fila[1])
                
        self.suma_total = round(self.suma_total, 2)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Actualizar_datos(self):
        
        # cosas para la tabla 6 y para la normal 
        
        if self.lista_datos_activa is None or self.indice_selec <= 0:
            messagebox.showwarning("ATENCION", "Primero seleccione una fila de una tabla")
            return
        
        if self.tabla_activa == self.Tabla_6_e:
            
            new_val = self.Valor.get()
            new_tiempo = int(self.Tiempo.get())
            
            self.lista_datos_activa[self.indice_selec - 1] = [new_val, new_tiempo]
            
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
        encabezado_6 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d 
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        
        
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
            
            if self.tabla_activa == self.Tabla_6_e:
                new_tiempo = self.Tiempo.get()
                self.lista_datos_activa.append([new_val, new_tiempo])
            
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
        encabezado_6 = [["Estado de la maquina", "Tiempo que se multiplica"]]
        
        datos_completos_1 = encabezado_1 + self.Tabla_1_e_d 
        datos_completos_2 = encabezado_2 + self.Tabla_2_e_d
        datos_completos_3 = encabezado_3 + self.Tabla_3_e_d
        datos_completos_4 = encabezado_4 + self.Tabla_4_e_d
        datos_completos_5 = encabezado_5 + self.Tabla_5_e_d
        datos_completos_6 = encabezado_6 + self.Tabla_6_e_d
        
        
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
            
            self.filas_tabla_monte_carlo = 10
            
        except Exception:
                messagebox.showerror("INVALIDACION","Datos invalidos", parent= self.Interfaz)
                return False
            
        if self.Tabla:
            self.Tabla.destroy()
            
        encabezados = [["Dias", "Aleatorio\ncargas", "Rango de\nCargas", "Cargas\nExactas", "Aleatorio\ntipo de\ncargas", "Tipo de\ncargas","Aleatorio\nmaquinas", "Cantidad de\nmaquinas", "Aleatorio\ntiempo de\nciclo", "Tiempo de\nciclo", "Aleatorio\nestado\nmaquinas", "Estado\nmaquinas", "Tiempo"]]
        
        for i in range(self.filas_tabla_monte_carlo):
            fila_vacia = [str(i+1)] + [""] * 12
            encabezados.append(fila_vacia)
            
        #crear la tabla principal
        
        self.Tabla = CTkTable(
            master = self.scroll_frame, 
            row = self.filas_tabla_monte_carlo + 1, 
            column= len(fila_vacia), #12 
            values= encabezados,
            width = 100,
            justify = "center",
            wraplength = 100
        )
        
        #mostrar tabla
        self.Tabla.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.Generacion_aleatorios()
    
    
    def Generacion_aleatorios(self):
        
        self.L_tabla_1 = []
        self.L_tabla_2 = []
        self.L_tabla_3 = []
        self.L_tabla_4 = []
        self.L_tabla_5 = []
        
        for _ in range(self.filas_tabla_monte_carlo):
            
            
            ale_tabla_1 = round(random.random(), 4)
            ale_tabla_2 = round(random.random(), 4)
            ale_tabla_3 = round(random.random(), 4)
            ale_tabla_4 = round(random.random(), 4)
            ale_tabla_5 = round(random.random(), 4)
            
            
            self.L_tabla_1.append(ale_tabla_1)
            self.L_tabla_2.append(ale_tabla_2)
            self.L_tabla_3.append(ale_tabla_3)
            self.L_tabla_4.append(ale_tabla_4)
            self.L_tabla_5.append(ale_tabla_5)
            
            
            # Aleatorios 1  (cargas exactas)
            
            columna_tabla_1 = 1
            for indice_1 in range(len(self.L_tabla_1)):
                valor_1 = self.L_tabla_1[indice_1]
                
                self.Tabla.insert(indice_1 + 1, columna_tabla_1, valor_1)
            
            
            # Aleatorios 2 (tipos de cargas)
            
            columna_tabla_2 = 4
            for indice_2 in range(len(self.L_tabla_2)):
                valor_2 = self.L_tabla_2[indice_2]
                
                self.Tabla.insert(indice_2 + 1, columna_tabla_2, valor_2)
            
            
            
            # Aleatorios 3 (estados de maquinas)
            
            columna_tabla_3 = 10
            for indice_3 in range(len(self.L_tabla_3)):
                valor_3 = self.L_tabla_3[indice_3]
                
                self.Tabla.insert(indice_3 + 1, columna_tabla_3, valor_3)
            
            
            
            # Aleatorios 4 (numero de maquinas)
            
            columna_tabla_4 = 6
            for indice_4 in range(len(self.L_tabla_4)):
                valor_4 = self.L_tabla_4[indice_4]
                
                self.Tabla.insert(indice_4 + 1, columna_tabla_4, valor_4)
            
            
            
            # Aleatorios 5 (tiempo de ciclo)
            
            columna_tabla_5 = 8
            for indice_5 in range(len(self.L_tabla_5)):
                valor_5 = self.L_tabla_5[indice_5]
                
                self.Tabla.insert(indice_5 + 1, columna_tabla_5, valor_5)
            
        self.Probabilidades_Cargas_dias()
    
    
    def Probabilidades_Cargas_dias(self):
        
        #comparar con los rangos
        
        resultados_tabla_1 = []
        resultados_cargas_exactos = []
        
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
                    
                    suma = (primero + segundo) 
                    res = suma // 2
                    
                    resultados_cargas_exactos.append(res)
                    
                    break
                
                
                
            # Cargas Dias
            
            columna_tabla_1 = 2
            for indice_1 in range(len(resultados_tabla_1)):
                valor_1 = resultados_tabla_1[indice_1]
                
                self.Tabla.insert(indice_1 + 1, columna_tabla_1, valor_1)
            
            
            
            
            #Cargas exactas 
            
            columna_tabla_1_1 = 3
            for indice_1_1 in range(len(resultados_cargas_exactos)):
                valor_1_1 = resultados_cargas_exactos[indice_1_1]
                
                self.Tabla.insert(indice_1_1 + 1, columna_tabla_1_1, valor_1_1)
            
        self.Probabilidades_Tipos_cargas()
    
    
    def Probabilidades_Tipos_cargas(self):
        
        #comparar con los rangos 
        
        resultados_tabla_2 = []
        
        
        for ale in self.L_tabla_2:
            
            for fila in self.Tabla_2_e_d:
                
                str_rango = fila[-1]
                partes = str_rango.split(" - ")
                
                inf = float(partes [0].strip())
                sup = float(partes [1].strip())
                
                if ale > inf and ale <= sup:
                    
                    valor_correcto = fila[0]
                    
                    resultados_tabla_2.append(valor_correcto)
                    
                    break
                
        
            # Tipos de cargas
            columna_tabla_2 = 5

            for indice_2 in range(len(resultados_tabla_2)): 
                valor_2 = resultados_tabla_2[indice_2]

                self.Tabla.insert(indice_2 + 1, columna_tabla_2, valor_2)
        
        self.Probabilidades_Numero_maquinas()
    
    
    def Probabilidades_Numero_maquinas(self):
        
        resultados_tabla_4 = []
        
        for ale in self.L_tabla_4:
            
            for fila in self.Tabla_4_e_d:
                
                str_rango = fila[-1]
                partes = str_rango.split(" - ")
                
                inf = float(partes[0].strip())
                sup = float(partes[1].strip())
                
                if ale > inf and ale <= sup:
                    
                    valor_correcto = fila[0]
                    
                    resultados_tabla_4.append(valor_correcto)
                    
                    break
                
            # Numero de maquinas
            
            columna_tabla_4 = 7
            
            for indice_4 in range(len(resultados_tabla_4)):
                valor_4 = resultados_tabla_4[indice_4]
                
                self.Tabla.insert(indice_4 + 1, columna_tabla_4, valor_4)
                
        self.Probabilidades_Tiempo_ciclo()
    
    
    def Probabilidades_Tiempo_ciclo(self):
        
        self.resultados_tabla_5 = []
        
        for ale in self.L_tabla_5:
            
            for fila in self.Tabla_5_e_d:
                
                str_rango = fila[-1]
                partes = str_rango.split(" - ")
                
                inf = float(partes[0].strip())
                sup = float(partes[1].strip())
                
                if ale > inf and ale <= sup:
                    
                    valor_correcto = fila[0]
                    
                    self.resultados_tabla_5.append(valor_correcto)
                    
                    break
                
            # Tiempo_ciclo  
            
            columna_tabla_5 = 9
            
            for indice_5 in range(len(self.resultados_tabla_5)):
                
                valor_5 = self.resultados_tabla_5[indice_5]
                
                self.Tabla.insert(indice_5 + 1, columna_tabla_5, valor_5)
                
        
        self.Probabilidades_Estados_maquinas()
    
    
    def Probabilidades_Estados_maquinas(self):
        
        #comparar con los rangos 
        
        self.resultados_tabla_3 = []
        
        for ale in self.L_tabla_3:
            
            for fila in self.Tabla_3_e_d:
                
                str_rango = fila[-1]
                partes = str_rango.split(" - ")
                
                inf = float(partes [0].strip())
                sup = float(partes [1].strip())
                
                if ale > inf and ale <= sup:
                    
                    valor_correcto = fila[0]
                    
                    self.resultados_tabla_3.append(valor_correcto)
                    
                    break
                
            #Estados de maquinas
            
            columna_tabla_3 = 11
            
            for indice_3 in range(len(self.resultados_tabla_3)):
                valor_3 = self.resultados_tabla_3[indice_3]
                
                self.Tabla.insert(indice_3 + 1, columna_tabla_3, valor_3)
                
        self.Tiempo_final()
    
    def Tiempo_final(self):
        
        resultado_tabla_6 = []
        
        for i in range(len(self.resultados_tabla_3)):
            
            res_t_3 = self.resultados_tabla_3[i]
            
            for val, n in self.Tabla_6_e_d:
                
                if res_t_3 == val:
                    
                    res_t_5 = self.resultados_tabla_5[i]
                    
                    mult = float(res_t_5) * n
                    
                    resultado_tabla_6.append(mult)
                    
                    break
                
            #ultima columna
            
            columna_tabla_6 = 12
            
            for indice_6 in range(len(resultado_tabla_6)):
                valor_6 = resultado_tabla_6[indice_6]
                
                self.Tabla.insert(indice_6 + 1, columna_tabla_6, valor_6)
    
Lavanderia()