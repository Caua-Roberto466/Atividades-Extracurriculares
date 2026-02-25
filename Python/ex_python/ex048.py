#Calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500

n = 0
soma = 0

for c in range(1, 501):
    if c % 2 != 0:
        if c %  3 == 0:
            soma += c
            n += 1

print(f"A soma dos {n} deu {soma} e")