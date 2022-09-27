#include <stdio.h>

int main()
{
    float v1,v2,vth,r1,r2,r3,rth;
    printf("Dame el voltaje de la fuente 1: ");
    scanf("%f",&v1);
    printf("\nDame el voltaje de la fuente 2: ");
    scanf("%f",&v2);
    printf("\nDame el valor de la resistencia 1: ");
    scanf("%f",&r1);
    printf("\nDame el valor de la resistencia 2: ");
    scanf("%f",&r2);
    printf("\nDame el valor de la resistencia r3: ");
    scanf("%f",&r3);
    rth=1/((1/r1)+(1/r2)+(1/r3));
    vth=((v1/r1)+(v2/r2))*rth;
    printf("\nEl valor de rth es: %4.2f.",rth);
    printf("\nEl valor de vth es: %4.2f.",vth);

    return 0;
}
