//Performace do time
#include <stdio.h>
int main(){
    int vitorias, empates, derrotas;
    printf("Digite o numeros de vitorias: ");
    scanf("%d", &vitorias);
    printf("Digite o numero de empates: ");
    scanf("%d", &empates);
    printf("Digite o numero de derrotas: ");
    scanf("%d", &derrotas);
    int pontos_vit = vitorias * 3;
    int total_points = pontos_vit + empates;
    printf("O total de pontos foi: %d", total_points);
    return 0;
}