import random 
from numpy import * 
import numpy as np 
from datetime import datetime
import customtkinter as ctk
import tkinter.ttk as ttk
from tabulate import tabulate
import tkinter as tk 

class GestionReservas():
    def __init__(self):

        """INFORMACION GENERAL: 
        habra 3 tipos de habitaciones: basica 1 ($2000), deluxe 2($2800) y suite 3($3500)
        numero de habitaciones: 55 estandar, 30 deluxe y 15 suite 
        capacidad: basica= 2, deluxe= 4, suite=6 
        3 temporadas: alta, media y baja 
        """

        #INTERFAZ 
        self.ventana=ctk.CTk()
        self.ventana.title("Gestion de Reservas Online")
        self.ventana.geometry("1200x800")

        w, h = 400, 60
        self.color_fondo = "#5D4037"
        self.color_hover = "#3E2723"
        self.color_texto = "#FFFFFF"
        self.color_Extra = "#8C8680"

        self.container = ctk.CTkFrame(self.ventana)
        self.container.pack(fill="both", expand=True)

        self.frame_principal = ctk.CTkFrame(self.container)
        self.frame_registro = ctk.CTkFrame(self.container)
        self.frame_simulacion = ctk.CTkFrame(self.container)

        self.crear_principal()
        self.crear_registro()
        self.crear_simulacion()

        self.mostrar_frame(self.frame_principal)

        self.ventana.mainloop()

    def mostrar_frame(self, frame):
        for f in (self.frame_principal, self.frame_registro, self.frame_simulacion):
            f.pack_forget()
        frame.pack(fill="both", expand=True)

    #BOTONES Y ELEMENTOS PRINCIPALES
    def crear_principal(self):

        self.boton_volver = ctk.CTkButton(self.frame_principal, text="←", width=35, height=35, corner_radius=25, fg_color=self.color_fondo, hover_color=self.color_hover, text_color="white", font=("Arial", 24, "bold")) 
        self.boton_volver.place(x=10,y=10 )

        self.tipo_habitacion = ctk.StringVar(value="basica")

        self.radio_basica = ctk.CTkRadioButton(self.frame_principal, text="Basica", variable=self.tipo_habitacion, value="basica", fg_color=self.color_hover, text_color=self.color_texto)
        self.radio_basica.place(x=120, y=300)

        self.radio_deluxe = ctk.CTkRadioButton(self.frame_principal, text="Deluxe", variable=self.tipo_habitacion, value="deluxe", fg_color=self.color_hover, text_color=self.color_texto)
        self.radio_deluxe.place(x=240, y=300)

        self.radio_suite = ctk.CTkRadioButton(self.frame_principal, text="Suite", variable=self.tipo_habitacion, value="suite", fg_color=self.color_hover, text_color=self.color_texto)
        self.radio_suite.place(x=360, y=300)

        self.guardar = ctk.CTkButton(self.frame_principal, text="Guardar", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto)
        self.guardar.place(x=80, y=750)

        self.registro = ctk.CTkButton(self.frame_principal, text="Registrarse", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=lambda: self.mostrar_frame(self.frame_registro))
        self.registro.place(x=360, y=750)

        self.simulacion = ctk.CTkButton(self.frame_principal, text="Simulacion", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=lambda: self.mostrar_frame(self.frame_simulacion))
        self.simulacion.place(x=650, y=750)

        #CAJAS DE TEXTO
        self.caja_num_habitaciones = ctk.CTkEntry(self.frame_principal, placeholder_text="Número de Habitaciones", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_num_habitaciones.place(x=50, y=100)

        self.caja_ingreso = ctk.CTkEntry(self.frame_principal, placeholder_text="Fecha Ingreso:", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_ingreso.place(x=50, y=200)

        self.caja_salida = ctk.CTkEntry(self.frame_principal, placeholder_text="Fecha Salida ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_salida.place(x=320, y=200)

        self.text_area = ctk.CTkTextbox(self.frame_principal, width=600, height=300, fg_color=self.color_fondo, text_color=self.color_texto)
        self.text_area.place(x=50, y=400)

    # ventana registro interfaz 
    def crear_registro(self):

        self.caja_nombre = ctk.CTkEntry(self.frame_registro, placeholder_text="Ingresa tu nombre: ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_nombre.place(x=35, y=20)
        
        self.caja_edad = ctk.CTkEntry(self.frame_registro, placeholder_text="Ingresa tu edad:", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_edad.place(x=35, y=100)
        
        self.caja_sexo = ctk.CTkEntry(self.frame_registro, placeholder_text="Seleccione su sexo: ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_sexo.place(x=35, y=180)
        
        self.caja_telefono = ctk.CTkEntry(self.frame_registro, placeholder_text="Ingresa tu número de telefono:", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_telefono.place(x=35, y=260)
        
        self.caja_correo = ctk.CTkEntry(self.frame_registro, placeholder_text="Ingresa tu correo electronico: ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_correo.place(x=35, y=340)
        
        self.caja_pago = ctk.CTkEntry(self.frame_registro, placeholder_text="Elija el metodo de pago:", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_pago.place(x=35, y=420)
        
        self.caja_ciudad = ctk.CTkEntry(self.frame_registro, placeholder_text="ingrese su ciudad de origen: ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_ciudad.place(x=35, y=500)
        
        self.guardar_registro = ctk.CTkButton(self.frame_registro, text="Guardar", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto)
        self.guardar_registro.place(x=35, y=610)

        ctk.CTkButton(self.frame_registro, text="Volver", width=250, height=60,fg_color=self.color_fondo, hover_color=self.color_hover,text_color=self.color_texto,command=lambda: self.mostrar_frame(self.frame_principal)).place(x=300, y=610)
    

    def crear_simulacion(self):
        # boton volver
        self.volver = ctk.CTkButton(self.frame_simulacion, text="Volver", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=lambda: self.mostrar_frame(self.frame_principal))
        self.volver.place(x=35, y=20)

        # botones para abrir cada tabla de probabilidades
        ctk.CTkButton(self.frame_simulacion, text="Tabla Reservas por Día", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_reservas_dias).place(x=35, y=110)
        ctk.CTkButton(self.frame_simulacion, text="Tabla Tipo Habitación", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_tipo_habitacion).place(x=35, y=180)
        ctk.CTkButton(self.frame_simulacion, text="Tabla Noches", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_noches).place(x=35, y=250)
        ctk.CTkButton(self.frame_simulacion, text="Tabla Porcentaje Pago", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_porcentaje_pago).place(x=35, y=320)
        ctk.CTkButton(self.frame_simulacion, text="Tabla Llegada", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_llegada).place(x=35, y=390)
        ctk.CTkButton(self.frame_simulacion, text="Tabla Cancelación", width=250, height=50, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.tabla_cancelacion).place(x=35, y=460)

        # boton que ejecuta noshows() y luego abre la tabla de resultados
        ctk.CTkButton(self.frame_simulacion, text="Ejecutar Simulación y Ver Resultados", width=350, height=60, fg_color=self.color_hover, hover_color=self.color_fondo, text_color=self.color_texto, command=self.ejecutar_y_ver_resultados).place(x=35, y=560)


    def ejecutar_y_ver_resultados(self):
        self.noshows()
        self.tablas_resultados()


    def noshows(self):
        
        self.ingreso_neto = 0
        self.penalizacion = 0
        self.ingreso_total = 0
        self.ingreso = 0
        self.reservas_hoy = 0
        self.porcentaje_pagado = 0
        self.numeros_aleatorios_habitacion = []
        self.numeros_aleatorios_evento = []
        self.numeros_aleatorios_dias = []
        self.numeros_aleatorios_noches = []
        self.numeros_aleatorios_porcentaje = []
        self.numeros_aleatorios_reservas = []
        self.filas_tabla = []

        self.estandar = 55
        self.deluxe = 30
        self.suite = 15
        
        self.ocupacion_estandar = [0] * 31
        self.ocupacion_deluxe = [0] * 31
        self.ocupacion_suite = [0] * 31
        self.ingreso_por_dia = [0] * 30 

        #generacion numeros aleatorios cantidad de reservas por dia 
        for i in range(30):
            self.numeros_aleatorios_reservas.append(random.random())

        indice = 0
        #cuantas habitaciones hay ocupadas (no haya sobrecarga)
    
        for i in range(30):
            self.estandar += self.ocupacion_estandar[i]
            self.deluxe += self.ocupacion_deluxe[i]
            self.suite += self.ocupacion_suite[i]
     
            n_reservas = self.numeros_aleatorios_reservas[i]
            if n_reservas <= 0.05:
                self.reservas_hoy = 0
            elif n_reservas <= 0.15:
                self.reservas_hoy = 1
            elif n_reservas <= 0.30:
                self.reservas_hoy = 2
            elif n_reservas <= 0.50:
                self.reservas_hoy = 3
            elif n_reservas <= 0.7:
                self.reservas_hoy = 4
            elif n_reservas <= 0.85:
                self.reservas_hoy = 5
            elif n_reservas <= 0.95:
                self.reservas_hoy = 6
            else:
                self.reservas_hoy = 7
            
            # generacion de numeros aleatoris 
            for j in range(self.reservas_hoy):
                self.alea = random.random()
                self.numeros_aleatorios_habitacion.append(self.alea)
                self.alea2 = random.random()
                self.numeros_aleatorios_evento.append(self.alea2)
                self.alea3 = random.random()
                self.numeros_aleatorios_dias.append(self.alea3)
                self.alea4 = random.random()
                self.numeros_aleatorios_noches.append(self.alea4)
                self.alea5 = random.random()
                self.numeros_aleatorios_porcentaje.append(self.alea5)
                
                #tipo de habitacion y si hay disponible o no 
                n_habit = self.numeros_aleatorios_habitacion[indice]
                if n_habit <= 0.5:
                    self.tipo_habitacion = 1
                    self.precio_por_noche = 2000
                    if self.estandar <= 0:
                        print(f"Día {i+1}: No hay estandar disponible")
                        indice += 1
                        continue
                    self.estandar -= 1
                elif n_habit <= 0.85:
                    self.tipo_habitacion = 2
                    self.precio_por_noche = 2800
                    if self.deluxe <= 0:
                        print(f"Día {i+1}: No hay deluxe disponible")
                        indice += 1
                        continue
                    self.deluxe -= 1
                else:
                    self.tipo_habitacion = 3
                    self.precio_por_noche = 3500
                    if self.suite <= 0:
                        print(f"Día {i+1}: No hay suite disponible")
                        indice += 1
                        continue
                    self.suite -= 1
                
                #cantidad de noches que se queda cada cliente 
                n_noches = self.numeros_aleatorios_noches[indice]
                if n_noches <= 0.2:
                    self.noches = 6
                elif n_noches <= 0.55:
                    self.noches = 5
                elif n_noches <= 0.75:
                    self.noches = 4
                elif n_noches <= 0.90:
                    self.noches = 3
                else:
                    self.noches = 2

                #tiene en cuenta cuantas noches esta ocupada un cuarto 
                # solo si no se pasa los 30 ddias del mes 
                #que dia sale (del mes)
                if self.tipo_habitacion == 1:
                    dia_salida = i + self.noches
                    if dia_salida <= 30:
                        self.ocupacion_estandar[dia_salida] += 1
                elif self.tipo_habitacion == 2:
                    dia_salida = i + self.noches
                    if dia_salida <= 30:
                        self.ocupacion_deluxe[dia_salida] += 1
                else:
                    dia_salida = i + self.noches
                    if dia_salida <= 30:
                        self.ocupacion_suite[dia_salida] += 1

                # porcentaje del total que pagan los clientes para reservar
                self.ingreso = self.precio_por_noche * self.noches

                n_porcentaje = self.numeros_aleatorios_porcentaje[indice]
                if n_porcentaje <= 0.50:
                    self.porcentaje_pagado = self.ingreso * 0.30
                elif n_porcentaje <= 0.80:
                    self.porcentaje_pagado = self.ingreso * 0.50
                else:
                    self.porcentaje_pagado = self.ingreso

                # prob que reserve y llegue, cancele o no-shows
                #probabilidad que llegue 
                n_evento = self.numeros_aleatorios_evento[indice]
                if n_evento <= 0.7:
                    self.ingreso_total += self.ingreso
                    self.ingreso_por_dia[i] += self.ingreso
                    print(f"Reserva {indice+1}: LLEGA - ${self.ingreso}")
                #probabilidad de no-shows
                elif n_evento <= 0.8:
                    self.ingreso_total += self.porcentaje_pagado
                    print(f"Reserva {indice+1}: NO-SHOW, el hotel cobra ${self.porcentaje_pagado}")
                #probabilidad de que cancele y con que anticipacion avisa
                #segun lo que tarde en cancelar la penalizacion que se cobra 
                else:
                    n_dias = self.numeros_aleatorios_dias[indice]
                    if n_dias <= 0.6:
                        penalizacion_porcentaje = 0.20
                        dias_anticipacion = 30
                    elif n_dias <= 0.85:
                        penalizacion_porcentaje = 0.50
                        dias_anticipacion = 20
                    else:
                        penalizacion_porcentaje = 0.90
                        dias_anticipacion = 10
                    
                    self.penalizacion = self.ingreso * penalizacion_porcentaje
                    self.ingreso_total += self.penalizacion
                    print(f"Reserva {indice+1}: CANCELA - Penalización {penalizacion_porcentaje*100}% - ${self.penalizacion}")

                # llenado de tabla
                if n_evento <= 0.7:
                    evento_str = "LLEGA"
                    n_dias_str = "-"
                    dias_anticip = "-"
                    penalizacion_str = "-"
                    devolucion_str = "-"
                    ganancia = self.ingreso
                elif n_evento <= 0.8:
                    evento_str = "NO-SHOW"
                    n_dias_str = "-"
                    dias_anticip = "-"
                    penalizacion_str = "-"
                    devolucion_str = "-"
                    ganancia = self.porcentaje_pagado
                else:
                    evento_str = "CANCELA"
                    n_dias_str = round(n_dias, 4)
                    dias_anticip = dias_anticipacion
                    penalizacion_str = round(self.penalizacion, 2)
                    devolucion_str = round(self.porcentaje_pagado - self.penalizacion, 2)
                    ganancia = self.penalizacion

                self.filas_tabla.append((
                    i + 1, round(n_reservas, 4), self.reservas_hoy,
                    round(n_habit, 4), self.tipo_habitacion, self.precio_por_noche,
                    round(n_noches, 4), self.noches,
                    round(n_porcentaje, 4), round(self.porcentaje_pagado, 2),
                    round(n_evento, 4), evento_str,
                    n_dias_str, dias_anticip,
                    penalizacion_str, devolucion_str,
                    round(ganancia, 2)
                ))

                indice += 1 # contador para cada reserva (no importa el dia)
        #for i in range(30):
            #print(f"Día {i+1}: ${self.ingreso_por_dia[i]}")

        print(f"\n--- INGRESO TOTAL DEL MES: ${self.ingreso_total} ---")


    # helper para crear el treeview 
    #se usa para que no se repita los bloques 
    def _crear_treeview(self, win, columnas, datos):
        container = tk.Frame(win)
        container.pack(fill="both", expand=True)
        tree = ttk.Treeview(container, columns=tuple(str(i) for i in range(1, len(columnas)+1)), show="headings")
        for idx, col in enumerate(columnas, start=1):
            tree.heading(str(idx), text=col)
            tree.column(str(idx), width=250, anchor="center")
        for fila in datos:
            tree.insert("", "end", values=tuple(fila))
        scroll_y = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        scroll_x = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


    def tabla_reservas_dias(self):
        #cantidad de reservas que hubo en el dia (probabilidad)
        #el usuario lo iingresa
        self.reservas_dias = np.zeros((8,4), dtype=object)
        self.titulos = ["Personas que reservan al dia", "probabilidad", "acumulada", "rango"]
        self.evento = [0,1,2,3,4,5,6,7]
        self.probabilidad = [0.05,0.1,0.15,0.2,0.2,0.15,0.1,0.05]
        self.acumulada = [0.05,0.15,0.3,0.5,0.7,0.85,0.95,1.0]
        self.rango = ["0.00-0.05", "0.05-0.15", "0.15-0.30", "0.30-0.50",
                      "0.50-0.70", "0.70-0.85", "0.85-0.95", "0.95-1.00"]
        for f in range(8):
            self.reservas_dias[f][0] = self.evento[f]
            self.reservas_dias[f][1] = self.probabilidad[f]
            self.reservas_dias[f][2] = self.acumulada[f]
            self.reservas_dias[f][3] = self.rango[f]

        win = tk.Toplevel()
        win.title("Reservas por día")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')

        # opcion para que el usuario cambie los datos
        frame_top = ctk.CTkFrame(win, fg_color=self.color_fondo)
        frame_top.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(frame_top, text="¿Quieres ingresar tus propios datos?", text_color=self.color_texto).pack(side="left", padx=10)
        self.opcion_reservas = ctk.StringVar(value="No")
        menu = ctk.CTkOptionMenu(frame_top, variable=self.opcion_reservas, values=["No", "Si"], fg_color=self.color_fondo, button_color=self.color_hover, text_color=self.color_texto)
        menu.pack(side="left", padx=10)

        # frame donde van los campos de captura (se muestra solo si elige Si)
        frame_campos = ctk.CTkFrame(win, fg_color=self.color_Extra)
        self.entradas_reservas_evento = []
        self.entradas_reservas_prob = []
        for i in range(8):
            fila = ctk.CTkFrame(frame_campos, fg_color=self.color_Extra)
            fila.pack(pady=2)
            ctk.CTkLabel(fila, text=f"Reservas dia {i}:", text_color=self.color_texto, width=120).pack(side="left")
            e1 = ctk.CTkEntry(fila, width=80, fg_color=self.color_fondo, text_color=self.color_texto)
            e1.insert(0, str(self.evento[i]))
            e1.pack(side="left", padx=5)
            ctk.CTkLabel(fila, text="Probabilidad:", text_color=self.color_texto, width=100).pack(side="left")
            e2 = ctk.CTkEntry(fila, width=80, fg_color=self.color_fondo, text_color=self.color_texto)
            e2.insert(0, str(self.probabilidad[i]))
            e2.pack(side="left", padx=5)
            self.entradas_reservas_evento.append(e1)
            self.entradas_reservas_prob.append(e2)

        # frame del treeview
        frame_tree = tk.Frame(win)

        def actualizar():
            # si eligio Si, leer los campos y recalcular
            if self.opcion_reservas.get() == "Si":
                frame_campos.pack(fill="x", padx=10, pady=5)
                self.evento = [int(e.get()) for e in self.entradas_reservas_evento]
                self.probabilidad = [float(e.get()) for e in self.entradas_reservas_prob]
                suma = 0
                self.acumulada = []
                self.rango = []
                limite_inferior = 0
                for x in self.probabilidad:
                    suma = suma + x
                    self.acumulada.append(round(suma, 4))
                for y in self.acumulada:
                    self.rango.append(f"{limite_inferior}-{y}")
            else:
                frame_campos.pack_forget()
                self.evento = [0,1,2,3,4,5,6,7]
                self.probabilidad = [0.05,0.1,0.15,0.2,0.2,0.15,0.1,0.05]
                self.acumulada = [0.05,0.15,0.3,0.5,0.7,0.85,0.95,1.0]
                self.rango = ["0.00-0.05", "0.05-0.15", "0.15-0.30", "0.30-0.50",
                              "0.50-0.70", "0.70-0.85", "0.85-0.95", "0.95-1.00"]
            for f in range(8):
                self.reservas_dias[f][0] = self.evento[f]
                self.reservas_dias[f][1] = self.probabilidad[f]
                self.reservas_dias[f][2] = self.acumulada[f]
                self.reservas_dias[f][3] = self.rango[f]
            # limpiar y redibujar el treeview
            for widget in frame_tree.winfo_children():
                widget.destroy()
            self._crear_treeview(frame_tree, self.titulos, self.reservas_dias)

        ctk.CTkButton(frame_top, text="Aplicar", fg_color=self.color_hover, hover_color=self.color_fondo, text_color=self.color_texto, command=actualizar).pack(side="left", padx=10)
        frame_tree.pack(fill="both", expand=True)
        self._crear_treeview(frame_tree, self.titulos, self.reservas_dias)


    def tabla_tipo_habitacion(self):
        #Tipo de habitacion(probabilidad)
        #cambiar la probabilidad 
        self.habitaciones = np.zeros((3,4), dtype=object)
        self.titulos1 = ["Tipo de habitación", "Probabilidad", "acumulada", "rango"]
        self.evento1 = ["Basica(1)", "Deluxe(2)", "Suite(3)"]
        self.probabilidad1 = [0.5,0.35,0.15]
        self.acumulada1 = [0.5,0.85,1.0]
        self.rango1 = ["0.0-0.5","0.51-0.85","0.86-1"]
        for f in range(3):
            self.habitaciones[f][0] = self.evento1[f]
            self.habitaciones[f][1] = self.probabilidad1[f]
            self.habitaciones[f][2] = self.acumulada1[f]
            self.habitaciones[f][3] = self.rango1[f]

        win = tk.Toplevel()
        win.title("Tipo de habitación")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')

        frame_top = ctk.CTkFrame(win, fg_color=self.color_fondo)
        frame_top.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(frame_top, text="¿Quieres cambiar las probabilidades?", text_color=self.color_texto).pack(side="left", padx=10)
        self.opcion_habitacion = ctk.StringVar(value="No")
        menu = ctk.CTkOptionMenu(frame_top, variable=self.opcion_habitacion, values=["No", "Si"], fg_color=self.color_fondo, button_color=self.color_hover, text_color=self.color_texto)
        menu.pack(side="left", padx=10)

        frame_campos = ctk.CTkFrame(win, fg_color=self.color_Extra)
        self.entradas_habit_prob = []
        nombres = ["Basica(1)", "Deluxe(2)", "Suite(3)"]
        for i in range(3):
            fila = ctk.CTkFrame(frame_campos, fg_color=self.color_Extra)
            fila.pack(pady=2)
            ctk.CTkLabel(fila, text=f"{nombres[i]} - Probabilidad:", text_color=self.color_texto, width=180).pack(side="left")
            e = ctk.CTkEntry(fila, width=80, fg_color=self.color_fondo, text_color=self.color_texto)
            e.insert(0, str(self.probabilidad1[i]))
            e.pack(side="left", padx=5)
            self.entradas_habit_prob.append(e)

        frame_tree = tk.Frame(win)

        def actualizar():
            if self.opcion_habitacion.get() == "Si":
                frame_campos.pack(fill="x", padx=10, pady=5)
                self.probabilidad1 = [float(e.get()) for e in self.entradas_habit_prob]
                suma = 0
                self.acumulada1 = []
                self.rango1 = []
                limite_inferior = 0
                for x in self.probabilidad1:
                    suma = suma + x
                    self.acumulada1.append(round(suma, 4))
                for y in self.acumulada1:
                    self.rango1.append(f"{limite_inferior}-{y}")
            else:
                frame_campos.pack_forget()
                self.probabilidad1 = [0.5,0.35,0.15]
                self.acumulada1 = [0.5,0.85,1.0]
                self.rango1 = ["0.0-0.5","0.51-0.85","0.86-1"]
            for f in range(3):
                self.habitaciones[f][0] = self.evento1[f]
                self.habitaciones[f][1] = self.probabilidad1[f]
                self.habitaciones[f][2] = self.acumulada1[f]
                self.habitaciones[f][3] = self.rango1[f]
            for widget in frame_tree.winfo_children():
                widget.destroy()
            self._crear_treeview(frame_tree, self.titulos1, self.habitaciones)

        ctk.CTkButton(frame_top, text="Aplicar", fg_color=self.color_hover, hover_color=self.color_fondo, text_color=self.color_texto, command=actualizar).pack(side="left", padx=10)
        frame_tree.pack(fill="both", expand=True)
        self._crear_treeview(frame_tree, self.titulos1, self.habitaciones)


    def tabla_noches(self):
        #Cantidad de noches que escoge cada cliente 
        #el usuario lo ingresa
        self.noches_probabilidad = np.zeros((5,4), dtype=object)
        self.titulos2 = ["Noches que un cliente reserva", "Probabilidad", "acumulada", "rango"]
        self.evento2 = [6,5,4,3,2]
        self.probabilidad2 = [0.2,0.35,0.2,0.15,0.1]
        self.acumulada2 = [0.2,0.55,0.75,0.90,1]
        self.rango2 = ["0.0-0.2", "0.201-0.55", "0.551-0.75", "0.751-0.90", "0.901-1"]
        for f in range(5):
            self.noches_probabilidad[f][0] = self.evento2[f]
            self.noches_probabilidad[f][1] = self.probabilidad2[f]
            self.noches_probabilidad[f][2] = self.acumulada2[f]
            self.noches_probabilidad[f][3] = self.rango2[f]

        win = tk.Toplevel()
        win.title("Noches por cliente")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')

        frame_top = ctk.CTkFrame(win, fg_color=self.color_fondo)
        frame_top.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(frame_top, text="¿Quieres ingresar tus propios datos?", text_color=self.color_texto).pack(side="left", padx=10)
        self.opcion_noches = ctk.StringVar(value="No")
        menu = ctk.CTkOptionMenu(frame_top, variable=self.opcion_noches, values=["No", "Si"], fg_color=self.color_fondo, button_color=self.color_hover, text_color=self.color_texto)
        menu.pack(side="left", padx=10)

        frame_campos = ctk.CTkFrame(win, fg_color=self.color_Extra)
        self.entradas_noches_evento = []
        self.entradas_noches_prob = []
        for i in range(5):
            fila = ctk.CTkFrame(frame_campos, fg_color=self.color_Extra)
            fila.pack(pady=2)
            ctk.CTkLabel(fila, text=f"Noches:", text_color=self.color_texto, width=60).pack(side="left")
            e1 = ctk.CTkEntry(fila, width=60, fg_color=self.color_fondo, text_color=self.color_texto)
            e1.insert(0, str(self.evento2[i]))
            e1.pack(side="left", padx=5)
            ctk.CTkLabel(fila, text="Probabilidad:", text_color=self.color_texto, width=100).pack(side="left")
            e2 = ctk.CTkEntry(fila, width=80, fg_color=self.color_fondo, text_color=self.color_texto)
            e2.insert(0, str(self.probabilidad2[i]))
            e2.pack(side="left", padx=5)
            self.entradas_noches_evento.append(e1)
            self.entradas_noches_prob.append(e2)

        frame_tree = tk.Frame(win)

        def actualizar():
            if self.opcion_noches.get() == "Si":
                frame_campos.pack(fill="x", padx=10, pady=5)
                self.evento2 = [int(e.get()) for e in self.entradas_noches_evento]
                self.probabilidad2 = [float(e.get()) for e in self.entradas_noches_prob]
                suma = 0
                self.acumulada2 = []
                self.rango2 = []
                limite_inferior = 0
                for x in self.probabilidad2:
                    suma = suma + x
                    self.acumulada2.append(round(suma, 4))
                for y in self.acumulada2:
                    self.rango2.append(f"{limite_inferior}-{y}")
            else:
                frame_campos.pack_forget()
                self.evento2 = [6,5,4,3,2]
                self.probabilidad2 = [0.2,0.35,0.2,0.15,0.1]
                self.acumulada2 = [0.2,0.55,0.75,0.90,1]
                self.rango2 = ["0.0-0.2", "0.201-0.55", "0.551-0.75", "0.751-0.90", "0.901-1"]
            for f in range(5):
                self.noches_probabilidad[f][0] = self.evento2[f]
                self.noches_probabilidad[f][1] = self.probabilidad2[f]
                self.noches_probabilidad[f][2] = self.acumulada2[f]
                self.noches_probabilidad[f][3] = self.rango2[f]
            for widget in frame_tree.winfo_children():
                widget.destroy()
            self._crear_treeview(frame_tree, self.titulos2, self.noches_probabilidad)

        ctk.CTkButton(frame_top, text="Aplicar", fg_color=self.color_hover, hover_color=self.color_fondo, text_color=self.color_texto, command=actualizar).pack(side="left", padx=10)
        frame_tree.pack(fill="both", expand=True)
        self._crear_treeview(frame_tree, self.titulos2, self.noches_probabilidad)


    def tabla_porcentaje_pago(self):
        #porcentaje del total de la reserva que paga el cliente
        #fijo
        self.porcentaje_proba = np.zeros((3,4), dtype=object)
        self.titulos3 = ["porcentajes que pagan", "probabilidad", "acumulada", "rango"]
        self.evento3 = ["30%", "50%","100%"]
        self.probabilidad3 = [0.5,0.3,0.2]
        self.acumulada3 = [0.5,0.8,1]
        self.rango3 = ["0.0-0.5", "0.51-0.8", "0.81-1"]
        for f in range(3):
            self.porcentaje_proba[f][0] = self.evento3[f]
            self.porcentaje_proba[f][1] = self.probabilidad3[f]
            self.porcentaje_proba[f][2] = self.acumulada3[f]
            self.porcentaje_proba[f][3] = self.rango3[f]

        win = tk.Toplevel()
        win.title("Porcentaje de pago")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')
        self._crear_treeview(win, self.titulos3, self.porcentaje_proba)


    def tabla_llegada(self):
        #Probabilidad de cancelacion, no-show o llegue el cliente
        #fija
        self.llegada_proba = np.zeros((3,4), dtype=object)
        self.titulos4 = ["Evento", "Probabilidad", "acumulada", "rango"]
        self.evento4 = ["Llega", "No-Show", "Cancela"]
        self.probabilidad4 = [0.7,0.1,0.2]
        self.acumulada4 = [0.7,0.8,1]
        self.rango4 = ["0.0-0.7", "0.71-0.8", "0.81-1"]
        for f in range(3):
            self.llegada_proba[f][0] = self.evento4[f]
            self.llegada_proba[f][1] = self.probabilidad4[f]
            self.llegada_proba[f][2] = self.acumulada4[f]
            self.llegada_proba[f][3] = self.rango4[f]

        win = tk.Toplevel()
        win.title("Llega / No-Show / Cancela")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')
        self._crear_treeview(win, self.titulos4, self.llegada_proba)


    def tabla_cancelacion(self):
        #si cancela los dias con los que cancela de anticipacion
        #fija
        self.cancela_proba = np.zeros((3,4), dtype=object)
        self.titulos5 = ["dias de anticipacion con los que cancela", "probabilidad", "acumulada", "rango"]
        self.evento5 = [30, 20, 10]
        self.probabilidad5 = [0.6,0.25,0.15]
        self.acumulada5 = [0.6,0.85,1]
        self.rango5 = ["0.0-0.6", "0.61-0.85", "0.851-1"]
        for f in range(3):
            self.cancela_proba[f][0] = self.evento5[f]
            self.cancela_proba[f][1] = self.probabilidad5[f]
            self.cancela_proba[f][2] = self.acumulada5[f]
            self.cancela_proba[f][3] = self.rango5[f]

        win = tk.Toplevel()
        win.title("Días de anticipación de cancelación")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')
        self._crear_treeview(win, self.titulos5, self.cancela_proba)


    def tablas_resultados(self):
        win = tk.Toplevel()
        win.title("Tabla final")
        ancho = win.winfo_screenwidth()
        alto = win.winfo_screenheight()
        win.geometry(f"{ancho}x{alto}+0+0")
        win.state('zoomed')

        # tk.Frame directo en la ventana, sin CTkFrame en medio
        container = tk.Frame(win)
        container.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(container, columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"), show="headings")

        self.tree.heading("1", text="Días")
        self.tree.heading("2", text="Números aleatorios")
        self.tree.heading("3", text="Reservas por dia")
        self.tree.heading("4", text="Números aleatorios")
        self.tree.heading("5", text="Tipo de habitación")
        self.tree.heading("6", text="Precio")
        self.tree.heading("7", text="Números aleatorios")
        self.tree.heading("8", text="Cantidad de noches")
        self.tree.heading("9", text="Números aleatorios")
        self.tree.heading("10", text="Porcentaje Pagado")
        self.tree.heading("11", text="Número aleatorio")
        self.tree.heading("12", text="Llega, no llega o cancelacion")
        self.tree.heading("13", text="Número aleatorio")
        self.tree.heading("14", text="Días con los que cancela de anticipacion")
        self.tree.heading("15", text="Penalizacion")
        self.tree.heading("16", text="devolución por cancelacion")
        self.tree.heading("17", text="Ganancia por día")

        self.tree.column("1", width=150)
        self.tree.column("2", width=150)
        self.tree.column("3", width=150)
        self.tree.column("4", width=150)
        self.tree.column("5", width=150)
        self.tree.column("6", width=150)
        self.tree.column("7", width=150)
        self.tree.column("8", width=150)
        self.tree.column("9", width=250)
        self.tree.column("10", width=150)
        self.tree.column("11", width=150)
        self.tree.column("12", width=250)
        self.tree.column("13", width=150)
        self.tree.column("14", width=250)
        self.tree.column("15", width=150)
        self.tree.column("16", width=200)
        self.tree.column("17", width=150)

        scroll_y = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        scroll_x = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # insertar datos generados en noshows()
        for f in self.filas_tabla:
            self.tree.insert("", "end", values=f)


si = GestionReservas()
