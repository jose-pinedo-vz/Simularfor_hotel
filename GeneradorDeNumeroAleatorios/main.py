"""
Base sentral de la interfaz, si le mueven que sea con cuidado
"""
#-----------------------------------------------------------------------------------------------------
#imports de los metodos echos por mi (bladimir)
from GeneradorDeNumeroAleatorios.GeneracionMixto import GeneraMixto
from GeneradorDeNumeroAleatorios.PruebaEstSeries import Prueba_Series
from GeneradorDeNumeroAleatorios.PruebaEstPoker import Prueba_Del_Poker
from GeneradorDeNumeroAleatorios.PruebaEstCorridas import Prueba_corridas
from GeneradorDeNumeroAleatorios.PruebaEstCorridasProm import Prueba_corridas_Promedio
"NOTA: Modifique la funcion  def Mixto(self): "
#-----------------------------------------------------------------------------------------------------




import customtkinter as ctk


class InterfazPrincipal:
    def __init__(self):
        self.VentanaP = ctk.CTk()
        self.VentanaP.title("Unidad 2 simulacion")
        self.Fuente=""
        try: self.VentanaP.state('zoomed')
        except: self.VentanaP.attributes('-zoomed', True)

        self.CuadradosMedios = ctk.CTkButton(self.VentanaP, text="Cuadrados medios",
                                             command=lambda: self.caudrados_medios())
        self.CuadradosMedios.pack(pady=20, padx=20)

        self.CongruencialM = ctk.CTkButton(self.VentanaP, text="Congruencial mixto",
                                           command=lambda: self.Mixto())
        self.CongruencialM.pack(pady=20, padx=20)

        self.CongruencialMul = ctk.CTkButton(self.VentanaP, text="Congruencial multiplicativo",
                                             command=lambda: self.multiplicativo())
        self.CongruencialMul.pack(pady=20, padx=20)

        # self.LineasDeEspera = ctk.CTkButton(self.VentanaP, text="Lineas de espra",
        #                                     command=lambda: self.Esperas())
        # self.LineasDeEspera.pack(pady=20, padx=20)

        # self.TeoriaIn = ctk.CTkButton(self.VentanaP, text="Teoria de inventarios")
        # self.TeoriaIn.pack(pady=20, padx=20)
                                  

        self.VentanaP.mainloop()


    def limpiar_pantalla_grande(self) -> None:
        """
        Descripcion:
            este bloque limpia los elementos del centro del frame
        """
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def FrameDeLosGeneradores(self) -> None:
        """
        Descripcion: 
            El objetivo de esta funcion es que contengra 2 frames, por un lado los metodos de
            comprogacion y por el otro como tal lo que se nesesita o el metodo de generacion.

            De esta forma no rescribo la funcion de los frames y podemos usar nada mas una ventana
            y limpiamos el frame central y podemos reultilisar el frame de los metodos
            de comprobacion

        return: 
            no retorna nada

        atributos: 
            y no ocupa nada, es independiendte 
        """

        self.ventana_genera = ctk.CTkToplevel()
        self.ventana_genera.title("METODOS DE GENERACION")
            
        try: self.ventana_genera.state('zoomed')
        except: self.ventana_genera.attributes('-zoomed', True)

        self.ventana_genera.grid_columnconfigure(1, weight=1) 
        self.ventana_genera.grid_rowconfigure(0, weight=1)

        self.frame_menu = ctk.CTkFrame(self.ventana_genera, width=200, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frame_menu.grid_propagate(False) 

        #Botones del menu:

        labelXd = ctk.CTkLabel(self.frame_menu, text="Evaluar con: ").pack(padx=10, pady=10)

        self.corridas = ctk.CTkButton(self.frame_menu, text="Corridas arriba y abajo",command=lambda: self.Llama_Prueba_Corridas())
        self.corridas.pack(pady=20, padx=20)

        self.corridasPromedio = ctk.CTkButton(self.frame_menu, text="Corridas arriba y abajo del promedio",command=lambda: self.Llama_Prueba_Corrida_Prom())
        self.corridasPromedio.pack(pady=20, padx=20)

        self.Distancia = ctk.CTkButton(self.frame_menu, text="Distancia")
        self.Distancia.pack(pady=20, padx=20)

        self.Poker = ctk.CTkButton(self.frame_menu, text="Poker",command=lambda: self.Llama_Prueba_Poker())
        self.Poker.pack(pady=20, padx=20)

        self.Kolmogorov = ctk.CTkButton(self.frame_menu, text="Kolmogorov")
        self.Kolmogorov.pack(pady=20, padx=20)

        self.Frecuencail = ctk.CTkButton(self.frame_menu, text="Frecuencail", command=lambda: self.FrecuencailLlamada())
        self.Frecuencail.pack(pady=20, padx=20)

        self.Series = ctk.CTkButton(self.frame_menu, text="Series",command=lambda: self.Llama_Prueba_Series())
        self.Series.pack(pady=20, padx=20)




        self.frame_contenido = ctk.CTkFrame(self.ventana_genera, fg_color="gray20")
        self.frame_contenido.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    def caudrados_medios(self):
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()
        self.Fuente="Cuadrados medios"

        lb_central = ctk.CTkLabel(self.frame_contenido, text=self.Fuente,
                                  font=("Arial", 18))
        lb_central.place(x=50, y=50)

        self.CantIteraciones = ctk.CTkEntry(self.frame_contenido, placeholder_text="Iteraciones",
                                            width=400, height=120)
        self.CantIteraciones.place(relx=0.2, rely=0.2, relwidth=0.25, anchor="center")

        self.Semilla = ctk.CTkEntry(self.frame_contenido, placeholder_text="Semilla",
                                    width=400, height=120)
        self.Semilla.place(relx=0.5, rely=0.2, relwidth=0.25, anchor="center")

        self.p1 = ctk.CTkTextbox(self.frame_contenido, font=("Consolas", 13))
        self.p1.place(relx=0.05, rely=0.55, relwidth=0.60, relheight=0.4)


        self.p3 = ctk.CTkTextbox(self.frame_contenido, font=("Consolas", 13))
        self.p3.place(relx=0.75, rely=0.55, relwidth=0.12, relheight=0.4)
                      
        def llamarCuadrados():
            semilla = self.Semilla.get()
            nf = int(self.CantIteraciones.get())
            from . import Cuadradosmedios

            self.lista, resultado_cadena = Cuadradosmedios.cuadradosMedios(semilla, nf)

            self.p1.insert("0.0", resultado_cadena)
            self.p1.configure(state="disabled") 


            texto_lista = "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(self.lista)])
            self.p3.insert("0.0", texto_lista)
            self.p3.configure(state="disabled") 

        boton = ctk.CTkButton(self.frame_contenido, text="Generar",  width=400, height=120,
                              command= llamarCuadrados)
        
        boton.place(relx=0.8, rely=0.2, relwidth=0.25, anchor="center")

    def Mixto(self):
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()
        self.Fuente="Cuadrados medios"

        lista_X0=["11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35", "37", "39", "41", "43", "45", "47", "49"]

        lista_M=["16", "32", "64", "128", "256", "512", "1024", "2048", "4096", "8192", "16384", "32768", "65536", "131072", "262144", "524288", "1048576", "2097152", "4194304", "8388608"]

        lista_A=["13", "17", "21", "25", "29", "33", "37", "41", "45", "49", "53", "57", "61", "65", "69", "73", "77", "81", "85", "89"]

        lista_C=["13", "21", "29", "37", "45", "53", "61", "69", "77", "85", "93", "101", "109", "117", "125", "133", "141", "149", "157", "165"]

        
        lb_central = ctk.CTkLabel(self.frame_contenido, text="Congruencial mixto",
                                  font=("Arial", 20))
        lb_central.place(relx=.5, rely=.05, anchor=ctk.CENTER)
        
        #___________________________________________________________________________________________________________________________#

        lb_1=ctk.CTkLabel(self.frame_contenido, 
                          text="Semilla X0 (X0>0 y de preferencia impar):",
                          font=("Arial", 15))
        lb_1.place(relx=1/5, rely=.15, anchor=ctk.CENTER)

        self.entry_X0=ctk.CTkEntry(self.frame_contenido)
        self.entry_X0.place(relx=2/5, rely=.15, anchor=ctk.CENTER)

        combo_X0=ctk.CTkComboBox(self.frame_contenido, 
                                values=lista_X0,
                                width=200,
                                state="readonly",
                                command=lambda v: (self.entry_X0.delete(0,"end"), self.entry_X0.insert(0, v)))
        combo_X0.place(relx=3/5, rely=.15, anchor=ctk.CENTER)
        
        #___________________________________________________________________________________________________________________________#

        lb_2=ctk.CTkLabel(self.frame_contenido,
                          text="Modulo m (m= 2^d) y (m> Xo, m>a, m>c):",
                          font=("Arial", 15))
        lb_2.place(relx=1/5, rely=.2, anchor=ctk.CENTER)

        self.entry_M=ctk.CTkEntry(self.frame_contenido)
        self.entry_M.place(relx=2/5, rely=.2, anchor=ctk.CENTER)

        combo_M=ctk.CTkComboBox(self.frame_contenido, 
                                values=lista_M,
                                width=200,
                                state="readonly",
                                command=lambda v: (self.entry_M.delete(0,"end"), self.entry_M.insert(0, v)))
        combo_M.place(relx=3/5, rely=.2, anchor=ctk.CENTER)

        #___________________________________________________________________________________________________________________________#

        lb_3=ctk.CTkLabel(self.frame_contenido,
                          text="Multiplicador a ((a-1)mod4 == 0):",
                          font=("Arial", 15))
        lb_3.place(relx=1/5, rely=.25, anchor=ctk.CENTER)

        self.entry_A=ctk.CTkEntry(self.frame_contenido)
        self.entry_A.place(relx=2/5, rely=.25, anchor=ctk.CENTER)

        combo_A=ctk.CTkComboBox(self.frame_contenido, 
                                values=lista_A,
                                width=200,state="readonly",
                                command=lambda v: (self.entry_A.delete(0,"end"), self.entry_A.insert(0, v)))
        combo_A.place(relx=3/5, rely=.25, anchor=ctk.CENTER)

        #___________________________________________________________________________________________________________________________#
    
        lb_4=ctk.CTkLabel(self.frame_contenido,
                          text="Constante aditiva c ((c)mod8 == 5):",
                          font=("Arial", 15))
        lb_4.place(relx=1/5, rely=.3, anchor=ctk.CENTER)

        self.entry_C=ctk.CTkEntry(self.frame_contenido)
        self.entry_C.place(relx=2/5, rely=.3, anchor=ctk.CENTER)

        combo_C=ctk.CTkComboBox(self.frame_contenido, 
                                values=lista_C,
                                width=200,
                                state="readonly",
                                command=lambda v: (self.entry_C.delete(0,"end"), self.entry_C.insert(0, v)))
        combo_C.place(relx=3/5, rely=.3, anchor=ctk.CENTER)

        #___________________________________________________________________________________________________________________________#

        combo_X0.set("Sugerencias de valor"),combo_M.set("Sugerencias de valor"),combo_A.set("Sugerencias de valor"),combo_C.set("Sugerencias de valor")

        #___________________________________________________________________________________________________________________________#

        self.box_numeros=ctk.CTkTextbox(self.frame_contenido,width=250,height=500,font=("Consolas", 12))
        self.box_numeros.place(relx=4/5,rely=.35,anchor=ctk.CENTER)

        #___________________________________________________________________________________________________________________________#
        def TomarValores(band):
            try:
                X0=int(self.entry_X0.get())
                M=int(self.entry_M.get())
                A=int(self.entry_A.get())
                C=int(self.entry_C.get())
            except ValueError:
                self.PopUp("Dato incorrecto","Debe ingresar un valor numerico")
            else:
                Gen=GeneraMixto()
                self.box_numeros.insert("end","GENERANDO NUMEROS...\n")

                if band:
                    self.lista=Gen.Recibe_valores(X0,M,A,C)
                else:
                    self.lista=Gen.Genera(X0,M,A,C)
                if self.lista!=[]:
                    for num in self.lista:
                        self.box_numeros.insert("end",str(num)+"\n")
                else:
                    self.box_numeros.insert("end","OUCRRIO UN PROBLEMA!\n")

        lb_5=ctk.CTkLabel(self.frame_contenido,
                          text="Generar con los valores dados:",
                          font=("Arial", 15))
        lb_5.place(relx=1/5, rely=.4, anchor=ctk.CENTER)

        btn=ctk.CTkButton(self.frame_contenido, text="COMPROBAR", command=lambda:TomarValores(True),fg_color="green")
        btn.place(relx=2/5,rely=.4,anchor=ctk.CENTER)

        btn2=ctk.CTkButton(self.frame_contenido, text="SIN RESTRICCIONES!",command=lambda:TomarValores(False),fg_color="red")
        btn2.place(relx=3/5,rely=.4,anchor=ctk.CENTER)
        
        

    def multiplicativo(self):
        v1 = "3 11 13 14 21 23 24 27 53 59 64 69 77 83 91 113 117 123 131 133 141 147 163 171 173 179 181 187 189 197"
        self.FrameDeLosGeneradores()
        self.limpiar_pantalla_grande()
        self.Fuente = "Congruencial multiplicativo"

        # Título
        lb_central = ctk.CTkLabel(self.frame_contenido, text=self.Fuente, font=("Arial", 22, "bold"))
        lb_central.pack(pady=10)

        # Contenedor Superior (Arreglo)
        frame_top = ctk.CTkFrame(self.frame_contenido, fg_color="transparent")
        frame_top.pack(fill="x", padx=20, pady=5)
        
        self.arreglo = ctk.CTkTextbox(frame_top, height=100, font=("Consolas", 13))
        self.arreglo.pack(fill="x", pady=5)
        self.arreglo.insert("0.0", f"{v1}")

        # Contenedor Controles Arreglo
        frame_controls_arr = ctk.CTkFrame(frame_top, fg_color="transparent")
        frame_controls_arr.pack(fill="x", pady=5)

        self.it = ctk.CTkEntry(frame_controls_arr, placeholder_text="Cantidad: ", width=150)
        self.it.pack(side="left", padx=5)
        self.liminf = ctk.CTkEntry(frame_controls_arr, placeholder_text="limite inferior: ", width=150)
        self.liminf.pack(side="left", padx=5)
        self.limsub = ctk.CTkEntry(frame_controls_arr, placeholder_text="limite superior: ", width=150)
        self.limsub.pack(side="left", padx=5)
        
        boton2 = ctk.CTkButton(frame_controls_arr, text="Nuevo arreglo", command=lambda: arreglo())
        boton2.pack(side="left", padx=10)

        # Contenedor Generación
        frame_gen = ctk.CTkFrame(self.frame_contenido, fg_color="transparent")
        frame_gen.pack(fill="x", padx=20, pady=10)

        self.CantIteraciones = ctk.CTkEntry(frame_gen, placeholder_text="Cantidad de aleatorios")
        self.CantIteraciones.pack(side="left", padx=5, expand=True, fill="x")
        self.Semilla = ctk.CTkEntry(frame_gen, placeholder_text="Semilla")
        self.Semilla.pack(side="left", padx=5, expand=True, fill="x")
        
        boton = ctk.CTkButton(frame_gen, text="Generar", command=lambda: llamarCuadrados())
        boton.pack(side="left", padx=5)

        # Contenedor Resultados
        frame_res = ctk.CTkFrame(self.frame_contenido, fg_color="transparent")
        frame_res.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.p1 = ctk.CTkTextbox(frame_res, font=("Consolas", 13))
        self.p1.pack(side="left", fill="both", expand=True, padx=5)
        self.p2 = ctk.CTkTextbox(frame_res, font=("Consolas", 13))
        self.p2.pack(side="left", fill="both", expand=True, padx=5)
        self.p3 = ctk.CTkTextbox(frame_res, font=("Consolas", 13), width=150)
        self.p3.pack(side="left", fill="y", padx=5)

        # --- FUNCIONES ---
        def llamarCuadrados():
            semilla = self.Semilla.get()
            try:
                itera = int(self.CantIteraciones.get())
                from . import congruencialMultiplicativo
                v1 = self.arreglo.get("0.0", "end")
                v2 = v1.split()
                cadena, self.lista, cadena2 = congruencialMultiplicativo.congruencial(semilla, itera, v2)
                self.p1.insert("0.0", cadena); self.p1.configure(state="disabled") 
                self.p2.insert("0.0", cadena2); self.p2.configure(state="disabled") 
                texto_lista = "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(self.lista)])
                self.p3.insert("0.0", texto_lista); self.p3.configure(state="disabled") 
            except ValueError:
                from tkinter import messagebox
                messagebox.showwarning("Error", "Asegúrate de ingresar números válidos")

        def arreglo():
            import random
            try:
                inf = int(self.liminf.get()); sub = int(self.limsub.get()); cant = int(self.it.get())
                lista = []
                for i in range(cant + 1):
                    num = random.randint(inf, sub)
                    if num not in lista: lista.append(num)
                lista.sort()
                v1 = " ".join(str(n) for n in lista)
                self.arreglo.delete("0.0", "end"); self.arreglo.insert("0.0", v1)   
            except:
                from tkinter import messagebox
                messagebox.showwarning("Atención", "ingrese correctamente los datos")

        

    # def Esperas(self):
    #     import LIneasUI 
    #     LIneasUI.ventana()

    def FrecuencailLlamada(self):
        from . import frecuacia

        frecuacia.frecuacual(self.lista)

    def Llama_Prueba_Series(self):
        prueba=Prueba_Series()
        prueba.Ventana(self.lista)
    
    def Llama_Prueba_Poker(self):
        prueba=Prueba_Del_Poker()
        prueba.Ventana(self.lista)

    def Llama_Prueba_Corridas(self):
        prueba=Prueba_corridas()
        prueba.Ventana(self.lista)

    def Llama_Prueba_Corrida_Prom(self):
        prueba=Prueba_corridas_Promedio()
        prueba.Ventana(self.lista)

    def PopUp(self,titulo,contenido):
        self.Emergente= ctk.CTkToplevel()
        self.Emergente.title("ATENCIÓN")
        self.Emergente.geometry("500x500")
        self.Emergente.grab_set()

        lblTitulo=ctk.CTkLabel(self.Emergente,text=titulo,font=("Arial",20,"bold"))
        lblTitulo.place(relx=.5,rely=.1,anchor=ctk.CENTER)

        lblContenido=ctk.CTkLabel(self.Emergente,text=contenido,font=("Arial",15,"bold"))
        lblContenido.place(relx=.5,rely=.3,anchor=ctk.CENTER)

        continuar=ctk.CTkButton(self.Emergente, text="Continuar",
                                command=self.Emergente.destroy)
        continuar.place(relx=.5,rely=.6,anchor=ctk.CENTER)
       





def llamarVentanaAleatorios():
    obj = InterfazPrincipal()