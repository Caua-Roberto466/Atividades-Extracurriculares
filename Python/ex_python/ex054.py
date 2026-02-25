#Ler o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

#Inicia as váriaveis
ano_atual = 2025
maior_idade = 0
menor_idade = 0

#Laço para inserir as 7 idades e calcular quem é menor de idade e quem não é
for i in range(0, 7):
    nascimento = int(input(f'Qual o {i+1}º ano de nascimento? '))
    if ano_atual - nascimento < 18:
        menor_idade += 1
    else:
        maior_idade += 1

#Exibe a mensagem na tela falando os valores do for
print(f'Tem {menor_idade} menor de idade e {maior_idade} maior')