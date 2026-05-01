import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Habitaciones:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Habitaciones")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)
        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)
        # DATOS
        self.datos_llegadas=[[0, 0.29],
                             [1, 0.30],
                             [2, 0.20],
                             [3, 0.21]]

        self.datos_tipo=[["Individual", 0.40],
                         ["Doble", 0.40],
                         ["Suite", 0.20]]

        self.datos_estancia=[[1, 0.25],
                             [2, 0.35],
                             [3, 0.25],
                             [4, 0.15]]
        
        self.reiniciar_llegadas=False
        self.reiniciar_tipo=False
        self.reiniciar_estancia=False

        # SCROLL
        self.frame_scroll=ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        # TITULO
        titulo=ctk.CTkLabel(self.frame_scroll, text="Simulación de habitaciones", text_color=COLOR_TEXTO, font=("Arial", 28, "bold", "italic"))
        titulo.pack(pady=20)
        # FRAME DATOS
        self.frame_datos=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry=180
        alto_entry=40

        ctk.CTkLabel(self.frame_datos, text="Cantidad de habitaciones:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))
        self.entry_habitaciones=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_habitaciones.grid(row=1, column=0, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.frame_datos, text="Costo de mantenimiento:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))
        self.entry_mantenimiento=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_mantenimiento.grid(row=1, column=1, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.frame_datos, text="Costo de limpieza por habitación:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))
        self.entry_limpieza=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_limpieza.grid(row=1, column=2, padx=20, pady=(0, 20))

        self.btn_simular=ctk.CTkButton(self.frame_datos,text="Simular", width=ancho_entry, height=alto_entry, fg_color="#D6C49E", text_color="#000000")
        self.btn_simular.grid(row=1, column=3, padx=20, pady=(0, 20))

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_ingresos=ctk.CTkLabel(self.frame_kpis, text="Ingresos Totales: $0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_ingresos.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_costos=ctk.CTkLabel(self.frame_kpis, text="Costos Totales: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_costos.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_ganancias=ctk.CTkLabel(self.frame_kpis, text="Ganancia Neta: $0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_ganancias.grid(row=0, column=2, padx=40, pady=30)

        # BOTONES
        self.frame_botones=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_botones.pack(fill="x", padx=20, pady=20)
        botones=["Cargar Datos",
                 "Limpiar",
                 "Valores Bajos",
                 "Valores Medios",
                 "Valores Altos"]

        for i, texto in enumerate(botones):
            boton=ctk.CTkButton(self.frame_botones, text=texto, width=180, height=40, fg_color="#FFBF42", text_color="#000000")
            boton.grid(row=0, column=i, padx=20, pady=30)

        # FRAME PROBABILIDADES
        self.frame_probabilidades=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_probabilidades.pack(fill="x", padx=20, pady=20)

        titulo_prob=ctk.CTkLabel(self.frame_probabilidades, text="TABLAS DE PROBABILIDAD", text_color=COLOR_TEXTO, font=("Arial", 22, "bold"))
        titulo_prob.pack(pady=20)

        self.contenedor=ctk.CTkFrame(self.frame_probabilidades, fg_color="transparent")
        self.contenedor.pack(padx=20, pady=20)

        self.crear_tabla("Llegadas por día", "Clientes", self.datos_llegadas, 0)

        self.crear_tabla("Tipo de habitación", "Tipo", self.datos_tipo, 1)

        self.crear_tabla("Duración de estancia", "Noches", self.datos_estancia, 2)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)

        tabla_resultados=[["Día", "Llegadas", "Habitaciones", "Ingresos", "Costos", "Ganancia"],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""],
                          ["", "", "", "", "", ""]]

        self.tabla_simulacion=CTkTable(self.frame_resultados, values=tabla_resultados)
        self.tabla_simulacion.pack(padx=20, pady=20)
        self.ventana.mainloop()

    # CREAR TABLAS
    def crear_tabla(self, titulo, encabezado, datos, fila):
        frame=ctk.CTkFrame(self.contenedor)
        frame.grid(row=fila, column=0, padx=20, pady=20)

        ctk.CTkLabel(frame, text=titulo, text_color=COLOR_TEXTO, font=("Arial", 16, "bold")).pack(pady=10)
        entrada1=ctk.CTkEntry(frame, width=150, placeholder_text=encabezado)
        entrada1.pack(pady=5)
        entrada2=ctk.CTkEntry(frame, width=150, placeholder_text="Probabilidad")
        entrada2.pack(pady=5)

        boton=ctk.CTkButton(frame, text="Agregar", command=lambda: self.agregar_dato(entrada1, entrada2, datos, encabezado, frame))
        boton.pack(pady=10)

        tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
        tabla.pack(padx=10, pady=10)

        if encabezado=="Clientes":
            self.tabla_llegadas=tabla

        elif encabezado=="Tipo":
            self.tabla_tipo=tabla

        else:
            self.tabla_estancia=tabla

    # CALCULAR TABLA
    def calcular_tabla(self, datos, encabezado):
        tabla=[[encabezado, "Probabilidad", "Prob. Acumulada", "Rango"]]
        acumulada=0
        for i, fila in enumerate(datos):
            valor=fila[0]
            prob=fila[1]
            inicio=acumulada
            acumulada+=prob

            if i==0:
                rango=(f"0.0000 - {acumulada:.4f}")
            else:
                rango=(f"{inicio + 0.0001:.4f} - {acumulada:.4f}")

            tabla.append([valor, f"{prob:.4f}", f"{acumulada:.4f}", rango])

        return tabla

    # AGREGAR DATOS
    def agregar_dato(self, entrada1, entrada2, datos, encabezado, frame):
        try:
            valor=entrada1.get().strip()
            prob=entrada2.get().strip()

            if valor=="" or prob=="":
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            prob=float(prob)
            if prob<=0 or prob>1:
                messagebox.showerror("Error", "Probabilidad inválida")
                return

            try:
                valor=int(valor)
            except:
                pass

            suma=0
            for fila in datos:
                suma=suma + fila[1]

            suma=round(suma, 4)
            if suma==1:
                if encabezado=="Clientes":
                    if self.reiniciar_llegadas==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_llegadas=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_llegadas=False
                
                elif encabezado=="Tipo":
                    if self.reiniciar_tipo==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_tipo=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_tipo=False

                else:
                    if self.reiniciar_estancia==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_estancia=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_estancia=False

            for fila in datos:
                if fila[0]==valor:
                    messagebox.showerror("Error", "Ese valor ya existe")
                    return

            datos.append([valor, prob])

            nueva_suma=0
            for fila in datos:
                nueva_suma=nueva_suma + fila[1]
            nueva_suma=round(nueva_suma, 4)

            if nueva_suma>1:
                datos.pop()
                messagebox.showerror("Error", "La suma de probabilidades no puede superar 1")
                return

            try:
                datos.sort()
            except:
                pass

            if encabezado=="Clientes":
                self.tabla_llegadas.destroy()
            elif encabezado=="Tipo":
                self.tabla_tipo.destroy()
            else:
                self.tabla_estancia.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Clientes":
                self.tabla_llegadas=nueva_tabla
            elif encabezado=="Tipo":
                self.tabla_tipo=nueva_tabla
            else:
                self.tabla_estancia=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")

            if nueva_suma==1:
                messagebox.showinfo("Correcto", "La tabla ya suma 1")

        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")
        except Exception as error:
            messagebox.showerror("Error", str(error))


Habitaciones()