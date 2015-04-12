import random
from random import randint
matriz=[]
matriz=[[1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,1,2,1,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1]]
for i in matriz:
    print i
def posicion():
    print""
    print"Introduzca las coordenadas de la posicion."
    print"Fila:"
    y=int(raw_input())
    print"Columna:"
    x=int(raw_input())
    if x>9:
        print"Esa posicion no existe"
        posicion()
    if y>9:
        print"Esa posicion no existe"
        posicion()
    if x<1:
        print"Esa posicion no existe"
        posicion()
    if y<1:
        print"Esa posicion no existe"
        posicion()
    print"La posicion escogida es:"    
    print matriz[y-1][x-1]
    def compro_abajo():
        a=0
        if matriz[y-1][x-1]==matriz[y][x]:
            matriz[y-1][x-1]=0
        while matriz[y-1][x-1]==matriz[y+a+1][x-1]:
            matriz[y+a][x-1]=0          
            
            print""
            a+=1              
            for i in matriz:
                print i          
        posicion()
    def compro_arriba():
        while matriz[y-1][x-1]==matriz[y-2][x-1]:
            print "correcto"
            a=0 #Variable para que se avance la posicion
            matriz[y-1][x-1]=0            
            matriz[y-a][x-1]=0
            a+=1
            if matriz[y-a][x-1]==matriz[y-(a+1)][x-1]:
                matriz[y-a][x-1]=0
                matriz[y-(a+1)][x-1]=0
                a+=1
            else:            
                for i in matriz:
                    print i
    def compro_derecha():
        a=-1
        while matriz[y-1][x-1]==matriz[y-1][x+a]:
            matriz[y-1][x-1]=0           
            matriz[y-1][x+a]=0
            print"correcto"
            a+=1
            if matriz[y-1][x+a]==matriz[y-1][x+a+1]:
                matriz[y-1][x-1]=0
                matriz[y-1][x+a]=0
                matriz[y-1][x+a+1]=0
                a+=1                       
            for i in matriz:
                print i 
        posicion()
    def compro_izquierda():
        a=-1
        while matriz[y-1][x-1]==matriz[y-1][x-2]:
            matriz[y-1][x-1]=0           
            matriz[y-1][x-2]=0
            print""
            a+=1
            if matriz[y-1][x-2]==matriz[y-1][x-a-1]:
                matriz[y-1][x-1]=0
                matriz[y-1][x-a]=0
                matriz[y-1][x-a-1]=0
                a+=1                       
            for i in matriz:
                print i 
        posicion()
    try:
        compro_abajo()
    except IndexError:
        posicion()
posicion()
