/*Toma de Decisiones  "if"                
  Operadores de Igualdad            |   Operadores de Relacion
        == x es igual que y                 > x es mayor que y
        != x es diferente que y             > x es menor que y
                                            >= x es menor o igual que y
                                            <= x es mayor o igual que y 
*/

#include <stdio.h>

int main(){

    int edad;
    printf("Ingresa tu edad: ");
    scanf("%d", &edad);
      
    if(edad >=18){
        printf("Eres mayor de edad\n");
    }
    else if (edad==17){
        printf("Casi eres mayor de edad crack\n");
    }
    else{
        printf("Eres menor de edad\n");
    }

return 0;/*Termina el programa*/
}