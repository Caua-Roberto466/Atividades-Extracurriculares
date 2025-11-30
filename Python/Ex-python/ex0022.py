numero_fatorial = int(input("Qual número você deseja descobrir o fatorial? "))
print(f"Fatorial de {numero_fatorial}")
fatorial = 1
for i in range(numero_fatorial, 0, -1):
    fatorial *= i

print(f'O fatorial de {numero_fatorial} é {fatorial}')