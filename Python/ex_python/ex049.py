#Tabuada utilizando o laço for

num = int(input("Digite um número para a tabuada: "))

for c in range(1, 11):
    print(f'{num} x {c:2} = {c*num}')
