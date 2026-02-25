valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input('Qual é o seu slário? R$'))
anos = int(input("Em quantos anos você vai pagar? "))

parcela = valor_casa / (anos*12)
porcentagem = (parcela / salario) *100

if porcentagem >= 30:
    print(f"O empréstimo não pode ser realizado devido o valor da parcela mensal ser de {parcela} e exceder 30% do seu salário")
elif porcentagem <= 2 and anos > 10:
    print("O senhor(a) consegue pagar sem ter dor de cabeça, não desejaria diminuir o tempo?")
else:
    print("O empréstimo pode ser realizado")