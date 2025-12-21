//Apresentação de jogador
#include <stdio.h>
int main(){
    char nome[10];
    int idade, gols;

    printf("Digite o seu primeiro nome: ");
    scanf("%s", &nome);

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite o numero de gols em sua carreira: ");
    scanf("%d", &gols);

    printf("\nNome: %s \nIdade: %d \nGols na carreira: %d", nome, idade, gols);
    return 0;
}