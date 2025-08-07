import random
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

nick = input(f'{nome}, escolha um nick de jogador ')

print(f'{nick}, escolha uma das 3 classes abaixos\
      \n1 - Guerreiro: Força[3] Velocidade[1] Resistência [1]\
      \n2 - Algoz: Força[1] Velocidade[3] Resistência[1]\
      \n3 - Lenhador: Força[1] Velocidade[1] Resistência[3]')
escolha = int(input(f'{nick}, escolha entre 1, 2 e 3 '))

if escolha in classes:
      classe = classes[escolha]
      print(f'\n{nick}, você escolheu a classe {classe['nome']}\
          \nForça = {classe['Força']}\
          \nVelçocidade = {classe['Velocidade']}\
          \nResistência = {classe['Resistência']}\n')
      força = classe['Força']
      velocidade = classe['Velocidade']
      resistência = classe['Resistência']
      
      #Estatos do jogador
      força_base = força*random.randint(1,3)
      velocidade_base = velocidade*random.randint(1,3)
      resistência_base = resistência*random.randint(1,3)

      #Sistema de níveis
      nível = 1
      xp = 0
      xp_up = 10
      def ganhar_xp(qtd):
            global xp, nível, xp_up
            xp += qtd 
            while xp >= xp_up:
                  xp -= xp_up
                  nível += 1
                  xp_up += 5
                  print(f"Parabéns! Você subiu para o nível {nível}! ")
                  print(f'agora seu progresso está assim: {xp} / {xp_up}')

      #Função de ataque
      def atacar(força_base, velocidade_base):
            chance_critico = random.randint(1,10)
            if chance_critico <= velocidade_base:
                  print('💥 Ataque crítico')
                  dano = força_base * 2
            else:
                  dano = força_base
            print(f'Você causou {dano} de dano ao inimigo\n')
            return dano
      
      #Fase 1

      

else:
    print("Opção inválida")