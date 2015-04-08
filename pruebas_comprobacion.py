import random
from random import randint
matriz=[]
for i in range(9):
        matriz.append([randint(1,3)for i in range(9)])
for i in matriz:
    print i

def posicion():
    print""
    print"Introduzca las coordenadas de la posicion:"
    posiciony=int(raw_input())
    posicionx=int(raw_input())
    print"La posicion escogida es:"
    print matriz[posicionx-1][posiciony-1]
    def compro_abajo():
        a=0
        while matriz[posicionx-1][posiciony-1]==matriz[posicionx][posiciony-1]:
            a+=1
            print"correcto"
            print a
            matriz[posicionx+a][posiciony-1]=0
            for i in matriz:
                print i                     
        posicion()
    def compro_arriba():    
        a=1
        while matriz[posicionx-1][posiciony-1]==matriz[posicionx-1][posiciony-a]:
            a+=1
            print "correcto"
            matriz[posicionx-1][posiciony-1]=0
            for i in matriz:
                print i
    compro_abajo()       
    
    try:
        compro_abajo()
    except IndexError():
        posicion()
    try:
        compro_arriba()
    except IndexError:
        posicion()
posicion()

