//Classificação da partida por torcedores
#include <stdio.h>
int main(){
    int quantidade_max, quantidade_ocupada;
    printf("Digite a quantidade máxima do estádio: ");
    scanf("%d", &quantidade_max);
    printf("Digite a quantidade ocupada no estádio: ");
    scanf("%d", &quantidade_ocupada);
    porcentagem = quantidade_ocupada / quantidade_max * 100;
    return 0;
}