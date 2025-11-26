num1 = int(input("Insira um valor inteiro "))
num2 = int(input("Insira um segundo valor inteiro "))

if num1 == num2:
    print("Os dois número são iguais")
elif num1 > num2:
    print(f"O número {num1} é maior que o {num2}")
else:
    print(f'O número {num2} é maior que {num1}')