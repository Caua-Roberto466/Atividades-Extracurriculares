def calculadora(a, b, operacao):
    if operacao == "soma":
        soma = a + b
        print(f"A soma é {soma}")
    elif operacao == "subtração":
        sub = a - b
        print(f"A subtração é {sub}")
    elif operacao == "multiplicação":
        mul = a * b
        print(f'A multiplicação é {mul}')
    elif operacao == "divisão":
        try:
            div = a / b
        except ZeroDivisionError:
            print("Não pode dividir por zero")
        else:
            print(f"A divisão é {div}")
    else:
        raise ValueError("Operação inválida")

try:
    num1 = int(input("Digite o primero número: "))
    num2 = int(input("Digite o segundo número: "))
    
except ValueError:
    print(f"Digite um número inteiro")
else:
    ope = input("Digite a operação (soma, subtração, multiplicação ou divisão): ").lower()
    try:
        calculadora(num1, num2, ope)
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        print("Cálculo finalizado")