import random
from random import randint
def menu():
        print"Elija el nivel del juego:"
        print"1. Facil"
        print"2. Medio"
        print"3. Dificil"
        print"4. Tablero fijo"
        print"5. Mejores puntuciones"
        print"6. Borrar mejores puntuaciones"
        print"0. Salir del juego"
        a=raw_input()
        eleccion=int(a)
        matriz=[]
        def posicion():
            print""
            print"Introduzca las coordenadas de la posicion."
            print"Fila:"
            y=int(raw_input())
            print"Columna:"
            x=int(raw_input())
            if x==0 & y==0 :
                print "PARTIDA TERMINADA POR EL JUGADOR, SALIENDO AL MENU"
                menu()
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
                a=-1
                while matriz[y-1][x-1]==matriz[y+a][x-1]:
                    matriz[y-1][x-1]=0           
                    matriz[y+a][x-1]=0
                    print"correcto"
                    a+=1
                    if matriz[y+a][x-1]==matriz[y+a+1][x-1]:
                        matriz[y-1][x-1]=0
                        matriz[y+a][x-1]=0
                        matriz[y+a+1][x-1]=0
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
        if eleccion==1:
            print"Has elegido el nivel FACIL"
            print""
            for i in range(9):
                    matriz.append([randint(1,3)for i in range(9)])
            for i in matriz:
                print i
            posicion()
        if eleccion==2:
            print"Has elegido el nivel INTERMEDIO"
            print""
            for i in range(9):
                    matriz.append([randint(1,4)for i in range(9)])
            for i in matriz:
                print i
            posicion()
        if eleccion==3:
            print"Has elegido el nivel DIFICIL"
            print""
            for i in range(9):
                    matriz.append([randint(1,5)for i in range(9)])
            for i in matriz:
                print i    
            posicion()        
        if eleccion==4:
                def tablerofijo():
                        print"Elija una de las opciones del menu:"
                        print"1. Cuadrado con 3 colores."
                        print"2. Rombo con 4 colores"
                        print"3. Casi-damero, con 2 colores"
                        print"0. Volver"
                        e4=int(raw_input())
                        while e4>3:
                                print"Esa opcion no existe."
                                tablerofijo()
                        while e4<0:
                                print"Esa opcion no existe."
                                tablerofijo()
                        if e4==1:
                                print"Has elegido el cuadrado con 3 colores:"
                                print""
                                matriz=[[1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,1,2,1,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1]]
                                for i in matriz:
                                        print i
                                posicion()
                        if e4==2:
                                print"Has elegido el rombo de 4 colores"
                                print""
                                matriz=[[4,4,4,4,1,4,4,4,4],[4,4,4,1,2,1,4,4,4],[4,4,1,2,3,2,1,4,4],[4,1,2,3,1,3,2,1,4],[1,2,3,1,2,1,3,2,1],[4,1,2,3,1,3,2,1,4],[4,4,1,2,3,2,1,4,4],[4,4,4,1,2,1,4,4,4],[4,4,4,4,1,4,4,4,4]]                            
                                for i in matriz:
                                        print i
                                posicion()
                        if e4==3:
                                print"Has escogido el casi-damero de 2 colores:"
                                print""
                                matriz=[[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1]]
                                for i in matriz:
                                        print i
                                posicion()
                        if e4==0:
                                menu()
                tablerofijo()
        if eleccion==0:
            print"Quieres salir del juego?"
            print"1. Si"
            print"2. No"
            salir=int(raw_input())
            if salir==2:
                menu()
            if salir<1:
                print"Esa opcion no existe"
                menu()
            if salir>2:
                print"Esa opcion no existe"
                menu()
        while eleccion>6:
                print"Esa opcion no existe"
                menu()
        while eleccion<0:
                print"Esa opcion no existe"
menu()
