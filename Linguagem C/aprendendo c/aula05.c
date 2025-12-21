#include <stdio.h>
int main(){
    int num1 = 10, num2 = 5;
    int resultado = num1 + num2;
    printf("Soma: %d + %d = %d \n", num1, num2, resultado);
    printf("Subtracao: %d - %d = %d\n", num1, num2, num1 - num2 );
    printf("Multiplicacao: %d x %d = %d\n", num1, num2, num1 * num2);
    printf("Divisao: %d / %d = %d \n", num1, num2, num1 / num2);
    printf("Modulo: %d %% %d = %d", num1, num2, num1 % num2);
    return 0;
}