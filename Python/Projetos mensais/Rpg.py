print('-=-'*35)
print("Venha jogar um jogo")
print('-=-'*35)

nome_completo = input("Insira seu nome completo ")
spr = nome_completo.split()
nome = spr[0]

classes = {
    1: {'nome': 'Guerreiro', 'Força': 3, 'Velocidade': 1, 'Resistência': 1},
    2: {'nome': 'Algoz', 'Força': 1, 'Velocidade': 3, 'Resistência': 1},
    3: {'nome': 'Lenhador', 'Força': 1, 'Velocidade': 1, 'Resistência': 3}
}

print(f'{nome}, escolha uma das 3 classes abaixos\
      \n1 - Guerreiro: Força[3] Velocidade[1] Resistência [1]\
      \n2 - Algoz: Força[1] Velocidade[3] Resistência[1]\
      \n3 - Lenhador: Força[1] Velocidade[1] Resistência[3]')
escolha = int(input(f'{nome}, escolha entre 1, 2 e 3 '))

if escolha in classes:
    classe = classes[escolha]
    print(f'{nome}, você escolheu a classe {classe['nome']}\
          \nForça = {classe['Força']}\
          \nVelçocidade = {classe['Velocidade']}\
          \nResistência = {classe['Resistência']}')