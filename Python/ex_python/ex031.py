distancia = float(input("Digite a distância que será percorrida na viagem: "))

if distancia <= 200:
    passagem = 0.50
    preco = distancia*passagem
else:
    passagem = 0.45
    preco = distancia*passagem
print(f'Com a distância de {distancia}km a passagem custa R${passagem:.2f}/km e a viagem sairá R${preco:.2f}')