import numpy as np
from scipy.stats import chi2
from ArchivosTXT import AbrirArchivo
import customtkinter as ctk
import random

class Prueba_Del_Poker():
    def Ventana(self,lista):
        self.VentanaPoker=ctk.CTkToplevel()
        self.VentanaPoker.title("PRUEBA DEL POKER")
        self.VentanaPoker.geometry("1000x700")
        
        lb_central = ctk.CTkLabel(self.VentanaPoker, text="Prueba del poker",
                                  font=("Arial", 20))
        lb_central.place(relx=.5, rely=.05, anchor=ctk.CENTER)

        self.p3 = ctk.CTkTextbox(self.VentanaPoker, font=("Consolas", 13))
        self.p3.place(relx=.25, rely=0, anchor="n")

        texto_lista="Numeros por probar:\n"
        texto_lista += "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])
        self.p3.insert("0.0", texto_lista)
        self.p3.configure(state="disabled") 

        lb_1=ctk.CTkLabel(self.VentanaPoker, 
                          text="Ingrese el porcentaje de aceptacion:"
                          "\n(ejemplo 5%)",
                          font=("Arial", 15))
        lb_1.place(relx=.25, rely=.3, anchor=ctk.CENTER)

        self.entry_P=ctk.CTkEntry(self.VentanaPoker,placeholder_text="%")
        self.entry_P.place(relx=.25, rely=.35, anchor=ctk.CENTER)

        lb_2=ctk.CTkLabel(self.VentanaPoker, 
                          text="Se van a comprobar "+str(len(lista))+" numeros aleatorios",
                          font=("Arial", 15))
        lb_2.place(relx=.25, rely=.4, anchor=ctk.CENTER)
        
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

        
        btn=ctk.CTkButton(self.VentanaPoker, text="COMPROBAR", command=lambda:TomarValores(lista),fg_color="green")
        btn.place(relx=.25,rely=.45,anchor=ctk.CENTER)
        self.VentanaPoker.grab_set()
        self.VentanaPoker.wait_window()
        return self.resultado_final

        
    def Prueba(self,aleatorios,porc):
        print(aleatorios)
        l=len(aleatorios)
        aleatorios=list(map(str,aleatorios))
        self.AjustaTamaño(aleatorios,l)
        

        self.TodosDif=.30240
        self.Par=.50400
        self.DosPares=.10800
        self.Tercia=.07200
        self.Full=.00900
        self.Pocker=.00450
        self.Quintilla=.00010
        lb_prob=ctk.CTkLabel(self.VentanaPoker, 
                          text="Se consideran las siguientes probabilidades" \
                          "\npara las combinaciones (Fe)"+
                          "\nTodos diferentes: "+str(self.TodosDif)+
                          "\nPares: "+str(self.Par)+
                          "\nDos pares: "+str(self.DosPares)+
                          "\nTercia: "+str(self.Tercia)+
                          "\nFull: "+str(self.Full)+
                          "\nPoker "+str(self.Pocker)+
                          "\nQuintilla: "+str(self.Quintilla)
                          ,font=("Arial", 13))
        lb_prob.place(relx=.25, rely=.88, anchor=ctk.CENTER)

        self.Fe=[self.TodosDif,
                 self.Par,
                 self.DosPares,
                 self.Tercia,
                 self.Full,
                 self.Pocker,
                 self.Quintilla]

        
        Frecuencias=self.Clasifica(aleatorios)

        X0=self.FrecuenciaObservada(Frecuencias,l)
        lb_1=ctk.CTkLabel(self.VentanaPoker, 
                          text="Se caluclo el estadistico X0 con la formula: "
                          "\nSUMATORIA DE : ( Foi - FEi)**2 / Fei\n"
                          +str(X0),
                          font=("Arial", 15))
        lb_1.place(relx=.75, rely=.7, anchor=ctk.CENTER)

        aceptado=self.Aceptacion(X0,porc)

        if aceptado:
            lb_final=ctk.CTkLabel(self.VentanaPoker, 
                          text="Proceden a guardar los numeros aleatorios",
                          font=("Arial", 15))
            lb_final.place(relx=.75, rely=.95, anchor=ctk.CENTER)
            self.Guardar(aleatorios)
    
    def AjustaTamaño(self,aleatorios,l):
        box_ajuste=ctk.CTkTextbox(self.VentanaPoker,width=250,height=200,font=("Consolas", 12))
        box_ajuste.place(relx=.25,rely=.65,anchor=ctk.CENTER)

        box_ajuste.tag_config("agregar", foreground="green")
        box_ajuste.tag_config("quitar", foreground="red")
        i=0
        box_ajuste.insert("end","Se agregaran o quitaran\ndigitos a los numeros\n")
        while i<l:

            num=aleatorios[i]
            box_ajuste.insert("end",num+"\t")
            lng=len(num)
            if lng<7:
                aux=7-lng
                for n in range(aux):
                    num=num+str(random.randrange(0,9))
                box_ajuste.insert("end",num+"\n","agregar")

            elif lng>7:
                num=str(round(float(num),5))
                box_ajuste.insert("end",num+"\n","quitar")
            else:
                box_ajuste.insert("end",num+"\n")
            aleatorios[i]=num
            
            i+=1
        return aleatorios




    def Clasifica(self,aleatorios):
        box_clas=ctk.CTkTextbox(self.VentanaPoker,width=300,height=400,font=("Consolas", 12))
        box_clas.place(relx=.75,rely=.3,anchor=ctk.CENTER)

        box_clas.insert("end","Se clasificara la mano\nde poker obtenida\n")
        
        TD, Pr, DPr, Tcia, Fll, Pkr, Qta = 0, 0, 0, 0, 0, 0, 0
        
        for num in aleatorios:
            mano=num[2:7]
            res_mano=""

            Full=False
            DosPares=False
            Todos=0
            comparados=""

            for c in mano:
                if c in comparados:
                    continue
                
                else:
                    comparados+=c
                    if mano.count(c)==5:
                        Qta+=1
                        res_mano="Quintilla"
                    elif mano.count(c)==4:
                        Pkr+=1
                        res_mano="Poker"
                    elif mano.count(c)==3:
                        Tcia+=1
                        res_mano="Tercia"
                        Full=True
                    elif mano.count(c)==2:
                        if Full==True:
                            Fll+=1
                            Tcia-=1
                            res_mano="Full"
                            Full=False
                        else:
                            if DosPares==True:
                                DPr+=1
                                res_mano="Dos Pares"
                                Pr-=1
                            else:
                                Pr+=1
                                res_mano="Un par"
                                DosPares=True
                    elif mano.count(c)==1:
                        Todos+=1
            if Todos==5:
                TD+=1
                res_mano="Todos diferentes"
            box_clas.insert("end", f"Mano: {mano} = {res_mano}\n")
        

        lbl_clas=ctk.CTkLabel(self.VentanaPoker, 
                          text="\nSe encontro el siguiente" \
                          "total de combinaciones (Fo)"+
                          "\nTodos diferentes: "+str(TD)+
                          "\nPares: "+str(Pr)+
                          "\nDos pares: "+str(DPr)+
                          "\nTercia: "+str(Tcia)+
                          "\nFull: "+str(Fll)+
                          "\nPoker "+str(Pkr)+
                          "\nQuintilla: "+str(Qta)
                          ,font=("Arial", 15))
        lbl_clas.place(relx=.75, rely=.5, anchor=ctk.CENTER)
        return [TD,Pr,DPr,Tcia,Fll,Pkr,Qta]
    

    def FrecuenciaObservada(self,Frecuencias,l):
        Fo=0
        for f in range(len(Frecuencias)):
           Fo+=((Frecuencias[f] -    (self.Fe[f]*l)   )**2)    /   (self.Fe[f]*l)
        return Fo
    

    def Aceptacion(self,X0,porc):
        alfa=porc/100
        gl=7
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            lb_aceptado=ctk.CTkLabel(self.VentanaPoker, 
                          text=f"ji2: {ji2}, X0: {X0}"
                          "\nSe acepta los numeros aleatorios",
                          font=("Arial", 15))
            lb_aceptado.place(relx=.75, rely=.85, anchor=ctk.CENTER)
            self.resultado_final = True
            return True
        else:
            lb_rechazado=ctk.CTkLabel(self.VentanaSeries, 
                          text=f"ji2: {ji2}\tX0: {X0}"
                            "\nSe rechazan los numeros aleatorios",
                          font=("Arial", 15))
            lb_rechazado.place(relx=.75, rely=.8, anchor=ctk.CENTER)
            self.resultado_final = False
            return False

    def Guardar(self,numeros):
        numeros=list(map(float,numeros))
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
