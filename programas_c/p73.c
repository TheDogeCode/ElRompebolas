#include<stdio.h>
#define MAX_NUM_BITS 32
//andres.exe has stopped working
int Decimal_A_Binario(int num_bits, int [], int num_10);
main()
{
     int num_10,num_bits,i,num_bin;
     printf("Introduzca numero de bits. ");
     if(Pedir_Valor(&num_bits,MAX_NUM_BITS))
     {
         int num_bin[num_bits];
         printf("Introduzca entero: ");
         scanf("%d", &num_10);
    }
     if(Decimal_A_Binario(num_bits,num_bin, num_10))
     {
            for(i=num_bits-1;i>=0;i--)
            {
                printf("");
            }
    }

    else
        {
            printf("El número de bits no es valido\n ");
        }
}
int Decimal_A_Binario(int num_bits, int num_bin[], int num_10)
{
    num_bin[num_bits-1]=0;
    int i,contador=0;
    int exito=1;
    int resto;
    for(i=0;i<num_bits;i++)
    {
        //introducir algo, luego lo miro
        num_10=;
    }
    if(num_10<0)
    {
        num_bin[num_bits-1]=1;
        num_10*=-1;
    }
    do
    {
        resto=num_10%2;
        num_10=num_10/2;
        num_bin[contador]=resto;
        contador++;
    }while(num_10>1&&contador<num_bits-1);

    if(contador==num_bits-1)
    {
        printf("Numero de bits insuficiente\n");
        exito=0;
    }
    else
        {
            num_bin[contador]=num_10;
        }
    return (exito);
}
