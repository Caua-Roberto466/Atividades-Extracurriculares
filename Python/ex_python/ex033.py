num1 = int(input("Insira um número: "))
num2 = int(input("Insira outro número: "))
num3 = int(input("Insira mais um número: "))

#Identifica o menor
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3

#identifica o maior
maior = num3
if num1>num3 and num1>num2:
    maior = num1
if num2>num3 and num2>num1:
    maior = num2
print(f'O maior valor é {maior} e o menor é {menor}')