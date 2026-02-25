#Ler o primeiro termo e a razão de uma Progressão Aritimética. No final mostre os 10 primeiros termos dessa progressão

termo1 = int(input("Qual o primeiro termo? "))
razão = int(input("insira a razão "))
decimo = termo1 + (10 -1) * razão

for termo1 in range(termo1, termo1+(10*razão), razão):
    print(termo1, end="  ➡  ")
print('Acabou')