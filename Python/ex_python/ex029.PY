velocidade = float(input("Qual a velocidade que o carro está? Km/h"))

if velocidade <= 80:
    print(f'Você está dentro do limite. Tenha um bom dia')
else:
    acima = velocidade - 80
    multa = acima*7
    print(f'Com a velocidade de {velocidade:.2f}, o carro está {acima:.2f}Km/h acima da velocidade permitida, e a multa é de R${multa:.2f}')