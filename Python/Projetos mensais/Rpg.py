import time
import random
#classes
classes = {
    1: {'nome': 'Guerreiro', 'força': 20, 'velocidade': 10, 'resistência': 10},
    2: {'nome': 'Assassino', 'força': 10, 'velocidade': 20, 'resistência': 10},
    3: {'nome': 'Ferreiro', 'força': 10, 'velocidade': 10, 'resistência': 20}
}

#vida do jogador
vida_player = 20
vidaP_max = vida_player

#atribui o xp do jogador
xp_gan = 0
xp_prox = 20
nível = 1

#Laço que faz o jogo rodar
while True:
      print("Escolha sua classe \
        \n1 - Guerreiro - Força[20] Velocidade[10] Resistência[10] \
        \n2 - Assassino - Força[10] Velocidade[20] Resistência[10] \
        \n3 - Ferreiro - Força[10] Velocidade[10] Resitência[20]")

      escolha = int(input("\n\nFaça sua escolha (1, 2 ou 3)"))

      if escolha in classes:
            #Atribui os status do jogador
            classe_player = classes[escolha]['nome']
            dano_player = classes[escolha]['força']
            velocidade_player = classes[escolha]['velocidade']
            resistencia_player = classes[escolha]['resistência']
            print(f'\n\nClasse escolhida foi {classe_player}')
            
            #função para upar de level
            def ganhar_xp(xp):
                  global xp_gan, xp_prox, nível, vidaP_max, vida_player
                  xp_gan += xp
                  if xp_gan >= xp_prox:
                        nível += 1
                        xp_gan -= xp_prox
                        xp_prox += 5
                        vidaP_max += 5
                        vida_player = vidaP_max
                        print(f"\n\nVocê subil de nível, agora seu progresso está assim: Nível {nível} {xp_gan}/{xp_prox}")

            #função de ataque
            def atacar(dano, vida_inimiga):
                  vida_inimiga -= dano
            
            #Função de defender
            def defender(dano_inimigo, defesa, vida):
                  if dano_inimigo > defesa:
                        vida = dano_inimigo - defesa
                        print(f"Você tomou {dano_inimigo - defesa} sua vida atual é {vida}")
                  elif dano_inimigo <= defesa:
                        print(f"Você defendeu e não recebeu nada de dano")

            #função de curar vida
            def curar_vida(cura):
                  global vida_player 
                  if cura <= vidaP_max:
                        vida_player = vida_player
                  else:
                        a_mais = cura - vidaP_max
                        vida_player = cura - a_mais

            break
      else:
            print("Classe inválida")