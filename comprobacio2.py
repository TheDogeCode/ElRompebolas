import random
from random import randint

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
    if x==1:
        x=0
    if x==2:
        x=1
    if x==3:
        x=2
    if x==4:
        x=3
    if x==5:
        x=4
    if x==6:
        x=5
    if x==7:
        x=6
    if x==8:
        x=7
    if x==9:
        x=8
        
    if y==1:
        y=0
    if y==2:
        y=1
    if y==3:
        y=2
    if y==4:
        y=3
    if y==5:
        y=4
    if y==6:
        y=5
    if y==7:
        y=6
    if y==8:
        y=7
    if y==9:
        y=8 
    
    print"El valor de la posicion escogida es:"    
    print matriz[y][x]
    valor_inicial=matriz[y][x]
   
    def esparcir_mancha(y,x):
        compro_abajo()    
    
    def compro_abajo(y,x):
        if y==9:
            matriz[y][x]="A"
        valor_inicial=matriz[y][x]   
        if valor_inicial==matriz[y+a][x]:
            matriz[y+1][x]="A"          
            
            esparcir_mancha(y=+1,x)
            for i in matriz:
                print i
              
               
    def compro_arriba(y,x):
        if y==9:
            matriz[y][x]="A"
        if valor_inicial==matriz[y-1][x]:
            matriz[y-a][x]="A"          
            esparcir_mancha(y=-1,x)
            for i in matriz:
                print i
                 
    '''
## PRUEBA A VER SI FUNCIONA ESTO EN LA VERSION FINAL, PERO CON LO DE COMPROBAR ABAJO   
    def compro_abajo(y,x):
        a=0  
        while valor_inicial==matriz[y+a][x]:
            matriz[y+a][x]=0          
            a+=1
            print""
            for i in matriz:
                print i
                
        posicion()
    try:
        
        compro_abajo(x,y)
        
    except IndexError:
        posicion()  
    

'''
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
        posicion()'''
    
    
posicion()
