nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1+nota2)/2

if media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("Você está de recuperação")
elif media >= 7:
    print("Aprovado")