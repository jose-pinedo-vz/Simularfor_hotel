import customtkinter as ctk
from CTkTable import CTkTable
from tkinter import messagebox

COLOR_FONDO = "#5D4037"
COLOR_TEXTO = "#FFFFFF"
COLOR_CONTORNO = "#4281FF"

class Marketing:
    def __init__(self):
        self.ventana=ctk.CTk()
        self.ventana.title("Área de Marketing")
        self.ventana.geometry("1400x750")
        self.ventana.configure(fg_color=COLOR_FONDO)
        try:
            self.ventana.state("zoomed")
        except:
            self.ventana.attributes("-zoomed", True)

        self.datos_leads=[[0, 0.10],
                          [5, 0.20],
                          [10, 0.30],
                          [15, 0.25],
                          [20, 0.15]]

        self.datos_conversion=[[1, 0.20],
                               [2, 0.30],
                               [3, 0.25],
                               [4, 0.15],
                               [5, 0.10]]

        self.datos_impacto=[["Bajo", 0.30],
                            ["Medio", 0.50],
                            ["Alto", 0.20]]

        self.reiniciar_leads=False
        self.reiniciar_conversion=False
        self.reiniciar_impacto=False

        self.frame_scroll=ctk.CTkScrollableFrame(self.ventana)
        self.frame_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        titulo=ctk.CTkLabel(self.frame_scroll, text="Simulación de marketing", text_color=COLOR_TEXTO, font=("Arial", 28, "bold"))
        titulo.pack(pady=20)

        self.frame_datos=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_datos.pack(fill="x", padx=20, pady=20)

        ancho_entry=220
        alto_entry=40

        ctk.CTkLabel(self.frame_datos, text="Presupuesto mensual:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=0, padx=20, pady=(20, 5))
        self.entry_presupuesto=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_presupuesto.grid(row=1, column=0, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.frame_datos, text="Cantidad de campañas:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=1, padx=20, pady=(20, 5))
        self.entry_campanas=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_campanas.grid(row=1, column=1, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.frame_datos, text="Costo por anuncio:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=2, padx=20, pady=(20, 5))
        self.entry_anuncio=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_anuncio.grid(row=1, column=2, padx=20, pady=(0, 20))
        ctk.CTkLabel(self.frame_datos, text="Personal disponible:", text_color=COLOR_TEXTO, font=("Arial", 16)).grid(row=0, column=3, padx=20, pady=(20, 5))
        self.entry_personal=ctk.CTkEntry(self.frame_datos, width=ancho_entry, height=alto_entry)
        self.entry_personal.grid(row=1, column=3, padx=20, pady=(0, 20))
        self.btn_simular=ctk.CTkButton(self.frame_datos, text="Simular", width=ancho_entry, height=alto_entry, fg_color="#D6C49E", text_color="#000000")
        self.btn_simular.grid(row=1, column=4, padx=20, pady=(0, 20))

        # KPIS
        self.frame_kpis=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_kpis.pack(fill="x", padx=20, pady=20)

        self.lbl_leads=ctk.CTkLabel(self.frame_kpis, text="Leads Totales: 0", text_color="#00FF99", font=("Arial", 18, "bold"))
        self.lbl_leads.grid(row=0, column=0, padx=40, pady=30)

        self.lbl_reservas=ctk.CTkLabel(self.frame_kpis, text="Reservas Totales: 0", text_color="#FFD700", font=("Arial", 18, "bold"))
        self.lbl_reservas.grid(row=0, column=1, padx=40, pady=30)

        self.lbl_roi=ctk.CTkLabel(self.frame_kpis, text="ROI Total: $0", text_color="#FF6666", font=("Arial", 18, "bold"))
        self.lbl_roi.grid(row=0, column=2, padx=40, pady=30)

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

        self.crear_tabla("Generación de Leads", "Leads", self.datos_leads, 0)
        self.crear_tabla("Conversión de Reservas", "Reservas", self.datos_conversion, 1)
        self.crear_tabla("Impacto de Campaña", "Impacto", self.datos_impacto, 2)

        # RESULTADOS
        self.frame_resultados=ctk.CTkFrame(self.frame_scroll, border_width=2, border_color=COLOR_CONTORNO)
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=20)

        titulo_resultados=ctk.CTkLabel(self.frame_resultados, text="RESULTADOS DE LA SIMULACIÓN", text_color=COLOR_TEXTO, font=("Arial", 20, "bold"))
        titulo_resultados.pack(pady=20)
        tabla_resultados=[["Día", "Leads", "Reservas", "Ingresos", "Costos", "ROI"],
                           ["", "", "", "", "", ""],
                           ["", "", "", "", "", ""],
                           ["", "", "", "", "", ""],
                           ["", "", "", "", "", ""]]

        self.tabla_resultados=CTkTable(self.frame_resultados, values=tabla_resultados)
        self.tabla_resultados.pack(padx=20, pady=20)
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

        if encabezado=="Leads":
            self.tabla_leads=tabla
        elif encabezado=="Reservas":
            self.tabla_conversion=tabla
        else:
            self.tabla_impacto=tabla

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
                rango=f"0.0000 - {acumulada:.4f}"
            else:
                rango=f"{inicio + 0.0001:.4f} - {acumulada:.4f}"

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
                if encabezado=="Leads":
                    if self.reiniciar_leads==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_leads=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_leads=False

                elif encabezado=="Reservas":
                    if self.reiniciar_conversion==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_conversion=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_conversion=False

                else:
                    if self.reiniciar_impacto==False:
                        messagebox.showwarning("Advertencia", "La tabla ya suma 1\n" "Si agregas otro dato se reiniciará")
                        self.reiniciar_impacto=True
                        return
                    else:
                        datos.clear()
                        self.reiniciar_impacto=False

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

            if encabezado=="Leads":
                self.tabla_leads.destroy()
            elif encabezado=="Reservas":
                self.tabla_conversion.destroy()
            else:
                self.tabla_impacto.destroy()

            nueva_tabla=CTkTable(frame, values=self.calcular_tabla(datos, encabezado))
            nueva_tabla.pack(padx=10, pady=10)

            if encabezado=="Leads":
                self.tabla_leads=nueva_tabla
            elif encabezado=="Reservas":
                self.tabla_conversion=nueva_tabla
            else:
                self.tabla_impacto=nueva_tabla

            entrada1.delete(0, "end")
            entrada2.delete(0, "end")

            if nueva_suma==1:
                messagebox.showinfo("Correcto", "La tabla ya suma 1")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos")
        except Exception as error:
            messagebox.showerror("Error", str(error))


Marketing()