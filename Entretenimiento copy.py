
import customtkinter as ctk
class Area_Entretenimiento():
    def Iniciar(self,Dias_simulacion):
        self.color_fondo = "#5D4037"
        self.color_hover = "#3E2723"
        self.color_texto = "#FFFFFF"
        self.color_Extra = "#D7CCC8"

        self.Dias_simulacion = Dias_simulacion
        self.Ventana=ctk.CTk()
        self.Ventana.title("Simulacion de entretenimiento")
        self.Ventana.geometry("1000x700")

        ctk.CTkLabel(self.Ventana,text="AREA DE ENTRETENIMIENTO",font=("arial",20,"bold"),text_color=self.color_texto
                     ).place(relx=.5,rely=.05,anchor=ctk.CENTER)

        self.Main_frame=ctk.CTkFrame(self.Ventana,fg_color=self.color_Extra)
        self.Main_frame.place(
        relx=0.05,   
        rely=0.1,    
        relwidth=0.9, 
        relheight=0.9)

        self.Frame_tablas=ctk.CTkScrollableFrame(self.Main_frame)
        self.Frame_tablas.place(
        relx=0.05,   
        rely=0.2,    
        relwidth=0.9, 
        relheight=0.8)

        #ctk.CTkLabel(self.Main_frame,text="Personal Medico",font=("arial",15,"bold"),text_color="black").place(relx=.5,rely=.05,anchor=ctk.CENTER)
        
        btn_Area_gimnacio=ctk.CTkButton(self.Main_frame,text="Gimnacio",command=self.Mostrar_tablas_gimnacio)
        btn_Area_gimnacio.place(relx=.1,rely=.1,anchor=ctk.CENTER)

        btn_Area_spa=ctk.CTkButton(self.Main_frame,text="Spa/jacussi")
        btn_Area_spa.place(relx=.3,rely=.1,anchor=ctk.CENTER)

        btn_Area_piscina=ctk.CTkButton(self.Main_frame,text="Piscina")
        btn_Area_piscina.place(relx=.5,rely=.1,anchor=ctk.CENTER)

        btn_Area_depacuaticos=ctk.CTkButton(self.Main_frame,text="Deportes Acuáticos")
        btn_Area_depacuaticos.place(relx=.7,rely=.1,anchor=ctk.CENTER)

        btn_Area_bar=ctk.CTkButton(self.Main_frame,text="Música en vivo / Bar ")
        btn_Area_bar.place(relx=.9,rely=.1,anchor=ctk.CENTER)
        

        #ctk.CTkLabel(self.Main_frame,text="Inventario Medico",font=("arial",15,"bold"),text_color="black").place(relx=.5,rely=.15,anchor=ctk.CENTER)

        
        self.Ventana.mainloop()

    def Mostrar_tablas_gimnacio(self):
        self.Limpiar_frame(self.Frame_tablas)
        ancho_fijo = 100
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
        # 1. Obtener todo el texto del widget
        # "1.0" es el inicio, "end-1c" es el final menos el último salto de línea
        contenido = textbox_widget.get("1.0", "end-1c")
        
        lineas = contenido.split("\n")
        
        lista_eventos = []
        lista_probabilidades = []
        
        for i, linea in enumerate(lineas):
            linea = linea.strip() # Limpiar espacios en blanco
            
            if not linea: # Saltar líneas vacías
                continue
                
            if "," in linea:
                try:
                    # Separar por la coma
                    partes = linea.split(",")
                    
                    # Convertimos a float (o int según necesites)
                    evento = float(partes[0].strip())
                    probabilidad = float(partes[1].strip())
                    
                    lista_eventos.append(evento)
                    lista_probabilidades.append(probabilidad)
                    
                except ValueError:
                    print(f"Error en línea {i+1}: Formato numérico incorrecto en '{linea}'")
            else:
                print(f"Error en línea {i+1}: Falta la coma separadora en '{linea}'")
        print(lista_eventos,lista_probabilidades)        
        return lista_eventos, lista_probabilidades

        


        