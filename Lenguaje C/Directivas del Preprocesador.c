/*Directivas del Preprocesador*/

#include <stdio.h> /*Biblioteca(S), guardadas en las bibliotecas estandar*/
/*#include "nombre del archivo" /*Busca la biblioteca en el mismo directorio o carpeta del archivo a compilar*/
/*#define PI 3.14159 /*Estas "MACRO" son constantes son inmutables por lo tanto no puede cambiar*/
#define CUBO(a) a*a*a

int main(){

    int a=3;
    printf("El cubo de la variable a es: %i\n",CUBO(a));

    return 0;
}