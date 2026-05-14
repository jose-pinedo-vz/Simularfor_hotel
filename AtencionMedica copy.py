
import customtkinter as ctk
from CTkTable import CTkTable
import random
import threading
import time
import matplotlib.pyplot as plt
from pathlib import Path
from CTkMessagebox import CTkMessagebox


class Area_Atencion_Medica():
    def Iniciar(self,Dias_simulacion):
        self.color_fondo="#5D4037"
        self.color_hover="#3E2723"
        self.color_texto="#FFFFFF"
        self.color_Extra="#D7CCC8"

        

        self.Dias_simulacion=Dias_simulacion
        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulacion de area medica")
        self.Ventana.geometry("1000x700")
        self.Ventana.after(200,lambda:self.Ventana.state('zoomed'))


        ctk.CTkLabel(self.Ventana,text="AREA MEDICA",font=("arial",20,"bold"),text_color=self.color_texto
                     ).place(relx=.5,rely=.05,anchor=ctk.CENTER)
        
        self.btn_nav_tablas=ctk.CTkButton(self.Ventana, text="Tablas", width=100, command=self.mostrar_pestaña_tablas)
        self.btn_nav_tablas.place(relx=.35, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_simulacion=ctk.CTkButton(self.Ventana, text="Simulación", width=100, command=self.mostrar_pestaña_simulacion)
        self.btn_nav_simulacion.place(relx=.65, rely=.05, anchor=ctk.CENTER)

  
        self.Main_frame=ctk.CTkFrame(self.Ventana, fg_color=self.color_Extra)
        self.Main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

   
        self.Contenedor_Configuracion=ctk.CTkFrame(self.Main_frame, fg_color="transparent")
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.Frame_tablas= ctk.CTkScrollableFrame(self.Contenedor_Configuracion)
        self.Frame_tablas.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.7)


        self.Frame_simulacion=ctk.CTkFrame(self.Main_frame, fg_color="transparent")

        self.DeclaracionVarialbles()
        self.Ventana.mainloop()

    def DeclaracionVarialbles(self):
        self.Aleatoreos=[]
        
        self.datos_grafica_inventario=[]
        self.Llegadas_de_pacientes=[(5,6,7,8,9),(.1,.4,.2,.1,.2)]
        self.Prob_cruce=[(5,6,7,8,9),(.1,.1,.2,.2,.4)]
        self.Probabilidad_Conflicto={
                # "Numero de pacientes": "Probabilidad de que se encimen"
                "1": 0.0,
                "2": 0.15,
                "3": 0.30,
                "4": 0.50,
                "5": 0.75
            }
        self.Tipo_de_atencion=[("Consulta basica","Curacion menor","Procedimieto/sutura","Urgencia mayor"),(.5,.25,.15,.1)]
        self.TiempoAtencion=[(15,20,25,30),(.25,.35,.25,.15)]#minuto
        self.Medicamentos_usados=[(1,3,4,5),(.15,.4,.25,.2)]
        self.Farmacia=[(("DolorFiebre",100.0),("Inflamacion",100.0),("Migraña",100.0),("Alergia",100.0),("Diarrea",100.0),("Nausea",100.0),("Infeccion",100.0)),
                       (.2,.15,.15,.15,.15,.1,.1)]
        self.Cajas_pastillas=[10]*len(self.Farmacia[0])
        self.Cajas_pastillas=[self.Cajas_pastillas,[0] * len(self.Cajas_pastillas)]

        

        self.N_doctores=1
        self.Sueldo_doctor=3000
        self.Oscio_doctor={}
        self.Tiempo_laborado_doc={}



        self.Horario_doctor=(10.0,15.0)


        

        self.kit_higienico=20
        self.costo_kit_higienico=50

        self.kit_curacion=20
        self.costo_kit_curacion=70

        self.kit_sutura=20
        self.costo_kit_sutura=350

        self.queja_paciente=.65
        self.Costo_habitacion=5000
        self.costo_reorden=200

        self.CostoKits={"Higienico":0.0,"Curacion":0.0,"Sutura":0.0}
        self.CostoPersonal={}
        self.CostoMedicamento={"DolorFiebre":0.0,"Inflamacion":0.0,"Migraña":0.0,"Alergia":0.0,"Diarrea":0.0,"Nausea":0.0,"Infeccion":0.0}
        self.DescuentoXqueja=.35
        self.CostoQuejas=0
        self.CostoGeneral=0
        self.tiempo_extra={}
        self.OcasionesNoDisponibles={}
        self.doc_disponible={}
    

    def set_val(self, entry, valor):
        entry.delete(0, "end") or entry.insert(0, str(valor))

    def cargar_datos_original(self):
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)

        self.set_val(self.entradas["Cantidad de enfermeros_n"],self.N_enfermeros)
        self.set_val(self.entradas["Cantidad de enfermeros_val"],self.Sueldo_enfermero)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],self.kit_higienico)
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico)

        self.set_val(self.entradas["Cantidad kits curacion_n"],self.kit_curacion)
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion)

        self.set_val(self.entradas["Cantidad kits sutura_n"],self.kit_sutura)
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura)

        self.set_val(self.entradas["Probabilidad queja paciente"],self.queja_paciente)

        self.set_val(self.entradas["Costo de reabastecer"],self.costo_reorden)


        self.Insertar_datos_en_txtbox(self.Llegadas_de_pacientes[0], self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox(self.Medicamentos_usados[0], self.Medicamentos_usados[1], self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], self.Tipo_de_atencion[1], self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox(self.Farmacia[0],self.Farmacia[1],self.TxtFarmacia)
        self.Insertar_datos_en_txtbox(self.Cajas_pastillas,[],self.txtPastillas)

    def cargar_datos_ligeros(self):
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)

        self.set_val(self.entradas["Cantidad de enfermeros_n"],self.N_enfermeros)
        self.set_val(self.entradas["Cantidad de enfermeros_val"],self.Sueldo_enfermero)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],round(self.kit_higienico+(self.kit_higienico*.5)))
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico-(self.costo_kit_higienico*.2))

        self.set_val(self.entradas["Cantidad kits curacion_n"],round(self.kit_higienico+(self.kit_higienico*.5)))
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion-(self.costo_kit_curacion*.2))

        self.set_val(self.entradas["Cantidad kits sutura_n"],round(self.kit_sutura+(self.kit_sutura*.5)))
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura-(self.costo_kit_sutura*.2))

        self.set_val(self.entradas["Probabilidad queja paciente"],.3)
        self.set_val(self.entradas["Costo de reabastecer"],round(self.costo_reorden-(self.costo_reorden*.2)))


        self.Insertar_datos_en_txtbox((0,5,6,7,8), self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox((0,1,2,3), self.Medicamentos_usados[1], self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], (.6,.25,.1,.05), self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox(self.Farmacia[0],self.Farmacia[1],self.TxtFarmacia)

    def cargar_datos_estres(self):
        self.set_val(self.entradas["Cantidad de doctores_n"],self.N_doctores)
        self.set_val(self.entradas["Cantidad de doctores_val"],self.Sueldo_doctor)

        self.set_val(self.entradas["Cantidad de enfermeros_n"],self.N_enfermeros)
        self.set_val(self.entradas["Cantidad de enfermeros_val"],self.Sueldo_enfermero)

        self.set_val(self.entradas["Cantidad kits higienicos_n"],round(self.kit_higienico-(self.kit_higienico*.5)))
        self.set_val(self.entradas["Cantidad kits higienicos_val"],self.costo_kit_higienico+(self.costo_kit_higienico*.2))

        self.set_val(self.entradas["Cantidad kits curacion_n"],round(self.kit_curacion-(self.kit_curacion*.5)))
        self.set_val(self.entradas["Cantidad kits curacion_val"],self.costo_kit_curacion+(self.costo_kit_curacion*.2))

        self.set_val(self.entradas["Cantidad kits sutura_n"],round(self.kit_sutura-(self.kit_sutura*.5)))
        self.set_val(self.entradas["Cantidad kits sutura_val"],self.costo_kit_sutura+(self.costo_kit_sutura*.2))


        self.set_val(self.entradas["Probabilidad queja paciente"],.9)
        self.set_val(self.entradas["Costo de reabastecer"],round(self.costo_reorden+(self.costo_reorden*.2)))


        self.Insertar_datos_en_txtbox((8,9,10,11,12), self.Llegadas_de_pacientes[1], self.TxtLLegada)
        self.Insertar_datos_en_txtbox((4,5,6,7), self.Medicamentos_usados[1], self.Txtmedicamentos)
        self.Insertar_datos_en_txtbox(self.Tipo_de_atencion[0], (.35,.2,.25,.2), self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox(self.Farmacia[0],self.Farmacia[1],self.TxtFarmacia)

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

        self.btn_iniciar_simulacion= ctk.CTkButton(self.Frame_simulacion, 
                                                text="Simular", 
                                                fg_color="#693700", 
                                                hover_color="#816343", 
                                                command=self.Simulacion)
        self.btn_iniciar_simulacion.place(relx=0.07, rely=0.12, anchor=ctk.CENTER)

        self.Frame_tabla_montecarlo=ctk.CTkScrollableFrame(self.Frame_simulacion)
        self.Frame_tabla_montecarlo.place(relx=0.15, rely=0.1, relwidth=0.65, relheight=0.8)

        self.lbl_costo_de_iniciar=ctk.CTkLabel(self.Frame_simulacion,text="Costo de iniciar...",text_color="black")
        self.lbl_costo_de_iniciar.place(relx=0.07, rely=0.3, anchor=ctk.CENTER)

        self.lbl_costo_de_mantener=ctk.CTkLabel(self.Frame_simulacion,text="Costo de mantener...",text_color="black")
        self.lbl_costo_de_mantener.place(relx=0.07, rely=0.4, anchor=ctk.CENTER)

        self.lbl_costo_total=ctk.CTkLabel(self.Frame_simulacion,text="Costo de total invertido...",text_color="black")
        self.lbl_costo_total.place(relx=0.07, rely=0.5, anchor=ctk.CENTER)

        self.txt_aleatorios=ctk.CTkTextbox(self.Frame_simulacion, font=("Consolas", 13))
        self.txt_aleatorios.place(relx=.9, rely=.25, anchor="n", relheight=.65)

        ctk.CTkButton(self.Frame_simulacion,
                      text="Generar aleatorios",
                      fg_color=self.color_fondo,
                      hover_color="#816343",
                      command=lambda:self.Generar_aleatorios()
                      ).place(relx=0.9, rely=0.12, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                        text="Refrescar", 
                        fg_color="#5A3D1D", 
                        hover_color="#816343", 
                        command=lambda:self.leer_numeros_de_archivo()
                        ).place(relx=0.9, rely=.17, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                        text="Grafica", 
                        fg_color="#693700", 
                        hover_color="#816343", 
                        command=self.Graficar_Inventario
                        ).place(relx=0.07, rely=0.7, anchor=ctk.CENTER)

        ctk.CTkButton(self.Frame_simulacion, 
                        text="Resumen", 
                        fg_color="#693700", 
                        hover_color="#816343", 
                        command=self.Mostrar_Resumen_Final
                        ).place(relx=0.07, rely=0.8, anchor=ctk.CENTER)
        
        
        self.Mostrar_aleatorios()

    def Mostrar_aleatorios(self):
        self.txt_aleatorios.delete("0.0",ctk.END)
        if len(self.Aleatoreos)==0:
            self.txt_aleatorios.insert("0.0","No hay numeros para\niniciar la simulacion")
        else:
            texto_lista="Numeros a utilizar:\n"
            texto_lista += "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(self.Aleatoreos)])

            self.txt_aleatorios.insert("0.0", texto_lista)
            self.txt_aleatorios.configure(state="disabled")
         


    def Mostrar_tablas(self):
        ancho_fijo=200
        alto_fijo=200


        filas_config=[
        ("Cantidad de doctores", "Sueldo mensual"),
        ("Cantidad de enfermeros", "Sueldo mensual"),
        (None, None),
        ("Cantidad kits higienicos", "Costo cada una"),
        ("Cantidad kits curacion", "Costo cada una"),
        ("Cantidad kits sutura", "Costo cada una"),
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
        label1=ctk.CTkLabel(self.Frame_tablas, text="LLegada de pacientes\nal dia", font=("Arial", 16))
        label1.grid(row=fil, column=0, padx=5, pady=(0, 0), sticky="n")


        self.TxtLLegada= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtLLegada.grid(row=fil+1, column=0, padx=5, pady=(2, 5), sticky="n")



        label2=ctk.CTkLabel(self.Frame_tablas, text="Tipo de atencion", font=("Arial", 16))
        label2.grid(row=fil, column=2, padx=5, pady=(0, 0), sticky="n")

        self.TxtTipoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTipoAtencion.grid(row=fil+1, column=1, padx=5, pady=(2, 5), sticky="n")
        


        label3=ctk.CTkLabel(self.Frame_tablas, text="Cajas de medicamentos\nusadas", font=("Arial", 16))
        label3.grid(row=fil, column=3, padx=5, pady=(0, 0), sticky="n")

        self.Txtmedicamentos= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.Txtmedicamentos.grid(row=fil+1, column=2, padx=5, pady=(2, 5), sticky="n")

        
        label4=ctk.CTkLabel(self.Frame_tablas, text="Medicamento \nusado", font=("Arial", 16))
        label4.grid(row=fil, column=4, padx=5, pady=(0, 0), sticky="n")

        self.TxtFarmacia= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtFarmacia.grid(row=fil+1, column=3, padx=5, pady=(2, 5), sticky="n")

        label5=ctk.CTkLabel(self.Frame_tablas, text="Cajas de pastillas por \nmedicamento", font=("Arial", 16))
        label5.grid(row=fil, column=4, padx=5, pady=(0, 0), sticky="n")

        self.txtPastillas= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.txtPastillas.grid(row=fil+1, column=4, padx=5, pady=(2, 5), sticky="n")
        

    def Guardar_datos(self):
        self.Llegadas_de_pacientes=self.procesar_datos_textbox(self.TxtLLegada)
        self.Tipo_de_atencion=self.procesar_datos_textbox(self.TxtTipoAtencion)
        self.Medicamentos_usados=self.procesar_datos_textbox(self.Txtmedicamentos)
        self.Farmacia=self.procesar_datos_textbox(self.TxtFarmacia)
        self.Cajas_pastillas=self.procesar_datos_textbox(self.txtPastillas)

        self.procesar_datos_contables()
    

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
            

    
    def procesar_datos_textbox(self, textbox_widget):
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
            lista_eventos=tuple(lista_eventos)
            lista_probabilidades=tuple(lista_probabilidades)       
            return [lista_eventos, lista_probabilidades]


    def procesar_datos_contables(self):

        self.N_doctores=int(self.entradas["Cantidad de doctores_n"].get())
        self.Sueldo_doctor=float(self.entradas["Cantidad de doctores_val"].get())

        self.N_enfermeros=int(self.entradas["Cantidad de enfermeros_n"].get())
        self.Sueldo_enfermero=float(self.entradas["Cantidad de enfermeros_val"].get())

        self.kit_higienico=int(self.entradas["Cantidad kits higienicos_n"].get())
        self.costo_kit_higienico=float(self.entradas["Cantidad kits higienicos_val"].get())

        self.kit_curacion=int(self.entradas["Cantidad kits curacion_n"].get())
        self.costo_kit_curacion=float(self.entradas["Cantidad kits curacion_val"].get())

        self.kit_sutura=int(self.entradas["Cantidad kits sutura_n"].get())
        self.costo_kit_sutura=float(self.entradas["Cantidad kits sutura_val"].get())

        self.costo_reorden=float(self.entradas["Costo de reabastecer"].get())

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
        
        self.Datos_subtablas={}
        self.Costo_Inicial()
        self.resultados_totales=[]
        costoinicial=self.CostoGeneral
    


        rango_de_llegadas=self.calcular_rangos(self.Llegadas_de_pacientes[1])

        rango_tipo_atencion=self.calcular_rangos(self.Tipo_de_atencion[1])

        rango_tiempo_atencion=self.calcular_rangos(self.TiempoAtencion[1])

        rango_medicamentos=self.calcular_rangos(self.Medicamentos_usados[1])

        rango_farmacia=self.calcular_rangos(self.Farmacia[1])

        print("Rango de llegadads de pacientes",rango_de_llegadas)
        print("Rango de tipo de atencion",rango_tipo_atencion)
        print("Rango de medicamentos usados",rango_medicamentos)
        #"DolorFiebre,Inflamacion,Migraña,Alergia,Diarrea,Nausea,Infeccion
        print("Pastillas: ",self.Cajas_pastillas)
        faltantes=[]
        dia=0
        self.Total_Pacientes_Atendidos=0

        while dia < self.Dias_simulacion:
            dia+=1
            print(f"--- Iniciando Día {dia} ---")
            #input("Presiona Enter para el siguiente día...")
            
            self.Calculo_Sueldo(dia)

            for i in range(1,self.N_doctores+1):
                self.Tiempo_laborado_doc[f"Doctor {i}"]=self.Horario_doctor[0]

            aleatorio_llegada=self.obtener_siguiente_aleatorio()#aleatorio de llegada de pacientes

            for i,rango in enumerate(rango_de_llegadas):
                if rango[0]<=aleatorio_llegada<=rango[1]:
                    print("###################### seccion en analisis ####################3##")
                    pacientes=int(self.Llegadas_de_pacientes[0][i])

            atendido=int(pacientes)
            pastillastotales=0
            orden_de_atencion=[]
            self.Datos_subtablas[dia]=[]
            self.kitsUsados=0
            self.kitsUsadosSub={"Higienico":0,"Curacion":0,"Sutura":0}
            #self.kitsUsados={"Higienico":0,"Curacion":0,"Sutura":0}
            print("###################### seccion en analisis ####################3##")
            for paciente in range(pacientes):
                
                self.datos_sub=[]
                self.datos_sub.append(paciente+1)#cuenta regresiva de los pacientes atendidos
                
                atendido-=1
                aleatorio=self.obtener_siguiente_aleatorio()
                self.datos_sub.append(round(aleatorio,5))#aleatorio de tipo de atencion

                print(aleatorio)
                for i,rango in enumerate(rango_tipo_atencion):
                    if rango[0]<=aleatorio<=rango[1]:
                        atencion=self.Tipo_de_atencion[0][i]
                        print("El paciente acudio por:  ",atencion," en el dia",dia)
                        self.datos_sub.append(atencion)#tipo de atencion por la cual acudio el paciente
                
                orden_de_atencion.append(atencion)
                self.Asignacion_Personal(atencion,orden_de_atencion,pacientes,rango_tiempo_atencion)

                if atencion=="Consulta basica":
                    
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
                    pastillastotales+=pastillas

                    self.datos_sub.append(round(aleatorio,5))#aleatorio de cuantas pastillas recibio
                    self.datos_sub.append(pastillas)#pastillas recetadas
                    print("El paciente requirio de",pastillas," pastillas para ",medicamento,"en el dia ",dia,"\n")
                    self.Restar_pastillas(medicamento[0],pastillas)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)

                    

                elif atencion=="Curacion menor":
                    self.kit_curacion-=1
                    self.kit_higienico-=1
                    self.kitsUsadosSub["Higienico"]+=1
                    self.kitsUsadosSub["Curacion"]+=1

                    pastillas,aleatorio=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                    pastillastotales+=pastillas

                    self.datos_sub.append(None)#aleatori de medicamento dado
                    self.datos_sub.append("DolorFiebre")#medicamento resetado

                    self.datos_sub.append(round(aleatorio,5))#aleatorio de cuantas pastillas recibio
                    self.datos_sub.append(pastillas)#pastillas recetadas

                    self.Restar_pastillas("DolorFiebre",pastillas)
                    self.datos_sub.append(medicamento[0])

                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)
                    print("Se uso un kit higienico y de curacion")

                elif atencion=="Procedimieto/sutura":
                    self.kit_curacion-=1
                    self.kit_higienico-=1
                    self.kit_sutura-=1
                    self.kitsUsados+=3
                    self.kitsUsadosSub["Higienico"]+=1
                    self.kitsUsadosSub["Curacion"]+=1
                    self.kitsUsadosSub["Sutura"]+=1

                    pastillas1,aleatorio1=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                    pastillastotales+=pastillas1

                    self.Restar_pastillas("DolorFiebre",pastillas)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)

                    pastillas2,aleatorio2=self.Cuantas_pastillas_ocupo(rango_medicamentos)#pendiente
                    pastillastotales+=pastillas2

                    self.Restar_pastillas("Inflamacion",pastillas)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)

                    self.datos_sub.append(None)#aleatori de medicamento dado
                    self.datos_sub.append("Dolor\nInflamacion")#medicamento resetado
                    self.datos_sub.append(f"{round(aleatorio1,5)}\n{round(aleatorio2,5)}")#aleatorio de cuantas pastillas recibio
                    self.datos_sub.append(f"{pastillas1}\n{pastillas2}")#pastillas recetadas

                    print("Se uso un kit higienico, de curacion y sutura")

                elif atencion=="Urgencia mayor":
                    self.kit_curacion-=2
                    self.kit_higienico-=1
                    self.kit_sutura-=2
                    self.kitsUsados+=5
                    self.kitsUsadosSub["Higienico"]+=1
                    self.kitsUsadosSub["Curacion"]+=2
                    self.kitsUsadosSub["Sutura"]+=2

                    pastillas1,aleatorio1=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                    pastillastotales+=pastillas1
                    self.Restar_pastillas("DolorFiebre",pastillas1)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)

                    pastillas2,aleatorio2=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                    pastillastotales+=pastillas2
                    self.Restar_pastillas("Inflamacion",pastillas2)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)

                    pastillas3,aleatorio3=self.Cuantas_pastillas_ocupo(rango_medicamentos)
                    pastillastotales+=pastillas3
                    self.Restar_pastillas("Infeccion",pastillas3)
                    faltantes=self.Calcular_faltantes()
                    print("faltantes",faltantes)
                    self.Rabastece(faltantes)
                    print("Se uso mas de un kit de curacion y sutura")

                    self.datos_sub.append(None)#aleatori de medicamento dado
                    self.datos_sub.append("Dolor\nInflamacion\nInfeccion")#medicamento resetado
                    self.datos_sub.append(f"{round(aleatorio1,5)}\n{round(aleatorio2,5)}\n{round(aleatorio3,5)}")#aleatorio de cuantas pastillas recibio
                    self.datos_sub.append(f"{pastillas1}\n{pastillas2}\n{pastillas3}")#pastillas recetadas

                self.Datos_subtablas[dia].append(self.datos_sub)
            print("$$$$$$$$$$$$$$$$$#$$$$$$$$$$$$$$$$")
            print(orden_de_atencion)
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
        

        self.Tabla_montecarlo(self.resultados_totales)
        self.CostoTotal()#Final de la simulación
        self.lbl_costo_de_mantener.configure(text=f"EL costo de mantener\nfue de: {self.CostoGeneral-costoinicial}")
        self.lbl_costo_total.configure(text=f"El total de dinero invertido\nfue de: {self.CostoGeneral}")
    
    def Verificar_Conflicto_Estadistico(self, n_pacientes):
        if n_pacientes <= 1:
            return False,0.0

        limite_definido=max([int(k) for k in self.Probabilidad_Conflicto.keys()])
        
        llave_busqueda=str(n_pacientes) if n_pacientes < limite_definido else str(limite_definido)
        
        prob_limite=self.Probabilidad_Conflicto.get(llave_busqueda, 0.95)
        
        aleatorio=self.obtener_siguiente_aleatorio()
        self.hubo_cruce=aleatorio <= prob_limite
        
        return self.hubo_cruce, aleatorio
    
    
    def Asignacion_Personal(self, atencion, orden_de_atencion, pacientes, rango_tiempo_atencion):
        print("============ area de asignacion de personal ============")
        
        self.hubo_cruce=False
        if pacientes > 1:
            llave=pacientes if pacientes <= self.max_p_configurado else self.max_p_configurado
            prob_limite=self.dict_cruce.get(llave, 0.5)
            
            self.aleatorio_cruce=self.obtener_siguiente_aleatorio()
            if self.aleatorio_cruce <= prob_limite:
                self.hubo_cruce=True
                print(f"¡CRUCE DETECTADO! Probabilidad: {prob_limite} con aleatorio: {self.aleatorio_cruce}")
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
                self.OcasionesNoDisponibles[doc] += 1
   
    def TiempoLaborado(self, doctor, tiempo):
        tiempo_decimal=tiempo / 60.0
        
        if self.Tiempo_laborado_doc[doctor] >= self.Horario_doctor[1]:
            self.doc_disponible[doctor]=False
            return False
        
        # Sumar el tiempo
        self.Tiempo_laborado_doc[doctor] += tiempo_decimal
        print(f"Tiempo laborado hoy por {doctor}: {self.Tiempo_laborado_doc[doctor]:.2f}")
        
        # tiempo extra?
        if self.Tiempo_laborado_doc[doctor] > self.Horario_doctor[1]:
            tiempo_extra=self.Tiempo_laborado_doc[doctor] - self.Horario_doctor[1]
            print(f"El {doctor} trabajó tiempo extra de: {tiempo_extra:.2f}")
            self.tiempo_extra[doctor] += tiempo_extra
            self.doc_disponible[doctor]=False 
            return False
        
        return True
                        
    def TiempoOscioso(self):
        duracion_jornada=self.Horario_doctor[1]-self.Horario_doctor[0]
    
        for i in range(1, self.N_doctores + 1):
            nombre_doc=f"Doctor {i}"
            trabajado_real=self.Tiempo_laborado_doc[nombre_doc]-self.Horario_doctor[0]
            ocio_decimal=max(0, duracion_jornada-trabajado_real)
            
            horas=int(ocio_decimal)
            minutos=int((ocio_decimal-horas) * 60)
            
            self.Oscio_doctor[nombre_doc] += ocio_decimal
            
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
            print("Costo por quejas: ",self.CostoQuejas)
            return True,aleatorio
        else:
            return False,aleatorio

    def Rabastece(self,lista_faltantes):
        print("---------costo de reabastecer--------------")
        if len(lista_faltantes)>2:
            for nombre_med, cantidad_pedida in lista_faltantes:
                # Buscamos el precio del medicamento en self.Farmacia
                for i, med_info in enumerate(self.Farmacia[0]):
                    if med_info[0]==nombre_med:
                        precio_caja=med_info[1]
                        
                        costo_compra=(cantidad_pedida * precio_caja) + self.costo_reorden
                 
                        self.Cajas_pastillas[0][i] += cantidad_pedida
                        
                        self.CostoMedicamento[nombre_med] += costo_compra
                        
                        print(f"Compradas {cantidad_pedida} cajas de {nombre_med}. Costo: ${costo_compra:.2f}")
            
            print("------------------------------------------------")
        else:
            print("Stock seguro")
                      
                
                

    def Restar_pastillas(self,Med,cantidad):
        for e, med in enumerate(self.Farmacia[0]):
            if med[0]==Med:
                self.Cajas_pastillas[1][e] += int(cantidad)
                tamaño_caja=20 
                if med[0]=="Alergia": tamaño_caja=10 
                if med[0]=="Diarrea": tamaño_caja=12 
                if self.Cajas_pastillas[1][e] >= tamaño_caja:
                    # cuantas cajas completas se formaron
                    cajas_a_restar=self.Cajas_pastillas[1][e] // tamaño_caja
                    self.Cajas_pastillas[0][e] -= cajas_a_restar
                    self.Cajas_pastillas[1][e] %= tamaño_caja
                    
                    print(f"Inventario: Se consumió caja de {Med}. Quedan {self.Cajas_pastillas[0][e]} cajas.")
                break

    def Calcular_faltantes(self):
        faltantes=[]
        for e, cajas in enumerate(self.Cajas_pastillas[0]):

            if cajas <= 0:
                print(f" Inventario agotado de {self.Farmacia[0][e][0]}")
                faltantes.append((self.Farmacia[0][e][0], 10)) # Pedimos el stock completo
            
    
            elif cajas <= 3:
                cantidad_a_pedir=10-cajas
                faltantes.append((self.Farmacia[0][e][0], cantidad_a_pedir))
                
        return faltantes

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
        self.CostoKits["Higienico"]=float(self.kit_higienico*self.costo_kit_higienico)
        self.CostoKits["Curacion"]=float(self.kit_curacion*self.costo_kit_curacion)
        self.CostoKits["Sutura"]=float(self.kit_sutura*self.costo_kit_sutura)
        
        for prod,costo in self.CostoMedicamento.items():
            i=0
            for prod2,costo2 in self.Farmacia[0]:
                if prod==prod2:
                    self.CostoMedicamento[prod]=float(costo2*self.Cajas_pastillas[0][i])
                else:
                    i+=1
        self.CostoTotal()
        print("costo inicial de operacion: ",self.CostoGeneral)
        self.lbl_costo_de_iniciar.configure(text=f"costo inicial de operacion:\n{self.CostoGeneral}")

    
    def CostoTotal(self):
        try:
            for e,costo in self.CostoKits.items():
                self.CostoGeneral+=float(costo)
            for e,costo in self.CostoPersonal.items():
                self.CostoGeneral+=float(costo)
            for e,costo in self.CostoMedicamento.items():
                self.CostoGeneral+=float(costo)
            

        except:
            print("error inesperado")
        
    
    def Calculo_Sueldo(self,dia):
        if dia%30==0:
            
            self.CostoPersonal["Doctor"]+=float(self.Sueldo_doctor)
            self.CostoPersonal["Enfermero"]+=float(self.Sueldo_enfermero)

            print("costo del sueldo del personal: ",self.CostoPersonal)

    
    
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


    def Tabla_montecarlo(self,resultados_totales):#A quien le corresponda, esta funcion define la tabla para mostra las iteraciones de los dias de la simulacion
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
                      "Hubo un cruce?",
                      "Aleatorio ->",
                      "Se quejo\nel paciente?",
                      "Pastillas\nUtilizadas",
                      "kits\nusados"]] + resultados_totales)

        self.tabla.edit_row(0, text_color="white")
        self.tabla.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    

    def Graficar_Inventario(self):
        plt.figure(figsize=(10, 5))
        # 'self.datos_grafica_inventario' es una lista donde cada elemento es el stock de ese día.
        plt.plot(self.datos_grafica_inventario)
        plt.title("Niveles de Inventario por Día")
        plt.xlabel("Día de Simulación")
        plt.ylabel("Cajas Disponibles")
        plt.legend(["Alergia", "Diarrea", "Fiebre", "Dolor"]) 
        plt.grid(True)
        plt.show()
    
  
    def Mostrar_Resumen_Final(self):
        for widget in self.Frame_tabla_montecarlo.winfo_children():
            widget.destroy()


        titulo=ctk.CTkLabel(self.Frame_tabla_montecarlo, text="ESTADÍSTICAS TOTALES", 
                            font=("Arial", 24, "bold"), text_color="white")
        titulo.place(relx=0.5, y=50, anchor="center")

     
        ganancia_total=self.Total_Pacientes_Atendidos * 200 
        balance_neto=ganancia_total-self.CostoGeneral

   
        info_texto=(
            f"Días Simulados: {self.Dias_simulacion}\n\n"
            f"Total Pacientes: {self.Total_Pacientes_Atendidos}\n"
            f"Gasto Total: ${self.CostoGeneral:,.2f}\n"
            f"Ingresos: ${ganancia_total:,.2f}\n"
            f"---------------------------\n"
            f"Balance Neto: ${balance_neto:,.2f}"
        )

  
        resumen=ctk.CTkLabel(self.Frame_tabla_montecarlo, text=info_texto, 
                            font=("Consolas", 16), justify="left",
                            fg_color="#3E2723", padx=20, pady=20, corner_radius=10)
        resumen.place(relx=0.5, rely=0.45, anchor="center")

        
        btn_grafica=ctk.CTkButton(self.Frame_tabla_montecarlo, text="Ver Gráfica de Inventario",
                                    command=self.Graficar_Inventario, fg_color="#5D4037",
                                    width=200, height=40)
        btn_grafica.place(relx=0.5, rely=0.8, anchor="center")
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
            if hasattr(self, 'Dias_simulacion'):
                generador.Iniciar(self.Dias_simulacion,self.Ventana)
                self.Ventana.wait_window(generador.VentanaP)
                print("algo")
                if generador.generados and generador.comprobados:
                    print("simon")
                    self.leer_numeros_de_archivo()
                else:
                    CTkMessagebox(title="Error", message="No se pueden usar los números: o no se generaron o no pasaron las pruebas.")
            else:
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
obj.Iniciar(20)