numero = input("Digite um número entre 0 e 9999: ")

dividir = numero.split()
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f"A unidade é {unidade}")
print(f'A dezena é {dezena}')
print(f"A centena é {centena}")
print(f'A milhar é {milhar}')