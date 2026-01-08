//Classificação da partida por torcedores
#include <stdio.h>
int main(){
    int quantidade_max, quantidade_ocupada;
    printf("Digite a quantidade máxima do estádio: ");
    scanf("%d", &quantidade_max);
    printf("Digite a quantidade ocupada no estádio: ");
    scanf("%d", &quantidade_ocupada);
    float porcentagem = quantidade_ocupada / quantidade_max * 100;
    if(porcentagem > 90){
        printf("Lotado!");
    }else if(porcentagem > 70){
        printf("Otima presenca de publico");
    }else if(porcentagem > 50){
        printf("Publico razoavel");
    }else if(porcentagem < 50){
        printf("Morumbis");
    }
    return 0;
}