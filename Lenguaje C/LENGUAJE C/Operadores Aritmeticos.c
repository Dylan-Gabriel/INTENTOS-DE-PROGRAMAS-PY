/*EJEMPLO DE OPERADORES ARITMETICOS*/

#include <stdio.h>

int main(){

    int a, b, res;
    int num1= 12, num2=3;

    printf("Escribe tu numero a: ");
    scanf ("%d", &a);

    printf("\nEscribe tu numero b: ");
    scanf ("%d", &b);

    res=a*(num1 + num2)*(b/ (num2 - num1));
    
    printf("\nEl resultado es: %d", res);

    return 0;

}