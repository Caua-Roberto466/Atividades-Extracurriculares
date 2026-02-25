print("O que você deseja fazer? \
    \n1 - Converter para binário \
    \n2 - Converter para octal \
    \n3 - converter para hexadecimal")
escolha = int(input("Escolha entre 1, 2 e 3 "))

if escolha == 1:
    numero = int(input("Digite o número para converter para binário "))
    if numero == 0:
        binario = 0
        print(f'Número em binário: {binario}')
    elif numero == 1:
        binario = 1
        print(f'Número em binário: {binario}')
    else:
        binario = bin(numero)[2:]
        print(f'Numero binário: {binario}')
elif escolha == 2:
    numero = int(input ("Digite o número para convereter em octal: "))
    octal = oct(numero)[2:]
    print(f'O número em octal é: {octal}')

elif escolha == 3:
    numero = int(input("Digite o número para converter em hexadecimal: "))
    hexadecimal = hex(numero)[2:]
    print(f'O número em hexadecimal é: {hexadecimal}')
else:
    print("Opção inválida")
