import customtkinter as ctk
from CTkTable import CTkTable
import threading
import matplotlib.pyplot as plt
from pathlib import Path
from CTkMessagebox import CTkMessagebox
import datetime


class Area_Entretenimiento():
    def Iniciar(self):
        self.color_fondo="#5D4037"
        self.color_hover="#3E2723"
        self.color_texto="#FFFFFF"
        self.color_Extra="#D7CCC8"

        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulación de Entretenimiento")
        self.Ventana.geometry("1000x700")
        self.Ventana.after(200, lambda: self.Ventana.state('zoomed'))

        ctk.CTkLabel(self.Ventana, text="AREA DE ENTRETENIMIENTO",
                     font=("arial", 20, "bold"),
                     text_color=self.color_texto).place(relx=.5, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_tablas=ctk.CTkButton(self.Ventana, text="Tablas", width=100,
                                            command=self.Mostrar_pestaña_tablas)
        self.btn_nav_tablas.place(relx=.3, rely=.05, anchor=ctk.CENTER)

        self.btn_nav_simulacion=ctk.CTkButton(self.Ventana, text="Simulación", width=100,
                                                command=self.mostrar_pestaña_simulacion)
        self.btn_nav_simulacion.place(relx=.7, rely=.05, anchor=ctk.CENTER)

        self.Main_frame=ctk.CTkFrame(self.Ventana, fg_color=self.color_Extra)
        self.Main_frame.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)

        self.Contenedor_Configuracion=ctk.CTkFrame(self.Main_frame, fg_color="transparent")
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.Frame_simulacion=ctk.CTkFrame(self.Main_frame, fg_color="transparent")

        self.DeclaracionVarialbles()
        self.Ventana.mainloop()


    def DeclaracionVarialbles(self):
        # valores por defecto
        self.recursos_gim={
            "coaches": 2, 
            "maquinas": 15, 
            "cap_maxima": 15,
            "costo_entrada": 150, 
            "costo_rep_maqaracion": 250,
            "sueldo_coach": 400,}
        
        self.recursos_spa={
            "masajistas": 10, 
            "jacuzzis": 10,
            "costo_masajista_ocupado": 50,
            "costo_masaje": 450, 
            "costo_rep_maqaracion_jacuzzi": 400, 
            "sueldo_masajista": 500,}
        
        self.recursos_acuatica={
            "motos": 10,
            "parasailing": 10,
            "snorkel": 10,
            "buceo": 10,
            "costo_moto": 800,
            "costo_parasailing": 600,
            "costo_snorkel": 600,
            "costo_buceo": 600,
            "costo_rep_maqaracion": 500,}
        
        self.recursos_musica={
            "costo_queja_show": 20,
            "costo_entrada_show": 350,}

        
        self.listiempo_en_maquinas_rotas=[]
        self.list_jacuzzis_rotos=[]
        self.list_equipos_rotos={"Moto acuatica":[],
                             "Parasailing":[],
                             "Snorkel": [],
                             "buceo": []}
        
        self.dicc_visitantes_rechazados={
            "Gimnasio":0,
            "Spa":0,
            "Acuatica":0,
            "Musica":0}


        self.ingresos_gim=0.0
        self.ingresos_spa=0.0
        self.ingresos_acuatica=0.0
        self.ingresos_musica=0.0
        self.egresos_personal=self.egresos_operativos=0.0
        self.visitantes_gim=0
        self.visitantes_spa=0
        self.visitantes_acuatica=0
        self.visitantes_musica=0
        self.visitantes_rechazados=0
        self.resultados_totales=[]
        self.Datos_subtablas={}

 
        self.Entradas={}
        self.entries_recursos={}
        self.frames_subareas={}
        self.N_frames_creados=False
        self.Aleatoreos=[]
        self.registro_aleatorios=[]  # [(aleatorio, tabla_usada, resultado), ...]

        self._inicializar_tablas_maestras()

    def _inicializar_tablas_maestras(self):
        #datos preestablecido en caso de que el usuario no entre a ninguna tabla
        defaults={
            # generales 
            "Llegada Grupos": ((5, 6, 7, 8, 9, 10), 
                   (0.05, 0.15, 0.20, 0.30, 0.20, 0.10)),

            "Destino":(("Gym", "Spa", "Acuatica", "Musica"),
                       (0.20, 0.15, 0.55, 0.10)),
                       
            "Decision":(("Espera", "Cambia", "Se va"),
                        (0.30, 0.50, 0.20)),

            "Tamaño de Grupo": ((1, 2, 3, 4), 
                    (0.20, 0.40, 0.25, 0.15)),

            # gimnasio 
            "Requiere Coach":(("No", "Sí"),
                              (0.75, 0.25)),

            "Tiempo en Maquina":((10, 20, 30, 45),
                                 (0.30, 0.45, 0.20, 0.05)),

            "Tiempo Total Gym":((30, 60, 90, 120),
                                (0.20, 0.60, 0.15, 0.05)),

            "Descompostura Maquina": ((0, 1, 2), 
                                      (0.95, 0.04, 0.01)),

            # espa 
            "Duracion Masaje":((30, 35, 40, 45),
                               (0.30, 0.40, 0.20, 0.10)),

            "Usara Jacuzzi":(("No", "Sí"),
                             (0.75, 0.25)),

            "Duracion Jacuzzi":((20, 25, 30, 35),
                                (0.30, 0.40, 0.20, 0.10)),

            "Descompostura Jacuzzi": ((0, 1, 2), 
                                      (0.95, 0.04, 0.01)),
            
            # area acuatica
            "Eleccion":(("Piscina","Moto acuatica","Parasailing","Snorkel","buceo"),
                        (0.30, 0.30, 0.20, 0.10, 0.10)),

            "Descompostura Equipo": ((0, 1, 2), 
                                     (0.96, 0.03, 0.01)),

            "Duración Actividad":((35, 40, 60, 70),
                                  (0.10, 0.20, 0.40, 0.30)),

            # show en vivo
            "Incidente en Show": (("No", "Sí"), 
                                  (0.88, 0.12)),

            "Tiempo en Show":((30, 60, 90, 120),
                              (0.20, 0.60, 0.15, 0.05)),

            "Costo Show":((1000.0, 1200.0, 1300.0, 1500.0),
                          (0.20, 0.60, 0.15, 0.05)),

            "Prob Compra Bebida": ((0, 1, 2, 3), 
                                   (0.10, 0.10, 0.30, 0.50)),

            "Precio Bebida":((60.0, 80.0, 100.0, 120.0),
                             (0.10, 0.50, 0.20, 0.20)),}
        
        self.tablas_maestras={}
        for nombre, (eventos, probs) in defaults.items():
            acum=self.calcular_acumulada(probs)
            rangos=self.calcular_rangos(acum)
            self.tablas_maestras[nombre]={
                "eventos": eventos,
                "probabilidades": probs,
                "acumuladas": acum,
                "rangos": rangos,}

    def Mostrar_pestaña_tablas(self):
        self.Frame_simulacion.place_forget()
        self.Contenedor_Configuracion.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.btn_nav_tablas.configure(fg_color=self.color_hover)
        self.btn_nav_simulacion.configure(fg_color=self.color_fondo)

        if not self.N_frames_creados:
            self.Crear_frames_subareas()

        # botones subareas
        areas=[
            ("General",1/6),
            ("Gimnasio",2/6),
            ("Spa",3/6),
            ("Acuatica",4/6),
            ("Musica",5/6),]
        
        for texto, pos in areas:
            ctk.CTkButton(
                self.Contenedor_Configuracion,
                text=texto,
                fg_color=self.color_fondo,
                hover_color=self.color_hover,
                command=lambda t=texto: self.Mostrar_frame_subarea(t)
            ).place(relx=pos, rely=0.05, anchor=ctk.CENTER)

        ctk.CTkButton(
            self.Contenedor_Configuracion,
            text="Guardar datos",
            fg_color="#00AD31", hover_color="#007A22",
            command=self.Guardar_datos
        ).place(relx=0.5, rely=0.12, anchor=ctk.CENTER)

        self.Mostrar_frame_subarea("General")

    def Crear_frames_subareas(self):

        for area in ["General", "Gimnasio", "Spa", "Acuatica", "Musica"]:
            frame=ctk.CTkScrollableFrame(self.Contenedor_Configuracion)
            frame.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)
            self.frames_subareas[area]=frame

        self.Llenar_frame_general()
        self.Llenar_frame_gimnasio()
        self.Llenar_frame_spa()
        self.Llenar_frame_acuatica()
        self.Llenar_frame_musica()
        
        self.N_frames_creados=True

    def Mostrar_frame_subarea(self, area):
        if area in self.frames_subareas:
            for frame in self.frames_subareas.values():
                frame.place_forget() 
            
            frame_seleccionado=self.frames_subareas[area]
            frame_seleccionado.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.80)
            frame_seleccionado.lift()

    def Llenar_frame_general(self):
        frame=self.frames_subareas["General"]
        ctk.CTkLabel(frame, text="TABLAS GENERALES",
                      font=("Arial", 15, "bold")).pack(pady=(10, 5))

        fila=ctk.CTkFrame(frame, fg_color="transparent")
        fila.pack(fill="x", pady=5)

        for i in range(4): 
            fila.grid_columnconfigure(i, weight=1)

        self.Crear_txt_box(fila, "Llegada Grupos",
                           (5, 6, 7, 8, 9, 10),
                           (0.05, 0.15, 0.20, 0.30, 0.20, 0.10), 0)
        
        self.Crear_txt_box(fila, "Destino",
                           ("Gym", "Spa", "Acuatica", "Musica"),
                           (0.20, 0.15, 0.55, 0.10), 1)
  
        self.Crear_txt_box(fila, "Decision",
                           ("Espera", "Cambia", "Se va"),
                           (0.30, 0.50, 0.20), 2)
        
        self.Crear_txt_box(fila, "Tamaño de Grupo",
                           (1, 2, 3, 4),
                           (0.20, 0.40, 0.25, 0.15), 3)

    def Llenar_frame_gimnasio(self):
        frame=self.frames_subareas["Gimnasio"]
        ctk.CTkLabel(frame, text="GIMNASIO",
                     font=("Arial", 15, "bold")).pack(pady=(10, 5))

        frame_entrys=ctk.CTkFrame(frame, fg_color="transparent")
        frame_entrys.pack(fill="x", pady=8)
        
        campos=[
            ("Coaches", "coaches", "2", 0),
            ("Maquinas", "maquinas", "15", 1),
            ("Capacidad Máxima", "cap_maxima", "15", 2),
            ("Costo entrada", "costo_entrada", "150", 3),  
            ("Costo reparacion", "costo_rep_maqaracion", "250", 4),
            ("Sueldo coach", "sueldo_coach", "400", 5),]
        
        self.entries_recursos["gim"]={}

        for label, clave, default, col in campos:
            frame_entrys.grid_columnconfigure(col, weight=1)
            ctk.CTkLabel(frame_entrys, text=label, font=("Arial", 11, "bold")).grid(row=0, column=col, padx=8)
            
            entry=ctk.CTkEntry(frame_entrys, width=90, justify="center")
            entry.grid(row=1, column=col, padx=8, pady=4)
            entry.insert(0, default)
            self.entries_recursos["gim"][clave]=entry

       
        ctk.CTkLabel(frame, text="TABLAS", font=("Arial", 13, "bold"),
                     text_color="#2E7D32").pack(pady=(8, 2))
        
        fila=ctk.CTkFrame(frame, fg_color="transparent")
        fila.pack(fill="x", pady=5)

        for i in range(4): 
            fila.grid_columnconfigure(i, weight=1)

        self.Crear_txt_box(fila, "Requiere Coach",
                           ("No", "Sí"), (0.75, 0.25), 0)
        
        self.Crear_txt_box(fila, "Tiempo en Maquina",
                           (10, 20, 30, 45), (0.30, 0.45, 0.20, 0.05), 1)
        
        self.Crear_txt_box(fila, "Tiempo Total Gym",
                           (30, 60, 90, 120), (0.20, 0.60, 0.15, 0.05), 2)
        
        self.Crear_txt_box(fila, "Descompostura Maquina",
                           (0, 1, 2), (0.95, 0.04, 0.01), 3)
        

    def Llenar_frame_spa(self):
        frame=self.frames_subareas["Spa"]
        ctk.CTkLabel(frame, text="SPA",
                     font=("Arial", 15, "bold")).pack(pady=(10, 5))

        frame_entrys=ctk.CTkFrame(frame, fg_color="transparent")
        frame_entrys.pack(fill="x", pady=8)
        
        campos=[
            ("Masajistas", "masajistas", "10", 0),
            ("Jacuzzis", "jacuzzis", "10", 1),
            ("Costo masaje", "costo_masaje", "450", 2),          
            ("Costo masajista ocupado", "costo_masajista_ocupado", "50", 3), 
            ("Reparación jacuz.", "costo_rep_maqaracion_jacuzzi", "400", 4),
            ("Sueldo masajista", "sueldo_masajista", "500", 5),]
        
        self.entries_recursos["spa"]={}
        for label, clave, default, col in campos:
            frame_entrys.grid_columnconfigure(col, weight=1)
            ctk.CTkLabel(frame_entrys, text=label, font=("Arial", 11, "bold")).grid(row=0, column=col, padx=8)
            
            entry=ctk.CTkEntry(frame_entrys, width=90, justify="center")
            entry.grid(row=1, column=col, padx=8, pady=4)
            entry.insert(0, default)
            self.entries_recursos["spa"][clave]=entry

        ctk.CTkLabel(frame, text="TABLAS", font=("Arial", 13, "bold"),
                     text_color="#8E24AA").pack(pady=(8, 2))
        
        fila=ctk.CTkFrame(frame, fg_color="transparent")
        fila.pack(fill="x", pady=5)

        for i in range(4): 
            fila.grid_columnconfigure(i, weight=1)

        self.Crear_txt_box(fila, "Duracion Masaje", (30, 35, 40, 45), (0.30, 0.40, 0.20, 0.10), 0)
        self.Crear_txt_box(fila, "Usara Jacuzzi", ("No", "Sí"), (0.75, 0.25), 1)
        self.Crear_txt_box(fila, "Duracion Jacuzzi", (20, 25, 30, 35), (0.30, 0.40, 0.20, 0.10), 2)
        
        self.Crear_txt_box(fila, "Descompostura Jacuzzi", (0, 1, 2), (0.95, 0.04, 0.01), 3)

    def Llenar_frame_acuatica(self):
        frame=self.frames_subareas["Acuatica"]
        ctk.CTkLabel(frame, text="AREA ACUATICA",
                     font=("Arial", 15, "bold")).pack(pady=(10, 5))

        frame_entrys=ctk.CTkFrame(frame, fg_color="transparent")
        frame_entrys.pack(fill="x", pady=8)
        
        campos=[
            ("Motos", "motos", "10", 0),
            ("Parasail", "parasailing", "10", 1),
            ("Snorkel", "snorkel", "10", 2),
            ("Buceo", "buceo", "10", 3),
            ("Costo moto", "costo_moto", "800", 4),     
            ("Costo parasail", "costo_parasailing", "600", 5),
            ("Costo snorkel", "costo_snorkel", "600", 6), 
            ("Costo buceo", "costo_buceo", "600", 7),  
            ("Reparación", "costo_rep_maqaracion", "500", 8),]
        
        self.entries_recursos["acuatica"]={}
        for label, clave, default, col in campos:
            frame_entrys.grid_columnconfigure(col, weight=1)
            ctk.CTkLabel(frame_entrys, text=label, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=5)
            
            entry=ctk.CTkEntry(frame_entrys, width=80, justify="center")
            entry.grid(row=1, column=col, padx=5, pady=4)
            entry.insert(0, default)
            self.entries_recursos["acuatica"][clave]=entry

    
        ctk.CTkLabel(frame, text="TABLAS", font=("Arial", 13, "bold"), 
                     text_color="#0288D1").pack(pady=(8, 2))
        
        fila=ctk.CTkFrame(frame, fg_color="transparent")
        fila.pack(fill="x", pady=5)
        for i in range(3): fila.grid_columnconfigure(i, weight=1)

        self.Crear_txt_box(fila, "Eleccion", 
                           ("Piscina", "Moto", "Parasail", "Snorkel", "Buceo"),
                           (0.20, 0.35, 0.25, 0.10, 0.10), 0) 
        
        self.Crear_txt_box(fila, "Duración Actividad", 
                           (35, 40, 60, 70), (0.10, 0.20, 0.40, 0.30), 1)
        
        self.Crear_txt_box(fila, "Descompostura Equipo", 
                           (0, 1, 2), (0.96, 0.03, 0.01), 2)


    def Llenar_frame_musica(self):
        frame=self.frames_subareas["Musica"]
        ctk.CTkLabel(frame, text="SHOWS Y MUSICA EN VIVO",
                     font=("Arial", 15, "bold")).pack(pady=(10, 5))

        frame_entrys=ctk.CTkFrame(frame, fg_color="transparent")
        frame_entrys.pack(fill="x", pady=8)
        
        campos=[
            ("Costo queja (x persona)", "costo_queja_show", "30", 0),
            ("Costo entrada show", "costo_entrada_show", "350", 1),]
        
        self.entries_recursos["musica"]={}
        for label, clave, default, col in campos:
            frame_entrys.grid_columnconfigure(col, weight=1)
            ctk.CTkLabel(frame_entrys, text=label, 
                         font=("Arial", 11, "bold")
                         ).grid(row=0, column=col, padx=25)
            
            entry=ctk.CTkEntry(frame_entrys, width=100, justify="center")
            entry.grid(row=1, column=col, padx=25, pady=4)
            entry.insert(0, default)
            self.entries_recursos["musica"][clave]=entry

        ctk.CTkLabel(frame, text="TABLAS ",
                     font=("Arial", 13, "bold"), text_color="#7B1FA2").pack(pady=(8, 2))

    
        fila1=ctk.CTkFrame(frame, fg_color="transparent")
        fila1.pack(fill="x", pady=5)
        for i in range(3): 
            fila1.grid_columnconfigure(i, weight=1)

    
        self.Crear_txt_box(fila1, "Incidente en Show", ("No", "Sí"), (0.88, 0.12), 0)
        self.Crear_txt_box(fila1, "Tiempo en Show", (30, 60, 90, 120), (0.20, 0.60, 0.15, 0.05), 1)
        self.Crear_txt_box(fila1, "Costo Operación Show", (1000.0, 1200.0, 1300.0, 1500.0), (0.20, 0.60, 0.15, 0.05), 2)

        fila2=ctk.CTkFrame(frame, fg_color="transparent")
        fila2.pack(fill="x", pady=5)
        for i in range(2): 
            fila2.grid_columnconfigure(i, weight=1)

        self.Crear_txt_box(fila2, "Bebidas por persona", (0, 1, 2, 3), (0.10, 0.10, 0.30, 0.50), 0)
        self.Crear_txt_box(fila2, "Precio Bebida", (60.0, 80.0, 100.0, 120.0), (0.10, 0.30, 0.30, 0.30), 1)

  
    def Crear_txt_box(self, frame, titulo, datos, probs,columna):

        ctk.CTkLabel(frame, 
                     text=titulo, 
                     font=("Arial", 11, "bold")
                     ).grid(row=2, column=columna, padx=5, pady=5)
        
        txt=ctk.CTkTextbox(frame, width=145, height=130)
        txt.grid(row=3, column=columna, padx=5, pady=5)

        tabla_actual=self.tablas_maestras.get(titulo, {})

        datos_definidos=tabla_actual.get("eventos", datos)
        probs_definidas=tabla_actual.get("probabilidades", probs)

        self.Insertar_datos_txtbox(datos_definidos, probs_definidas, txt)
        self.Entradas[titulo]=txt


    def Guardar_datos(self):
        guardados=0
        errores=[]

        for titulo, widget in self.Entradas.items():
            resultado=self.Procesar_textbox(widget, titulo)

            if resultado is None:
                errores.append(titulo)

            else:
                eventos, probs=resultado
                acum=self.calcular_acumulada(probs)
                rangos=self.calcular_rangos(acum)
                self.tablas_maestras[titulo]={
                    "eventos": eventos, "probabilidades": probs,
                    "acumuladas": acum, "rangos": rangos,}
                guardados += 1

    
        def convertir_a_numero(widget):
            try:
                val=widget.get().strip()
                if "." in val:
                    return float(val)
                return int(val)
            
            except ValueError:
                return None  

        areas={
            "gim": self.recursos_gim,
            "spa": self.recursos_spa,
            "acuatica": self.recursos_acuatica,
            "musica": self.recursos_musica,}

        for area_key, diccionario_destino in areas.items():
            widgets_area=self.entries_recursos.get(area_key, {})
            
            for clave, widget in widgets_area.items():
                valor_numerico=convertir_a_numero(widget)
                
                if valor_numerico is not None:
                    diccionario_destino[clave]=valor_numerico

        if errores:
            CTkMessagebox(title="Advertencia",
                          message=f"Se guardaron {guardados} tablas.\n"
                                  f"Revisa: {', '.join(errores)}",
                          icon="warning")
        else:
            CTkMessagebox(title="Guardado",
                          message=f"{guardados} tablas y todos los recursos\n"
                                  f"guardados correctamente",
                          icon="check")

    
    def mostrar_pestaña_simulacion(self):
        self.Contenedor_Configuracion.place_forget()

        self.Frame_simulacion.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.btn_nav_simulacion.configure(fg_color=self.color_hover)
        self.btn_nav_tablas.configure(fg_color=self.color_fondo)

        ctk.CTkLabel(self.Frame_simulacion, text="Días a simular:",
                     font=("arial", 15), text_color="black"
                     ).place(relx=0.07, rely=0.15, anchor=ctk.CENTER)
        
        self.Dias_a_simular=ctk.CTkEntry(self.Frame_simulacion, width=150,
                                           font=("arial", 15), justify="center")
        self.Dias_a_simular.place(relx=0.07, rely=0.20, anchor=ctk.CENTER)

        ctk.CTkButton(self.Frame_simulacion, 
                      text="Simular",
                      fg_color="#693700", 
                      hover_color="#816343",
                      command=self.Simulacion
                      ).place(relx=0.07, rely=0.26, anchor=ctk.CENTER)

        self.Frame_tabla_montecarlo=ctk.CTkScrollableFrame(self.Frame_simulacion)
        self.Frame_tabla_montecarlo.place(relx=0.15, rely=0.10, relwidth=0.70, relheight=0.80)



        self.lbl_ing_total=ctk.CTkLabel(self.Frame_simulacion,
                                          text="Ingresos totales...", 
                                          text_color="black")
        self.lbl_ing_total.place(relx=0.07, rely=0.38, anchor=ctk.CENTER)
        
        self.lbl_egr_total=ctk.CTkLabel(self.Frame_simulacion,
                                          text="Egresos totales...", 
                                          text_color="black")
        self.lbl_egr_total.place(relx=0.07, rely=0.46, anchor=ctk.CENTER)

        self.lbl_neto=ctk.CTkLabel(self.Frame_simulacion,
                                     text="Resultado neto...", 
                                     text_color="black")
        self.lbl_neto.place(relx=0.07, rely=0.54, anchor=ctk.CENTER)

        self.txt_aleatorios=ctk.CTkTextbox(self.Frame_simulacion,
                                             font=("Consolas", 13), width=200)
        self.txt_aleatorios.place(relx=.93, rely=.25, anchor="n", relheight=.65)



        ctk.CTkButton(self.Frame_simulacion, 
                      text="Generar aleatorios",
                      fg_color=self.color_fondo, 
                      hover_color="#816343",
                      command=self.Generar_aleatorios
                      ).place(relx=0.93, rely=0.12, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                      text="Refrescar",
                      fg_color="#5A3D1D", 
                      hover_color="#816343",
                      command=self.leer_numeros_de_archivo
                      ).place(relx=0.93, rely=.17, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                      text="Tablas de rango",
                      fg_color="#693700", 
                      hover_color="#816343",
                      command=self.Mostrar_tablas_rango
                      ).place(relx=0.07, rely=0.76, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                      text="Aleatorios usados",
                      fg_color="#5D4037", 
                      hover_color="#3E2723",
                      command=self.Mostrar_Aleatorios_Usados
                      ).place(relx=0.07, rely=0.65, anchor=ctk.CENTER)
        
        ctk.CTkButton(self.Frame_simulacion, 
                      text="Resumen",
                      fg_color="#693700", 
                      hover_color="#816343",
                      command=self.Mostrar_Resumen_Final
                      ).place(relx=0.07, rely=0.86, anchor=ctk.CENTER)
        

        self.Mostrar_aleatorios()

    def Mostrar_aleatorios(self):
        self.txt_aleatorios.delete("0.0", ctk.END)
        if not self.Aleatoreos:
            self.txt_aleatorios.insert("0.0", "No hay numeros para\niniciar la simulacion")
        else:
            texto_lista="Numeros a utilizar:\n"
            
            for i, val in enumerate(self.Aleatoreos):
                texto_lista += f"[{i + 1}] -> {val}\n"

            self.txt_aleatorios.insert("0.0", texto_lista)
            self.txt_aleatorios.configure(state="disabled")

   
    def Simulacion(self):
        try:
            self.Dias_simulacion=int(self.Dias_a_simular.get())
        except ValueError:
            CTkMessagebox(title="Error", message="Ingrese un numero valido de dias.", icon="cancel")
            return
            
        if not self.Aleatoreos:
            CTkMessagebox(title="Error", message="No hay numeros aleatorios. Generalos primero.", icon="cancel")
            return

        self.ingresos_gim=0.0
        self.ingresos_spa=0.0
        self.ingresos_acuatica=0.0
        self.ingresos_musica=0.0
        
        self.egresos_personal=0.0
        self.egresos_operativos=0.0
        self.ingresos_perdidos_gim=0.0
        self.ingresos_perdidos_spa=0.0
        self.ingresos_perdidos_acuatica=0.0
        self.ingresos_perdidos_shows=0.0

 
        self.visitantes_gim=0
        self.visitantes_spa=0
        self.visitantes_acuatica=0
        self.visitantes_musica=0
        self.visitantes_rechazados=0

        self.resultados_totales=[]
        self.Datos_subtablas={}


        self.listiempo_en_maquinas_rotas=[]
        self.list_jacuzzis_rotos=[]
        self.registro_aleatorios=[]  # Limpiar registro


        self.listiempo_en_maquinas_rotas=[]
        self.list_jacuzzis_rotos=[]
        self.list_equipos_rotos={"Moto acuatica": [], 
                                 "Parasailing": [], 
                                 "Snorkel": [], 
                                 "buceo": []}

    
        equipos_disp={
            "Moto acuatica": int(self.recursos_acuatica["motos"]),
            "Parasailing": int(self.recursos_acuatica["parasailing"]),
            "Snorkel": int(self.recursos_acuatica["snorkel"]),
            "buceo": int(self.recursos_acuatica["buceo"])}
        

        total_coaches=int(self.recursos_gim["coaches"])
        sueldo_coach=float(self.recursos_gim["sueldo_coach"])
        nomina_coaches=total_coaches * sueldo_coach

        total_masajistas=int(self.recursos_spa["masajistas"])
        sueldo_masajista=float(self.recursos_spa["sueldo_masajista"])
        nomina_masajistas=total_masajistas * sueldo_masajista

        nomina_mensual_total=nomina_coaches + nomina_masajistas


        for dia in range(1, self.Dias_simulacion + 1):
            print("dia actual: ",dia)
            if dia % 30 == 0:
                self.egresos_personal += nomina_mensual_total

            maquinas_siguen_en_taller=[]
            for dias_restantes in self.listiempo_en_maquinas_rotas:
                if dias_restantes > 1:
                    maquinas_siguen_en_taller.append(dias_restantes - 1)
            self.listiempo_en_maquinas_rotas=maquinas_siguen_en_taller
            print("maqinas que aun siguen en rep: ",self.listiempo_en_maquinas_rotas)

            jacuzzis_siguen_en_rep=[]
            for dias_restantes in self.list_jacuzzis_rotos:
                if dias_restantes > 1:
                    jacuzzis_siguen_en_rep.append(dias_restantes - 1)
            self.list_jacuzzis_rotos=jacuzzis_siguen_en_rep
            print("jacuzzis averiados: ",self.list_jacuzzis_rotos)

            nombre_clave_equipo={
                "Moto acuatica":"motos",
                "Parasailing":"parasailing",
                "Snorkel":"snorkel",
                "buceo": "buceo",}

            for nombre_equipo, clave_recurso in nombre_clave_equipo.items():
                lista_averias_actual=self.list_equipos_rotos[nombre_equipo]
                
                equipos_reparados_hoy=0
                equipos_que_siguen_rotos=[]
                
                for dias_restantes in lista_averias_actual:
                    if dias_restantes == 1:
                        equipos_reparados_hoy += 1
                    elif dias_restantes > 1:
                        equipos_que_siguen_rotos.append(dias_restantes - 1)
                        
                self.list_equipos_rotos[nombre_equipo]=equipos_que_siguen_rotos
                print("equipos descompuestos del area acuatica: ",self.list_equipos_rotos)

                stock_maximo_original=int(self.recursos_acuatica[clave_recurso])
                stock_actual_mas_reparados=equipos_disp[nombre_equipo] + equipos_reparados_hoy
                
                equipos_disp[nombre_equipo]=min(stock_maximo_original, stock_actual_mas_reparados)

            # Gimnasio
            cap_gim_dia=int(self.recursos_gim["cap_maxima"])
            coaches_dia=int(self.recursos_gim["coaches"])
            
            total_maquinas=int(self.recursos_gim["maquinas"])
            maquinas_rotas=len(self.listiempo_en_maquinas_rotas)
            maquinas_disp=max(0, total_maquinas - maquinas_rotas)
            print("maquinas del gimnacion disp: ",maquinas_disp)

            # Spa
            masaj_dia=int(self.recursos_spa["masajistas"])

            total_jacuzzis=int(self.recursos_spa["jacuzzis"])
            jacuzzis_rotos=len(self.list_jacuzzis_rotos)
            jacuzzis_disp=max(0, total_jacuzzis - jacuzzis_rotos)
            print("jacuzzis del spa disp: ",jacuzzis_disp)

            # Show del día
            aleatoreo_costo_show=self.obtener_siguiente_aleatorio()
            costo_show=float(self.Obtener_Evento("Costo show", aleatoreo_costo_show) or 1000.0)
            
            self.Registrar_aleatorio(aleatoreo_costo_show, 
                                     f"Determinar el costo del show del dia {dia} : {costo_show}")
            print(f"el show del dia {dia} costo : {costo_show}")
            self.egresos_operativos += costo_show

            aleatoreo_incidente=self.obtener_siguiente_aleatorio()
            hay_incidente=str(self.Obtener_Evento("Incidente en show", aleatoreo_incidente)) == "Sí"
            self.Registrar_aleatorio(aleatoreo_incidente, 
                                     f"Determinar si hay incidente en el show del dia {dia} : {hay_incidente}")

            print(f"va a ocurrir un incidente? {hay_incidente}")

            aleatoreo_llegada=self.obtener_siguiente_aleatorio()
            n_grupos=int(self.Obtener_Evento("Llegada Grupos", aleatoreo_llegada) or 0)
            self.Registrar_aleatorio(aleatoreo_llegada, 
                                     f"Determinar cuantos grupos llegaron en el dia {dia} : {n_grupos}")
            print(f"lleagaron {n_grupos} grupos")

            ingresos_dia={"Gym": 0.0, 
                          "Spa": 0.0, 
                          "Acuatica": 0.0, 
                          "Musica": 0.0}
            egresos_dia=0.0
            sub_eventos=[]
            personas_musica_dia=0 

            for grupo in range(n_grupos):
            
                aleatoreo_destino=self.obtener_siguiente_aleatorio()
                destino=str(self.Obtener_Evento("Destino", aleatoreo_destino) or "Gym")
                self.Registrar_aleatorio(aleatoreo_destino, 
                                     f"Determinar el destino del grupo {grupo} del dia {dia} : {destino}")
                print(f"el grupo {grupo} se fue a {destino}")

                aleatoreo_tamaño=self.obtener_siguiente_aleatorio()
                personas=int(self.Obtener_Evento("Tamaño de Grupo", aleatoreo_tamaño) or 1)
                self.Registrar_aleatorio(aleatoreo_tamaño, 
                                     f"Determinar el tamaño del grupo {grupo} del dia {dia} : {personas}")
                print(f"el grupo {grupo} estaba confomeado por {personas} personas")
                ing=0.0
                egr=0.0
                evento_str=""

                #gym
                if destino == "Gym":
                    if cap_gim_dia >= personas:
                        cap_gim_dia -= personas
                        ing=personas * float(self.recursos_gim["costo_entrada"])
                        self.visitantes_gim += personas

                        for p in range(personas):
                            
                            aleatoreo_requ_coach=self.obtener_siguiente_aleatorio()

                            if str(self.Obtener_Evento("Requiere Coach", aleatoreo_requ_coach)) == "Sí":
                                e="Sí"
                                if coaches_dia > 0:
                                     
                                    coaches_dia -= 1
                            else:
                                e="No"

                            self.Registrar_aleatorio(aleatoreo_requ_coach, 
                                     f"     GYM | la persona {p} requiere coach del dia {dia}? : {e}")
                            
                            aleatoero_tiempo_gym=self.obtener_siguiente_aleatorio()
                            tiempo_gym_total=int(self.Obtener_Evento("Tiempo Total Gym", aleatoero_tiempo_gym) or 30)
                            self.Registrar_aleatorio(aleatoero_tiempo_gym, 
                                     f"     GYM | Estancia en gym de la persona {p} del dia {dia}? : {tiempo_gym_total}")
                            tiempo_acumulado=0
                            
                            while tiempo_acumulado < tiempo_gym_total and maquinas_disp > 0:
                                aleatoreo_tiempo_maq=self.obtener_siguiente_aleatorio()
                                tiempo_en_maq=int(self.Obtener_Evento("Tiempo en Maquina", aleatoreo_tiempo_maq) or 10)
                                self.Registrar_aleatorio(aleatoreo_tiempo_maq, 
                                     f"     GYM | duracion en maquina de la persona {p} del dia {dia}? : {tiempo_en_maq}")
                                tiempo_acumulado += tiempo_en_maq
                                
                                aleatoreo_averia_maq=self.obtener_siguiente_aleatorio()
                                dias_averia_maq=int(self.Obtener_Evento("Descompostura Maquina", aleatoreo_averia_maq) or 0)
                                self.Registrar_aleatorio(aleatoreo_averia_maq, 
                                     f"     GYM | Hay averia de maquina en el dia {dia}? : {dias_averia_maq}")
                                
                                if dias_averia_maq > 0:
                                    self.listiempo_en_maquinas_rotas.append(dias_averia_maq)
                                    maquinas_disp=max(0, maquinas_disp - 1)
                                    
                                    costo_rep_maq=float(self.recursos_gim["costo_rep_maqaracion"])
                                    egr += costo_rep_maq
                                    self.egresos_operativos += costo_rep_maq

                        evento_str=f"Atendido | {personas}p | maq.disp:{maquinas_disp}"
                    

                    else:
                        aleatoreo_decision=self.obtener_siguiente_aleatorio()
                        dec=self.Obtener_Evento("Decision", aleatoreo_decision)
                        self.Registrar_aleatorio(aleatoreo_decision, 
                                                 f"     GYM | Hubo saturacion, los clinetes decidieron {dec} en el {dia} ")
                        if str(dec) == "Se va":
                            self.ingresos_perdidos_gim += personas * float(self.recursos_gim["costo_entrada"])
                            self.dicc_visitantes_rechazados["Gimnasio"]+=personas
                            self.visitantes_rechazados += personas
                            
                        
                            
                        evento_str=f"Capacidad llena -> {dec}"

                    self.ingresos_gim += ing
                    ingresos_dia["Gym"] += ing
                    egresos_dia += egr

                elif destino == "Spa":
                    atendidos=min(personas, masaj_dia)
                    no_atend=personas - atendidos
                    masaj_dia -= atendidos

                    if atendidos > 0:
                        ing += atendidos * float(self.recursos_spa["costo_masaje"])
                        self.visitantes_spa += atendidos
                        
                        for _ in range(atendidos):
                            aleatoreo_usara_jacz=self.obtener_siguiente_aleatorio()
                            
                            if str(self.Obtener_Evento("Usara Jacuzzi", aleatoreo_usara_jacz)) == "Sí":
                                self.Registrar_aleatorio(aleatoreo_usara_jacz, 
                                                 f"     SPA | El cliente {p} en el {dia} decidio usar jacuzzi?: Sí")
                                if jacuzzis_disp > 0:
                                    jacuzzis_disp -= 1
                                    
                                    aleatoreo_averia_jacz=self.obtener_siguiente_aleatorio()
                                    dias_averia_jzzi=int(self.Obtener_Evento("Descompostura Jacuzzi", aleatoreo_averia_jacz) or 0)
                                    self.Registrar_aleatorio(aleatoreo_averia_jacz, 
                                                 f"     SPA | Se descompuso un jacuzzi en el dia {dia}?: {dias_averia_jzzi}")
                                    
                                    if dias_averia_jzzi > 0:
                                        self.list_jacuzzis_rotos.append(dias_averia_jzzi)
                                        jacuzzis_disp=max(0, jacuzzis_disp - 1)
                                        
                                        costo_rep_maq_j=float(self.recursos_spa["costo_rep_maqaracion_jacuzzi"])
                                        egr += costo_rep_maq_j
                                        self.egresos_operativos += costo_rep_maq_j
                            else:
                                self.Registrar_aleatorio(aleatoreo_usara_jacz, 
                                                 f"     SPA | El cliente {p} en el {dia} decidio usar jacuzzi?: No")

                    if no_atend > 0:
                        costo_penalizacion=float(self.recursos_spa["costo_masajista_ocupado"])
                        self.dicc_visitantes_rechazados["Spa"]+=no_atend
                        egr += no_atend * costo_penalizacion
                        self.ingresos_perdidos_spa += no_atend * costo_penalizacion
                        self.visitantes_rechazados += no_atend

                    evento_str=f"Atendidos:{atendidos} | Sin masaj:{no_atend}"
                    self.ingresos_spa += ing
                    ingresos_dia["Spa"] += ing
                    egresos_dia += egr


                elif destino == "Acuatica":
                    
                    aleatoreo_subarea_acu=self.obtener_siguiente_aleatorio()
                    elec=str(self.Obtener_Evento("Eleccion", aleatoreo_subarea_acu) or "Piscina")
                    self.Registrar_aleatorio(aleatoreo_subarea_acu, 
                                                 f"     ACUATICA | el grupo {grupo} decidio ir en el dia {dia} a: {elec}")
                    costo_mapa={
                        "Piscina": 0.0,
                        "Moto acuatica": float(self.recursos_acuatica["costo_moto"]),
                        "Parasailing": float(self.recursos_acuatica["costo_parasailing"]),
                        "Snorkel": float(self.recursos_acuatica["costo_snorkel"]),
                        "buceo": float(self.recursos_acuatica["costo_buceo"]),}
                    
                    costo_unit=costo_mapa.get(elec, 0.0)

                    if elec == "Piscina":
                        self.visitantes_acuatica += personas
                        evento_str=f"Piscina | {personas}p"

                    else:
                        disp=equipos_disp.get(elec, 0)
                        
                        if disp >= personas:
                            equipos_disp[elec] -= personas
                            ing=personas * costo_unit
                            self.visitantes_acuatica += personas
                            evento_str=f"{elec} | {personas}p | DISP"
                            
                            aleatoreo_averia_maq_e=self.obtener_siguiente_aleatorio()
                            dias_averia_maq_e=int(self.Obtener_Evento("Descompostura Equipo", aleatoreo_averia_maq_e) or 0)
                            self.Registrar_aleatorio(aleatoreo_averia_maq_e, 
                                                 f"     ACUATICA | dias de averia del equipo usado del dia {dia}: {dias_averia_maq_e}")
                            
                            if dias_averia_maq_e > 0:
                                self.list_equipos_rotos[elec].append(dias_averia_maq_e)
                                equipos_disp[elec]=max(0, equipos_disp[elec] - 1)
                                
                                costo_rep_maq_e=float(self.recursos_acuatica["costo_rep_maqaracion"])
                                egr += costo_rep_maq_e
                                self.egresos_operativos += costo_rep_maq_e
                        
                        else:
                            ing=0.0
                            self.dicc_visitantes_rechazados["Acuatica"]+=personas
                            self.ingresos_perdidos_acuatica+=personas * costo_unit
                            self.visitantes_rechazados += personas
                            evento_str=f"{elec} | {personas}p | NO DISP -> Abandono"

                    self.ingresos_acuatica += ing
                    ingresos_dia["Acuatica"] += ing
                    egresos_dia += egr


                elif destino == "Musica":
                    ing=personas * float(self.recursos_musica["costo_entrada_show"])
                    self.visitantes_musica += personas
                    personas_musica_dia += personas

                    for p1 in range(personas):
                        aleatoreo_compra_bebida=self.obtener_siguiente_aleatorio()
                        compra_bebida=int(self.Obtener_Evento("Prob Compra Bebida", aleatoreo_compra_bebida) or 0)
                        self.Registrar_aleatorio(aleatoreo_compra_bebida, 
                                                 f"     SHOW/MUSICA | El cliente {p1} del {dia} compara bebidas?: {compra_bebida}")
                        
                        for p2 in range(compra_bebida):
                            aleatroeo_precio_bebida=self.obtener_siguiente_aleatorio()
                            precio_b=float(self.Obtener_Evento("Precio Bebida", aleatroeo_precio_bebida) or 60.0)
                            self.Registrar_aleatorio(aleatroeo_precio_bebida, 
                                                 f"     SHOW/MUSICA | El cliente {p1} del {dia} gasto {compra_bebida} en una bebida")
                            ing += precio_b

                    evento_str=f"Show | {personas}p"
                    self.ingresos_musica += ing
                    ingresos_dia["Musica"] += ing
                    egresos_dia += egr

                sub_eventos.append([
                    grupo + 1, round(aleatoreo_destino, 4), destino, personas, evento_str,
                    f"${ing:,.2f}", f"${egr:,.2f}"])

            
            if hay_incidente and personas_musica_dia > 0:
                costo_q=personas_musica_dia * float(self.recursos_musica["costo_queja_show"])
                self.ingresos_perdidos_shows+=costo_q

                self.egresos_operativos += costo_q
                egresos_dia += costo_q


            self.Datos_subtablas[dia]=sub_eventos
            total_ing_dia=sum(ingresos_dia.values())
            
            self.resultados_totales.append([
                dia, round(aleatoreo_llegada, 4),
                n_grupos,
                round(ingresos_dia["Gym"], 2),
                round(ingresos_dia["Spa"], 2),
                round(ingresos_dia["Acuatica"], 2),
                round(ingresos_dia["Musica"], 2),
                round(egresos_dia, 2),
                round(total_ing_dia - egresos_dia, 2),])

  
        self.Tabla_montecarlo(self.resultados_totales)

        total_ing=self.ingresos_gim + self.ingresos_spa + self.ingresos_acuatica + self.ingresos_musica
        total_egr=self.egresos_personal + self.egresos_operativos
        
        self.lbl_ing_total.configure(text=f"Ingresos totales:\n${total_ing:,.2f}")
        self.lbl_egr_total.configure(text=f"Egresos totales:\n${total_egr:,.2f}")
        self.lbl_neto.configure(text=f"Resultado neto:\n${total_ing - total_egr:,.2f}")


    def Tabla_montecarlo(self, resultados_totales):
        self.Frame_tabla_montecarlo.grid_columnconfigure(0, weight=1)
        if hasattr(self, 'tabla') and self.tabla:
            try: self.tabla.destroy()
            except: pass

        self.tabla=CTkTable(
            master=self.Frame_tabla_montecarlo,
            command=self.Subtabla,
            row=len(resultados_totales) + 1,
            column=len(resultados_totales[0]),
            header_color="#3E2723", text_color="black",
            colors=["#D7CCC8", "#FFFFFF"],
            values=[["Día","Aleatorio →","Grupos","Ing.Gym","Ing.Spa","Ing.Acuctica","Ing.Musica",
                     "Egresos","Neto Día"]]
                   + resultados_totales)
        self.tabla.edit_row(0, text_color="white")
        self.tabla.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def Subtabla(self, datos_celda):
        try:
            dia_int=int(str(datos_celda["value"]))
        except (ValueError, KeyError):
            return
        if dia_int not in self.Datos_subtablas:
            return

        ventana_detalle=ctk.CTkToplevel()
        ventana_detalle.title(f"Detalle del dia {dia_int}")
        ventana_detalle.geometry("1000x420")
        ventana_detalle.after(100, ventana_detalle.lift)

        columnas=["Grupo N","Aleatorio →","Destino","Personas","Evento / Estado","Ingreso","Egreso"]
        subtabla=CTkTable(ventana_detalle, values=[columnas], header_color="#3E2723",
                     colors=["#D7CCC8","#FFFFFF"], text_color="black")
        subtabla.pack(expand=True, fill="both")
        subtabla.edit_row(0, text_color="white")
        for fila in self.Datos_subtablas[dia_int]:
            subtabla.add_row(values=fila)

   
    def Registrar_aleatorio(self, aleatorio, mensaje):
        """Registra un aleatorio usado con su propósito y resultado."""
        self.registro_aleatorios.append({
            "aleatorio": round(aleatorio, 4),
            "texto": str( mensaje)})

    def Mostrar_Aleatorios_Usados(self):
        if not self.registro_aleatorios:
            CTkMessagebox(title="Error", 
                          message="Ejecuta una simulación primero para ver los aleatorios usados.",
                          icon="cancel")
            return

        ventana=ctk.CTkToplevel()
        ventana.title("Aleatorios Usados en la Simulación")
        ventana.geometry("800x600")
        ventana.after(100, ventana.lift)

        frame_info=ctk.CTkFrame(ventana, fg_color="#3E2723", corner_radius=8)
        frame_info.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(frame_info, 
                     text=f"Total de aleatorios utilizados: {len(self.registro_aleatorios)}",
                     font=("Arial", 20,"bold"), text_color="#81C784").pack(pady=5)

        txt_aleatorios=ctk.CTkTextbox(ventana, font=("Consolas", 12), width=780)
        txt_aleatorios.pack(fill="both", expand=True, padx=10, pady=10)
        
        contenido=""
        for i, reg in enumerate(self.registro_aleatorios, 1):
            contenido += f"[{i}] Aleatorio: {reg["aleatorio"]:.4f} → {reg["texto"]}\n"
            contenido +="\n"
        
        txt_aleatorios.insert("0.0", contenido)
        txt_aleatorios.configure(state="disabled")

        frame_btn=ctk.CTkFrame(ventana, fg_color="transparent")
        frame_btn.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(frame_btn, text="Cerrar",
                      fg_color="#5A3D1D", hover_color="#816343",
                      command=ventana.destroy
                      ).pack(side="left", padx=5)

    def Mostrar_tablas_rango(self):
        if not self.tablas_maestras:
            CTkMessagebox(title="Error", message="No hay tablas configuradas.", icon="cancel")
            return
        
        ventana_detalle=ctk.CTkToplevel()
        ventana_detalle.title("Rangos de probabilidad")
        ventana_detalle.geometry("950x600")
        ventana_detalle.after(100, ventana_detalle.lift)

        scroll_main=ctk.CTkScrollableFrame(ventana_detalle)
        scroll_main.pack(fill="both", expand=True, padx=10, pady=10)

        fila_frame=None
        
        for i, (nombre, data) in enumerate(self.tablas_maestras.items()):
            if "rangos" not in data: 
                continue

            if i % 3 == 0:
                fila_frame=ctk.CTkFrame(scroll_main, fg_color="transparent")
                fila_frame.pack(fill="x", pady=5)

            datos_tabla=[[nombre]]
            for idx, ev in enumerate(data["eventos"]):
                rango=data["rangos"][idx]
                rango_str=f"{rango[0]:g} - {rango[1]:g}"
                datos_tabla.append([f"{rango_str} : {ev}"])

            tabla=CTkTable(
                fila_frame,
                values=datos_tabla,
                header_color="#3E2723",
                colors=["#D7CCC8", "#FFFFFF"],
                text_color="black"
            )
            tabla.edit_row(0, text_color="white")
            tabla.pack(side="left", padx=10, pady=5, expand=True)
    
    def Mostrar_Resumen_Final(self):
        if not self.resultados_totales:
            CTkMessagebox(title="Error", message="Primero ejecuta la simulación.", icon="cancel")
            return

        for widget in self.Frame_tabla_montecarlo.winfo_children():
            widget.destroy()

        def card(row, col, titulo):
            frame=ctk.CTkFrame(ct, fg_color="#3E2723", corner_radius=12,
                             border_width=2, border_color="#D7CCC8")
            frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            ctk.CTkLabel(frame, text=titulo, font=("Arial", 16, "bold"), text_color="white").pack(pady=8)
            return frame

        ctk.CTkLabel(self.Frame_tabla_montecarlo, text="RESUMEN DE RESULTADOS FINALES",
                     font=("Arial", 26, "bold"), text_color="white").pack(pady=15)

        ct=ctk.CTkFrame(self.Frame_tabla_montecarlo, fg_color="transparent")
        ct.pack(expand=True, fill="both", padx=15, pady=5)
        ct.grid_columnconfigure((0, 1, 2), weight=1)

        # calculos
        ingreso_total=(self.ingresos_gim + self.ingresos_spa + self.ingresos_acuatica + self.ingresos_musica)
        egreso_total=self.egresos_personal + self.egresos_operativos
        resultado_neto=ingreso_total - egreso_total
        total_atendidos=(self.visitantes_gim + self.visitantes_spa + self.visitantes_acuatica + self.visitantes_musica)

        # Ingresos
        c1=card(0, 0, "INGRESOS POR AREA")
        for nombre, valor in [("Gimnasio", self.ingresos_gim), ("Spa", self.ingresos_spa),
                              ("Acuatica", self.ingresos_acuatica), ("Musica", self.ingresos_musica)]:
            ctk.CTkLabel(c1, text=f"{nombre}: ${valor:,.2f}", 
                         font=("Arial", 12), 
                         text_color="white").pack(anchor="w", padx=20, pady=2)


        ctk.CTkLabel(c1, text=f"TOTAL: ${ingreso_total:,.2f}", 
                     font=("Arial", 14, "bold"), 
                     text_color="#81C784").pack(pady=8)
        
        ctk.CTkButton(c1, text="Ver ingresos por área",
                      fg_color="#5D4037", hover_color="#3E2723",
                      command=self.Graficar_ingresos).pack(pady=15)

        # Egresos
        c2=card(0, 1, "EGRESOS")
        ctk.CTkLabel(c2, text=f"Personal: ${self.egresos_personal:,.2f}", 
                     font=("Arial", 12), 
                     text_color="white").pack(anchor="w", padx=20, pady=4)
        

        ctk.CTkLabel(c2, text=f"Operativos: ${self.egresos_operativos:,.2f}", 
                     font=("Arial", 12), 
                     text_color="white").pack(anchor="w", padx=20, pady=4)
        

        ctk.CTkLabel(c2, text=f"TOTAL: ${egreso_total:,.2f}", 
                     font=("Arial", 14, "bold"), 
                     text_color="#EF9A9A").pack(pady=8)
        
        color_neto="#81C784" if resultado_neto >= 0 else "#EF9A9A"
        ctk.CTkLabel(c2, text=f"Resultado Neto:\n${resultado_neto:,.2f}", 
                     font=("Arial", 16, "bold"), 
                     text_color=color_neto).pack(pady=10)

        # clientes
        c3=card(0, 2, "CLIENTES")
        for nombre, n in [("Gimnasio", self.visitantes_gim), 
                          ("Spa", self.visitantes_spa),
                          ("Acuatica", self.visitantes_acuatica), 
                          ("Musica", self.visitantes_musica),
                          ("Rechazados", self.visitantes_rechazados)]:
            
            ctk.CTkLabel(c3, text=f"{nombre}: {n}", 
                         font=("Arial", 12), 
                         text_color="white").pack(anchor="w", padx=20, pady=1)
        
        ctk.CTkLabel(c3, text=f"Total atendidos: {total_atendidos}", 
                     font=("Arial", 13, "bold"), 
                     text_color="#81C784").pack(pady=6)
        
        if total_atendidos + self.visitantes_rechazados > 0:
            porcentaje=self.visitantes_rechazados / (total_atendidos + self.visitantes_rechazados) * 100
            ctk.CTkLabel(c3, text=f"Tasa rechazo: {porcentaje:.1f}%", 
                         font=("Arial", 12),
                         text_color="#EF9A9A" if porcentaje > 15 else "white").pack()

        # Rechazos
        c4=card(1, 0, "ABANDONOS Y COSTO * AREA")
        ctk.CTkLabel(c4, text=f"Ingresos perdidos de\nGimnacio: {self.ingresos_perdidos_gim}", 
                         font=("Arial", 12), 
                         text_color="white").pack(padx=20, pady=5)
        ctk.CTkLabel(c4, text=f"clientes perdidos de\narea acuatica: {self.dicc_visitantes_rechazados["Gimnasio"]}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        

        ctk.CTkLabel(c4, text=f"Ingresos perdidos de\nSpa: {self.ingresos_perdidos_spa}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        ctk.CTkLabel(c4, text=f"clientes perdidos de\nSpa: {self.dicc_visitantes_rechazados["Spa"]}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        

        ctk.CTkLabel(c4, text=f"Ingresos perdidos de\narea acuatica: {self.ingresos_perdidos_acuatica}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        ctk.CTkLabel(c4, text=f"clientes perdidos de\narea acuatica: {self.dicc_visitantes_rechazados["Acuatica"]}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        

        ctk.CTkLabel(c4, text=f"Ingresos perdidos de\nshows: {self.ingresos_perdidos_shows}", 
                         font=("Arial", 12), 
                         text_color="white").pack( padx=20, pady=5)
        

        # Sugerencias 
        c5=card(1, 1, "SUGERENCIAS")
        sugerencias=[]
        if self.visitantes_rechazados > total_atendidos * 0.2:
            sugerencias.append("Tasa de rechazo >20%. Considera ampliar capacidad.")


        if len(self.listiempo_en_maquinas_rotas) > int(self.recursos_gim["maquinas"]) * 0.3:
            sugerencias.append("Alta tasa de avería en máquinas del gimnasio.")


        if self.ingresos_musica < ingreso_total * 0.05:
            sugerencias.append("Musica genera <5% de ingresos. Revisa precios/shows.")

        
        if not sugerencias:
            sugerencias.append("Operación sin alertas graves")

            
        for texto_sugerencia in sugerencias:
            ctk.CTkLabel(c5, text=f"• {texto_sugerencia}", font=("Arial", 11), 
                         text_color="white", wraplength=220, justify="left").pack(anchor="w", padx=15, pady=5)

        # balancr final
        c6=card(1, 2, "BALANCE FINAL")
        color_balance="#1B5E20" if resultado_neto >= 0 else "#B71C1C"
        c6.configure(fg_color=color_balance)
        
        datos_balance=[
            ("Ingresos Totales", f"${ingreso_total:,.2f}", "#81C784"),
            ("Egresos Totales", f"${egreso_total:,.2f}", "#EF9A9A"),
            ("Resultado Neto", f"${resultado_neto:,.2f}", "#FFFFFF")]
        
        for titulo, valor, color in datos_balance:
            ctk.CTkLabel(c6, text=titulo, font=("Arial", 13), text_color="white").pack(pady=(8, 0))
            ctk.CTkLabel(c6, text=valor, font=("Arial", 18, "bold"), text_color=color).pack()

    def Graficar_ingresos(self):
        if not self.resultados_totales:
            return
        
        dias=[resultado[0] for resultado in self.resultados_totales]
        ingresos_gim=[resultado[2] for resultado in self.resultados_totales]
        ingresos_spa=[resultado[3] for resultado in self.resultados_totales]
        ingresos_acu=[resultado[4] for resultado in self.resultados_totales]
        ingresos_mus=[resultado[5] for resultado in self.resultados_totales]

  
        plt.figure(figsize=(10, 5))
        plt.style.use('seaborn-v0_8-darkgrid') 


        plt.plot(dias, ingresos_gim, label="Gimnasio", marker="o", linestyle="-", linewidth=1.5)
        plt.plot(dias, ingresos_spa, label="Spa/Jacuzzi", marker="s", linestyle="-", linewidth=1.5)
        plt.plot(dias, ingresos_acu, label="Área Acuatica", marker="^", linestyle="-", linewidth=1.5)
        plt.plot(dias, ingresos_mus, label="Musica/Shows", marker="v", linestyle="-", linewidth=1.5)

        plt.title("Ingresos Diarios por Área", fontsize=14, fontweight="bold")
        plt.xlabel("Día de Simulación")
        plt.ylabel("Ingresos ($)")
        plt.legend(loc="upper left")
        plt.tight_layout()
        
        plt.show()


    def Obtener_Evento(self, nombre_tabla, aleatorio):
        tabla=self.tablas_maestras.get(nombre_tabla)

        if tabla is None: 
            return None
        
        for i, (inferior, superior) in enumerate(tabla["rangos"]):
            if inferior <= aleatorio <= superior:
                return tabla["eventos"][i]
            
        return tabla["eventos"][-1]

    def calcular_acumulada(self, probs):
        acumulada=[]
        suma_parcial=0.0
        
        for probabilidad in probs:
            suma_parcial += probabilidad
            acumulada.append(round(suma_parcial, 4))
            
        return acumulada

    def calcular_rangos(self, acum):
        rangos=[]
        limite_anterior=0.0
        for prob in acum:
            rangos.append((limite_anterior, prob))
            limite_anterior=prob
        return rangos


    def Comprobar_probabilidades(self, probs, contenedor=""):
        suma=sum(probs)
        if round(suma, 4) != 1.0:
            CTkMessagebox(title="Error",
                          message=f"Las probabilidades no suman 1.0 en '{contenedor}'.\nSuman {suma:.4f}",
                          icon="cancel")
            return False
        return True

    def Procesar_textbox(self, widget, nombre=""):
        contenido=widget.get("1.0", "end-1c")
        eventos, probs=[], []
        for i, linea in enumerate(contenido.split("\n")):
            linea=linea.strip()
            if not linea: continue
            if "," in linea:
                try:
                    partes=[p.strip() for p in linea.split(",")]
                    if len(partes)== 2:
                        ev=partes[0]
                        try: ev=int(ev)
                        except ValueError:
                            try: ev=float(ev)
                            except ValueError: pass
                        eventos.append(ev)
                        probs.append(float(partes[1]))
                    elif len(partes)== 3:
                        ev=partes[0]
                        eventos.append((ev, float(partes[1])))
                        probs.append(float(partes[2]))
                except ValueError:
                    print(f"Procesar_textbox: error línea {i+1} en '{nombre}'")
            else:
                eventos.append(linea)
        if not probs:
            return (tuple(eventos), tuple())
        if self.Comprobar_probabilidades(probs, nombre):
            return (tuple(eventos), tuple(probs))
        return None

    def Insertar_datos_txtbox(self, eventos, probs, txtbox):
        txtbox.delete("0.0", "end")
        txt=""
        for i, evento in enumerate(eventos):
            texto=str(evento)
            if "(" in texto:
                texto=texto.strip("() '").replace("'", "")
            if probs and i < len(probs):
                txt+=f"{texto} , {probs[i]}\n"
            else:
                txt += f"{texto}\n"
        txtbox.insert("0.0", txt)

 
    def Generar_aleatorios(self):
        import sys, importlib.util
        ruta_gen=Path(__file__).resolve().parent / "Generador"
        if str(ruta_gen) not in sys.path:
            sys.path.insert(0, str(ruta_gen))
        try:
            spec=importlib.util.spec_from_file_location("mod_gen", ruta_gen / "main.py")
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            gen=mod.InterfazPrincipal()
            gen.Iniciar(self.Ventana)
            self.Ventana.wait_window(gen.VentanaP)
            if gen.generados and gen.comprobados:
                self.leer_numeros_de_archivo()
            else:
                CTkMessagebox(title="Error",
                              message="Números no generados o no validados.", icon="cancel")
        except Exception as e:
            print(f"Error generador: {e}")

    def leer_numeros_de_archivo(self):
        self.Aleatoreos=[]
        ruta=Path(__file__).resolve().parent / "Generador" / "aleatorios.txt"
        try:
            if ruta.exists():
                with open(ruta) as f:
                    for linea in f:
                        linea=linea.strip()
                        if linea: self.Aleatoreos.append(float(linea))
                self.Mostrar_aleatorios()
        except Exception as e:
            print(f"Error leyendo aleatorios: {e}")

    def obtener_siguiente_aleatorio(self):
        if not self.Aleatoreos:
            self.Generar_aleatorios()
        aleatorio=self.Aleatoreos.pop(0) if self.Aleatoreos else 0.5
        
        return aleatorio
