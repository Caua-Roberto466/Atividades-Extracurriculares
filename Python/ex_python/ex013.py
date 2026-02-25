salario = float(input('Qual o salário do funcionário? R$'))
porcent = int(input('Qual a porcentagem que deve ser calculada? '))
desconto = salario * porcent / 100

print('A porcentagem deve ser: 1- adicionada ao salário. 2- subtraida do salário')
escolha = int(input('Escolha entre 1 e 2: '))
if escolha == 1:
    salario_final = salario + (salario * porcent / 100)
    print(f'O salário inicial era de R${salario:.2f}, com um aumento de {porcent}% foi para R${salario_final:.2f}')
elif escolha == 2:
    salario_final = salario - desconto
    print(f'O salário inicial era de R${salario:.2f}, com um aumento de {porcent}% foi para R${salario_final:.2f}')
else:
    print('Opção inválida')



