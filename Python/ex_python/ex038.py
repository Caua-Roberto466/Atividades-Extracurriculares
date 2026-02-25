numero_1 = float(input("Inisira o primeiro número: "))
numero_2 = float(input("Insira o segundo número: "))

if numero_1 > numero_2:
    print(f'O número {numero_1} é maior')
elif numero_2 > numero_1:
    print(f'O número {numero_2} é maior')
elif numero_1 == numero_2:
    print(f'Os valores {numero_1} e {numero_2} são iguais, logo não tem maior')
