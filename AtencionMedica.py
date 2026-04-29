
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

        self.Main_frame=ctk.CTkFrame(self.Ventana,fg_color=self.color_Extra)
        self.Main_frame.place(
        relx=0.05,   
        rely=0.1,    
        relwidth=0.9, 
        relheight=0.9)

        self.Frame_tablas=ctk.CTkScrollableFrame(self.Main_frame)
        self.Frame_tablas.place(
        relx=0.05,   
        rely=0.3,    
        relwidth=0.9, 
        relheight=0.7)

        ctk.CTkLabel(self.Main_frame,text="Personal Medico",font=("arial",15,"bold"),text_color="black"
                     ).place(relx=.5,rely=.05,anchor=ctk.CENTER)
        
        self.ntry_doctor=ctk.CTkEntry(self.Main_frame)
        self.ntry_doctor.place(relx=.1,rely=.1,anchor=ctk.CENTER)
        
        self.ntry_enfer=ctk.CTkEntry(self.Main_frame)
        self.ntry_enfer.place(relx=.3,rely=.1,anchor=ctk.CENTER)

        ctk.CTkLabel(self.Main_frame,text="Inventario Medico",font=("arial",15,"bold"),text_color="black"
                     ).place(relx=.5,rely=.15,anchor=ctk.CENTER)

        self.ntry_kithigiene=ctk.CTkEntry(self.Main_frame)
        self.ntry_kithigiene.place(relx=.1,rely=.2,anchor=ctk.CENTER)

        self.ntry_kitcuracion=ctk.CTkEntry(self.Main_frame)
        self.ntry_kitcuracion.place(relx=.3,rely=.2,anchor=ctk.CENTER)

        self.ntry_kitsutura=ctk.CTkEntry(self.Main_frame)
        self.ntry_kitsutura.place(relx=.5,rely=.2,anchor=ctk.CENTER)

        self.ntry_kitfarmaco=ctk.CTkEntry(self.Main_frame)
        self.ntry_kitfarmaco.place(relx=.7,rely=.2,anchor=ctk.CENTER)
        self.Mostrar_tablas()
        
        self.Ventana.mainloop()

    def Mostrar_tablas(self):
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
        


        self.btnLlegada = ctk.CTkButton(self.Frame_tablas,text="Guardar" )
        self.btnLlegada.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="n")



        label2 = ctk.CTkLabel(self.Frame_tablas, text="Tipo de caso", font=("Arial", 16))
        label2.grid(row=0, column=1, padx=10, pady=(0, 0), sticky="n")

        self.TxtTipocaso= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTipocaso.grid(row=1, column=1, padx=10, pady=(2, 5), sticky="n")

        self.btnTipocaso = ctk.CTkButton(self.Frame_tablas,text="Guardar" )
        self.btnTipocaso.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="n")



        label3 = ctk.CTkLabel(self.Frame_tablas, text="Tiempo en atender", font=("Arial", 16))
        label3.grid(row=0, column=2, padx=10, pady=(0, 0), sticky="n")

        self.TxtTiempoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTiempoAtencion.grid(row=1, column=2, padx=10, pady=(2, 5), sticky="n")

        self.btnTiempoAtencion = ctk.CTkButton(self.Frame_tablas,text="Guardar" )
        self.btnTiempoAtencion.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="n")



        label4 = ctk.CTkLabel(self.Frame_tablas, text="Tipo de atencion", font=("Arial", 16))
        label4.grid(row=0, column=3, padx=10, pady=(0, 0), sticky="n")

        self.TxtTipoAtencion= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtTipoAtencion.grid(row=1, column=3, padx=10, pady=(2, 5), sticky="n")

        self.btnTipoAtencion=ctk.CTkButton(self.Frame_tablas,text="Guardar" )
        self.btnTipoAtencion.grid(row=2, column=3, padx=10, pady=(0, 10), sticky="n")



        label5 = ctk.CTkLabel(self.Frame_tablas, text="Tiepo de respuesta en\nemergencia", font=("Arial", 16))
        label5.grid(row=3, column=0, padx=10, pady=(0, 0), sticky="n")

        self.TxtEmergencia= ctk.CTkTextbox(self.Frame_tablas,
                                             font=("Arial", 15),
                                             width=ancho_fijo, height=alto_fijo)

        self.TxtEmergencia.grid(row=4, column=0, padx=10, pady=(2, 5), sticky="n")

        self.btnEmergencia= ctk.CTkButton(self.Frame_tablas,text="Guardar" )
        self.btnEmergencia.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="n")



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
                
        return lista_eventos, lista_probabilidades
