#Ler nome idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade, o nome do homem mais velho e quantas mulheres têm menos de 20 anos

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulhero20 = 0

for p in range(1, 5):
    print(f'--------{p}º Pessoa--------')
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("M | F: ").strip()
    somaddade = somaIdade + idade
    if p == 1 and sexo in "Mm":
        maiorIdadeHomem = idade
        nomeVelho = nome

    if sexo in "Mm" and idade > maiorIdadeHomem:
        nomeVelho = nome
        maiorIdadeHomem = idade
    
    if sexo in "Ff" and idade < 20:
        totMulhero20 += 1

mediaIdade = somaIdade / 4

print(f"A média de idade do grupo é: {mediaIdade}")
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}')
print(f'Tem {totMulhero20} mulheres com menos de 20 anos')