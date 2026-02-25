altura = float(input("Qual a sua altura? (em metros)"))
peso = float(input("Qual o seu peso? (em kilos)"))

IMC = peso/(altura**2)
print(f'Seu IMC deu: {IMC:.2f}')
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print("Peso ideal")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso")
elif IMC >= 30 and IMC < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
