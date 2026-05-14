import numpy as np
import customtkinter as ctk
class GeneraMixto():
    def Recibe_valores(self,X0,m,a,c):
        errores = []

        if self.SeleccionXo(X0)==False:
            errores.append("Error en la selección de Xo")

        if self.SeleccionA(a)==False:
            errores.append("Error en la selección de a")

        if self.SeleccionC(c)==False:
            errores.append("Error en la selección de c")

        if self.SeleccionM(m, X0, a, c)==False:
            errores.append("Error en la seleccion de m")

        if errores!=[]:
            self.PopUp("Datos invalidos",errores)
            return[]
        else:
            return self.Genera(X0,m,a,c)

        
    def Genera(self,X0,m,a,c):
        
        print("Todos los valores son correctos. Generando...")
        numeros_aleatorios=[]
        i=0
        Xi=X0
        if m>X0 and m>a and m>c:
            band=self.SeleccionM(m, X0, a, c)
            if band:
                while i<m:
                    Xi=(a*Xi+c)%m
                    print("X",i,": ",Xi/m," Resulatado: ",Xi)
                    numeros_aleatorios.append(Xi/m)
                    i+=1
            else:
                m2=self.completar(m)
                self.PopUp("Seleccion Automatica de m","Se tomo m como "+str(m2)+" para completar\nla cantidad de numeros solicitados")
                while i<m:
                    Xi=(a*Xi+c)%m2
                    print("X",i,": ",Xi/m2," Resulatado: ",Xi)
                    numeros_aleatorios.append(Xi/m2)
                    i+=1
                
        else:
            self.PopUp("Error en la seleccion de m","m debe de ser mayor que x0, a y c")
            return
        
        print(numeros_aleatorios)
        return numeros_aleatorios
    
    def completar(self,m):
        pot=0
        i=1
        while m>pot:
            pot=2**i
            i+=1
        return pot
    
    def SeleccionXo(self,X0):
        # semilla
        # cualquier valor entero preferiblemente que sea primo
        # mayor que cero
        if X0>0:
            return True
        else:
            return False
    
    def SeleccionM(self,m,X0,a,c):
        # modulo 
        # m= p^d, p es la base de la numeracion binaria y d cualquier numero entero
        # m> Xo, m>a, m>c
        if m>X0 and m>a and m>c:
            pot=0
            i=1
            while pot<=m:
                pot=2**i
                if pot==m:
                    return True
                else:
                    i+=1
            return False
        else:
            return False


    def SeleccionA(self,a):
        # multiplicador
        # (a-1)mod4 == 0
        # mayor a cero
        if a>0:
            if (a-1)%4==0:
                return True
            else:
                return False
        else:
            return False
    
    def SeleccionC(self,c):
        # constante aditiva
        # (c)mod8 == 5
        # mayor a cero
        if c%8==5:
            return True
        else:
            return False
        
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
