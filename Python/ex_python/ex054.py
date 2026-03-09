#Ler o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

#Inicia as váriaveis
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

#Laço para inserir as 7 idades e calcular quem é menor de idade e quem não é
for i in range(1, 8):
    nascimento = int(input(f'Qual o {i}º ano de nascimento? '))
    if ano_atual - nascimento < 18:
        menor_idade += 1
    else:
        maior_idade += 1

#Exibe a mensagem na tela falando os valores do for
print(f'Tem {menor_idade} menor de idade e {maior_idade} maior')