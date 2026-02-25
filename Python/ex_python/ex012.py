preco = float(input('Qual o preço do produto? R$'))
desconto = int(input('Quantia do desconto: '))
descontando = preco/100 * desconto
#preco_final = preco - descontando
print('A porcentagem deve ser: 1- adicionada ao preço. 2- subtraida do preço')
escolha = int(input('Escolha entre 1 e 2: '))
if escolha == 1:
    preco_final = preco + (preco * desconto / 100)
    print(f'O preço inicial era de R${preco:.2f}, com um aumento de {desconto}% foi para R${preco_final:.2f}')
elif escolha == 2:
    preco_final = preco - desconto
    print(f'O preço inicial era de R${preco:.2f}, com um aumento de {desconto}% foi para R${preco_final:.2f}')
else:
    print('Opção inválida')

#print(f'O produto custava R${preco:.2f}, com o desconto de {desconto}% passou a custar R${preco_final:.2f}')