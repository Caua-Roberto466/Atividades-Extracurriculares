questoes = int(input("Quantas questões você acertou? "))

if questoes < 5:
    print("Você tirou D na prova")
elif questoes < 7:
    print("Você tirou C na prova")
elif questoes < 9:
    print("Você tirou B na prova")
elif questoes <11:
    print("VOcê tirou A na prova")
else:
    print("Valor inválido")