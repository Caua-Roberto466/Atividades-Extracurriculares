#include <stdio.h>
int main(){
    int partidas, total_gols;
    printf("Digite o total de gols em sua carreira: ");
    scanf("%d", &total_gols);
    printf("Digite o total de partidas: ");
    scanf("%d", &partidas);

    float media = (float)total_gols / partidas;
    printf("A media de gols por partida e: %0.f", media);
    return 0;
}