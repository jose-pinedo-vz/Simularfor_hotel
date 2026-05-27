
import customtkinter as ctk
from CTkTable import CTkTable
import random
import threading
import time
import matplotlib.pyplot as plt
from pathlib import Path
from CTkMessagebox import CTkMessagebox


class Area_Atencion_Medica():
    def Iniciar(self):
        self.color_fondo="#5D4037"
        self.color_hover="#3E2723"
        self.color_texto="#FFFFFF"
        self.color_Extra="#D7CCC8"

    
        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulacion de área medica")
        self.Ventana.geometry("1000x700")
        self.Ventana.after(200,lambda:self.Ventana.state('zoomed'))


        ctk.CTkLabel(self.Ventana,text="ÁREA MEDICA",font=("arial",20,"bold"),text_color=self.color_texto
                     ).place(relx=.5,rely=.05,anchor=ctk.CENTER)
        
        self.btn_nav_tablas=ctk.CTkButton(self.Ventana, text="Tablas",
                                          width=100,
                                          fg_color=self.color_hover,
                                          hover_color="#694F48",
                                          command=self.mostrar_pestaña_tablas)
        self.btn_nav_tablas.place(relx=.35, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_simulacion=ctk.CTkButton(self.Ventana,
                                              text="Simulación",
                                              width=100,
                                              fg_color=self.color_hover,
                                              hover_color="#694F48",
                                              command=self.mostrar_pestaña_simulacion)
        self.btn_nav_simulacion.place(relx=.65, rely=.05, anchor=ctk.CENTER)

  
        self.Main_frame=ctk.CTkFrame(self.Ventana,
                                     fg_color=self.color_Extra)
        self.Main_frame.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)

   
        self.Contenedor_Configuracion=ctk.CTkFrame(self.Main_frame,
                                                   fg_color="transparent")
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.Frame_tablas= ctk.CTkScrollableFrame(self.Contenedor_Configuracion)
        self.Frame_tablas.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.7)


        self.Frame_simulacion=ctk.CTkFrame(self.Main_frame,
                                           fg_color="transparent")

        self.DeclaracionVarialbles()
        self.Ventana.mainloop()

    def DeclaracionVarialbles(self):
        self.Aleatoreos=[]
        
        self.datos_grafica_inventario=[]
        self.Llegadas_de_pacientes=[(5,6,7,8,9),
                                    (.1,.4,.2,.1,.2)]
        
        self.Prob_cruce=[(5,6,7,8,9),
                         (.1,.1,.2,.2,.4)]
        
        self.Probabilidad_Conflicto={
                "1": 0.0,
                "2": 0.15,
                "3": 0.30,
                "4": 0.50,
                "5": 0.75
            }
        
        self.Tipo_de_atencion=[("Consulta basica",
                                "Curacion menor",
                                "Procedimieto/sutura",
                                "Urgencia mayor"),
                               (.5,.25,.15,.1)]

        self.TiempoAtencion=[(15,20,25,30),
                             (.25,.35,.25,.15)]#minuto

        self.Medicamentos_usados=[(1,3,4,5),
                                  (.15,.4,.25,.2)]
        
        self.Farmacia=[(("DolorFiebre",50.0),
                        ("Inflamacion",60.0),
                        ("Migraña",80.0),
                        ("Alergia",45.0),
                        ("Diarrea",40.0),
                        ("Nausea",50.0),
                        ("Infeccion",120.0)),
                       (.2,.15,.15,.15,.15,.1,.1)]
        

        self.N_doctores=1
        self.Sueldo_doctor=3000
        self.Horario_doctor=(10.0,15.0)

        self.kit_higienico=20
        self.costo_kit_higienico=50
        self.kit_higienico_stock_min=15

        self.kit_curacion=20
        self.costo_kit_curacion=70
        self.kit_curacion_stock_min=10

        self.kit_sutura=20
        self.costo_kit_sutura=350
        self.kit_sutura_stock_min=10

        self.queja_paciente=.65
        self.Costo_habitacion=5000
        self.costo_reorden=200
        self.tiempo_reabastecer=[(1,2,3),
                                 (.5,.35,.15)]

        #--------- Datos no ingresables -----------------
        self.Cajas_pastillas=[10]*len(self.Farmacia[0])
        self.Cajas_pastillas=[self.Cajas_pastillas,[0] *len(self.Cajas_pastillas)]
        self.CostoKits={"Higienico":0.0,
                        "Curacion":0.0,
                        "Sutura":0.0}
        self.CostoPersonal={}
        self.CostoMedicamento={"DolorFiebre":0.0,
                               "Inflamacion":0.0,
                               "Migraña":0.0,
                               "Alergia":0.0,
                               "Diarrea":0.0,
                               "Nausea":0.0,
                               "Infeccion":0.0}
        
        self.Veces_abasto_medicamento={"DolorFiebre":0,
                               "Inflamacion":0,
                               "Migraña":0,
                               "Alergia":0,
                               "Diarrea":0,
                               "Nausea":0,
                               "Infeccion":0}
        
        self.Veces_medicamento_no_disponible={"DolorFiebre":0,
                               "Inflamacion":0,
                               "Migraña":0,
                               "Alergia":0,
                               "Diarrea":0,
                               "Nausea":0,
                               "Infeccion":0}
        
        self.Veces_kit_no_disponible={"Higienico":0,
                                      "Curacion":0,
                                      "Sutura":0}
        
        self.dias_espera_pedido={"Higienico": 0,
                                 "Curacion": 0,
                                 "Sutura": 0}
        
        self.kits_en_camino={"Higienico": 0,
                               "Curacion": 0,
                               "Sutura": 0}
        
        self.dias_espera_med={
            "DolorFiebre": 0, 
            "Inflamacion": 0, 
            "Migraña": 0, 
            "Alergia": 0, 
            "Diarrea": 0, 
            "Nausea": 0, 
            "Infeccion": 0}
        

        self.med_en_camino={
            "DolorFiebre": 0, 
            "Inflamacion": 0, 
            "Migraña": 0, 
            "Alergia": 0, 
            "Diarrea": 0, 
            "Nausea": 0,
            "Infeccion": 0}
        
        self.Pacientes_Totales_Simulados=0
        self.DescuentoXqueja=.35
        self.CostoQuejas=0
        self.conteo_quejas=0
        self.CostoGeneral=0
        self.tiempo_extra={}
        self.OcasionesNoDisponibles={}
        self.Pacientes_No_Atendidos=0
        self.doc_disponible={}
        self.Oscio_doctor={}
        self.Tiempo_laborado_doc={}
        self.CostoInventarioInicial=0.0
        self.CostoOperativoAcumulado=0.0
        #-------------------------------------------------
    

    def set_val(self, entry, valor):
        entry.delete(0, "end") or entry.insert(0, str(valor))

    def cargar_datos_original(self):
        self.DeclaracionVarialbles()
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)
        self.set_val(self.entradas["Horario del doctor"],self.Horario_doctor)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],self.kit_higienico)
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico)
        self.set_val(self.entradas["Cantidad min kits higienicos"],self.kit_higienico_stock_min)

        self.set_val(self.entradas["Cantidad kits curacion_n"],self.kit_curacion)
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion)
        self.set_val(self.entradas["Cantidad min kits curacion"],self.kit_curacion_stock_min)

        self.set_val(self.entradas["Cantidad kits sutura_n"],self.kit_sutura)
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura)
        self.set_val(self.entradas["Cantidad min kits sutura"],self.kit_sutura_stock_min)

        self.set_val(self.entradas["Probabilidad queja paciente"],self.queja_paciente)

        self.set_val(self.entradas["Costo de reabastecer"],self.costo_reorden)


        self.Insertar_datos_en_txtbox(self.Llegadas_de_pacientes[0], self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox(self.Prob_cruce[0], self.Prob_cruce[1], self.TxtCruceEnAtencion)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], self.Tipo_de_atencion[1], self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox(self.TiempoAtencion[0], self.TiempoAtencion[1], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox(self.Medicamentos_usados[0],self.Medicamentos_usados[1],self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox(self.Farmacia[0],self.Farmacia[1],self.TxtFarmacia)
        self.Insertar_datos_en_txtbox(self.Cajas_pastillas[0],[],self.TxtPastillasIniciales)
        self.Insertar_datos_en_txtbox(self.tiempo_reabastecer[0],self.tiempo_reabastecer[1],self.TxtTiempoReabastecer)

    def cargar_datos_ligeros(self):
        self.DeclaracionVarialbles()
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)
        self.set_val(self.entradas["Horario del doctor"],self.Horario_doctor)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],self.kit_higienico)
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico)
        self.set_val(self.entradas["Cantidad min kits higienicos"],self.kit_higienico_stock_min)

        self.set_val(self.entradas["Cantidad kits curacion_n"],self.kit_curacion)
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion)
        self.set_val(self.entradas["Cantidad min kits curacion"],self.kit_curacion_stock_min)

        self.set_val(self.entradas["Cantidad kits sutura_n"],self.kit_sutura)
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura)
        self.set_val(self.entradas["Cantidad min kits sutura"],self.kit_sutura_stock_min)

        self.set_val(self.entradas["Probabilidad queja paciente"],self.queja_paciente)

        self.set_val(self.entradas["Costo de reabastecer"],self.costo_reorden)


        self.Insertar_datos_en_txtbox((3,4,5,6,7), self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox((3,4,5,6,7), self.Prob_cruce[1], self.TxtCruceEnAtencion)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], (.5,.3,.1,.1), self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox((10,15,20,25), self.TiempoAtencion[1], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox((0,1,2,3),self.Medicamentos_usados[1],self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox((("DolorFiebre",40.0),
                                       ("Inflamacion",50.0),
                                       ("Migraña",50.0),
                                       ("Alergia",30.0),
                                       ("Diarrea",30.0),
                                       ("Nausea",40.0),
                                       ("Infeccion",100.0)),self.Farmacia[1],self.TxtFarmacia)
        self.Insertar_datos_en_txtbox(self.Cajas_pastillas[0],[],self.TxtPastillasIniciales)
        self.Insertar_datos_en_txtbox((0,1,2),self.tiempo_reabastecer[1],self.TxtTiempoReabastecer)
    def cargar_datos_estres(self):
        self.DeclaracionVarialbles()
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)
        self.set_val(self.entradas["Horario del doctor"],self.Horario_doctor)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],self.kit_higienico)
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico)
        self.set_val(self.entradas["Cantidad min kits higienicos"],self.kit_higienico_stock_min)

        self.set_val(self.entradas["Cantidad kits curacion_n"],self.kit_curacion)
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion)
        self.set_val(self.entradas["Cantidad min kits curacion"],self.kit_curacion_stock_min)

        self.set_val(self.entradas["Cantidad kits sutura_n"],self.kit_sutura)
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura)
        self.set_val(self.entradas["Cantidad min kits sutura"],self.kit_sutura_stock_min)

        self.set_val(self.entradas["Probabilidad queja paciente"],self.queja_paciente)

        self.set_val(self.entradas["Costo de reabastecer"],self.costo_reorden)

        self.Insertar_datos_en_txtbox((7,8,9,10,11), self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox((7,8,9,10,11), self.Prob_cruce[1], self.TxtCruceEnAtencion)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], (.4,.25,.2,.15), self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox((25,30,35,40), self.TiempoAtencion[1], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox((4,5,6,7),self.Medicamentos_usados[1],self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox((("DolorFiebre",80.0),
                                       ("Inflamacion",120.0),
                                       ("Migraña",150.0),
                                       ("Alergia",100.0),
                                       ("Diarrea",90.0),
                                       ("Nausea",110.0),
                                       ("Infeccion",250.0)),self.Farmacia[1],self.TxtFarmacia)
        self.Insertar_datos_en_txtbox(self.Cajas_pastillas[0],[],self.TxtPastillasIniciales)
        self.Insertar_datos_en_txtbox((2,3,4),self.tiempo_reabastecer[1],self.TxtTiempoReabastecer)

    def mostrar_pestaña_tablas(self):
        self.Frame_simulacion.place_forget()
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.btn_carga_original=ctk.CTkButton(self.Contenedor_Configuracion, 
                                                text="Carga Original", 
                                                fg_color="#DDB206", 
                                                hover_color="#DDB206", 
                                                command=self.cargar_datos_original)
        self.btn_carga_original.place(relx=0.25, rely=0.1, anchor=ctk.CENTER)

        self.btn_carga_ligera=ctk.CTkButton(self.Contenedor_Configuracion, 
                                              text="Carga Ligera", 
                                              fg_color="#2196F3", 
                                              hover_color="#1976D2", 
                                              command=self.cargar_datos_ligeros)
        self.btn_carga_ligera.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

        self.btn_carga_estres=ctk.CTkButton(self.Contenedor_Configuracion, 
                                              text="Carga Estres",
                                                fg_color="#F44336", 
                                                hover_color="#D32F2F", 
                                                command=self.cargar_datos_estres)
        self.btn_carga_estres.place(relx=0.75, rely=0.1, anchor=ctk.CENTER)

        self.btn_guardar_cambios=ctk.CTkButton(self.Contenedor_Configuracion, 
                                                 text="Guardar datos",
                                                   fg_color="#00AD31", 
                                                   hover_color="#00AD31", 
                                                   command=self.Guardar_datos)
        self.btn_guardar_cambios.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        
        self.btn_nav_tablas.configure(fg_color=self.color_hover)
        self.Mostrar_tablas()
        self.cargar_datos_original()
        


    def mostrar_pestaña_simulacion(self):
        self.Contenedor_Configuracion.place_forget()
        self.Frame_simulacion.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.btn_nav_simulacion.configure(fg_color=self.color_hover)

        ctk.CTkLabel(self.Frame_simulacion,
                     text="Días a simular: ",
                     font=("arial",15),
                     text_color="black"
                     ).place(relx=0.07, rely=0.15, anchor=ctk.CENTER)
        
        self.Dias_a_simular=ctk.CTkEntry(self.Frame_simulacion,
                                         width=150,
                                         font=("arial",15),
                                         justify="center")
        self.Dias_a_simular.place(relx=0.07, rely=0.2, anchor=ctk.CENTER)

        self.btn_iniciar_simulacion= ctk.CTkButton(self.Frame_simulacion, 
                                                text="Simular", 
                                                fg_color="#693700", 
                                                hover_color="#816343", 
                                                command=self.Simulacion)
        self.btn_iniciar_simulacion.place(relx=0.07, rely=0.25, anchor=ctk.CENTER)

        self.Frame_tabla_montecarlo=ctk.CTkScrollableFrame(self.Frame_simulacion)
        self.Frame_tabla_montecarlo.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.8)

        self.lbl_costo_de_iniciar=ctk.CTkLabel(self.Frame_simulacion,
                                               text="Costo de iniciar...",
                                               text_color="black")
        self.lbl_costo_de_iniciar.place(relx=0.07, rely=0.35, anchor=ctk.CENTER)

        self.lbl_costo_de_mantener=ctk.CTkLabel(self.Frame_simulacion,
                                                text="Costo de mantener...",
                                                text_color="black")
        self.lbl_costo_de_mantener.place(relx=0.07, rely=0.45, anchor=ctk.CENTER)

        self.lbl_costo_total=ctk.CTkLabel(self.Frame_simulacion,
                                          text="Costo de total invertido...",
                                          text_color="black")
        self.lbl_costo_total.place(relx=0.07, rely=0.55, anchor=ctk.CENTER)

        self.txt_aleatorios=ctk.CTkTextbox(self.Frame_simulacion, 
                                           font=("Consolas", 13),
                                           width=200)
        self.txt_aleatorios.place(relx=.93, rely=.25, anchor="n", relheight=.65)

        ctk.CTkButton(self.Frame_simulacion,
                      text="Generar aleatorios",
                      fg_color=self.color_fondo,
                      hover_color="#816343",
                      command=lambda:self.Generar_aleatorios()
                      ).place(relx=0.93, rely=0.12, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                        text="Refrescar", 
                        fg_color="#5A3D1D", 
                        hover_color="#816343", 
                        command=lambda:self.leer_numeros_de_archivo()
                        ).place(relx=0.93, rely=.17, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                        text="Tabla de reorden", 
                        fg_color="#693700", 
                        hover_color="#816343", 
                        command=self.Subtabla_reorden
                        ).place(relx=0.07, rely=0.68, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                        text="Tablas de rango", 
                        fg_color="#693700", 
                        hover_color="#816343", 
                        command=self.Mostrar_tablas_rango
                        ).place(relx=0.07, rely=0.78, anchor=ctk.CENTER)

        ctk.CTkButton(self.Frame_simulacion, 
                        text="Resumen", 
                        fg_color="#693700", 
                        hover_color="#816343", 
                        command=self.Mostrar_Resumen_Final
                        ).place(relx=0.07, rely=0.88, anchor=ctk.CENTER)
        
        
        
        
        self.Mostrar_aleatorios()

    def Mostrar_aleatorios(self):
        self.txt_aleatorios.delete("0.0",ctk.END)
        if len(self.Aleatoreos)==0:
            self.txt_aleatorios.insert("0.0","No hay numeros para\niniciar la simulacion")
        else:
            texto_lista="Numeros a utilizar:\n"
            texto_lista+="\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(self.Aleatoreos)])

            self.txt_aleatorios.insert("0.0", texto_lista)
            self.txt_aleatorios.configure(state="disabled")
         


    def Mostrar_tablas(self):
        ancho_fijo=200
        alto_fijo=200


        filas_config=[
        ("Cantidad de doctores", "Sueldo mensual"),
        ("Horario del doctor",None),
        ("Cantidad kits higienicos", "Costo cada uno"),
        ("Cantidad min kits higienicos",None),
        ("Cantidad kits curacion", "Costo cada uno"),
        ("Cantidad min kits curacion",None),
        ("Cantidad kits sutura", "Costo cada uno"),
        ("Cantidad min kits sutura",None),
        ("Probabilidad queja paciente",None),
        ("Costo de reabastecer",None)]

        for i in range(5):
            self.Frame_tablas.grid_columnconfigure(i, weight=1)

        self.entradas={} 
        fil=0
        for i,(campo1,campo2) in enumerate(filas_config):
            if campo1 is None: 
                continue
            elif campo2 is None:
                lbl1=ctk.CTkLabel(self.Frame_tablas, text=f"{campo1}:")
                lbl1.grid(row=i, column=0, padx=(20, 5), pady=5, sticky="n")
                
                ent1=ctk.CTkEntry(self.Frame_tablas, width=80)
                ent1.grid(row=i, column=1, padx=5, pady=5, sticky="n")
                self.entradas[f"{campo1}"]=ent1

            else:
                
                lbl1=ctk.CTkLabel(self.Frame_tablas, text=f"{campo1}:")
                lbl1.grid(row=i, column=0, padx=(20, 5), pady=5, sticky="n")
                
                ent1=ctk.CTkEntry(self.Frame_tablas, width=80)
                ent1.grid(row=i, column=1, padx=5, pady=5, sticky="n")
                
                lbl2=ctk.CTkLabel(self.Frame_tablas, text=f"{campo2}:")
                lbl2.grid(row=i, column=2, padx=(20, 5), pady=5, sticky="n")
                
                ent2=ctk.CTkEntry(self.Frame_tablas, width=80)
                ent2.grid(row=i, column=3, padx=(5, 20), pady=5, sticky="n")

                self.entradas[f"{campo1}_n"]=ent1
                self.entradas[f"{campo1}_val"]=ent2
            fil=i

        fil+=1

        label1=ctk.CTkLabel(self.Frame_tablas, 
                            text="LLegada de pacientes\nal dia", 
                            font=("Arial", 16))
        label1.grid(row=fil, column=0, padx=5, pady=(0, 0), sticky="n")
        self.TxtLLegada= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, 
                                             height=alto_fijo)

        self.TxtLLegada.grid(row=fil+1, column=0, padx=5, pady=(2, 5), sticky="n")


        label2=ctk.CTkLabel(self.Frame_tablas,
                             text="Probabilidad de\ncruce", 
                             font=("Arial", 16))
        label2.grid(row=fil, column=1, padx=5, pady=(0, 0), sticky="n")
        self.TxtCruceEnAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, 
                                             height=alto_fijo)

        self.TxtCruceEnAtencion.grid(row=fil+1, column=1, padx=5, pady=(2, 5), sticky="n")


        label3=ctk.CTkLabel(self.Frame_tablas,
                             text="Tipo de atencion",
                               font=("Arial", 16))
        label3.grid(row=fil, column=2, padx=5, pady=(0, 0), sticky="n")
        self.TxtTipoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                               height=alto_fijo)

        self.TxtTipoAtencion.grid(row=fil+1, column=2, padx=5, pady=(2, 5), sticky="n")
        

        label4=ctk.CTkLabel(self.Frame_tablas,
                             text="Tiempo de atencion",
                               font=("Arial", 16))
        label4.grid(row=fil, column=3, padx=5, pady=(0, 0), sticky="n")
        self.TxtTiempoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                               height=alto_fijo)

        self.TxtTiempoAtencion.grid(row=fil+1, column=3, padx=5, pady=(2, 5), sticky="n")

        
        label5=ctk.CTkLabel(self.Frame_tablas,
                             text="Pastillas\nrecetadas",
                               font=("Arial", 16))
        label5.grid(row=fil+2, column=0, padx=5, pady=(0, 0), sticky="n")
        self.Txtmedicamentos= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                               height=alto_fijo)

        self.Txtmedicamentos.grid(row=fil+3, column=0, padx=5, pady=(2, 5), sticky="n")

        
        label6=ctk.CTkLabel(self.Frame_tablas,
                             text="Cajas de medicamentos\nusadas",
                             font=("Arial", 16))
        label6.grid(row=fil+2, column=1, padx=5, pady=(0, 0), sticky="n")
        self.TxtFarmacia= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                             height=alto_fijo)

        self.TxtFarmacia.grid(row=fil+3, column=1, padx=5, pady=(2, 5), sticky="n")

        label7=ctk.CTkLabel(self.Frame_tablas,
                             text="Cajas de pastillas\niniciales",
                             font=("Arial", 16))
        label7.grid(row=fil+2, column=2, padx=5, pady=(0, 0), sticky="n")
        self.TxtPastillasIniciales= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                             height=alto_fijo)
        self.TxtPastillasIniciales.grid(row=fil+3, column=2, padx=5, pady=(2, 5), sticky="n")

        label8=ctk.CTkLabel(self.Frame_tablas,
                             text="Tiempo de reabastecer",
                             font=("Arial", 16))
        label8.grid(row=fil+2, column=3, padx=5, pady=(0, 0), sticky="n")
        self.TxtTiempoReabastecer= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo,
                                             height=alto_fijo)
        self.TxtTiempoReabastecer.grid(row=fil+3, column=3, padx=5, pady=(2, 5), sticky="n")


    def Guardar_datos(self):
        self.Llegadas_de_pacientes=self.procesar_datos_textbox(self.TxtLLegada,"Llegada de pacientes")
        self.Prob_cruce=self.procesar_datos_textbox(self.TxtCruceEnAtencion,"Probabilidad de cruce en atención")
        self.Tipo_de_atencion=self.procesar_datos_textbox(self.TxtTipoAtencion,"Tipo de atención")
        self.TiempoAtencion=self.procesar_datos_textbox(self.TxtTiempoAtencion,"Tiempo de atención")
        self.Medicamentos_usados=self.procesar_datos_textbox(self.Txtmedicamentos,"Medicamentos usados")
        self.Farmacia=self.procesar_datos_textbox(self.TxtFarmacia,"Farmacia")
        cajas_iniciales=self.procesar_datos_textbox(self.TxtPastillasIniciales,"Pastillas iniciales")
        self.tiempo_reabastecer=self.procesar_datos_textbox(self.TxtTiempoReabastecer,"Tiempo de reorden")
        lista=[self.Llegadas_de_pacientes,
               self.Prob_cruce,
               self.Tipo_de_atencion,
               self.TiempoAtencion,
               self.Medicamentos_usados, 
               self.Farmacia,
               self.tiempo_reabastecer,
               self.Cajas_pastillas[0]]
        if any(item is None for item in lista):
            return
        else:
            try:
                self.stock_min_cajas=list(map(int, cajas_iniciales))
                self.Cajas_pastillas[0]=list(map(int, cajas_iniciales))
                self.procesar_datos_contables()
            except ValueError:
                CTkMessagebox(title="Error", message="Ingrese valores numericos enteros para la cantidad de cajas iniciales", icon="cancel")
                return
        
    def Insertar_datos_en_txtbox(self,eventos,prob,entry):
        entry.delete("0.0", "end") 
        txt=""
        if prob==[]:
            for i in range(len(eventos)):
                t=str(eventos[i])
                if "(" in t:
                    t=t.strip("() '")
                    t=t.replace("'", "")
                    txt+=t+"\n"
                else:
                    txt+=str(eventos[i])+"\n"
            entry.insert(0.0,txt)
        else:
            for i in range(len(eventos)):
                t=str(eventos[i])
                if "(" in t:
                    t=t.strip("() '")
                    t=t.replace("'", "")
                    txt+=t+" , "+str(prob[i])+"\n"
                else:
                    txt+=str(eventos[i])+" , "+str(prob[i])+"\n"
            entry.insert(0.0,txt)
        

    
    def procesar_datos_textbox(self, textbox_widget, nombre_campo):
        contenido=textbox_widget.get("1.0", "end-1c")
        
        lineas=contenido.split("\n")
        
        lista_eventos=[]
        lista_probabilidades=[]
        
        for i, linea in enumerate(lineas):
            linea=linea.strip()
            
            if not linea: 
                continue
                
            if "," in linea:
                try:
                    partes=linea.split(",")
                    if len(partes)==2:
                    
                        evento=partes[0].strip()
                        try:
                            evento=int(evento)
                        except ValueError:
                            evento=evento
                        probabilidad=float(partes[1].strip())
                        
                        lista_eventos.append(evento)
                        lista_probabilidades.append(probabilidad)
                    elif len(partes)==3:
                        evento=partes[0].strip()
                        costo=float(partes[1].strip())
                        probabilidad=float(partes[2].strip())
                        
                        lista_eventos.append((evento,costo))
                        lista_probabilidades.append(probabilidad)
                    
                except ValueError:
                    print(f"Error en línea {i+1}: Formato numérico incorrecto en '{linea}'")
            else:
                evento=linea.strip()
                lista_eventos.append(evento)
        if lista_probabilidades==[]:
            return lista_eventos
        else:
            if self.Comprobar_probabilidades(lista_probabilidades,nombre_campo):

                lista_eventos=tuple(lista_eventos)
                lista_probabilidades=tuple(lista_probabilidades)       
                return [lista_eventos, lista_probabilidades]
            else:
                return None
    

    def procesar_datos_contables(self):
        try:
            self.N_doctores=int(self.entradas["Cantidad de doctores_n"].get())
            self.Sueldo_doctor=float(self.entradas["Cantidad de doctores_val"].get())

            horario=self.entradas["Horario del doctor"].get()
            limpio=horario.replace("(", "").replace(")", "").strip()
            
            valores=[float(x.strip()) for x in limpio.split(",")]
            self.Horario_doctor=(valores[0], valores[1])
        
            self.kit_higienico=int(self.entradas["Cantidad kits higienicos_n"].get())
            self.costo_kit_higienico=float(self.entradas["Cantidad kits higienicos_val"].get())
            self.kit_higienico_stock_min=int(self.entradas["Cantidad min kits higienicos"].get())
        

        
            self.kit_curacion=int(self.entradas["Cantidad kits curacion_n"].get())
            self.costo_kit_curacion=float(self.entradas["Cantidad kits curacion_val"].get())
            self.kit_curacion_stock_min=int(self.entradas["Cantidad min kits curacion"].get())
       

            self.kit_sutura=int(self.entradas["Cantidad kits sutura_n"].get())
            self.costo_kit_sutura=float(self.entradas["Cantidad kits sutura_val"].get())
            self.kit_sutura_stock_min=int(self.entradas["Cantidad min kits sutura"].get())

            self.costo_reorden=float(self.entradas["Costo de reabastecer"].get())

            CTkMessagebox(title="Éxito", message="Datos guardados correctamente", icon="check")
        
        except ValueError:
            CTkMessagebox(title="Error", message="Ingrese valores numéricos válidos para el horario del doctor", icon="cancel")
            return
        except Exception as e:
            CTkMessagebox(title="Error", message=f"Error al procesar datos contables: {str(e)}", icon="cancel")
            return
        
    def Comprobar_probabilidades(self,lista_probabilidades,contenedor):
        suma=0.0
        for p in lista_probabilidades:
            suma+=p
        if round(suma,4)!=1.0:
            CTkMessagebox(title="Error",
                          message=f"Las probabilidades no suman 1.0 en el contenedor {contenedor}. Suman {suma:.4f} ",
                          icon="cancel")
            return False
        return True
    
    def calcular_rangos(self, lista_probabilidades):
        lista_acumulada=[]
        suma=0.0
        for p in lista_probabilidades:
            suma+=p
            lista_acumulada.append(round(suma,4))
        rangos=[]
        limite_inferior=0.0
        for valor in lista_acumulada:
            rangos.append((limite_inferior, valor))
            limite_inferior=valor
        return rangos

    def Simulacion(self):
        try:
            self.Dias_simulacion=int(self.Dias_a_simular.get())
        except ValueError:
            CTkMessagebox(title="Error", message="Ingrese un número válido para los días a simular", icon="cancel")
            return
        
        if self.Aleatoreos==[]:
            CTkMessagebox(title="Error", message="No hay numeros aleatorios para iniciar la simulación", icon="cancel")
            return
        
        for i in range(1,self.N_doctores+1):
            self.tiempo_extra[f"Doctor {i}"]=0.0
            self.OcasionesNoDisponibles[f"Doctor {i}"]=0
            self.doc_disponible[f"Doctor {i}"]=True
            self.CostoPersonal[f"Doctor {i}"]=0
            self.Oscio_doctor[f"Doctor {i}"]=0.0
            self.Tiempo_laborado_doc[f"Doctor {i}"]=self.Horario_doctor[0]

        self.dict_cruce=dict(zip(self.Prob_cruce[0], self.Prob_cruce[1]))
        self.max_p_configurado=max(self.Prob_cruce[0])
        self.CostoGeneral=0
        self.Datos_subtablas={}
        self.Costo_Inicial()
        self.resultados_totales=[]


        rango_de_llegadas=self.calcular_rangos(self.Llegadas_de_pacientes[1])

        rango_tipo_atencion=self.calcular_rangos(self.Tipo_de_atencion[1])

        rango_tiempo_atencion=self.calcular_rangos(self.TiempoAtencion[1])

        rango_medicamentos=self.calcular_rangos(self.Medicamentos_usados[1])

        rango_farmacia=self.calcular_rangos(self.Farmacia[1])
        
        self.rango_espera=self.calcular_rangos(self.tiempo_reabastecer[1])

        
        faltantes=[]
        dia=0

        self.Total_Pacientes_Atendidos=0
        self.Datos_tabla_reorden=[]

        while dia < self.Dias_simulacion:
            dia+=1
            self.dia_actual=dia
            print(f"--- Iniciando Día {dia} ---")
            self.Calculo_Sueldo(dia)
            self.Calcular_faltantes_kits()
            self.Actualizar_Pedidos_Farmacia_Entrantes()
            for i in range(1,self.N_doctores+1):
                self.Tiempo_laborado_doc[f"Doctor {i}"]=self.Horario_doctor[0]
                self.doc_disponible[f"Doctor {i}"]=True

            aleatorio_llegada=self.obtener_siguiente_aleatorio()#aleatorio de llegada de pacientes

            for i,rango in enumerate(rango_de_llegadas):
                if rango[0]<=aleatorio_llegada<=rango[1]:
                    pacientes=int(self.Llegadas_de_pacientes[0][i])

            self.Total_Pacientes_Atendidos+=pacientes
            self.Pacientes_Totales_Simulados += pacientes
            atendido=int(pacientes)
            pastillastotales=0
            self.Datos_subtablas[dia]=[]
            self.kitsUsados=0
            self.aleatorio_cruce=None
            self.hubo_cruce=False
            self.bandqueja, self.aleatorioqueja=False,None

            #------------
            self.col_pedido=""
            self.col_cantidad=""
            self.col_alea=""
            self.col_dias=""
            self.col_costo=""
            #------------
            
            for paciente in range(pacientes):
                self.kitsUsadosSub={"Higienico":0,"Curacion":0,"Sutura":0}
                self.datos_sub=[]
                self.datos_sub.append(paciente+1)#cuenta regresiva de los pacientes atendidos
                atendido-=1
                aleatorio=self.obtener_siguiente_aleatorio()
                self.datos_sub.append(round(aleatorio,5))#aleatorio de tipo de atencion


                for i,rango in enumerate(rango_tipo_atencion):
                    if rango[0]<=aleatorio<=rango[1]:
                        atencion=self.Tipo_de_atencion[0][i]
                        print("El paciente acudio por:  ",atencion," en el dia",dia)
                        self.datos_sub.append(atencion)#tipo de atencion por la cual acudio el paciente
                
                asignado=self.Asignacion_Personal(pacientes,rango_tiempo_atencion)
                
                if asignado:
                    if atencion=="Consulta basica":
                        if self.kit_higienico>=1:
                            self.kit_higienico-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Higienico"]+=1
                            print("Se uso un kit higienico")
                            

                        aleatorio=self.obtener_siguiente_aleatorio()
                        self.datos_sub.append(round(aleatorio,5))#aleatorio de que medicamiento recibio
                        print(aleatorio)

                        for i,rango in enumerate(rango_farmacia):
                            if rango[0]<=aleatorio<=rango[1]:
                                medicamento=self.Farmacia[0][i]
                                self.datos_sub.append(medicamento[0])
                            
                        pastillas,aleatorio=self.Cuantas_pastillas_ocupo(rango_medicamentos)
            
                        self.datos_sub.append(round(aleatorio,5))#aleatorio de cuantas pastillas recibio
                        self.datos_sub.append(pastillas)#pastillas recetadas
                        self.datos_sub.append(f"""Higienico :{self.kitsUsadosSub["Higienico"]}""")
                        print("El paciente requirio de",pastillas," pastillas para ",medicamento,"en el dia ",dia,"\n")
                        pastillas=self.Restar_pastillas(medicamento[0],pastillas)
                        pastillastotales+=pastillas
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)

                        

                    elif atencion=="Curacion menor":
                        if self.kit_higienico>=1:
                            self.kit_higienico-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Higienico"]+=1
                            print("Se uso un kit higienico")
                            
                        else:
                            self.Veces_kit_no_disponible["Higienico"]+=1
                        if self.kit_curacion>=1:
                            self.kit_curacion-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Curacion"]+=1
                            print("Se uso un kit de curacion")
                            
                        else:
                            self.Veces_kit_no_disponible["Curacion"]+=1
                        pastillas,aleatorio=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                       

                        self.datos_sub.append(None)#aleatori de medicamento dado
                        self.datos_sub.append("DolorFiebre")#medicamento resetado

                        self.datos_sub.append(round(aleatorio,5))#aleatorio de cuantas pastillas recibio
                        self.datos_sub.append(pastillas)#pastillas recetadas
                        self.datos_sub.append(f"Higienico :{self.kitsUsadosSub["Higienico"]}\n"\
                        f"Curacion: {self.kitsUsadosSub["Curacion"]}")
                        pastillas=self.Restar_pastillas("DolorFiebre",pastillas)
                        pastillastotales+=pastillas
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)
                        print("Se uso un kit higienico y de curacion")

                    elif atencion=="Procedimieto/sutura":
                        if self.kit_higienico>=1:
                            self.kit_higienico-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Higienico"]+=1
                            print("Se uso un kit higienico")
                            
                        else:
                            self.Veces_kit_no_disponible["Higienico"]+=1
                        if self.kit_curacion>=1:
                            self.kit_curacion-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Curacion"]+=1
                            print("Se uso un kit de curacion")
                            
                        else:
                            self.Veces_kit_no_disponible["Curacion"]+=1
                        if self.kit_sutura>=1:
                            self.kit_sutura-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Sutura"]+=1
                            print("Se uso un kit de sutura")
                            
                        else:
                            self.Veces_kit_no_disponible["Sutura"]+=1
                        
                        pastillas1,aleatorio1=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                        

                        pastillas1=self.Restar_pastillas("DolorFiebre",pastillas1)
                        pastillastotales+=pastillas1
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)

                        pastillas2,aleatorio2=self.Cuantas_pastillas_ocupo(rango_medicamentos)#pendiente

                        pastillas2=self.Restar_pastillas("Inflamacion",pastillas2)
                        pastillastotales+=pastillas2
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)

                        self.datos_sub.append(None)#aleatori de medicamento dado
                        self.datos_sub.append("Dolor\nInflamacion")#medicamento resetado
                        self.datos_sub.append(f"{round(aleatorio1,5)}\n{round(aleatorio2,5)}")#aleatorio de cuantas pastillas recibio
                        self.datos_sub.append(f"{pastillas1}\n{pastillas2}")#pastillas recetadas
                        self.datos_sub.append(f"Higienico :{self.kitsUsadosSub["Higienico"]}\n"\
                        f"Curacion: {self.kitsUsadosSub["Curacion"]}\n"\
                        f"Sutura: {self.kitsUsadosSub["Sutura"]}")
                        print("Se uso un kit higienico, de curacion y sutura")

                    elif atencion=="Urgencia mayor":
                        if self.kit_higienico>=1:
                            self.kit_higienico-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Higienico"]+=1
                            print("Se uso un kit higienico")
                            
                        else:
                            self.Veces_kit_no_disponible["Higienico"]+=1
                        if self.kit_curacion>=2:
                            self.kit_curacion-=2
                            self.kitsUsados+=2
                            self.kitsUsadosSub["Curacion"]+=2
                            print("Se uso DOS kits de curacion")
                            
                        
                        elif self.kit_curacion==1:
                            self.kit_curacion-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Curacion"]+=1
                            print("Se uso un kit de curacion")
                            
                            self.Veces_kit_no_disponible["Curacion"]+=1
                        else:
                            self.Veces_kit_no_disponible["Curacion"]+=2
                        if self.kit_sutura>=2:
                            self.kit_sutura-=2
                            self.kitsUsados+=2
                            self.kitsUsadosSub["Sutura"]+=2
                            print("Se uso DOS kit de sutura")
                            
                        elif self.kit_sutura==1:
                            self.kit_sutura-=1
                            self.kitsUsados+=1
                            self.kitsUsadosSub["Sutura"]+=1
                            print("Se uso un kit de sutura")
                            
                            self.Veces_kit_no_disponible["Sutura"]+=1
                        else:
                            self.Veces_kit_no_disponible["Sutura"]+=2
                        

                        pastillas1,aleatorio1=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                        
                        pastillas1=self.Restar_pastillas("DolorFiebre",pastillas1)
                        pastillastotales+=pastillas1
                        faltantes=self.Calcular_faltantes_pastillas()

                        self.Rabastece(faltantes)

                        pastillas2,aleatorio2=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                        
                        pastillas2=self.Restar_pastillas("Inflamacion",pastillas2)
                        pastillastotales+=pastillas2
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)

                        pastillas3,aleatorio3=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                        
                        pastillas3pastillas3=self.Restar_pastillas("Infeccion",pastillas3)
                        pastillastotales+=pastillas3
                        faltantes=self.Calcular_faltantes_pastillas()
                        self.Rabastece(faltantes)
                        print("Se uso mas de un kit de curacion y sutura")

                        self.datos_sub.append(None)#aleatori de medicamento dado
                        self.datos_sub.append("Dolor\nInflamacion\nInfeccion")#medicamento resetado
                        self.datos_sub.append(f"{round(aleatorio1,5)}\n{round(aleatorio2,5)}\n{round(aleatorio3,5)}")#aleatorio de cuantas pastillas recibio
                        self.datos_sub.append(f"{pastillas1}\n{pastillas2}\n{pastillas3}")#pastillas recetadas}
                        self.datos_sub.append(f"Higienico :{self.kitsUsadosSub["Higienico"]}\n"\
                        f"Curacion: {self.kitsUsadosSub["Curacion"]}\n"\
                        f"Sutura: {self.kitsUsadosSub["Sutura"]}")
                        
                    self.Datos_subtablas[dia].append(self.datos_sub)

                else:
                    self.Pacientes_No_Atendidos+=1
                    self.datos_sub.append(None)#aleatorio de tipo de atencion
                    self.datos_sub.append(None)#tipo de atencion por la cual acudio el paciente
                    self.datos_sub.append(None)#aleatorio de que medicamiento recibio
                    self.datos_sub.append(None)#medicamento resetado
                    self.datos_sub.append(None)#aleatorio de cuantas pastillas recibio
                    self.datos_sub.append(None)#pastillas recetadas
                    self.datos_sub.append(None)#kits usados
                    
                    self.Datos_subtablas[dia].append(self.datos_sub)

            self.TiempoOscioso()

            self.resultados_totales.append([dia,
                                        aleatorio_llegada,
                                        pacientes,
                                        self.aleatorio_cruce,
                                        self.hubo_cruce,
                                        self.aleatorioqueja,
                                        self.bandqueja,
                                        pastillastotales,
                                        self.kitsUsados])
            self.datos_grafica_inventario.append(list(self.Cajas_pastillas[0]))

            if any([self.col_pedido, self.col_cantidad, self.col_alea, self.col_dias, self.col_costo]):
                self.Datos_tabla_reorden.append([dia,self.col_pedido,
                                           self.col_cantidad,
                                           self.col_alea,
                                           self.col_dias,
                                           self.col_costo])

        self.Tabla_montecarlo(self.resultados_totales)
        self.CostoTotal()#Final de la simulación
        self.lbl_costo_de_mantener.configure(text=f"EL costo de mantener\nfue de: {self.CostoOperativoAcumulado}")
        self.lbl_costo_total.configure(text=f"El total de dinero invertido\nfue de: {self.CostoGeneral}")
        
    

    
    def Asignacion_Personal(self, pacientes, rango_tiempo_atencion):
        print("============ area de asignacion de personal ============")
        
        self.hubo_cruce=False
        if pacientes > 1:
            llave=pacientes if pacientes <= self.max_p_configurado else self.max_p_configurado
            prob_limite=self.dict_cruce.get(llave, 0.5)
            
            self.aleatorio_cruce=self.obtener_siguiente_aleatorio()
            if self.aleatorio_cruce <= prob_limite:
                self.hubo_cruce=True
                print(f"CRUCE DETECTADO Probabilidad: {prob_limite} con aleatorio: {self.aleatorio_cruce}")
        else:
            self.aleatorio_cruce=None

        aleatorio=self.obtener_siguiente_aleatorio()  
        tiempo=0
        for i, rango in enumerate(rango_tiempo_atencion):
            if rango[0] <= aleatorio <= rango[1]:
                tiempo=self.TiempoAtencion[0][i]
                print("Tiempo que duró la atención:", tiempo)
                break

        # Si hubo cruce o no hay doctores, el paciente se queja por el servicio saturado
        if self.hubo_cruce or not any(self.doc_disponible.values()):
            print("El paciente se queja por saturación/espera.")
            self.bandqueja, self.aleatorioqueja=self.El_paciente_se_queja()
  
        else:
            self.bandqueja, self.aleatorioqueja=False,None

        asignado=False
        for doc in self.doc_disponible:
            if self.doc_disponible[doc]:
                disponible=self.TiempoLaborado(doc, tiempo)
                asignado=True
                break 
                
        if not asignado:
            for doc in self.doc_disponible:
                self.OcasionesNoDisponibles[doc]+=1
            return asignado
        else:
            return asignado
   
    def TiempoLaborado(self, doctor, tiempo):
        tiempo_decimal=tiempo / 60.0
        
        if self.Tiempo_laborado_doc[doctor] >= self.Horario_doctor[1]:
            self.doc_disponible[doctor]=False
            return False
        
        # Sumar el tiempo
        self.Tiempo_laborado_doc[doctor]+=tiempo_decimal
        print(f"Tiempo laborado hoy por {doctor}: {self.Tiempo_laborado_doc[doctor]:.2f}")
        
        # tiempo extra?
        if self.Tiempo_laborado_doc[doctor] > self.Horario_doctor[1]:
            tiempo_extra=self.Tiempo_laborado_doc[doctor]-self.Horario_doctor[1]
            print(f"El {doctor} trabajó tiempo extra de: {tiempo_extra:.2f}")
            self.tiempo_extra[doctor] += tiempo_extra
            
            self.doc_disponible[doctor]=False 
            
            return True
        return True
                        
    def TiempoOscioso(self):
        duracion_jornada=self.Horario_doctor[1]-self.Horario_doctor[0]
    
        for i in range(1, self.N_doctores + 1):
            nombre_doc=f"Doctor {i}"
            trabajado_real=self.Tiempo_laborado_doc[nombre_doc]-self.Horario_doctor[0]
            ocio_decimal=max(0, duracion_jornada-trabajado_real)
            
            horas=int(ocio_decimal)
            minutos=int((ocio_decimal-horas) *60)
            
            self.Oscio_doctor[nombre_doc]+=ocio_decimal
            
            print(f"{nombre_doc} trabajó {trabajado_real:.2f} hrs.")
            print(f"Ocio hoy: {horas} horas con {minutos} minutos (Equivale a {ocio_decimal:.2f} hrs)")

        

    def Cruce(self,pacientes):
        for i,llegadas in enumerate(self.Prob_cruce[0]):
           if llegadas==pacientes:
               aleatorio=self.obtener_siguiente_aleatorio()
               print(aleatorio,self.Prob_cruce[1][i])
               if aleatorio<=self.Prob_cruce[1][i]:
                   return True,aleatorio
               else:
                   return False,aleatorio
        
    def El_paciente_se_queja(self):
        aleatorio=self.obtener_siguiente_aleatorio()
        if aleatorio<=self.queja_paciente:
            print("El cliente mamon se quejo")
            self.CostoQuejas+=(self.DescuentoXqueja*self.Costo_habitacion)
            self.CostoOperativoAcumulado+=(self.DescuentoXqueja*self.Costo_habitacion)
            print("Costo por quejas: ",self.CostoQuejas)
            self.conteo_quejas+=1
            return True,aleatorio
        else:
            return False,aleatorio

    def Rabastece(self,lista_faltantes):
        
        print("--------- costo de reabastecer MEDICAMENTOS --------------")
        print("faltantes solicitados: ", lista_faltantes)
        
        if len(lista_faltantes) > 0:
            hubo_pedido_med=False # Para aplicar un solo costo fijo de reorden si se piden varios juntos
            
            for nombre_med, cantidad_pedida in lista_faltantes:
                # Si ya hay un pedido en camino de este medicamento, no duplicamos la orden
                if self.dias_espera_med[nombre_med] > 0:
                    print(f"Ya hay un pedido para {nombre_med}")
                    continue
                    
                for i, med_info in enumerate(self.Farmacia[0]):
                    if med_info[0] == nombre_med:
                        precio_caja=med_info[1]
                        
                        costo_compra=(cantidad_pedida * precio_caja)
                        
                        aleatorio=self.obtener_siguiente_aleatorio()
                        for i,rango in enumerate(self.rango_espera):
                            if rango[0]<=aleatorio<=rango[1]:
                                dias_retraso=self.tiempo_reabastecer[0][i]

                        self.col_pedido+=f"{nombre_med}\n"
                        self.col_cantidad+=f"{cantidad_pedida}\n"
                        self.col_alea+=f"{aleatorio}\n"
                        self.col_dias+=f"{dias_retraso}\n"
                        self.col_costo+=f"{costo_compra}\n"

                        self.dias_espera_med[nombre_med]=dias_retraso
                        self.med_en_camino[nombre_med]=cantidad_pedida
                        
                        self.Veces_abasto_medicamento[nombre_med] += 1
                        self.CostoMedicamento[nombre_med] += costo_compra
                        self.CostoOperativoAcumulado += costo_compra
                        hubo_pedido_med=True
                        
                        print(f"ORDEN FARMACIA: Solicitadas {cantidad_pedida} cajas de {nombre_med}. Llegarán en {dias_retraso} días. Costo: ${costo_compra}")
                        break
            
            if hubo_pedido_med:
                self.CostoOperativoAcumulado += self.costo_reorden
                print(f" Se aplicó un cargo de {self.costo_reorden} por costo de reorden.")
                
            print("------------------ termina reabastecer -------------------")
        else:
            print("Stock seguro en Farmacia")
                      
    def Actualizar_Pedidos_Farmacia_Entrantes(self):
        print("--- Actualizando estantes de Farmacia (Entregas de la mañana) ---")
        for nombre_med in self.dias_espera_med.keys():
            if self.dias_espera_med[nombre_med] > 0:
                self.dias_espera_med[nombre_med] -= 1
                print(f"{nombre_med} en camino dias restantes: {self.dias_espera_med[nombre_med]}")
                
                if self.dias_espera_med[nombre_med] == 0 and self.med_en_camino[nombre_med] > 0:
                    for i, med_info in enumerate(self.Farmacia[0]):
                        if med_info[0] == nombre_med:
                            self.Cajas_pastillas[0][i] += self.med_en_camino[nombre_med]
                            print(f"FARMACIA SURTIDA Llegaron {self.med_en_camino[nombre_med]} cajas de {nombre_med}")
                            self.med_en_camino[nombre_med]=0
                            break           
                

    def Restar_pastillas(self,Med,cantidad):
        print("________________ restar medicamento_________________")
        print("Pastillas: ", self.Cajas_pastillas)
        print("medicamento: ", Med, " : ", cantidad)
        
        cantidad=int(cantidad)
        
        for e, med in enumerate(self.Farmacia[0]):
            if med[0] == Med:
                # define el tamaño de la caja según el tipo de medicamento
                tamaño_caja=20 
                if med[0] == "Alergia": tamaño_caja=10 
                if med[0] == "Diarrea": tamaño_caja=12
                cajas_actuales=self.Cajas_pastillas[0][e]
                sueltas_actuales=self.Cajas_pastillas[1][e]
                total_pastillas_disponibles=(cajas_actuales * tamaño_caja) + sueltas_actuales
                
                #revisa di alcanzan las pastillas
                if cantidad > total_pastillas_disponibles:
                    pastillas_faltantes=cantidad-total_pastillas_disponibles
                    
                    if Med in self.Veces_medicamento_no_disponible:
                        self.Veces_medicamento_no_disponible[Med] += pastillas_faltantes
                    
                    print(f"Se necesitan {cantidad} de {Med}, pero solo hay {total_pastillas_disponibles} faltaron: {pastillas_faltantes}")
                    
                    
                    pastillas_entregadas=total_pastillas_disponibles
                    
                    self.Cajas_pastillas[0][e]=0
                    self.Cajas_pastillas[1][e]=0
                    
                    print("Pastillas: ", self.Cajas_pastillas)
                    print("________________ termina restar medicamento_________________")
                    return pastillas_entregadas
                    
                else:
                    # alcanza el medicamento?
                    self.Cajas_pastillas[1][e] += cantidad
                    
                    if self.Cajas_pastillas[1][e] >= tamaño_caja:
                        cajas_a_restar=self.Cajas_pastillas[1][e] // tamaño_caja
                        self.Cajas_pastillas[0][e]=max(0, self.Cajas_pastillas[0][e]-cajas_a_restar)
                        self.Cajas_pastillas[1][e] %= tamaño_caja
                        
                    print(f"Inventario: Se consumió {Med}. Quedan {self.Cajas_pastillas[0][e]} cajas y {self.Cajas_pastillas[1][e]} pastillas sueltas.")
                    
                    print("Pastillas: ", self.Cajas_pastillas)
                    print("________________ termina restar medicamento_________________")
                    return cantidad 
                
                break 
        return 0
    
    def Calcular_faltantes_pastillas(self):
        print("--------------- calculo de faltantes------------------")
        faltantes=[]
        for e, cajas in enumerate(self.Cajas_pastillas[0]):
            stock_min_del_med=self.stock_min_cajas[e]
            print("Stok minnimo del medicamento: ",stock_min_del_med)
            if cajas <= 0:
                print(f" Inventario agotado de {self.Farmacia[0][e][0]}")
                faltantes.append((self.Farmacia[0][e][0], stock_min_del_med)) # Pedimos el stock completo
                return
            elif cajas <= stock_min_del_med//3:
                cantidad_a_pedir=stock_min_del_med-cajas
                faltantes.append((self.Farmacia[0][e][0], cantidad_a_pedir))
        print("Pastillas: ",self.Cajas_pastillas)
        print("Faltantes: ",faltantes)
        print("---------------TERMINA calculo de faltantes------------------")
        return faltantes
    
    def Calcular_faltantes_kits(self):
        print("--------------- calculo de faltantes kits  ------------------")
        
        for tipo in ["Higienico", "Curacion", "Sutura"]:
            if self.dias_espera_pedido[tipo] > 0:
                self.dias_espera_pedido[tipo] -= 1
                print(f"pedido de Kit {tipo} en tránsito. Días restantes para entrega: {self.dias_espera_pedido[tipo]}")
                
                # Si el contador llegó a 0 hoy en la mañana, el camión llegó al hotel
                if self.dias_espera_pedido[tipo] == 0 and self.kits_en_camino[tipo] > 0:
                    if tipo == "Higienico": self.kit_higienico += self.kits_en_camino[tipo]
                    if tipo == "Curacion": self.kit_curacion += self.kits_en_camino[tipo]
                    if tipo == "Sutura": self.kit_sutura += self.kits_en_camino[tipo]
                    
                    print(f" Llegó el pedido de {self.kits_en_camino[tipo]} unidades de Kit {tipo}.")
                    self.kits_en_camino[tipo]=0 #vaciar pedido ya que entró al stock físico

        
        higienico=False
        curacion=False
        sutura=False
        hubo_pedido_global=False 

        
        if (self.kit_higienico + self.kits_en_camino["Higienico"]) < self.kit_higienico_stock_min and self.dias_espera_pedido["Higienico"] == 0:
            if self.kit_higienico == 0:
                faltante=self.kit_higienico_stock_min * 2
            else:
                faltante=self.kit_higienico_stock_min-self.kit_higienico
                
            higienico=True
            hubo_pedido_global=True
            
            aleatorio=self.obtener_siguiente_aleatorio()
            for i,rango in enumerate(self.rango_espera):
                if rango[0]<=aleatorio<=rango[1]:
                    dias_retraso=self.tiempo_reabastecer[0][i]
            self.dias_espera_pedido["Higienico"]=dias_retraso
            self.kits_en_camino["Higienico"]=faltante
            costo=faltante * self.costo_kit_higienico

            self.col_pedido+="Higienico\n"
            self.col_cantidad+=f"{faltante}\n"
            self.col_alea+=f"{aleatorio}\n"
            self.col_dias+=f"{dias_retraso}\n"
            self.col_costo+=f"{costo}\n"
            
            self.CostoKits["Higienico"] += costo
            self.CostoOperativoAcumulado += costo
            print(f"se solicitaron {faltante} unidades de Kit Higiénico. Llegarán en {dias_retraso} días")

        
        if (self.kit_curacion + self.kits_en_camino["Curacion"]) < self.kit_curacion_stock_min and self.dias_espera_pedido["Curacion"] == 0:
            if self.kit_curacion == 0:
                faltante=self.kit_curacion_stock_min * 2
            else:
                faltante=self.kit_curacion_stock_min-self.kit_curacion
                
            curacion=True
            hubo_pedido_global=True
            
            aleatorio=self.obtener_siguiente_aleatorio()
            for i,rango in enumerate(self.rango_espera):
                if rango[0]<=aleatorio<=rango[1]:
                    dias_retraso=self.tiempo_reabastecer[0][i]
            self.dias_espera_pedido["Curacion"]=dias_retraso
            self.kits_en_camino["Curacion"]=faltante
            costo=faltante * self.costo_kit_curacion

            self.col_pedido+="Curacion\n"
            self.col_cantidad+=f"{faltante}\n"
            self.col_alea+=f"{aleatorio}\n"
            self.col_dias+=f"{dias_retraso}\n"
            self.col_costo+=f"{costo}\n"

            self.CostoKits["Curacion"] += costo
            self.CostoOperativoAcumulado += costo
            print(f" Se solicitaron {faltante} unidades de Kit de Curación. Llegarán en {dias_retraso} días.")

        
        if (self.kit_sutura + self.kits_en_camino["Sutura"]) < self.kit_sutura_stock_min and self.dias_espera_pedido["Sutura"] == 0:
            if self.kit_sutura == 0:
                faltante=self.kit_sutura_stock_min * 2
            else:
                faltante=self.kit_sutura_stock_min-self.kit_sutura
                
            sutura=True
            hubo_pedido_global=True
            
            aleatorio=self.obtener_siguiente_aleatorio()
            for i,rango in enumerate(self.rango_espera):
                if rango[0]<=aleatorio<=rango[1]:
                    dias_retraso=self.tiempo_reabastecer[0][i]
            self.dias_espera_pedido["Sutura"]=dias_retraso
            self.kits_en_camino["Sutura"]=faltante
            costo=faltante * self.costo_kit_sutura

            self.col_pedido+="Sutura\n"
            self.col_cantidad+=f"{faltante}\n"
            self.col_alea+=f"{aleatorio}\n"
            self.col_dias+=f"{dias_retraso}\n"
            self.col_costo+=f"{costo}\n"

            self.CostoKits["Sutura"] += costo
            self.CostoOperativoAcumulado += costo
            print(f"se solicitaron {faltante} unidades de Kit de sutura Llegarán en {dias_retraso} días")

       
        if hubo_pedido_global:
            self.CostoOperativoAcumulado += self.costo_reorden
            print(f"Se aplicó un cargo único de +${self.costo_reorden} por costo de reorden de insumos.")

        print("--------------- TERMINA calculo de faltanteskits ------------------")

    def Cuantas_pastillas_ocupo(self,rango_medicamentos):
        aleatorio=self.obtener_siguiente_aleatorio()
        print(aleatorio)
        pastillas=0 
        for i,rango in enumerate(rango_medicamentos):
            if rango[0] <= aleatorio < rango[1]: 
                pastillas=self.Medicamentos_usados[0][i]
                return pastillas, aleatorio
                
        if aleatorio >= 1.0 and rango_medicamentos:
            return rango_medicamentos[-1][2], aleatorio
            
        return pastillas, aleatorio
        
    def Costo_Inicial(self):
        costo_kits=(self.kit_higienico *self.costo_kit_higienico) + \
                     (self.kit_curacion *self.costo_kit_curacion) + \
                     (self.kit_sutura *self.costo_kit_sutura)
        
        costo_meds=0.0
        for i, med_info in enumerate(self.Farmacia[0]):
            medicamento=med_info[0]
            precio_caja=med_info[1]
            cajas_iniciales=self.Cajas_pastillas[0][i]
            costo_meds+=(cajas_iniciales *precio_caja)
            self.Veces_abasto_medicamento[medicamento]+=1
            self.CostoMedicamento[medicamento]+=cajas_iniciales *precio_caja
        self.CostoInventarioInicial=costo_kits + costo_meds
        self.CostoOperativoAcumulado=0.0
        self.CostoQuejas=0.0
        
        print(f"Costo inicial de operación: {self.CostoInventarioInicial}")
        self.lbl_costo_de_iniciar.configure(text=f"Inversión Inicial:\n{self.CostoInventarioInicial}")

    
    def CostoTotal(self):
        
        total_invertido=self.CostoInventarioInicial + self.CostoOperativoAcumulado + self.CostoQuejas
        
        self.CostoGeneral=total_invertido 
        
        print(f"Total dinero invertido al final: {self.CostoGeneral}")
        return self.CostoGeneral
        
    
    def Calculo_Sueldo(self,dia):
        if dia % 30 == 0:
            pago_nomina=(self.N_doctores *self.Sueldo_doctor) 
            self.CostoOperativoAcumulado+=pago_nomina
            print(f"Día {dia}: Se pagó nómina mensual de ${pago_nomina}")

    
    def Subtabla_reorden(self):
        ventana_detalle=ctk.CTkToplevel()
        ventana_detalle.title("Visualizacion de reorden")
        ventana_detalle.geometry("700x500")
        ventana_detalle.after(100, ventana_detalle.lift)
        scroll_frame=ctk.CTkScrollableFrame(ventana_detalle,
                                                 fg_color="transparent",
                                                 border_width=0)
        scroll_frame.pack(expand=True, fill="both")
        if not self.Datos_tabla_reorden:
                ctk.CTkLabel(ventana_detalle, text="No se han realizado pedidos de reabastecimiento.").pack(pady=20)
                return
        else:
            columnas=["Dia",
                    "Pedido ->","Cantidad",
                    "Aleatorio ->", "Dias de entrega",
                    "Costo"]
            
            tabla_sub=CTkTable(
                scroll_frame,
                values=[columnas]+self.Datos_tabla_reorden,
                header_color="#3E2723",
                colors=["#D7CCC8", "#FFFFFF"],
                text_color="black")
            tabla_sub.pack(expand=True, fill="both")
            tabla_sub.edit_row(0, text_color="white")
        

    def Subtabla(self,datos_celda):
        fila=datos_celda["row"]
        valor_clicado=str(datos_celda["value"])
        if valor_clicado not in self.Datos_subtablas:
            try:
                dia_int=int(valor_clicado)
                if dia_int in self.Datos_subtablas:
                    datos_del_dia=self.Datos_subtablas[dia_int]
                else:
                    print(f"Error: El día {valor_clicado} no tiene datos guardados.")
                    return
            except ValueError:
                return
        else:
            datos_del_dia=self.Datos_subtablas[valor_clicado]

        ventana_detalle=ctk.CTkToplevel()
        ventana_detalle.title(f"Sub-eventos del Día {valor_clicado}")
        ventana_detalle.geometry("1000x500")
        ventana_detalle.after(100, ventana_detalle.lift)


        columnas=["Paciente N", "Aleatorio ->", "Tipo de atencion", "Aleatorio ->", 
                    "Medicacion para ", "Aleatorio ->", "Pastillas recetadas","kits usados"]

        tabla_sub=CTkTable(
            ventana_detalle,
            values=[columnas], 
            header_color="#3E2723",
            colors=["#D7CCC8", "#FFFFFF"],
            text_color="black"
        )
        tabla_sub.pack(expand=True, fill="both")
        tabla_sub.edit_row(0, text_color="white")
        for fila_datos in datos_del_dia:
            tabla_sub.add_row(values=fila_datos)


    def Tabla_montecarlo(self,resultados_totales):
        self.Frame_tabla_montecarlo.grid_columnconfigure(0, weight=1)
        if hasattr(self, 'tabla') and self.tabla:
            self.tabla.destroy()

        total_filas=len(resultados_totales)
        total_columnas=len(resultados_totales[0])
        self.tabla=CTkTable(
            master=self.Frame_tabla_montecarlo,
            command=self.Subtabla,
            row=total_filas + 1,
            column=total_columnas,
            header_color="#3E2723",
            text_color="black",
            colors=["#D7CCC8", "#FFFFFF"],
            values=[ ["Dia", 
                      "Aleatorio ->", 
                      "Llegadas\npacientes",
                      "Aleatorio ->",
                      "Hubo \nun cruce?",
                      "Aleatorio ->",
                      "Se quejo\nel paciente?",
                      "Pastillas\nUtilizadas",
                      "kits\nusados"]] + resultados_totales)

        self.tabla.edit_row(0, text_color="white")
        self.tabla.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    

    def Graficar_Inventario(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.datos_grafica_inventario)
        plt.title("Niveles de Inventario por Día")
        plt.xlabel("Día de Simulación")
        plt.ylabel("Cajas Disponibles")
        plt.legend([med[0] for med in self.Farmacia[0]])
        plt.grid(True)
        plt.show()
    
    def Mostrar_tablas_rango(self):
        rango_de_llegadas=self.calcular_rangos(self.Llegadas_de_pacientes[1])

        rango_tipo_atencion=self.calcular_rangos(self.Tipo_de_atencion[1])

        rango_tiempo_atencion=self.calcular_rangos(self.TiempoAtencion[1])

        rango_medicamentos=self.calcular_rangos(self.Medicamentos_usados[1])

        rango_farmacia=self.calcular_rangos(self.Farmacia[1])

        rango_espera=self.calcular_rangos(self.tiempo_reabastecer[1])

        rangos=[("Rango llegadas: ",rango_de_llegadas,self.Llegadas_de_pacientes[0]),
                ("Rango tipo\nde atencion: ",rango_tipo_atencion,self.Tipo_de_atencion[0]),
                ("Rango tiempo de\natencion: ",rango_tiempo_atencion,self.TiempoAtencion[0]),
                ("Rango medicamentos\nusados: ",rango_medicamentos,self.Medicamentos_usados[0]),
                ("Rango farmacia: ",rango_farmacia,self.Farmacia[0]),
                ("Rango Tiempo de\n espera pedido: ",rango_espera,self.tiempo_reabastecer[0])]
        
        ventana_detalle=ctk.CTkToplevel()
        ventana_detalle.title("Rangos de probabilidad")
        ventana_detalle.geometry("700x500")
        ventana_detalle.after(100, ventana_detalle.lift)

        frame=ctk.CTkFrame(master=ventana_detalle,height=100)
        frame.pack(fill="x", pady=5, padx=5)
        for i,rango in enumerate(rangos,start=1):
            titulo=rango[0]
            rangos=rango[1]
            evento=rango[2]
            aux=[]
            for e, (a, b) in enumerate(rangos):
                print(a, b)
                aux.append([f"{str(a)}-{str(b)} : {evento[e]}"])

            tabla=CTkTable(
            frame,
            values=[[titulo]]+aux, 
            header_color="#3E2723",
            colors=["#D7CCC8", "#FFFFFF"],
            text_color="black")
            tabla.edit_row(0, text_color="white")
            tabla.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
            if i%3==0:
                frame=ctk.CTkFrame(master=ventana_detalle,height=100)
                frame.pack(fill="x", pady=5, padx=5)
            
    

    def Mostrar_Resumen_Final(self):
        try:
            
            total_pascientes=self.Total_Pacientes_Atendidos
        
        except Exception as e:
            CTkMessagebox(title="Error", message=e, icon="cancel")
            return

        for widget in self.Frame_tabla_montecarlo.winfo_children():
            widget.destroy()

        # Título Principal
        titulo=ctk.CTkLabel(self.Frame_tabla_montecarlo,
                              text="📊 RESULTADOS", 
                            font=("Arial", 28, "bold"), text_color="white")
        titulo.pack(pady=20)

        container=ctk.CTkFrame(self.Frame_tabla_montecarlo,
                                 fg_color="transparent")
        container.pack(expand=True, fill="both", padx=20, pady=10)

        

        card_finanzas=ctk.CTkFrame(container,
                                     fg_color="#3E2723",
                                     corner_radius=15,
                                     border_width=2,
                                     border_color="#D7CCC8")
        card_finanzas.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_finanzas,
                     text="FINANZAS",
                     font=("Arial", 18, "bold")).pack(pady=10)
        ctk.CTkLabel(card_finanzas,
                     text=f"Inversión Inicial: \n${self.CostoInventarioInicial:,.2f}").pack(anchor="w", padx=20,fill="both")
        ctk.CTkLabel(card_finanzas,
                     text=f"Costo de operacion: \n${self.CostoOperativoAcumulado:,.2f}").pack(anchor="w", padx=20,fill="both")
        ctk.CTkLabel(card_finanzas,
                     text=f"Inversion total: ${self.CostoGeneral:,.2f}", 
                    text_color="#e74c3c", font=("Arial", 16, "bold")).pack(pady=15)

        # desempeño medico
        card_medica=ctk.CTkFrame(container,
                                   fg_color="#3E2723",
                                   corner_radius=15,
                                   border_width=2,
                                   border_color="#D7CCC8")
        card_medica.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_medica,
                     text="PERSONAL",
                     font=("Arial", 18, "bold")).pack(pady=10)
        duracion_jornada=int(self.Horario_doctor[1]-self.Horario_doctor[0])
        horas_totales=duracion_jornada*self.Dias_simulacion
        scroll_doctor=ctk.CTkScrollableFrame(card_medica,
                                                 fg_color="transparent",
                                                 height=100)
        scroll_doctor.pack(fill="both", expand=True, padx=10)
        for i in range(1, min(self.N_doctores + 1, 3)): 
            doc=f"Doctor {i}"
            ocio=self.Oscio_doctor.get(doc, 0)
            fallas=self.OcasionesNoDisponibles.get(doc, 0)
            ctk.CTkLabel(scroll_doctor,
                         text=f"{doc}: {ocio:.1f}h ocio de {horas_totales}h totales",
                         font=("Arial", 12)).pack(anchor="w", padx=20)
            hras_xtra=float(self.tiempo_extra[doc])
            ctk.CTkLabel(scroll_doctor,
                         text=f"El {doc} trabajo {hras_xtra:.1f} horas extra",
                         font=("Arial", 12)).pack(anchor="w", padx=20)
        
        ctk.CTkLabel(card_medica,
                     text=f"Total Pacientes: {total_pascientes}",
                     font=("Arial", 14, "bold")).pack(pady=10)

        #  CALIDAD Y QUEJAS 
        card_quejas=ctk.CTkFrame(container,
                                   fg_color="#3E2723",
                                   corner_radius=15,
                                   border_width=2,
                                   border_color="#D7CCC8")
        card_quejas.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_quejas,
                     text="CALIDAD",
                     font=("Arial", 18, "bold")).pack(pady=10)
        
        scroll_no_disponibles=ctk.CTkScrollableFrame(card_quejas,
                                                 fg_color="transparent",
                                                 height=100)
        scroll_no_disponibles.pack(fill="both", expand=True, padx=10)
        for kit, veces in self.Veces_kit_no_disponible.items():
            if veces>0:
                ctk.CTkLabel(scroll_no_disponibles,
                                text=f"{kit}: {veces} veces no disponible",
                                font=("Arial", 12)).pack(anchor="w")
                
        for med, veces in self.Veces_medicamento_no_disponible.items():
            if veces>0:
                ctk.CTkLabel(scroll_no_disponibles,
                            text=f"{med}: {veces} veces no disponible",
                            font=("Arial", 11)).pack(anchor="w")
        
        ctk.CTkLabel(card_quejas,
                     text=f"Quejas Totales: {self.conteo_quejas}").pack(anchor="w", padx=20)
        ctk.CTkLabel(card_quejas,
                     text=f"Pacientes no atendido por ausencia: {self.Pacientes_No_Atendidos}").pack(anchor="w", padx=20)
        for i in range(1, min(self.N_doctores + 1, 3)): 
            doc=f"Doctor {i}"
            ocio=self.Oscio_doctor.get(doc, 0)
            fallas=self.OcasionesNoDisponibles.get(doc, 0)
            ctk.CTkLabel(card_quejas,
                        text=f"Ausencias por parte del {doc}: {fallas} ",
                        font=("Arial", 12)).pack(anchor="w", padx=20)
        ctk.CTkLabel(card_quejas,
                     text=f"Pérdida por Descuentos:").pack(anchor="w", padx=20)
        ctk.CTkLabel(card_quejas,
                     text=f"${self.CostoQuejas:,.2f}",
                     text_color="#e67e22",
                     font=("Arial", 16, "bold")).pack()

        # Inventario
        card_inv=ctk.CTkFrame(container,
                                fg_color="#3E2723",
                                corner_radius=15,
                                border_width=2,
                                border_color="#D7CCC8")
        card_inv.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_inv,
                     text="INVENTARIO Y MEDICAMENTOS",
                     font=("Arial", 18, "bold")).pack(pady=10)
        
        scroll_farmacia=ctk.CTkScrollableFrame(card_inv,
                                                 fg_color="transparent",
                                                 height=100)
        scroll_farmacia.pack(fill="both", expand=True, padx=10)
        for kit, costo in self.CostoKits.items():
            if costo > 0: 
                ctk.CTkLabel(scroll_farmacia,
                             text=f"Gasto {kit}: ${costo:,.2f}",
                             font=("Arial", 12)).pack(anchor="w")
                
        for med, costo in self.CostoMedicamento.items():
            ctk.CTkLabel(scroll_farmacia,
                         text=f"{med}: ${costo:,.2f} invertidos",
                         font=("Arial", 11)).pack(anchor="w")

        btn_grafica=ctk.CTkButton(card_inv,
                                    text="📊 Ver Gráfica de Stock",
                                    command=self.Graficar_Inventario, 
                                    fg_color="#5D4037", hover_color="#3E2723", width=120)
        btn_grafica.pack(pady=10)
        container.grid_columnconfigure((0, 1), weight=1)
        
        #  rECOMENDACIONES
        card_sugerencias=ctk.CTkFrame(container,
                                        fg_color="#3E2723",
                                        corner_radius=15,
                                        border_width=2,
                                        border_color="#D7CCC8")
        card_sugerencias.grid(row=2, column=0, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_sugerencias,
                     text="SUGERENCIAS",
                     font=("Arial", 18, "bold"),
                     text_color=self.color_texto).pack(pady=10)
        
        # Etiqueta para sugerencia de doctores
        self.lbl_sug_doctores=ctk.CTkLabel(card_sugerencias,
                                             text="Analizando personal...",
                                             font=("Arial", 13),
                                             text_color=self.color_texto,
                                             justify="left")
        self.lbl_sug_doctores.pack(anchor="w", padx=20, pady=5)
        
        ctk.CTkLabel(card_sugerencias,
                     text="Sugerencia de Reabastecimiento (Stock Mínimo):",
                     font=("Arial", 14, "bold"),
                     text_color="#e67e22").pack(anchor="w", padx=20, pady=10)
        
        # Frame scrollable para listar los medicamentos que hicieron falta
        self.scroll_inventario_sug=ctk.CTkScrollableFrame(card_sugerencias,
                                                            fg_color="#2D1A15",
                                                            corner_radius=10,
                                                            height=100)
        self.scroll_inventario_sug.pack(fill="both", expand=True, padx=20, pady=5)
        
        # Probabilidad observada
        card_probabilidad=ctk.CTkFrame(container,
                                         fg_color="#3E2723",
                                         corner_radius=15,
                                         border_width=2,
                                         border_color="#D7CCC8")
        card_probabilidad.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_probabilidad,
                     text="PROBABILIDAD OBSERVADA",
                     font=("Arial", 18, "bold"),
                     text_color=self.color_texto).pack(pady=10)
        
        # etiquetas para las probabilidades calculadas
        self.lbl_prob_colapso=ctk.CTkLabel(card_probabilidad,
                                             text="Calculando tasa de colapso...",
                                             font=("Arial", 14),
                                             text_color=self.color_texto,
                                             justify="left")
        self.lbl_prob_colapso.pack(anchor="w", padx=20, pady=8)
        
        self.lbl_prob_desabasto=ctk.CTkLabel(card_probabilidad,
                                               text="Calculando tasa de desabasto...",
                                               font=("Arial", 14),
                                               text_color=self.color_texto,
                                               justify="left")
        self.lbl_prob_desabasto.pack(anchor="w", padx=20, pady=8)
        
        self.Calcular_Sugerencias_Y_Probabilidades()

        # Veces que un medicamento fue reordenado
        card_veces_reorden=ctk.CTkFrame(container,
                                         fg_color="#3E2723",
                                         corner_radius=15,
                                         border_width=2,
                                         border_color="#D7CCC8")
        card_veces_reorden.grid(row=3, column=0, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(card_veces_reorden,
                     text="Veces que un medicamento fue\nreabastecido",
                     font=("Arial", 18, "bold"),
                     text_color=self.color_texto).pack(pady=10)
        scroll_reabasto=ctk.CTkScrollableFrame(card_veces_reorden,
                                                 fg_color="transparent",
                                                 height=100)
        scroll_reabasto.pack(fill="both", expand=True, padx=10)
        for med,veces in self.Veces_abasto_medicamento.items(): 
            ctk.CTkLabel(scroll_reabasto,
                            text=f"{med}: {veces} pedidos",
                            font=("Arial", 12)).pack(anchor="w")
                
    
    def Calcular_Sugerencias_Y_Probabilidades(self):
       
        total_pacientes=self.Pacientes_Totales_Simulados
        
        #probabilidad de un paciente no encuentre doctor disponible)
        prob_no_atencion=(self.Pacientes_No_Atendidos / total_pacientes) * 100
        
        self.lbl_prob_colapso.configure(
            text=f"Probabilidad de colapso del servicio: {prob_no_atencion:.2f}%\n"
                 f"({self.Pacientes_No_Atendidos} de {total_pacientes} pacientes se quedaron sin consulta)."
        )
        
        # probabilidad global de desabasto en farmacia
        total_pastillas_faltantes=sum(self.Veces_medicamento_no_disponible.values())
        if total_pastillas_faltantes > 0:
            texto_desabasto=f"Hubo desabasto crítico en farmacia.\n  Hicieron falta {total_pastillas_faltantes} unidades recetadas."
        else:
            texto_desabasto="Tasa de desabasto en farmacia: 0.00%\n  El inventario inicial fue suficiente."
            
        self.lbl_prob_desabasto.configure(text=texto_desabasto)

        if prob_no_atencion > 20.0:
            # si supera el 20% calculamos cuantos sugerir segun la gravedad
            doctores_sugeridos=1 if prob_no_atencion <= 40.0 else 2
            texto_sug_doc=(f" La probabilidad de colapso ({prob_no_atencion:.1f}%) supera el límite del 20%.\n"
                             f" Se recomienda contratar de manera inmediata a {doctores_sugeridos} doctor(es)\n"
                             f" adicional(es) para mitigar las penalizaciones por quejas.")
        elif prob_no_atencion > 5.0:
            texto_sug_doc=(f" Servicio con sobrecarga ligera ({prob_no_atencion:.1f}% sin atender).\n"
                             f"Optimizar horarios o evaluar la contratación de 1 doctor de refuerzo")
        else:
            texto_sug_doc=(f"El personal actual de {self.N_doctores} doctor(es) es suficiente.\n"
                             f"   La probabilidad de rechazo es del {prob_no_atencion:.1f}% ")
            
        self.lbl_sug_doctores.configure(text=texto_sug_doc)

        # analisis de eabastecimiento de medicamentos
        for widget in self.scroll_inventario_sug.winfo_children():
            widget.destroy()
            
        hay_faltantes=False
        for med, faltantes in self.Veces_medicamento_no_disponible.items():
            if faltantes > 0:
                hay_faltantes=True
                # normalmente las cajas traen 20 u, para diarrea son 12 y alergia 10
                tam_caja=12 if med == "Diarrea" else (10 if med == "Alergia" else 20)
                cajas_sugeridas=(faltantes // tam_caja) + 1
                
                lbl_med=ctk.CTkLabel(self.scroll_inventario_sug,
                                       text=f"{med}: Faltaron {faltantes} pastillas. Sugerido: +{cajas_sugeridas} cajas.",
                                       font=("Arial", 12),
                                       text_color="#FF8A65",
                                       anchor="w")
                lbl_med.pack(fill="x", padx=5, pady=2)
                
        if not hay_faltantes:
            lbl_ok=ctk.CTkLabel(self.scroll_inventario_sug,
                                  text="No se requiere reabastecimiento de emergencia.",
                                  font=("Arial", 12),
                                  text_color="#81C784",
                                  anchor="w")
            lbl_ok.pack(fill="x", padx=5, pady=2)
        
    
    def Generar_aleatorios(self):
        import sys
        import importlib.util
        from pathlib import Path


        directorio_actual=Path(__file__).resolve().parent
        ruta_generador=directorio_actual / "Generador"
        archivo_main_gen=ruta_generador / "main.py"

       
        if str(ruta_generador) not in sys.path:
            sys.path.insert(0, str(ruta_generador)) 

        try:
            spec=importlib.util.spec_from_file_location("modulo_generador_unico", archivo_main_gen)
            modulo_generador=importlib.util.module_from_spec(spec)
            
            spec.loader.exec_module(modulo_generador)

            generador=modulo_generador.InterfazPrincipal()
            generador.Iniciar(self.Ventana)
            self.Ventana.wait_window(generador.VentanaP)
            if generador.generados and generador.comprobados:
                self.leer_numeros_de_archivo()
            else:
                CTkMessagebox(title="Error", message="No se pueden usar los números: o no se generaron o no pasaron las pruebas.")
                return
 

        except Exception as e:
            print(f"Error al cargar el generador: {e}")
    def leer_numeros_de_archivo(self):
        self.Aleatoreos=[]
        ruta_txt=Path(__file__).resolve().parent / "Generador" / "aleatorios.txt"
        try:
            if ruta_txt.exists():
                with open(ruta_txt, "r") as f:
                    for linea in f:
                        linea=linea.strip()
                        if not linea:
                            continue
                        self.Aleatoreos.append(float(linea))
                self.Mostrar_aleatorios()
                
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return

    def obtener_siguiente_aleatorio(self):
        if len(self.Aleatoreos)==0:
            self.Generar_aleatorios() 

        if self.Aleatoreos:
            return self.Aleatoreos.pop(0)
        else:
            return

obj=Area_Atencion_Medica()
obj.Iniciar()