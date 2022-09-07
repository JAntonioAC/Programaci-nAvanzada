#include <stdio.h>

void main()
{
    int i, resp, cont, conti=0, primo=0, impar=0, num;
    float prom;
    do{
        cont=0;
        printf("Teclea un número entero: ");
        scanf("%d", &num);
        for(i=1;i<=num;i++){
           if((num%i)==0) cont++; 
        }
        
        if (cont==2) primo=primo+num;
        printf("Si quieres salir teclea 0 (cero): ");
        
        if ((num%2) != 0){
            conti++;
            impar=impar+num;
        }
        
        scanf("%d", &resp);
        
    }while(resp!=0);
    printf("Suma de primos es: %d",primo);
    prom=impar/conti;
    printf("\nPromedio de impares es: %f",prom);
}