import numpy as np
from scipy.stats import chi2
from ArchivosTXT import AbrirArchivo
import customtkinter as ctk


class Prueba_Series():
    def Ventana(self,lista):
        self.VentanaSeries=ctk.CTkToplevel()
        self.VentanaSeries.title("PRUEBA DE SERIES")
        self.VentanaSeries.geometry("1000x700")

        self.p3 = ctk.CTkTextbox(self.VentanaSeries, font=("Consolas", 13))
        self.p3.place(relx=.2, rely=0, anchor="n")

        texto_lista="Numeros por probar:\n"
        texto_lista += "\n".join([f"[{i+1}] -> {val}" for i, val in enumerate(lista)])

        self.p3.insert("0.0", texto_lista)
        self.p3.configure(state="disabled") 
        
        lb_central = ctk.CTkLabel(self.VentanaSeries, text="Prueba de series",
                                  font=("Arial", 20))
        lb_central.place(relx=.5, rely=.05, anchor=ctk.CENTER)

        lb_1=ctk.CTkLabel(self.VentanaSeries, 
                          text="Se requiere de n, el tamaño que tendra la cuadricula:"
                          "\n(se recomienda n>2)",
                          font=("Arial", 15))
        lb_1.place(relx=.2, rely=.3, anchor=ctk.CENTER)

        self.entry_N=ctk.CTkEntry(self.VentanaSeries,placeholder_text="n")
        self.entry_N.place(relx=.2, rely=.35, anchor=ctk.CENTER)


        lb_2=ctk.CTkLabel(self.VentanaSeries, 
                          text="Ingrese el porcentaje de aceptacion:"
                          "\n(ejemplo 5%)",
                          font=("Arial", 15))
        lb_2.place(relx=.2, rely=.4, anchor=ctk.CENTER)

        self.entry_P=ctk.CTkEntry(self.VentanaSeries,placeholder_text="%")
        self.entry_P.place(relx=.2, rely=.45, anchor=ctk.CENTER)


        self.box_matriz=ctk.CTkTextbox(self.VentanaSeries,width=300,height=300,font=("Consolas", 12))
        self.box_matriz.place(relx=.2,rely=.75,anchor=ctk.CENTER)

        self.box_matriz.tag_config("resaltado", foreground="green")
        

        btn=ctk.CTkButton(self.VentanaSeries, text="COMPROBAR", command=lambda:TomarValores(False,lista),fg_color="green")
        btn.place(relx=.1,rely=.5,anchor=ctk.CENTER)

        btn2=ctk.CTkButton(self.VentanaSeries, text="AUTOMATICO",command=lambda:TomarValores(True,lista),fg_color="blue")
        btn2.place(relx=.3,rely=.5,anchor=ctk.CENTER)
        
        
    
        def TomarValores(auto,lista):
            if auto:
                N=self.SeleccionN(len(lista))
                porc=5
                self.entry_N.insert(0,N)
                self.entry_P.insert(0,porc)
            else:
                try:
                    N=int(self.entry_N.get())
                    porc=int(self.entry_P.get())
                    
                except ValueError:
                    self.PopUp("Dato incorrecto","Debe ingresar un valor numerico")

            self.Prueba(lista,N,porc)

        btn_finalizar = ctk.CTkButton(self.VentanaSeries, text="Terminar Prueba", 
                            command=self.VentanaSeries.destroy)
        btn_finalizar.place(relx=.75, rely=.9, anchor=ctk.CENTER)
        self.VentanaSeries.grab_set()
        self.VentanaSeries.wait_window()
        return self.resultado_final
        


        

    def Prueba(self,aleatorios,n,porc):
        self.box_matriz.insert("end","Matriz de conteo:\n")
        l=len(aleatorios)
        
        Matriz=np.zeros((n,n))
    
        i=1
        while i<l:
            self.box_matriz.insert("end","# Iteración " + str(i) + ":\n")
            x=aleatorios[i-1]
            y=aleatorios[i]
            self.box_matriz.insert("end","pareja: ( xi: " + str(x) + ", xi+1: " + str(y) + ")\n")
            print(x,y)
            
            r1=0
            r2=0
            posx=0
            posy=0
            for e in range(1,n+1):
                if x>r1 and x<e/n:
                    posx=e-1
                    break
                else:
                    r1=e/n

            for e in range(1,n+1):
                if y>r2 and y<e/n:
                    posy=e-1
                    break
                else:
                    r2=e/n
            print(posx,posy)
            Matriz[posx][posy]+=1
            self.Mostrar_matriz(Matriz,posx,posy)
            self.box_matriz.insert("end","--------------------------------------\n")
            i+=1
        print(Matriz)
        Fo=self.Conteo(Matriz)

        lb_conteo=ctk.CTkLabel(self.VentanaSeries, 
                          text="Se encontro la siguiente frecuencia (Fo) en la matriz:"
                          "\n"+str(Fo),
                          font=("Arial", 15))
        lb_conteo.place(relx=.75, rely=.1, anchor=ctk.CENTER)


        Fe=((l-1)/(n**2))
        lb_Fe=ctk.CTkLabel(self.VentanaSeries, 
                          text="Se determina la FRECUENCIA ESPERADA con la formula (l-1)/n^2"
                          " \ndonde l es el numero de aleatorios y n el tamaño de la cuadricula:"
                          "\n"+str(Fe),
                          font=("Arial", 15))
        lb_Fe.place(relx=.75, rely=.2, anchor=ctk.CENTER)


        X0=self.Sumatoria(Fo,Fe)
        lb_X0=ctk.CTkLabel(self.VentanaSeries, 
                          text="Se calcula la estadística de prueba X0 con la formula X0/Fe:"
                          "\n X0 = "+str(X0),
                          font=("Arial", 15))
        lb_X0.place(relx=.75, rely=.75, anchor=ctk.CENTER)

        aceptado=self.Aceptacion(X0,n,porc)

        if aceptado:
            
            lb_final=ctk.CTkLabel(self.VentanaSeries, 
                          text="Proceden a guardar los numeros aleatorios",
                          font=("Arial", 15))
            lb_final.place(relx=.75, rely=.95, anchor=ctk.CENTER)
            self.Guardar(aleatorios)


    def Mostrar_matriz(self,matriz,posx,posy):
        for fila in range(len(matriz)):
            for columna in range(len(matriz)):
                if fila==posx and columna==posy:
                    self.box_matriz.insert("end","\t"+str((matriz[fila][columna])), "resaltado")
                else:
                    self.box_matriz.insert("end","\t"+str((matriz[fila][columna])))
            self.box_matriz.insert("end","\n")
    

    def SeleccionN(self,l):
        n1=1
        n2=0
        while n2==0:
            Fe=(l-1)/(n1**2)
            print("Fe: ",Fe)
            print("n1: ",n1)
            if Fe<=5:
                n2=n1-1
            else:
                n1+=1
        if ((l-1)/(n1**2)-5)>=(5-(l-1)/(n2**2)):
            return n1
        else:
            return n2
    def Conteo(self,Matriz):
        Fo={}
        for f in range(len(Matriz)):
            for c in range(len(Matriz)):
                n=str(Matriz[f][c])
                if n in Fo:
                    Fo[n]+=1
                else:
                    Fo[n]=1
        return Fo
    
    def Sumatoria(self,Fo,Fe):
        box_sumatoria=ctk.CTkTextbox(self.VentanaSeries,width=300,height=300,font=("Consolas", 12))
        box_sumatoria.place(relx=.75,rely=.5,anchor=ctk.CENTER)
        box_sumatoria.insert("end","Calculo de X0: \n")
        if Fo=={}:
            print("Ocurrio un error en la sumatoria")
            box_sumatoria.insert("end","Ocurrio un error en la sumatoria \n")
            return 0
        else:
            X0=0
            for k in Fo:
                print(k)
                s=((Fo[k]*(float(k)-Fe))**2)
                box_sumatoria.insert("end",f" s= ( {Fo[k]} x {k} - {Fe} ) ^2"+"\n")
                box_sumatoria.insert("end","s: "+str(s)+"\n")
                X0+=s
                box_sumatoria.insert("end","X0: "+str(X0)+"\n")
            X0=X0/Fe
            return X0

    def Aceptacion(self,X0,n,porc,):
        alfa=porc/100
        print(n)
        gl=(n**2)-1
        # En estadística, ppf es 'Percent Point Function' (la inversa de la CDF)
        # Se usa (1 - alfa) porque queremos el valor del límite derecho
        ji2=chi2.ppf(1-alfa,gl)
        print("ji2: ",ji2, " X0: ",X0)
        if X0<ji2:
            lb_aceptado=ctk.CTkLabel(self.VentanaSeries, 
                          text=f"ji2: {ji2}, X0: {X0}"
                          "\nSe acepta los numeros aleatorios",
                          font=("Arial", 15))
            lb_aceptado.place(relx=.75, rely=.8, anchor=ctk.CENTER)
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

