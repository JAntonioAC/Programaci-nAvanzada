#include <stdio.h>

void main(){
    
    int n, i;
    unsigned long a=0, b=1,c;
    printf("Cuantos numeros de la serie fibonacci deseas mostrar: ? ");
    scanf("%d", &n);
    
    if (n<=0) printf("\n no hay serie");
    if (n==1) printf("\n %lu",a);
    if (n>=2) printf("%lu %lu",a,b);
    for(i=3;i<=n;i++)
    {
        c=a+b;
        printf(" %lu",c);
        a=b;
        b=c;
    }
}