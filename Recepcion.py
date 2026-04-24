

#* el codigo no esta terminado

import random

class Recepcion:
    
    def Datos(self):
        self.n = int(input("Cuantas iteraciones quieres: "))
        self.Recepcionistas = int(input("Cuantos recepcionistas quieres: "))
        
    def Tabla_1(self):
        #tiempo entre llegadas
        
        self.Tiempo_llegadas = []
        
        for _ in range(self.n):
            
            num_ale = random.random()
            
            if num_ale > 0 and num_ale < 0.02:
                self.Tiempo_llegadas.append(1)
                
            elif num_ale > 0.0201 and num_ale < 0.07:
                self.Tiempo_llegadas.append(2)
                
            elif num_ale > 0.0701 and num_ale < 0.15:
                self.Tiempo_llegadas.append(3)
                
            elif num_ale > 0.1501 and num_ale < 0.27:
                self.Tiempo_llegadas.append(4)
                
            elif num_ale > 0.2701 and num_ale < 0.5:
                self.Tiempo_llegadas.append(5)
                
            elif num_ale > 0.501 and num_ale < 0.73:
                self.Tiempo_llegadas.append(6)
                
            elif num_ale > 0.7301 and num_ale < 0.85:
                self.Tiempo_llegadas.append(7)
                
            elif num_ale > 0.8501 and num_ale < 0.93:
                self.Tiempo_llegadas.append(8)
                
            elif num_ale > 0.9301 and num_ale < 0.98:
                self.Tiempo_llegadas.append(9)
                
            elif num_ale > 0.9801 and num_ale < 1:
                self.Tiempo_llegadas.append(10)
                
        print(F"Minutos: {self.Tiempo_llegadas}")
    
    def Hora(self):
        
        hora = 8
        
        minutos = 0
        lim_minutos = 60
        aux = 0
        
        for i in self.Tiempo_llegadas:
            
            minutos += i
            
            #esto es provicional 
            if minutos >= 60:
                aux = minutos - lim_minutos
                minutos = 0
                hora += 1
                minutos += aux
                
            print(F"Hora: {hora:02d}, Minutos: {minutos:02d}")
            # print(F"{hora}:{minutos}")
        
    def Tabla_2(self):
        #tiempo de atencion
        
        self.Tiempo = []
        
        tam = self.n * self.Recepcionistas
        
        for _ in range(tam):
            #para poder hacer esto se podria hacer algo mas simple multiplicar n por la cantidad de recepcionistas y si llega a n ya se acabaron los numeros del primer recepcionista 

            num_ale = random.random()
            
            if num_ale > 0 and num_ale < 0.49:
                self.Tiempo.append(5)
                
            elif num_ale > 0.4901 and num_ale < 0.73:
                self.Tiempo.append(10)
                
            elif num_ale > 0.7301 and num_ale < 0.88:
                self.Tiempo.append(15)
                
            elif num_ale > 0.8801 and num_ale < 1:
                self.Tiempo.append(20)
                
        for i in range(len(self.Tiempo)):
            print(F"Minutos: {self.Tiempo[i]}")
            
            if i == self.n - 1:
                print("\n")
        
    def Tiempo_inicial_final(self):
        pass
    
R = Recepcion()
R.Datos()
R.Tabla_1()
R.Hora()
R.Tabla_2()
