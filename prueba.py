import random 
from numpy import * 
import numpy as np 
from datetime import datetime
import customtkinter as ctk


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

        self.caja_pordia = ctk.CTkEntry(self.frame_simulacion, placeholder_text="Total por dias: ", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_pordia.place(x=35, y=20)
        
        self.caja_pormes = ctk.CTkEntry(self.frame_simulacion, placeholder_text="Total:", width=250, height=60, fg_color=self.color_fondo, text_color=self.color_texto)
        self.caja_pormes.place(x=35, y=100)

        self.boton_simular = ctk.CTkButton(self.frame_simulacion, text="Simular", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=self.noshows)
        self.boton_simular.place(x=35, y=200)

        ctk.CTkButton(self.frame_simulacion, text="Volver", width=250, height=60, fg_color=self.color_fondo, hover_color=self.color_hover, text_color=self.color_texto, command=lambda: self.mostrar_frame(self.frame_principal)).place(x=35, y=280)

        self.text_area_simulacion = ctk.CTkTextbox(self.frame_simulacion, width=600, height=450, fg_color=self.color_fondo, text_color=self.color_texto)
        self.text_area_simulacion.place(x=320, y=20)



        #CALCULAR NUMERO DE NOCHES UWU'NT 
        """from datetime import datetime
        try: 
            fecha1=datetime.strptime(self.fecha_entrada, "%Y-%m-%d")
            fecha2=datetime.strptime(self.fecha_salida, "%Y-%m-%d")
        except:
            self.noches=1

        #se lee la cantidad de numeros que se encuentran en el archivo(numero de habitaciones)
        #para despues sacar la cantidad de habitaciones que estan ocupadas
        with open("habitaciones.txt", "r") as archivo_lectura:
            for linea in archivo_lectura:
                self.numeros.append(int(linea.strip()))
        self.cantidad=len(self.numeros)
        
        while self.band:
            if self.cantidad>=50:
                print("ho hay habitaciones disponibles")
                self.band=False
                break
            
            for i in range(self.numero_habitaciones):
                self.tipo_habitacion=str(input("¿Qué tipo de habitación desea? (Basica/Deluxe/Suite)"))
                if self.tipo_habitacion == "basica": 
                    self.archivo_habitaciones.write(str(1) + "\n")
                    self.capacidad_maxima=2
                    self.precio_por_noche=2000
                elif self.tipo_habitacion=="deluxe":
                    self.archivo_habitaciones.write(str(2) + "\n")
                    self.capacidad_maxima=4
                    self.precio_por_noche=2800
                elif self.tipo_habitacion=="suite":
                    self.archivo_habitaciones.write(str(3) + "\n")
                    self.capacidad_maxima=6
                    self.precio_por_noche=3500
                else: 
                    print("Opcion no valida, intente de nuevo")
                    continue

            # Volver a leer el archivo para actualizar la cantidad
            self.numeros = []
            with open("habitaciones.txt", "r") as archivo_lectura:
                for linea in archivo_lectura:
                    self.numeros.append(int(linea.strip()))
            self.cantidad = len(self.numeros)

            for i in self.numeros:
                if i==1:
                    self.estandar=self.estandar-1
                elif i==2:
                    self.deluxe=self.deluxe-1
                elif i==3:
                    self.suite=self.suite-1

            self.band=False

            print(self.numeros)
            print(self.cantidad)
            return self.numeros,self.cantidad

        self.archivo_habitaciones.close()

    def registrocliente(self):

        #Registo datos cliente (REGISTRO DATOS DEL HUESPED)
        self.mayores=0
        self.menores=0
        self.numero_reservas = self.capacidad_maxima
        
        print(f"La habitación {self.tipo_habitacion} tiene capacidad para {self.capacidad_maxima} personas")
        print(f"Se registrarán {self.numero_reservas} personas")
        
        for i in range(self.numero_reservas):
            self.nombre_completo=str(input("Ingrese su nombre completo: "))
            self.edad=int(input("Ingrese su edad: "))
            self.sexo=str(input("Ingrese su genero: "))
            if self.edad>18:
                self.telefono=int(input("Ingrese su número telefonico: "))
                self.correo=input("Ingrese su correo electronico: ")
                self.metodo_pago = input("Método de pago (Tarjeta/Efectivo/Transferencia): ")
                self.ciudad=input("Ingrese su ciudad de origen: ")
                self.mayores=self.mayores+1
            else: 
                print("registro completo")
                self.menores=self.menores+1
        
        #CALCULAR EL TOTAL DE LA RESERVA 
        self.total_reserva= self.numero_habitaciones*self.precio_por_noche*self.noches
        print("el total es:",self.total_reserva)
        print(f"El total a pagar es: {self.total_reserva}")
        self.pago = int(input("Ingrese la cantidad a pagar: "))
        self.porcentaje=(self.pago/self.total_reserva)*100
        print("el porcentaje abonado es",self.porcentaje)

    def confirmacionreserva(self):
        print("\n" + "="*50)
        print("CONFIRMACION DE RESERVA")
        print("="*50)
        print(f"Tipo de habitacion: {self.tipo_habitacion}")
        print(f"Capacidad: {self.capacidad_maxima} personas")
        print(f"Numero de habitaciones: {self.numero_habitaciones}")
        print(f"Fecha entrada: {self.fecha_entrada}")
        print(f"Fecha salida: {self.fecha_salida}")
        print(f"Noches: {self.noches}")
        print(f"Precio por noche: ${self.precio_por_noche}")
        print(f"Total a pagar: ${self.total_reserva}")
        print("="*50)"""

    def noshows(self):
        self.text_area_simulacion.delete("1.0", "end")
        
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

            #cantidad de reservas que hubo en el dia (probabilidad)
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
                        self.text_area_simulacion.insert("end", f"Día {i+1}: No hay estandar disponible\n")
                        indice += 1
                        continue
                    self.estandar -= 1
                elif n_habit <= 0.85:
                    self.tipo_habitacion = 2
                    self.precio_por_noche = 2800
                    if self.deluxe <= 0:
                        self.text_area_simulacion.insert("end", f"Día {i+1}: No hay deluxe disponible\n")
                        indice += 1
                        continue
                    self.deluxe -= 1
                else:
                    self.tipo_habitacion = 3
                    self.precio_por_noche = 3500
                    if self.suite <= 0:
                        self.text_area_simulacion.insert("end", f"Día {i+1}: No hay suite disponible\n")
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
                    self.text_area_simulacion.insert("end", f"Reserva {indice+1}: LLEGA - ${self.ingreso}\n")
                #probabilidad de no-shows
                elif n_evento <= 0.8:
                    self.ingreso_total += self.porcentaje_pagado
                    self.text_area_simulacion.insert("end", f"Reserva {indice+1}: NO-SHOW, el hotel cobra ${self.porcentaje_pagado}\n")
                #probabilidad de que cancele y con que anticipacion avisa
                #segun lo que tarde en cancelar la penalizacion que se cobra 
                else:
                    n_dias = self.numeros_aleatorios_dias[indice]
                    if n_dias <= 0.6:
                        penalizacion_porcentaje = 0.20
                    elif n_dias <= 0.85:
                        penalizacion_porcentaje = 0.50
                    else:
                        penalizacion_porcentaje = 0.90
                    
                    self.penalizacion = self.ingreso * penalizacion_porcentaje
                    self.ingreso_total += self.penalizacion
                    self.text_area_simulacion.insert("end", f"Reserva {indice+1}: CANCELA - Penalización {penalizacion_porcentaje*100}% - ${self.penalizacion}\n")

                indice += 1
        
        # Mostrar ingreso por dia
        self.text_area_simulacion.insert("end", "\n" + "="*50 + "\n")
        self.text_area_simulacion.insert("end", "INGRESO POR DIA\n")
        self.text_area_simulacion.insert("end", "="*50 + "\n")
        
        for i in range(30):
            self.text_area_simulacion.insert("end", f"Día {i+1}: ${self.ingreso_por_dia[i]}\n")
        
        self.text_area_simulacion.insert("end", "\n" + "="*50 + "\n")
        self.text_area_simulacion.insert("end", f"INGRESO TOTAL DEL MES: ${self.ingreso_total}\n")
        self.text_area_simulacion.insert("end", "="*50 + "\n")
        
        self.caja_pordia.delete(0, "end")
        self.caja_pordia.insert(0, f"Total por dia: ${self.ingreso_por_dia[-1]}")
        
        self.caja_pormes.delete(0, "end")
        self.caja_pormes.insert(0, f"Total mes: ${self.ingreso_total}")
        
        print(f"\n--- INGRESO TOTAL DEL MES: ${self.ingreso_total} ---")

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
        round(ganancia, 2) ))

    indice += 1

    
    def tablas_probabilidades(self):
        #cantidad de reservas que hubo en el dia (probabilidad)
        #el usuario lo iingresa
        self.reservas_dias=np.zeros((8,4), dtype=object)
        self.titulos=["Personas que reservan al dia", "probabilidad", "acumulada", "rango"]
        self.evento=[0,1,2,3,4,5,6,7]
        self.probabilidad=[0.05,0.1,0.15,0.2,0.2,0.15,0.1,0.05]
        self.acumulada=[0.05,0.15,0.3,0.5,0.7,0.85,0.95,1.0]
        self.rango = ["0.00-0.05", "0.05-0.15", "0.15-0.30", "0.30-0.50", 
             "0.50-0.70", "0.70-0.85", "0.85-0.95", "0.95-1.00"]
        for f in range(8):  # filas
            self.reservas_dias[f][0] = self.evento[f]
            self.reservas_dias[f][1] = self.probabilidad[f]
            self.reservas_dias[f][2] = self.acumulada[f]
            self.reservas_dias[f][3] = self.rango[f]

        #Tipo de habitacion(probabilidad)
        #cambiar la probabilidad 
        self.habitaciones=np.zeros((3,4), dtype=object)
        self.titulos1=["Tipo de habitación", "Probabilidad", "acumulada", "rango"]
        self.evento1=["Basica(1)", "Deluxe(2)", "Suite(3)"]
        self.probabilidad1=[0.5,0.35,0.15]
        self.acumulada1=[0.5,0.85,1.0]
        self.rango1=["0.0-0.5","0.51-0.85","0.86-1"]
        for f in range(3):
            self.habitaciones[f][0]=self.evento1[f]
            self.habitaciones[f][1]=self.probabilidad1[f]
            self.habitaciones[f][2]=self.acumulada1[f]
            self.habitaciones[f][3]=self.rango1[f]

        #Cantidad de noches que escoge cada cliente 
        #el usuario lo ingresa
        self.noches_probabilidad=np.zeros((5,4), dtype=object)
        self.titulos2=["Noches que un cliente reserva", "Probabilidad", "acumulada", "rango"]
        self.evento2=[6,5,4,3,2,1]
        self.probabilidad2=[0.2,0.35,0.2,0.15,0.1]
        self.acumulada2=[0.2,0.55,0.75,0.90,1]
        self.rango2=["0.0-0.2", "0.201-0.55", "0.551-0.75", "0.751-0.90", "0.901-1"]
        for f in range(5):
            self.noches_probabilidad[f][0]=self.evento2[f]
            self.noches_probabilidad[f][1]=self.probabilidad2[f]
            self.noches_probabilidad[f][2]=self.acumulada2[f]
            self.noches_probabilidad[f][3]=self.rango2[f]

        #porcentaje del total de la reserva que paga el cliente
        #fijo
        self.porcentaje_proba=np.zeros((3,4),dtype=object)
        self.titulos3=["porcentajes que pagan", "probabilidad", "acumulada", "rango"]
        self.evento3=["30%", "50%","100%"]
        self.probabilidad3=[0.5,0.3,0.2]
        self.acumulada3=[0.5,0.8,1]
        self.rango3=["0.0-0.5", "0.51-0.8", "0.81-1"]
        for f in range(3):
            self.porcentaje_proba[f][0]=self.evento3[f]
            self.porcentaje_proba[f][1]=self.probabilidad3[f]
            self.porcentaje_proba[f][2]=self.acumulada3[f]
            self.porcentaje_proba[f][3]=self.rango3[f]

        #Probabilidad de cancelacion, no-show o llegue el cliente
        #fija
        self.llegada_proba=np.zeros((3,4), dtype=object)
        self.titulos4=["Evento", "Probabilidad", "acumulada", "rango"]
        self.evento4=["Llega", "No-Show", "Cancela"]
        self.probabilidad4=[0.7,0.1,0.2]
        self.acumulada4=[0.7,0.8,1]
        self.rango4=["0.0-0.7", "0.71-0.8", "0.81-1"]
        for f in range(3):
            self.llegada_proba[f][0]=self.evento4[f]
            self.llegada_proba[f][1]=self.probabilidad4[f]
            self.llegada_proba[f][2]=self.acumulada4[f]
            self.llegada_proba[f][3]=self.rango4[f] 

        #si cancela los dias con los que cancela de anticipacion
        #fija
        self.cancela_proba=np.zeros((3,4),dtype=object)
        self.titulos5=["dias de anticipacion con los que cancela", "probabilidad", "acumulada", "rango"]
        self.evento5=[30, 20, 10]
        self.probabilidad5=[0.6,0.25,0.15]
        self.acumulada5=[0.6,0.85,1]
        self.rango5=["0.0-0.6", "0.61-0.85", "0.851-1"]
        for f in range(3):
            self.cancela_proba[f][0]=self.evento5[f]
            self.cancela_proba[f][1]=self.probabilidad5[f]
            self.cancela_proba[f][2]=self.acumulada5[f]
            self.cancela_proba[f][3]=self.rango5[f] 

        #cantidad de reservas que hubo en el dia (probabilidad)
        print(tabulate(self.reservas_dias, headers=self.titulos, tablefmt="fancy_grid"))
        #tipo de habitacion que escoge cada cliente
        print(tabulate(self.habitaciones,headers=self.titulos1, tablefmt="fancy_grid"))
        #cantidad de noches que se queda cada cliente 
        print(tabulate(self.noches_probabilidad, headers=self.titulos2, tablefmt="fancy_grid"))
        #porcentaje del total de la reserva que paga el cliente
        print(tabulate(self.porcentaje_proba,headers=self.titulos3, tablefmt="fancy_grid"))
        #Probabilidad de cancelacion, no-show o llegue el cliente
        print(tabulate(self.llegada_proba, headers=self.titulos4,tablefmt="fancy_grid"))
        #si cancela los dias con los que cancela de anticipacion
        print(tabulate(self.cancela_proba, headers=self.titulos5, tablefmt="fancy_grid"))


    def tablas_resultados(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Tabla final")
        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")
        self.ventana.state('zoomed')

        # tk.Frame directo en la ventana, sin CTkFrame en medio
        container = tk.Frame(self.ventana)
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

        self.ventana.update_idletasks()
        self.ventana.update()
        self.ventana.mainloop()

        
    
        
si=GestionReservas()
#si.disponibilidad_habitacion()
#si.registrocliente()
#si.confirmacionreserva()
#si.noshows()