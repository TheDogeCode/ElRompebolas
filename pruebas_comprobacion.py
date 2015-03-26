import random
from random import randint
matriz=[]
matriz=[[1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,1,2,1,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1]]
for i in matriz:
    print i
def posicion():
    print""
    print"Introduzca las coordenadas de la posicion:"
    posicionx=int(raw_input())
    posiciony=int(raw_input())
    print"La posicion escogida es:"
    print matriz[posicionx-1][posiciony-1]
    def compro_abajo():
        a=0
        while matriz[posicionx-1][posiciony-1]==matriz[posicionx][posiciony-1]:
            print "correcto"
            a+=1
            matriz[posicionx+a][posiciony-1]=0
            for i in matriz:
                print i
            if a==7:
                break  
            ## esto es un comentario
        posicion()
    def compro_arriba():
        a=0
        while matriz[posicionx-1][posiciony-1]==matriz[posicionx-a][posiciony-1]:
            a=a+1
            print"correcto"
            if a==7:
                a=0
                matriz[poscicion-a][posiciony-1]=0
                for i in matriz:
                    print i
            else:
                posicion()
    compro_abajo()
posicion()
