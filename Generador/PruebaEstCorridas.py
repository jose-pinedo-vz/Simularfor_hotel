import numpy as np
from scipy.stats import chi2
from ArchivosTXT import AbrirArchivo
import customtkinter as ctk

class Prueba_corridas():
    def Ventana(self,lista):
        self.VentanaCorridas=ctk.CTkToplevel()
        self.VentanaCorridas.title("CORRIDAS ABAJO Y ARRIBA")
        self.VentanaCorridas.geometry("1000x700")

        lb_central = ctk.CTkLabel(self.VentanaCorridas, text="Prueba de corridas abajo y arriba",
                                  font=("Arial", 20))
        lb_central.place(relx=.5, rely=.02, anchor=ctk.CENTER)

        self.p3 = ctk.CTkTextbox(self.VentanaCorridas, font=("Consolas", 13))
        self.p3.place(relx=.5, rely=.1, anchor="n")

        texto_lista="Numeros por probar:\n"
        texto_lista += "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.p3.insert("0.0", texto_lista)
        self.p3.configure(state="disabled") 

        lb_1=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Ingrese el porcentaje de aceptacion:"
                          "\n(ejemplo 5%)",
                          font=("Arial", 15))
        lb_1.place(relx=.25, rely=.1, anchor=ctk.CENTER)

        self.entry_P=ctk.CTkEntry(self.VentanaCorridas,placeholder_text="%")
        self.entry_P.place(relx=.25, rely=.15, anchor=ctk.CENTER)

        lb_2=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Ingrese el 'tope' de las corridas"\
                          "\n Tope= 3"
                          "\n Ejemplo: Tope= 3"
                          "\n corrida de 1 hasta 3 o mas ",
                          font=("Arial", 15))
        lb_2.place(relx=.25, rely=.25, anchor=ctk.CENTER)

        self.entry_tope=ctk.CTkEntry(self.VentanaCorridas,placeholder_text="N corridas")
        self.entry_tope.place(relx=.25, rely=.35, anchor=ctk.CENTER)

        lb_3=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Se van a comprobar "+str(len(lista))+" numeros aleatorios",
                          font=("Arial", 15))
        lb_3.place(relx=.25, rely=.4, anchor=ctk.CENTER)


        def TomarValores(auto,lista):
            if auto:
                self.tope=3
                porc=5
                self.entry_tope.insert(0,self.tope)
                self.entry_P.insert(0,porc)
            else:
                try:
                    self.tope=int(self.entry_tope.get())
                    porc=int(self.entry_P.get())
                    if porc<0:
                        raise Exception("El porcentaje no puede ser negativo")
                    if self.tope<1:
                        raise Exception("El tope no puede ser negativo")
                    
                except ValueError:
                    self.PopUp("Dato incorrecto","Debe ingresar un valor numerico")
                except Exception as e:
                    self.PopUp("Dato incorrecto",e)

            self.Prueba(lista,porc)

        btn=ctk.CTkButton(self.VentanaCorridas, text="COMPROBAR", command=lambda:TomarValores(False,lista),fg_color="green")
        btn.place(relx=.15,rely=.45,anchor=ctk.CENTER)

        btn2=ctk.CTkButton(self.VentanaCorridas, text="AUTOMATICO",command=lambda:TomarValores(True,lista),fg_color="blue")
        btn2.place(relx=.35,rely=.45,anchor=ctk.CENTER)
        self.VentanaCorridas.grab_set()
        self.VentanaCorridas.wait_window()
        return self.resultado_final
        

    def Prueba(self,aleatorios,porc):
        
        l=len(aleatorios)
        i=0
        delimitacion=[]

        box_delimitacion=ctk.CTkTextbox(self.VentanaCorridas,width=250,height=300,font=("Consolas", 12))
        box_delimitacion.place(relx=.25,rely=.75,anchor=ctk.CENTER)

        box_delimitacion.tag_config("cero", foreground="red")
        box_delimitacion.tag_config("uno", foreground="green")
        box_delimitacion.insert("end","Insercion de ceros y unos:\n")

        while i<l-1:
            box_delimitacion.insert("end",f"Xi: {aleatorios[i]} Xi+1{aleatorios[i+1]}\n-Corida= ")
            if aleatorios[i]<aleatorios[i+1]:
                delimitacion.append(0)
                box_delimitacion.insert("end","0\n","cero")
            else:
                delimitacion.append(1)
                box_delimitacion.insert("end","0\n","uno")
            i+=1
        
        corridas=self.Conteo(delimitacion)
        lb_conteo=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Se encontro la siguiente frecuencia (Fo) en la matriz:"
                          "\n"+str(corridas),
                          font=("Arial", 15))
        lb_conteo.place(relx=.75, rely=.5, anchor=ctk.CENTER)
        
        Fe=self.FrecuenciaEsperada(corridas,l)
        lb_Fe=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Se determina la FRECUENCIA ESPERADA"
                          "\nFe: "+str(Fe),
                          font=("Arial", 15))
        lb_Fe.place(relx=.75, rely=.6, anchor=ctk.CENTER)

        lb_X0=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Calculamos el estadistico X0 con la sumatoria"
                          "\n de la formula( Foi - FEi)**2 / Fei",
                          font=("Arial", 15))
        lb_X0.place(relx=.75, rely=.65, anchor=ctk.CENTER)
        X0=self.CalcularEstadistico(Fe,corridas)
        
        aceptado=self.Aceptacion(X0,porc)

        if aceptado:
            lb_final=ctk.CTkLabel(self.VentanaCorridas, 
                          text="Proceden a guardar los numeros aleatorios",
                          font=("Arial", 15))
            lb_final.place(relx=.75, rely=.95, anchor=ctk.CENTER)
            self.Guardar(aleatorios)
        

    def Conteo(self,delimitacion):
        box_conteo=ctk.CTkTextbox(self.VentanaCorridas,width=250,height=300,font=("Consolas", 12))
        box_conteo.place(relx=.75,rely=.27,anchor=ctk.CENTER)
        box_conteo.insert("end","Conteo de corridas:\n")
        corrida={}
        c=1
        for i in range(len(delimitacion)-1):
            simbol=delimitacion[i]
            if simbol==delimitacion[i+1]:
                c+=1
            else:
                box_conteo.insert("end",f"Corrida de {simbol} de tamaño {c}\n")
                if c>=self.tope:
                    box_conteo.insert("end",f"Corrida de{c}\npasa a ser de {self.tope} o mas.")
                    c=self.tope
                if c in corrida:
                    corrida[c]+=1
                    box_conteo.insert("end",f"N corrida {c} +=1: {corrida[c]}")
                else:
                    box_conteo.insert("end",f"Se agrega el tamaño de corrida {c}")
                    corrida[c]=1
                c=1
            box_conteo.insert("end","-------\n")
            
        return corrida                    

    def FrecuenciaEsperada(self,corridas,l):
        Fe=[]
        m=(((2*l)-1)/self.tope)
        a1=0
        a2=0
        d=1
        for k in corridas:
            if k!=self.tope:
                a1= ((k**2) + (3*k) + 1)*l
                a2= ((k**3) + (3*(k**2)) - k - 4)
                d=1
                for i in range(k+3):
                    d+=i*d
                print(d)
                Fe.append(2*((a1-a2)/d))
        if self.tope in corridas:
            Fe.append(m-sum(Fe))
        return Fe
        

    def CalcularEstadistico(self,Fe,corridas):
        X0=0
        i=0
        txtlbl=""
        for k in corridas:
            if k!=self.tope:
                X0+=    (   (corridas[k] - Fe[i]  )**2  ) /   Fe[i]
                txtlbl+=f"X0+= {round(corridas[k],3)} - {round(Fe[i],3)}**2 / {round(Fe[i],3)} = {X0}\n"
                i+=1
        if self.tope in corridas:
            X0+=(   (   corridas[self.tope] - Fe[-1]   )**2    )   /   Fe[-1]
            txtlbl+=f"X0+= {round(corridas[k],3)} - {round(Fe[i],3)}**2 / {round(Fe[i],3)} = {X0}\n"
        lb_Fe=ctk.CTkLabel(self.VentanaCorridas, 
                          text=txtlbl,
                          font=("Arial", 15))
        lb_Fe.place(relx=.75, rely=.75, anchor=ctk.CENTER)
        return X0

    def Aceptacion(self,X0,porc):
        alfa=porc/100
        gl=self.tope-1
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            lb_aceptado=ctk.CTkLabel(self.VentanaCorridas, 
                          text=f"ji2: {ji2}, X0: {X0}"
                          "\nSe acepta los numeros aleatorios",
                          font=("Arial", 15))
            lb_aceptado.place(relx=.75, rely=.85, anchor=ctk.CENTER)
            self.resultado_final = True
            return True
        else:
            lb_rechazado=ctk.CTkLabel(self.VentanaCorridas, 
                          text=f"ji2: {ji2}\tX0: {X0}"
                            "\nSe rechazan los numeros aleatorios",
                          font=("Arial", 15))
            lb_rechazado.place(relx=.75, rely=.85, anchor=ctk.CENTER)
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
        