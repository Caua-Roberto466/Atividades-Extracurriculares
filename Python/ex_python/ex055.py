#Ler o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(0, 5):
    peso = float(input(f"Adicione {i+1}º peso: "))
    pesos.append(peso)

menor = min(pesos)
maior = max(pesos)

print(f'O menor peso registrado é: {menor}Kg e o maior peso é {maior}Kg')