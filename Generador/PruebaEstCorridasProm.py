import numpy as np
from scipy.stats import norm
from ArchivosTXT import AbrirArchivo
import customtkinter as ctk

class Prueba_corridas_Promedio():
    def Ventana(self,lista):
        self.VentanaPromedio=ctk.CTkToplevel()
        self.VentanaPromedio.title("PRUEBA DE CORRIDAS ABAJO Y ARRIBA DEL PROMEDIO")
        self.VentanaPromedio.geometry("1000x700")

        lb_central = ctk.CTkLabel(self.VentanaPromedio, text="Prueba de corridas abajo y arriba del promedio",
                                  font=("Arial", 20))
        lb_central.place(relx=.5, rely=.05, anchor=ctk.CENTER)

        self.p3 = ctk.CTkTextbox(self.VentanaPromedio, height=500, font=("Consolas", 13))
        self.p3.place(relx=.05, rely=.05)

        texto_lista="Numeros por probar:\n"
        texto_lista += "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.p3.insert("0.0", texto_lista)
        self.p3.configure(state="disabled") 

        lb_1=ctk.CTkLabel(self.VentanaPromedio, 
                          text="Ingrese el porcentaje de aceptacion:"
                          "\n(ejemplo 5%)",
                          font=("Arial", 15))
        lb_1.place(relx=.5, rely=.1, anchor=ctk.CENTER)

        self.entry_P=ctk.CTkEntry(self.VentanaPromedio,placeholder_text="%")
        self.entry_P.place(relx=.5, rely=.15, anchor=ctk.CENTER)

        lb_2=ctk.CTkLabel(self.VentanaPromedio, 
                          text="Se van a comprobar "+str(len(lista))+" numeros aleatorios",
                          font=("Arial", 15))
        lb_2.place(relx=.5, rely=.2, anchor=ctk.CENTER)
        
        def TomarValores(lista):
            try:
                porc=int(self.entry_P.get())
                if porc<0:
                    raise Exception("El porcentaje no puede ser negativo")
            except ValueError:
                self.PopUp("Dato incorrecto","Debe ingresar un valor numerico")
            except Exception as e:
                self.PopUp("Dato incorrecto",e)

            self.Prueba(lista,porc)

        btn=ctk.CTkButton(self.VentanaPromedio, text="COMPROBAR", command=lambda:TomarValores(lista),fg_color="green")
        btn.place(relx=.5,rely=.3,anchor=ctk.CENTER)
        self.VentanaPromedio.grab_set()
        self.VentanaPromedio.wait_window()
        return self.resultado_final

        

    def Prueba(self,aleatorios,porc):
        box_res = ctk.CTkTextbox(self.VentanaPromedio, width=300, height=300, font=("Consolas", 12))
        box_res.place(relx=.5, rely=.55, anchor=ctk.CENTER)
        box_res.insert("end", f"PRUEBA DE PROMEDIOS\n")
        
        l=len(aleatorios)
        box_res.insert("end", f"Cantidad de numeros: {l}\n")

        suma=0
        for num in aleatorios:
            suma+=num
            box_res.insert("end", f"Suma+= suma: {suma:.4f}+ num: {num}\n")
        
        prom=suma/l
        box_res.insert("end", f"Promedio= suma: {suma} / n: {l}\n")

        Z0= (   (   prom - (1/2) ) * (   l**(1/2)  )   )   /   ((1/12)**(1/2))

        box_res.insert("end", f"\nZ0=( prom - 1/2 x √n ) / √1/12\n")
        if Z0<0:
            Z0=Z0*-1
        box_res.insert("end", f"Estadístico Z0= {Z0}\n")


        aceptado=self.Aceptacion(Z0,porc)

        if aceptado:
            lb_final=ctk.CTkLabel(self.VentanaPromedio, 
                          text="Proceden a guardar los numeros aleatorios",
                          font=("Arial", 15))
            lb_final.place(relx=.5, rely=.95, anchor=ctk.CENTER)
            self.Guardar(aleatorios)
        

    
    def Aceptacion(self,Z0,porc):
        alfa=(porc/100)/2
        z_tabla=norm.ppf(1 - 0.05/2)
        print(z_tabla)

        if Z0<z_tabla:
            lb_aceptado=ctk.CTkLabel(self.VentanaPromedio, 
                          text=f"Tabla z: {z_tabla}, X0: {Z0}"
                          "\nSe acepta los numeros aleatorios",
                          font=("Arial", 15))
            lb_aceptado.place(relx=.5, rely=.85, anchor=ctk.CENTER)
            self.resultado_final = True
            return True
        else:
            lb_rechazado=ctk.CTkLabel(self.VentanaPromedio, 
                          text=f"Tabla z: {z_tabla}, X0: {Z0}"
                            "\nSe rechazan los numeros aleatorios",
                          font=("Arial", 15))
            lb_rechazado.place(relx=.5, rely=.85, anchor=ctk.CENTER)
            self.resultado_final = False
            return False
        
         


    def Guardar(self,numeros):
        AbrirArchivo(numeros)

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