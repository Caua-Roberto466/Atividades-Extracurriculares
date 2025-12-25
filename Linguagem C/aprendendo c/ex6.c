//Analizador de cartão vermelho
#include <stdio.h>
int main(){
    int cartao_amarelo;
    printf("Digite a quantidade de cartoes amarelos: ");
    scanf("%d", &cartao_amarelo);
    if(cartao_amarelo >= 2){
        printf("O jogador sera expulso");
    }else{
        printf("O jogador ainda vai jogar");
    }
    return 0;
}