#ler seis números inteiros e mostre a soma  apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o

soma_par = 0

for i in range(0, 6):
    num = int(input(f'Difite o {i+1} número: '))
    if num % 2 == 0 or num == 0:
        soma_par += num

print(f'A soma dos números pares é: {soma_par}')