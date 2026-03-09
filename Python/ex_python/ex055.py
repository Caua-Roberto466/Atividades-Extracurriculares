#Ler o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#pesos = []
menor = 0
maior = 0

for i in range(0, 5):
    peso = float(input(f"Adicione {i+1}º peso: "))
    if i == 1:
        menor = i
        maior = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    #pesos.append(peso)

'''menor = min(pesos)
maior = max(pesos)'''

print(f'O menor peso registrado é: {menor}Kg e o maior peso é {maior}Kg')