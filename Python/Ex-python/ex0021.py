soma = 0
digitado = 1
while digitado != 0:
    digitado = int(input("Digite um número para ser somado (digite 0 para encerrar) "))
    soma += digitado
print(f'A soma dos números deu {soma}')