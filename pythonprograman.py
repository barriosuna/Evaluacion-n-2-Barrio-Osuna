

#misma idea de antes pero  en python, (php era utril para mostrar en una ttabla html, pero aprender el lenguaje de cero es mucho tiempo)
#6 niveles, primeras 6 celdas un nivel,seungas 5 otro, etc
#Inicilizo las 21 celdas con el vallor 0 (valor asignado para celdas desconocidas)
#PYTHON 2.7.10
import time
sinresolver = []*16
list=[0]*22 #22 entradas con 0s 
num=1
i=0
start_time=0
class Celda:
    def __init__(self,pos):
        self.pos = pos
        global num

        list[self.pos] = int(raw_input("Ingresa valor de celda " + str(num) + ": ") )
        num+= 1
        self.hijoizquierda=self.set_Hijo_izq()
        self.hijoderecha=self.set_Hijo_der()
        #self.level= self.nivel()
        #sinresolver.append(self)
        
    def set_Hijo_izq(self):
            if (self.pos <=21 and self.pos >= 16):
                return -1
            else:
                self.hijoi = self.pos + self.nivel()
                return self.hijoi


    def set_Hijo_der(self):
        
        if (self.pos <=21 and self.pos >= 16):
            return -1
        else:
            self.hijod = self.pos + self.nivel()+1
            return self.hijod

    def calcular(self):
        
        if(list[self.pos]== 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] != 0):
                    list[self.pos] = list[self.hijoderecha] + list[self.hijoizquierda]

        elif(list[self.pos]!= 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] == 0):
                    list[self.hijoizquierda] = list[self.pos] - list[self.hijoderecha]


        elif(list[self.pos]!= 0 and list[self.hijoderecha] == 0 and list[self.hijoizquierda] != 0):
                    list[self.hijoderecha] = list[self.pos] - list[self.hijoizquierda]


        if(list[self.pos]!= 0 and list[self.hijoderecha] != 0 and list[self.hijoizquierda] != 0):
                    self.a = self.calc()
                    if(self.a == 1):
                        return 1

        return 0
        

    
    def calc(self):
        if (list[self.pos] == list[self.hijoderecha] + list[self.hijoizquierda]):
            return 1
        else:
                       
            print("Error, la pirámide no se puede resolver")
            raise SystemExit

        
    def nivel(self):
            if(self.pos<2):
                return 1
            elif(self.pos<4):
                return 2
            elif(self.pos<7):
                return 3
            elif(self.pos<11):
                return 4
            elif(self.pos<16):
                return 5
            else:
                return 6
    
    
class Piramide(Celda):
    def __init__(self):
        sinresolver.append(Celda1)
        
        sinresolver.append(Celda2)
      
        sinresolver.append(Celda3)
        sinresolver.append(Celda4)
        sinresolver.append(Celda5)
        sinresolver.append(Celda6)
        sinresolver.append(Celda7)
        sinresolver.append(Celda8)
        sinresolver.append(Celda9)
        sinresolver.append(Celda10)
        sinresolver.append(Celda11)
        sinresolver.append(Celda12)
        sinresolver.append(Celda13)
        sinresolver.append(Celda14)
        sinresolver.append(Celda15)


    
        self.ciclo()
        

    
    def ciclo(self):
        global start_time
        start_time=(time.time())    
        global i
        #print("el tiempo:"+str(start_time))
        #Tiempo de inicio de ejecucion
        #if((time.time())-(start_time))==300:
        #Si la cola queda sin elementos o el tiempo llega a 500 segundos el programa finaliza
        #print("lista" +str(list[2]))
        #print("si resolver" + str(sinresolver[3]))
        #while i<10000000:
        #El time era en nano/micro segundos, me volvi loco arrenglandolo.
        while True:
            #print("el tiempo:"+str((time.time())-(start_time)))

            if((time.time())-(start_time)<500000000000000):
                if not(sinresolver):
                    self.imprimir()
                    break
                else:
                    self.primero=sinresolver[0]
                    if(self.primero.calcular()==1):
                        sinresolver.remove(self.primero)
                        i+=1
                    else:
                        self.b=sinresolver.pop(0)
                        sinresolver.append(self.b)
                        i+=1
            else:

                print("No se puede resolver la pirámide")
                raise SystemExit
            
    def imprimir(self):
        print("La piramide completa")
        print(" " +" " +" " +" " +" " +" " +" " +" " +" " +" " +str(list[1]))

        print(" " +" " +" " +" " +" " +" " +" " +" " +str(list[2])+ " " +str(list[3]))

        print(" " +" " +" " +" " +" " +" " +str(list[4])+" " +" " +  str(list[5])+" " +" " +str(list[6]))
        print(" " +" " +" " +" " +" "+str(list[7])+" " +" " +  str(list[8])+" " +" " +str(list[9])+" " +" " +str(list[10]))
        print(" " +" " +" " +str(list[11])+" " +" " + str(list[12])+" " +" " +str(list[13])+" " +" " +str(list[14])+" " +" " +str(list[15]))
        print(" " +" " +str(list[16])+ " " +" " +str(list[17])+" " +" " +str(list[18])+" " +" " +str(list[19])+" " +" " +str(list[20])+" " +" " +str(list[21]))
        tiempofinal=((time.time())-(start_time))
        print("El programa finalizo en"+" "+str(tiempofinal)+" segundos "+"transcurrido en " +str(i)+"  "+"pasadas")    
        


print ("La piramide se ingresa desde arriba hacia abajo siendo la posicion numero uno la punta de la piramide:")


Celda1 = Celda(1)
Celda2 = Celda(2)
Celda3 = Celda(3)
Celda4 = Celda(4)
Celda5 = Celda(5)
Celda6 = Celda(6)
Celda7 = Celda(7)
Celda8 = Celda(8)
Celda9 = Celda(9)
Celda10 = Celda(10)
Celda11 = Celda(11)
Celda12 = Celda(12)
Celda13 = Celda(13)
Celda14 = Celda(14)
Celda15 = Celda(15)
Celda16 = Celda(16)
Celda17 = Celda(17)
Celda18 = Celda(18)
Celda19 = Celda(19)
Celda20 = Celda(20)
Celda21 = Celda(21)
Pira=Piramide()




