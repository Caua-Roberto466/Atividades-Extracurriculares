//Classificação de idade
#include <stdio.h>
int main(){
    int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);
    if(idade <= 20){
        printf("Voce deve jogar na cetegoria sub-20");
    }else{
        printf("Voce deve jogar na categoria profissional");
    }
    return 0;
}