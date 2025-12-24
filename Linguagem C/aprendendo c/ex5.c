//Comparação de salário
#include <stdio.h>
int main(){
    float salario1, salario2, diferenca;
    printf("Digite o salario do primeiro jogador: ");
    scanf("%f", &salario1);
    printf("Digite o salario do segundo jogador: ");
    scanf("%f", &salario2);
    if (salario1 > salario2){
        diferenca = salario1 - salario2;
        printf("A diferenca de salario e: R$%.2f", diferenca);
    }else{
        diferenca = salario2 - salario1;
        printf("A diferenca de salario e: R$%.2f", diferenca);
    }
    return 0;
}