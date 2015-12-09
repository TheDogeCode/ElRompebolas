#include <stdio.h>
#include <stdlib.h>
#define TAM_MAX 100
int pedir_valor(int *,int);
main()
{
 int tam,seguir;
 int i;
 do
 {
    if(pedir_valor(&tam,TAM_MAX))
     {
         float v1[tam],v2[tam],resta[tam];//Se reservan en ejecución

         for(i=0;i<tam;i++)
         {
                // Introducimos valores del primer vector
                printf("Introduce valor del primer vector posicion %d \n",i);
                scanf("%f",&v1[i]);
                // Introducimos valores del segundo vector
                printf("Introduce valor del segundo vector posicion %d \n",i);
                scanf("%f",&v2[i]);

         }
         // Calculamos la resta
        for(i=0;i<tam;i++)
        {
            resta[i]=v1[i]-v2[i];
            printf("resultado posicion %d \n",i);
            printf("%f\n",resta[i]);
        }
         // A partir de aquí se libera automáticamente el espacio en memoria
         // ocupado por los vectores v1[], v2[] y resta[].
     }
     else
    {
         printf("El tamaño del vector no es válido\n");
         printf("Si desea continuar pulse 1:");
         scanf("%d",&seguir);
    }
 }while(seguir==1);
}

int pedir_valor(int *t,int valor_max)
{
    //Pedimos los tamanos de los arrays
    printf("Introduce el tamano de los arrays\n");
    //Es solo t porque nos interesa guardar la direccion a la memoria de t
    scanf("%d",t);
    if(*t<0||*t>valor_max)
    {
        return (0);
    }
    else{ return (1);}

}
