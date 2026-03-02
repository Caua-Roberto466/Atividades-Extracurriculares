nome = str(input("Qual o seu nome? "))
separador = nome.split()
primeiro_nome = separador[0]

if primeiro_nome == "Cauã":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print(f"Bom dia {nome}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média foi {media}, você passou.')
elif media == 10:
    print(f'Você passou com {media}, Parabéns! Temos um gênio entre nós!')
else:
    print(f'Sua média foi {media}, você reprovou. ESTUDE MAIS!!!!')