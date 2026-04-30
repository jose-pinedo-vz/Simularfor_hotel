
import customtkinter as ctk
class Area_Entretenimiento():
    def Iniciar(self, Dias_simulacion):
        self.color_fondo="#5D4037"
        self.color_hover="#3E2723"
        self.color_texto="#FFFFFF"
        self.color_Extra="#D7CCC8"
        self.Dias_simulacion=Dias_simulacion

        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulación de Entretenimiento")
        self.Ventana.geometry("1100x750")
        self.datos_simulacion={}
        self.textboxes_activos={} 
        self.tablas_maestras={}

        ctk.CTkLabel(self.Ventana, text="AREA DE ENTRETENIMIENTO", 
                     font=("arial", 20, "bold"), text_color=self.color_texto).place(relx=.5, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_tablas=ctk.CTkButton(self.Ventana, text="Tablas", width=100, command=self.mostrar_pestana_tablas)
        self.btn_nav_tablas.place(relx=.3, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_simulacion=ctk.CTkButton(self.Ventana, text="Simulación", width=100, command=self.mostrar_pestana_simulacion)
        self.btn_nav_simulacion.place(relx=.7, rely=.05, anchor=ctk.CENTER)

    
        self.Main_frame=ctk.CTkFrame(self.Ventana, fg_color=self.color_Extra)
        self.Main_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

        self.Contenedor_Configuracion=ctk.CTkFrame(self.Main_frame, fg_color="transparent")
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.Frame_simulacion=ctk.CTkScrollableFrame(self.Main_frame, fg_color="transparent")

  
        self.crear_botones_areas()

  
        self.Frame_tablas_dinamico=ctk.CTkScrollableFrame(self.Contenedor_Configuracion)
        self.Frame_tablas_dinamico.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        self.Ventana.mainloop()
    def crear_botones_areas(self):
        areas=[
            ("Gimnasio", 0.1, self.Mostrar_tablas_gimnacio),
            ("Spa/Jacuzzi", 0.3, self.Mostrar_tablas_spa),
            ("Piscina", 0.5, self.Mostrar_tablas_piscina),
            ("Deportes Acuáticos", 0.7, self.Mostrar_tablas_deportes),
            ("Música/Bar", 0.9, self.Mostrar_tablas_bar)
        ]
        for texto, pos, comando in areas:
            ctk.CTkButton(self.Contenedor_Configuracion, text=texto, command=comando).place(relx=pos, rely=0.1, anchor=ctk.CENTER)


    def mostrar_pestana_tablas(self):
        self.Frame_simulacion.place_forget()
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.btn_nav_tablas.configure(fg_color=self.color_hover)
        self.btn_nav_simulacion.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

    def ejecutar_preparacion_simulacion(self):
        for nombre, widget in self.textboxes_activos.items():
            self.procesar_tabla_para_simulacion(nombre, widget)
        self.mostrar_resumen_simulacion()

    def mostrar_pestana_simulacion(self):
        self.Contenedor_Configuracion.place_forget()
        self.Frame_simulacion.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.btn_nav_simulacion.configure(fg_color=self.color_hover)
        self.btn_nav_tablas.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        for widget in self.Frame_simulacion.winfo_children():
            widget.destroy()
            
        ctk.CTkButton(self.Frame_simulacion, text="Calcular Probabilidad", 
                      command=self.preparar_toda_la_simulacion, width=300, height=50).pack(pady=10)


        
    def preparar_toda_la_simulacion(self):
  
        if not self.tablas_maestras:
            print(" error")
            return

        print("\n" )
        print(f"   REPORTE GLOBAL DE SIMULACIÓN")
        print()

        for titulo, datos in self.tablas_maestras.items():
            print(f"\n TABLA: {titulo}")
            print(f"{"Evento":<20} | {"Prob.":<8} | {"Acum.":<8} | {"Rango":<20}")
            print("-" * 80)
            
            for i in range(len(datos["eventos"])):
                r_min, r_max=datos["rangos"][i]
                print(f"{str(datos["eventos"][i]):<20} | {datos["probabilidades"][i]:<8.4f} | {datos["acumuladas"][i]:<8.4f} | {r_min:>6.4f} - {r_max:>6.4f}")



    def calcular_acumulada(self, lista_probabilidades):
        acumulada=[]
        suma=0
        for p in lista_probabilidades:
            suma += p
            acumulada.append(round(suma, 4))
        return acumulada
    
    def obtener_rangos(self, lista_acumulada):
        rangos=[]
        limite_inferior=0.0
        for valor in lista_acumulada:
            rangos.append((limite_inferior, valor))
            limite_inferior=valor
        return rangos

    def limpiar_frame_tablas(self, frame):
        
        self.textboxes_activos={} 
        
        for widget in frame.winfo_children():
            widget.destroy()

    def Mostrar_tablas_gimnacio(self):
        self.limpiar_frame_tablas(self.Frame_tablas_dinamico)
        
        lbl_inst=ctk.CTkLabel(self.Frame_tablas_dinamico, text="CONFIGURACIÓN DE CAPACIDAD Y PERSONAL", font=("Arial", 16, "bold"))
        lbl_inst.pack(pady=(10, 5))
        
        frame_config=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_config.pack(fill="x", pady=10)

        recursos=[
            ("Coaches Disponibles", "2", 0),
            ("Máquinas Totales", "10", 1),
            ("Aforo Máximo Gim", "15", 2)
        ]
        
        self.variables_gim={} 
        for texto, valor, col in recursos:
            ctk.CTkLabel(frame_config, text=texto, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=30)
            entry=ctk.CTkEntry(frame_config, width=100)
            entry.grid(row=1, column=col, padx=30, pady=5)
            entry.insert(0, valor)
            self.variables_gim[texto]=entry


        ctk.CTkLabel(self.Frame_tablas_dinamico, text="1. CONTROL DE RECEPCIÓN Y ACCESO", font=("Arial", 15, "bold"), text_color="#1E88E5").pack(pady=10)
        
        frame_recepcion=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_recepcion.pack(fill="x", pady=5)
        for i in range(4): frame_recepcion.grid_columnconfigure(i, weight=1)


        self.crear_grid_tabla(frame_recepcion, "Llegada Grupos (1.1)", [0, 1, 2, 3, 4], [0.15, 0.40, 0.25, 0.15, 0.05], 0)
        self.crear_grid_tabla(frame_recepcion, "Destino (Gim=0.2) (1.2)", ["Gim", "Spa", "Pisc", "Dep", "Bar"], [0.20, 0.15, 0.30, 0.25, 0.10], 1)
        self.crear_grid_tabla(frame_recepcion, "Decisión si está lleno (1.3)", ["Espera", "Cambia", "Se va"], [0.20, 0.50, 0.30], 2)
        self.crear_grid_tabla(frame_recepcion, "Tamaño de Grupo (1.4)", [1, 2, 4], [0.40, 0.45, 0.15], 3)


        ctk.CTkLabel(self.Frame_tablas_dinamico, text="2. DINÁMICA INTERNA DEL GIMNASIO", font=("Arial", 15, "bold"), text_color="#2E7D32").pack(pady=10)
        
        frame_interno=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_interno.pack(fill="x", pady=5)
        for i in range(4): frame_interno.grid_columnconfigure(i, weight=1)


        self.crear_grid_tabla(frame_interno, "Requiere Coach (2.1)", ["No", "Sí"], [0.75, 0.25], 0)
        self.crear_grid_tabla(frame_interno, "Tiempo en Máquina (2.2)", [10, 20, 30, 45], [0.30, 0.45, 0.20, 0.05], 1)
        self.crear_grid_tabla(frame_interno, "Tiempo Total (2.3)", [30, 60, 90, 120], [0.20, 0.60, 0.15, 0.05], 2)
        self.crear_grid_tabla(frame_interno, "Uso de Baños (2.4)", ["No", "5 min", "10 min"], [0.40, 0.40, 0.20], 3)

    def crear_grid_tabla(self, master, titulo, datos, probs, col):
        container=ctk.CTkFrame(master, fg_color="gray20" if col % 2 == 0 else "gray25")
        container.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
        
        ctk.CTkLabel(container, text=titulo, font=("Arial", 11, "bold")).pack(pady=5)
        txt=ctk.CTkTextbox(container, width=140, height=120)
        txt.pack(padx=10, pady=5)
        
        self.Insertar_datos_en_txtbox(datos, probs, txt)

        btn_guardar=ctk.CTkButton(container, text="Guardar", width=80, height=20, 
                                     command=lambda t=titulo, w=txt: self.guardar_datos_persistentes(t, w))
        btn_guardar.pack(pady=5)
    
    def guardar_datos_persistentes(self, titulo, widget):
        eventos, probabilidades=self.procesar_datos_textbox(widget)
        
        if eventos and probabilidades:
            acumuladas=self.calcular_acumulada(probabilidades)
            rangos=self.obtener_rangos(acumuladas)
            
            self.tablas_maestras[titulo]={
                "eventos": eventos,
                "probabilidades": probabilidades,
                "acumuladas": acumuladas,
                "rangos": rangos
            }


    def procesar_individual(self, titulo, widget):
        eventos, probs=self.procesar_datos_textbox(widget)
        print(f"Datos de {titulo} guardados temporalmente.")


    def Limpiar_frame(self,frame):
        for widget in frame.winfo_children(): 
            widget.destroy()

    def Insertar_datos_en_txtbox(self,eventos,prob,entry):
            entry.delete("0.0", "end") 
            txt=""
            for i in range(len(eventos)):
                txt+=str(eventos[i])+" , "+str(prob[i])+"\n"
            entry.insert(0.0,txt)
            

    
    def procesar_datos_textbox(self, textbox_widget):
        contenido=textbox_widget.get("1.0", "end-1c")
        lineas=contenido.split("\n")
        
        lista_eventos=[]
        lista_probabilidades=[]
        
        for i, linea in enumerate(lineas):
            linea=linea.strip()
            if not linea or "," not in linea:
                continue
                
            try:
                partes=linea.split(",")
                evento_raw=partes[0].strip()
                prob_raw=partes[1].strip()
                
   
                try:
                    evento=float(evento_raw)
                except ValueError:
                    evento=evento_raw 
                
    
                probabilidad=float(prob_raw)
                
                lista_eventos.append(evento)
                lista_probabilidades.append(probabilidad)
                
            except ValueError:
                print(f"Error en línea {i+1}: Probabilidad inválida en {linea}")
        
        return lista_eventos, lista_probabilidades

    def Mostrar_tablas_spa(self):
        self.limpiar_frame_tablas(self.Frame_tablas_dinamico)
 
        lbl_inst=ctk.CTkLabel(self.Frame_tablas_dinamico, text="CONFIGURACIÓN DE PERSONAL Y RECURSOS DEL SPA", font=("Arial", 16, "bold"))
        lbl_inst.pack(pady=(10, 5))
        
        frame_config=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_config.pack(fill="x", pady=10)

        recursos=[
            ("Masajistas Disponibles", "3", 0),
            ("Cabinas de Masaje", "3", 1),
            ("Jacuzzis Habilitados", "2", 2)
        ]
        
        self.variables_spa={} 
        for texto, valor, col in recursos:
            ctk.CTkLabel(frame_config, text=texto, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=30)
            entry=ctk.CTkEntry(frame_config, width=100)
            entry.grid(row=1, column=col, padx=30, pady=5)
            entry.insert(0, valor)
            self.variables_spa[texto]=entry

       
        ctk.CTkLabel(self.Frame_tablas_dinamico, text="1. CONTROL DE RECEPCIÓN Y ACCESO", font=("Arial", 15, "bold"), text_color="#1E88E5").pack(pady=10)
        
        frame_recepcion=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_recepcion.pack(fill="x", pady=5)
        for i in range(4): frame_recepcion.grid_columnconfigure(i, weight=1)

        self.crear_grid_tabla(frame_recepcion, "Llegada Grupos (1.1)", [0, 1, 2, 3, 4], [0.15, 0.40, 0.25, 0.15, 0.05], 0)
        self.crear_grid_tabla(frame_recepcion, "Destino (Spa=0.15) (1.2)", ["Gim", "Spa", "Pisc", "Dep", "Bar"], [0.20, 0.15, 0.30, 0.25, 0.10], 1)
        self.crear_grid_tabla(frame_recepcion, "Abandono por Aforo (1.3)", ["Espera", "Cambia", "Se va"], [0.20, 0.50, 0.30], 2)
        self.crear_grid_tabla(frame_recepcion, "Tamaño de Grupo (1.4)", [1, 2, 4], [0.40, 0.45, 0.15], 3)

        ctk.CTkLabel(self.Frame_tablas_dinamico, text="2. DINÁMICA INTERNA DEL SPA Y JACUZZI", font=("Arial", 15, "bold"), text_color="#8E24AA").pack(pady=10)
        
        frame_interno=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_interno.pack(fill="x", pady=5)
        for i in range(3): frame_interno.grid_columnconfigure(i, weight=1)

  
        self.crear_grid_tabla(frame_interno, "Tipo de Servicio (3.1)", 
                              ["Normal", "Aromatizado", "Aceites"], [0.50, 0.30, 0.20], 0)


        self.crear_grid_tabla(frame_interno, "Tiempo Masaje (min) (3.2)", 
                              [30, 45, 60], [0.40, 0.35, 0.25], 1)

        
        self.crear_grid_tabla(frame_interno, "Decisión ante Fila (3.3)", 
                              ["Espera Turno", "Cancela/Se va"], [0.45, 0.55], 2)
    
    def Mostrar_tablas_piscina(self):
        self.limpiar_frame_tablas(self.Frame_tablas_dinamico)
        
      
        lbl_inst=ctk.CTkLabel(self.Frame_tablas_dinamico, text="CONFIGURACIÓN DE RECURSOS: ÁREA DE PISCINA", font=("Arial", 16, "bold"))
        lbl_inst.pack(pady=(10, 5))
        
        frame_config=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_config.pack(fill="x", pady=10)


        recursos=[
            ("Salvavidas de Turno", "2", 0),
            ("Sillas/Camillas", "25", 1),
            ("Stock Toallas", "50", 2)
        ]
        
        self.variables_piscina={} 
        for texto, valor, col in recursos:
            ctk.CTkLabel(frame_config, text=texto, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=30)
            entry=ctk.CTkEntry(frame_config, width=100)
            entry.grid(row=1, column=col, padx=30, pady=5)
            entry.insert(0, valor)
            self.variables_piscina[texto]=entry

        ctk.CTkLabel(self.Frame_tablas_dinamico, text="1. CONTROL DE RECEPCIÓN Y ACCESO", font=("Arial", 15, "bold"), text_color="#1E88E5").pack(pady=10)
        
        frame_recepcion=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_recepcion.pack(fill="x", pady=5)
        for i in range(4): frame_recepcion.grid_columnconfigure(i, weight=1)

        self.crear_grid_tabla(frame_recepcion, "Llegada Grupos (1.1)", [0, 1, 2, 3, 4], [0.15, 0.40, 0.25, 0.15, 0.05], 0)
        self.crear_grid_tabla(frame_recepcion, "Destino (Pisc=0.3) (1.2)", ["Gim", "Spa", "Pisc", "Dep", "Bar"], [0.20, 0.15, 0.30, 0.25, 0.10], 1)
        self.crear_grid_tabla(frame_recepcion, "Abandono por Aforo (1.3)", ["Espera", "Cambia", "Se va"], [0.20, 0.50, 0.30], 2)
        self.crear_grid_tabla(frame_recepcion, "Tamaño de Grupo (1.4)", [1, 2, 4], [0.40, 0.45, 0.15], 3)


        ctk.CTkLabel(self.Frame_tablas_dinamico, text="2. DINÁMICA INTERNA DE LA PISCINA", font=("Arial", 15, "bold"), text_color="#0288D1").pack(pady=10)
        
        frame_interno=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_interno.pack(fill="x", pady=5)
        for i in range(4): frame_interno.grid_columnconfigure(i, weight=1)


        self.crear_grid_tabla(frame_interno, "Requiere Toalla (4.1)", 
                              ["No", "1 Toalla", "2 Toallas"], [0.10, 0.70, 0.20], 0)

     
        self.crear_grid_tabla(frame_interno, "Tiempo Estancia (min) (4.2)", 
                              [60, 120, 180, 240], [0.30, 0.40, 0.20, 0.10], 1)

        self.crear_grid_tabla(frame_interno, "Evento Mantenimiento (4.3)", 
                              ["Ninguno", "Limpieza", "Químicos"], [0.85, 0.10, 0.05], 2)
     
        self.crear_grid_tabla(frame_interno, "Pedido Snacks (4.4)", 
                              ["Nada", "Bebida", "Snack", "Ambos"], [0.40, 0.30, 0.20, 0.10], 3)
    
    def Mostrar_tablas_bar(self):
        self.limpiar_frame_tablas(self.Frame_tablas_dinamico)
        
        lbl_inst=ctk.CTkLabel(self.Frame_tablas_dinamico, text="CONFIGURACIÓN DE RECURSOS: MÚSICA & BAR", font=("Arial", 16, "bold"))
        lbl_inst.pack(pady=(10, 5))
        
        frame_config=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_config.pack(fill="x", pady=10)

  
        recursos=[
            ("Bartenders/Meseros", "4", 0),
            ("Mesas Disponibles", "12", 1),
            ("Capacidad Barra", "10", 2)
        ]
        
        self.variables_bar={} 
        for texto, valor, col in recursos:
            ctk.CTkLabel(frame_config, text=texto, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=30)
            entry=ctk.CTkEntry(frame_config, width=100)
            entry.grid(row=1, column=col, padx=30, pady=5)
            entry.insert(0, valor)
            self.variables_bar[texto]=entry

        ctk.CTkLabel(self.Frame_tablas_dinamico, text="1. CONTROL DE RECEPCIÓN Y ACCESO", font=("Arial", 15, "bold"), text_color="#1E88E5").pack(pady=10)
        
        frame_recepcion=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_recepcion.pack(fill="x", pady=5)
        for i in range(4): frame_recepcion.grid_columnconfigure(i, weight=1)

        self.crear_grid_tabla(frame_recepcion, "Llegada Grupos (1.1)", [0, 1, 2, 3, 4], [0.15, 0.40, 0.25, 0.15, 0.05], 0)
        self.crear_grid_tabla(frame_recepcion, "Destino (Bar=0.1) (1.2)", ["Gim", "Spa", "Pisc", "Dep", "Bar"], [0.20, 0.15, 0.30, 0.25, 0.10], 1)
        self.crear_grid_tabla(frame_recepcion, "Abandono por Aforo (1.3)", ["Espera", "Cambia", "Se va"], [0.20, 0.50, 0.30], 2)
        self.crear_grid_tabla(frame_recepcion, "Tamaño de Grupo (1.4)", [1, 2, 4], [0.40, 0.45, 0.15], 3)

        ctk.CTkLabel(self.Frame_tablas_dinamico, text="2. DINÁMICA DE CONSUMO Y AMBIENTE", font=("Arial", 15, "bold"), text_color="#7B1FA2").pack(pady=10)
        
        frame_interno=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_interno.pack(fill="x", pady=5)
        for i in range(4): frame_interno.grid_columnconfigure(i, weight=1)

        self.crear_grid_tabla(frame_interno, "Pedido Principal (6.1)", 
                              ["Solo Bebida", "Bebida+Snack", "Cena Completa"], [0.60, 0.30, 0.10], 0)

        self.crear_grid_tabla(frame_interno, "Tiempo Estancia (min) (6.2)", 
                              [30, 60, 90, 150], [0.35, 0.40, 0.15, 0.10], 1)

        self.crear_grid_tabla(frame_interno, "Ambiente Musical (6.3)", 
                              ["DJ/En Vivo", "Ambiente", "Karaoke"], [0.30, 0.50, 0.20], 2)
        
       
        self.crear_grid_tabla(frame_interno, "Nivel Propina (6.4)", 
                              ["10%", "15%", "20%"], [0.50, 0.35, 0.15], 3)
    
    def Mostrar_tablas_deportes(self):
        self.limpiar_frame_tablas(self.Frame_tablas_dinamico)
        

        lbl_inst=ctk.CTkLabel(self.Frame_tablas_dinamico, text="CONFIGURACIÓN DE EQUIPOS: DEPORTES ACUÁTICOS", font=("Arial", 16, "bold"))
        lbl_inst.pack(pady=(10, 5))
        
        frame_config=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_config.pack(fill="x", pady=10)

        recursos=[
            ("Instructores", "3", 0),
            ("Kayaks (Stock)", "8", 1),
            ("Tablas Paddle", "6", 2)
        ]
        
        self.variables_deportes={} 
        for texto, valor, col in recursos:
            ctk.CTkLabel(frame_config, text=texto, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=30)
            entry=ctk.CTkEntry(frame_config, width=100)
            entry.grid(row=1, column=col, padx=30, pady=5)
            entry.insert(0, valor)
            self.variables_deportes[texto]=entry

     
        ctk.CTkLabel(self.Frame_tablas_dinamico, text="1. CONTROL DE RECEPCIÓN Y ACCESO", font=("Arial", 15, "bold"), text_color="#1E88E5").pack(pady=10)
        
        frame_recepcion=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_recepcion.pack(fill="x", pady=5)
        for i in range(4): frame_recepcion.grid_columnconfigure(i, weight=1)

        self.crear_grid_tabla(frame_recepcion, "Llegada Grupos (1.1)", [0, 1, 2, 3, 4], [0.15, 0.40, 0.25, 0.15, 0.05], 0)
        self.crear_grid_tabla(frame_recepcion, "Destino (Dep=0.25) (1.2)", ["Gim", "Spa", "Pisc", "Dep", "Bar"], [0.20, 0.15, 0.30, 0.25, 0.10], 1)
        self.crear_grid_tabla(frame_recepcion, "Abandono por Aforo (1.3)", ["Espera", "Cambia", "Se va"], [0.20, 0.50, 0.30], 2)
        self.crear_grid_tabla(frame_recepcion, "Tamaño de Grupo (1.4)", [1, 2, 4], [0.40, 0.45, 0.15], 3)

  
        ctk.CTkLabel(self.Frame_tablas_dinamico, text="2. DINÁMICA DE ACTIVIDADES ACUÁTICAS", font=("Arial", 15, "bold"), text_color="#E65100").pack(pady=10)
        
        frame_interno=ctk.CTkFrame(self.Frame_tablas_dinamico, fg_color="transparent")
        frame_interno.pack(fill="x", pady=5)
        for i in range(4): frame_interno.grid_columnconfigure(i, weight=1)

      
        self.crear_grid_tabla(frame_interno, "Actividad (5.1)", 
                              ["Kayak", "Paddle", "Snorkel"], [0.40, 0.35, 0.25], 0)
        
        self.crear_grid_tabla(frame_interno, "Tiempo Uso (min) (5.2)", 
                              [30, 45, 60, 90], [0.25, 0.45, 0.20, 0.10], 1)

    
        self.crear_grid_tabla(frame_interno, "Estado del Mar (5.3)", 
                              ["Calmo", "Picado", "Cerrado"], [0.70, 0.20, 0.10], 2)
    
        self.crear_grid_tabla(frame_interno, "Requiere Guía (5.4)", 
                              ["No (Autónomo)", "Sí (Clase)"], [0.60, 0.40], 3)
    
    def crear_componente_tabla(self, titulo, datos, probs, columna):
        ctk.CTkLabel(self.Frame_tablas_dinamico, text=titulo, font=("Arial", 14, "bold")).grid(row=0, column=columna, pady=5)
        txt_box=ctk.CTkTextbox(self.Frame_tablas_dinamico, width=120, height=150)
        txt_box.grid(row=1, column=columna, padx=10, pady=5)
        self.Insertar_datos_en_txtbox(datos, probs, txt_box)
        ctk.CTkButton(self.Frame_tablas_dinamico, text="Guardar", 
                    command=lambda: self.procesar_datos_textbox(txt_box)).grid(row=2, column=columna, pady=5)
    
    def procesar_tabla_para_simulacion(self, nombre_tabla, textbox_widget):
        eventos, probabilidades=self.procesar_datos_textbox(textbox_widget)
        
        if abs(sum(probabilidades) - 1.0) > 0.001:
            print(f"Advertencia en {nombre_tabla}: La suma es {sum(probabilidades)}")

        acumuladas=self.calcular_acumulada(probabilidades)
        rangos=self.obtener_rangos(acumuladas)
        
        self.datos_simulacion[nombre_tabla]={
            "eventos": eventos,
            "probabilidades": probabilidades,
            "acumuladas": acumuladas,
            "rangos": rangos
        }
        
        print(f"Tabla {nombre_tabla} lista para simular.")
        


        