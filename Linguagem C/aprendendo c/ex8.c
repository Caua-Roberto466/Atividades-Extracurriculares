#include <stdio.h>
int main(){
    int quantidade_gols;
    printf("Digite a quantidade de gols: ");
    scanf("%d", &quantidade_gols);
    if(quantidade_gols < 5){
        printf("Voce fez uma temporada abaixo do esperado");
    }else if(quantidade_gols < 11){
        printf("Voce fez uma boa temporada");
    }else{
        printf("Voce fez uma temporada excelente");
    }
    return 0;
}