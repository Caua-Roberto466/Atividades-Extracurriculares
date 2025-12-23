//Programa que mede tempo de jogo
#include <stdio.h>
int main(){
    int minutos;
    printf("Digite os minutos jogados: ");
    scanf("%d", &minutos);
    float horas = minutos / 60;
    int resto_minutos = minutos % 60;
    printf("O tempo em horas foi: %0.f horas e %d minutos", horas, resto_minutos);
    return 0;
}