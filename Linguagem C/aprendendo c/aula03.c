#include <stdio.h>
int main(){
    //Declara a variável
    int numero;
    printf("Digite um numero inteiro: ");
    
    //Pega o valor digitado e armazena na variável numero, precisa do & para armazenar a informação na memória
    scanf("%d", &numero);
    printf("O numero foi: %d", numero);
    return 0;
}