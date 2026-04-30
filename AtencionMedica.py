
import customtkinter as ctk
class Area_Atencion_Medica():
    def Iniciar(self,Dias_simulacion):
        self.color_fondo = "#5D4037"
        self.color_hover = "#3E2723"
        self.color_texto = "#FFFFFF"
        self.color_Extra = "#D7CCC8"

        

        self.Dias_simulacion = Dias_simulacion
        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulacion de area medica")
        self.Ventana.geometry("1000x700")

        ctk.CTkLabel(self.Ventana,text="AREA MEDICA",font=("arial",20,"bold"),text_color=self.color_texto
                     ).place(relx=.5,rely=.05,anchor=ctk.CENTER)
        
        self.btn_nav_tablas = ctk.CTkButton(self.Ventana, text="Tablas", width=100, command=self.mostrar_pestana_tablas)
        self.btn_nav_tablas.place(relx=.35, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_simulacion = ctk.CTkButton(self.Ventana, text="Simulación", width=100, command=self.mostrar_pestana_simulacion)
        self.btn_nav_simulacion.place(relx=.65, rely=.05, anchor=ctk.CENTER)

  
        self.Main_frame = ctk.CTkFrame(self.Ventana, fg_color=self.color_Extra)
        self.Main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

   
        self.Contenedor_Configuracion = ctk.CTkFrame(self.Main_frame, fg_color="transparent")
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.Frame_tablas= ctk.CTkScrollableFrame(self.Contenedor_Configuracion)
        self.Frame_tablas.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65)


        self.Frame_simulacion = ctk.CTkScrollableFrame(self.Main_frame, fg_color="transparent")
      

        ctk.CTkLabel(self.Contenedor_Configuracion, text="Personal Medico", font=("arial", 15, "bold"), text_color="black"
             ).place(relx=.5, rely=.05, anchor=ctk.CENTER)
        
        
        self.ntry_doctor=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_doctor.place(relx=1/3,rely=.1,anchor=ctk.CENTER)

        self.Doctores=1
        self.ntry_doctor.insert(0,self.Doctores)
        
        self.ntry_enfer=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_enfer.place(relx=2/3,rely=.1,anchor=ctk.CENTER)

        self.Enfermeras=2
        self.ntry_enfer.insert(0,self.Enfermeras)

        ctk.CTkLabel(self.Contenedor_Configuracion,text="Inventario Medico",font=("arial",15,"bold"),text_color="black"
                     ).place(relx=.5,rely=.15,anchor=ctk.CENTER)

        self.ntry_kithigiene=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_kithigiene.place(relx=1/5,rely=.2,anchor=ctk.CENTER)

        self.stock_kit_higiene=15
        self.ntry_kithigiene.insert(0,self.stock_kit_higiene)

        self.ntry_kitcuracion=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_kitcuracion.place(relx=2/5,rely=.2,anchor=ctk.CENTER)

        self.stock_kit_curacion=15
        self.ntry_kitcuracion.insert(0,self.stock_kit_curacion)

        self.ntry_kitsutura=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_kitsutura.place(relx=3/5,rely=.2,anchor=ctk.CENTER)

        self.stock_kit_sutura=15
        self.ntry_kitsutura.insert(0,self.stock_kit_sutura)

        self.ntry_kitfarmaco=ctk.CTkEntry(self.Contenedor_Configuracion)
        self.ntry_kitfarmaco.place(relx=4/5,rely=.2,anchor=ctk.CENTER)

        self.stock_kit_farmaco=15
        self.ntry_kitfarmaco.insert(0,self.stock_kit_farmaco)


        self.btn_carga_original = ctk.CTkButton(self.Contenedor_Configuracion, text="Carga Original", fg_color="#4CAF50", hover_color="#388E3C", command=self.cargar_datos_original)
        self.btn_carga_original.place(relx=0.25, rely=0.26, anchor=ctk.CENTER)

        self.btn_carga_ligera = ctk.CTkButton(self.Contenedor_Configuracion, text="Carga Ligera", fg_color="#2196F3", hover_color="#1976D2", command=self.cargar_datos_ligeros)
        self.btn_carga_ligera.place(relx=0.5, rely=0.26, anchor=ctk.CENTER)

        self.btn_carga_estres = ctk.CTkButton(self.Contenedor_Configuracion, text="Carga Estrés", fg_color="#F44336", hover_color="#D32F2F", command=self.cargar_datos_estres)
        self.btn_carga_estres.place(relx=0.75, rely=0.26, anchor=ctk.CENTER)
        
        self.Ventana.mainloop()

    def cargar_datos_original(self):
        self.ntry_doctor.delete(0, "end"); self.ntry_doctor.insert(0, "2")
        self.ntry_enfer.delete(0, "end"); self.ntry_enfer.insert(0, "3")
        self.ntry_kithigiene.delete(0, "end"); self.ntry_kithigiene.insert(0, "100")
        self.ntry_kitcuracion.delete(0, "end"); self.ntry_kitcuracion.insert(0, "50")
        self.ntry_kitsutura.delete(0, "end"); self.ntry_kitsutura.insert(0, "30")
        self.ntry_kitfarmaco.delete(0, "end"); self.ntry_kitfarmaco.insert(0, "20")

        self.Insertar_datos_en_txtbox([0, 1, 2, 3, 4], [0.25, 0.40, 0.20, 0.10, 0.05], self.TxtLLegada)
        self.Insertar_datos_en_txtbox(["Leve", "Urgencia", "Cita"], [0.70, 0.20, 0.10], self.TxtTipocaso)
        self.Insertar_datos_en_txtbox([10, 15, 20, 30], [0.50, 0.30, 0.15, 0.05], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox(["Basica", "Menor", "Sutura", "Mayor"], [0.60, 0.25, 0.10, 0.05], self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox([5, 12, 20], [0.45, 0.35, 0.20], self.TxtEmergencia)

    def cargar_datos_ligeros(self):
        self.ntry_doctor.delete(0, "end"); self.ntry_doctor.insert(0, "1")
        self.ntry_enfer.delete(0, "end"); self.ntry_enfer.insert(0, "2")
        
        self.Insertar_datos_en_txtbox([0, 1, 2], [0.70, 0.20, 0.10], self.TxtLLegada)
        self.Insertar_datos_en_txtbox(["Leve", "Cita"], [0.90, 0.10], self.TxtTipocaso)
        self.Insertar_datos_en_txtbox([10, 15], [0.80, 0.20], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox(["Basica"], [1.0], self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox([5, 10], [0.90, 0.10], self.TxtEmergencia)

    def cargar_datos_estres(self):
        self.ntry_doctor.delete(0, "end"); self.ntry_doctor.insert(0, "1")
        self.ntry_enfer.delete(0, "end"); self.ntry_enfer.insert(0, "1")
        for ntry in [self.ntry_kithigiene, self.ntry_kitcuracion, self.ntry_kitsutura, self.ntry_kitfarmaco]:
            ntry.delete(0, "end"); ntry.insert(0, "5")

        self.Insertar_datos_en_txtbox([3, 4, 5], [0.30, 0.40, 0.30], self.TxtLLegada)
        self.Insertar_datos_en_txtbox(["Urgencia", "Grave"], [0.40, 0.60], self.TxtTipocaso)
        self.Insertar_datos_en_txtbox([30, 45, 60], [0.20, 0.50, 0.30], self.TxtTiempoAtencion)
        self.Insertar_datos_en_txtbox(["Sutura", "Mayor"], [0.30, 0.70], self.TxtTipoAtencion)
        self.Insertar_datos_en_txtbox([20, 45, 60], [0.10, 0.40, 0.50], self.TxtEmergencia)

    def mostrar_pestana_tablas(self):
        self.Frame_simulacion.place_forget()
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.btn_nav_tablas.configure(fg_color=self.color_hover)
        self.btn_nav_simulacion.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

    def mostrar_pestana_simulacion(self):
        self.Contenedor_Configuracion.place_forget()
        self.Frame_simulacion.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.btn_nav_simulacion.configure(fg_color=self.color_hover)
        self.btn_nav_tablas.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        print("\n")
        print("INICIANDO PROCESAMIENTO DE TABLAS DE PROBABILIDAD")

        tablas = [
            {"nombre": "Llegada de Pacientes", "widget": self.TxtLLegada},
            {"nombre": "Tipo de Caso", "widget": self.TxtTipocaso},
            {"nombre": "Tiempo de Atención", "widget": self.TxtTiempoAtencion},
            {"nombre": "Tipo de Atención", "widget": self.TxtTipoAtencion},
            {"nombre": "Respuesta Emergencia", "widget": self.TxtEmergencia}
        ]

        for tabla in tablas:
            eventos, probabilidades = self.procesar_datos_textbox(tabla["widget"])
            
            if eventos and probabilidades:
                acumulada = self.calcular_acumulada(probabilidades)
                rangos = self.obtener_rangos(acumulada)
                
                print(f"\n TABLA: {tabla['nombre']}")
                print(f"{'Evento':<15} | {'Prob.':<8} | {'Acum.':<8} | {'Rango (Min - Max)':<20}")
                print("-" * 60)
                
                for i in range(len(eventos)):
                    r_min, r_max = rangos[i]
                    print(f"{str(eventos[i]):<15} | {probabilidades[i]:<8} | {acumulada[i]:<8} | {r_min:>5.4f} - {r_max:>5.4f}")

    def Mostrar_tablas(self):
        ancho_fijo = 120
        alto_fijo = 150
        color_texto = "#FFFFff" 

        lista_datos=[1,2,3,4,5,6]
        lista_probabilidad=[.1,.2,.3,.4,.5,.6]

        for i in range(6):
            self.Frame_tablas.grid_columnconfigure(i, weight=1)

        label1 = ctk.CTkLabel(self.Frame_tablas, text="LLegada de pacientes", font=("Arial", 16))
        label1.grid(row=0, column=0, padx=10, pady=(0, 0), sticky="n")

        self.TxtLLegada= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtLLegada.grid(row=1, column=0, padx=10, pady=(2, 5), sticky="n")

        self.Insertar_datos_en_txtbox(lista_datos,lista_probabilidad,self.TxtLLegada)

        self.btnLlegada = ctk.CTkButton(self.Frame_tablas,text="Guardar",command=lambda:self.procesar_datos_textbox(self.TxtLLegada) )
        self.btnLlegada.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="n")



        label2 = ctk.CTkLabel(self.Frame_tablas, text="Tipo de caso", font=("Arial", 16))
        label2.grid(row=0, column=1, padx=10, pady=(0, 0), sticky="n")

        self.TxtTipocaso= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTipocaso.grid(row=1, column=1, padx=10, pady=(2, 5), sticky="n")
        self.Insertar_datos_en_txtbox(lista_datos,lista_probabilidad,self.TxtTipocaso)
        self.btnTipocaso = ctk.CTkButton(self.Frame_tablas,text="Guardar",command=lambda:self.procesar_datos_textbox(self.TxtLLegada) )
        self.btnTipocaso.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="n")



        label3 = ctk.CTkLabel(self.Frame_tablas, text="Tiempo en atender", font=("Arial", 16))
        label3.grid(row=0, column=2, padx=10, pady=(0, 0), sticky="n")

        self.TxtTiempoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTiempoAtencion.grid(row=1, column=2, padx=10, pady=(2, 5), sticky="n")
        self.Insertar_datos_en_txtbox(lista_datos,lista_probabilidad,self.TxtTiempoAtencion)
        self.btnTiempoAtencion = ctk.CTkButton(self.Frame_tablas,text="Guardar",command=lambda:self.procesar_datos_textbox(self.TxtLLegada) )
        self.btnTiempoAtencion.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="n")



        label4 = ctk.CTkLabel(self.Frame_tablas, text="Tipo de atencion", font=("Arial", 16))
        label4.grid(row=0, column=3, padx=10, pady=(0, 0), sticky="n")

        self.TxtTipoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTipoAtencion.grid(row=1, column=3, padx=10, pady=(2, 5), sticky="n")
        self.Insertar_datos_en_txtbox(lista_datos,lista_probabilidad,self.TxtTipoAtencion)
        self.btnTipoAtencion=ctk.CTkButton(self.Frame_tablas,text="Guardar" ,command=lambda:self.procesar_datos_textbox(self.TxtLLegada))
        self.btnTipoAtencion.grid(row=2, column=3, padx=10, pady=(0, 10), sticky="n")



        label5 = ctk.CTkLabel(self.Frame_tablas, text="Tiepo de respuesta en\nemergencia", font=("Arial", 16))
        label5.grid(row=3, column=0, padx=10, pady=(0, 0), sticky="n")

        self.TxtEmergencia= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtEmergencia.grid(row=4, column=0, padx=10, pady=(2, 5), sticky="n")
        self.Insertar_datos_en_txtbox(lista_datos,lista_probabilidad,self.TxtEmergencia)
        self.btnEmergencia= ctk.CTkButton(self.Frame_tablas,text="Guardar",command=lambda:self.procesar_datos_textbox(self.TxtLLegada) )
        self.btnEmergencia.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="n")



    def Insertar_datos_en_txtbox(self,eventos,prob,entry):
            entry.delete("0.0", "end") 
            txt=""
            for i in range(len(eventos)):
                txt+=str(eventos[i])+" , "+str(prob[i])+"\n"
            entry.insert(0.0,txt)
            

    
    def procesar_datos_textbox(self, textbox_widget):
        contenido = textbox_widget.get("1.0", "end-1c")
        
        lineas = contenido.split("\n")
        
        lista_eventos = []
        lista_probabilidades = []
        
        for i, linea in enumerate(lineas):
            linea = linea.strip()
            
            if not linea: 
                continue
                
            if "," in linea:
                try:
                    partes = linea.split(",")
                    
                    evento = partes[0].strip()
                    probabilidad = float(partes[1].strip())
                    
                    lista_eventos.append(evento)
                    lista_probabilidades.append(probabilidad)
                    
                except ValueError:
                    print(f"Error en línea {i+1}: Formato numérico incorrecto en '{linea}'")
            else:
                print(f"Error en línea {i+1}: Falta la coma separadora en '{linea}'")
        print(lista_eventos,lista_probabilidades)        
        return lista_eventos, lista_probabilidades

    def calcular_acumulada(self, lista_probabilidades):
        acumulada = []
        suma = 0
        for p in lista_probabilidades:
            suma += p
            acumulada.append(round(suma, 4))
        return acumulada
    
    def obtener_rangos(self, lista_acumulada):

        rangos = []
        limite_inferior = 0.0
        for valor in lista_acumulada:
            rangos.append((limite_inferior, valor))
            limite_inferior = valor
        return rangos
