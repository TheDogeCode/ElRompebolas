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
        if eleccion==1:
            print"Has elegido el nivel FACIL"
            print""
            for i in range(9):
                    matriz.append([randint(1,3)for i in range(9)])
            for i in matriz:
                print i
        if eleccion==2:
            print"Has elegido el nivel INTERMEDIO"
            print""
            for i in range(9):
                    matriz.append([randint(1,4)for i in range(9)])
            for i in matriz:
                print i
        if eleccion==3:
            print"Has elegido el nivel DIFICIL"
            print""
            for i in range(9):
                    matriz.append([randint(1,5)for i in range(9)])
            for i in matriz:
                print i            
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
                                cuadrado=[[1,1,1,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,1],[1,2,3,3,3,3,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,1,2,1,3,2,1],[1,2,3,1,1,1,3,2,1],[1,2,3,3,3,3,3,2,1],[1,2,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1]]
                                for i in cuadrado:
                                        print i
                        if e4==2:
                                print"Has elegido el rombo de 4 colores"
                                print""
                                rombo=[[4,4,4,4,1,4,4,4,4],[4,4,4,1,2,1,4,4,4],[4,4,1,2,3,2,1,4,4],[4,1,2,3,1,3,2,1,4],[1,2,3,1,2,1,3,2,1],[4,1,2,3,1,3,2,1,4],[4,4,1,2,3,2,1,4,4],[4,4,4,1,2,1,4,4,4],[4,4,4,4,1,4,4,4,4]]                            
                                for i in rombo:
                                        print i
                        if e4==3:
                                print"Has escogido el casi-damero de 2 colores:"
                                print""
                                casidamero=[[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1],[2,1,2,1,2,1,2,1,2],[1,2,1,2,1,2,1,2,1]]
                                for i in casidamero:
                                        print i
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
        while eleccion>6:
                print"Esa opcion no existe"
                menu()
        while eleccion<0:
                print"Esa opcion no existe"
                menu()
menu()
