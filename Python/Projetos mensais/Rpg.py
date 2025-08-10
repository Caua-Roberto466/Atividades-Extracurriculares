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
      vida_jogador = 10 + random.randint(1, 5)

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
                  print(f'agora seu progresso está assim: {xp} / {xp_up}\n')

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
      
      #Função de defesa
      def defender(resistência_base, força_inimigo):
            if resistência_base >= força_inimigo:
                  dano_reduzido = 0
            else:
                  dano_reduzido = força_inimigo - resistência_base
            print(f'Você defendeu! Seu oponente causou {dano_reduzido} de dano')
            return dano_reduzido
      
      #Fase 1
      monstros_fase1 = {
                  1:{'nome' : 'Goblin Lvl 1', 'força': 2, 'velocidade': 1, 'resistência': 1, 'vida': 10}, 
                  2:{'nome' : 'Raposa Lvl 1', 'força': 1, 'velocidade': 2, 'resistência': 1, 'vida': 9}, 
                  3:{'nome' : 'Gnomo Lvl 1', 'força': 1, 'velocidade': 1, 'resistência': 2, 'vida': 8}}
      monstro_id = random.randint(1, 3)
      monstroF1 = monstros_fase1[monstro_id]
      nome_monstroF1 = monstroF1['nome']
      força_mosntroF1 = monstroF1['força'] * random.randint(1, 3)
      velocidade_monstroF1 = monstroF1['velocidade'] * random.randint(1, 3)
      resistência_monstroF1 = monstroF1['resistência']*random.randint(1, 3)
      vida_monstroF1 = monstroF1['vida']
      Monstro_Fase1 = [nome_monstroF1, força_mosntroF1, velocidade_monstroF1, resistência_monstroF1, vida_monstroF1]

      print(f'\nUma batalha se iniciou!\
            \nSeu oponente é {Monstro_Fase1[0]}')
      
      while vida_monstroF1 > 0 and vida_jogador >  0:
            turnoJ = int(input("O que você vai fazer? 1 - Atacar 2 - Defender "))
            turnoMF1 = random.randint(1, 2)
            if turnoJ == 1 and turnoMF1 == 1:
                  ataqueJ = atacar(força_base, velocidade_base)
                  vida_monstroF1 -= ataqueJ
                  ataqueMF1 = atacar(força_mosntroF1, velocidade_monstroF1)
                  vida_jogador -= ataqueMF1

            elif turnoJ == 2 and turnoMF1 == 1:
                  ataqueMF1 = atacar(força_mosntroF1, velocidade_monstroF1)
                  defesaJ = defender(resistência_base, ataqueMF1)
                  vida_jogador -= defesaJ
                  
            elif turnoJ == 1 and turnoMF1 == 2:
                  ataqueJ = atacar(força_base, velocidade_base)
                  defesaMF1 = defender(resistência_monstroF1, ataqueJ)
                  vida_monstroF1 -= ataqueJ
      ganhar_xp(5)
      print(f'\n{nick}, você venceu! Agora pode passar para a próxima Fase')
      

else:
    print("Opção inválida")