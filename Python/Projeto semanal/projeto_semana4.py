import random
from time import sleep 
opções = ['pedra','papel','tesoura']
print('-='*36)
print(" "*28+'Vamos Jogar!'+' '*28)
print('-='*36)

nick = input("Insira um nome de jogador ")


while True:
    play = input(f"{nick}, você deseja continuar? (sim / não) ")
    if play.lower() == 'sim':
        pontos_maquinas = 0
        pontos_player = 0
        while True:
            if pontos_player < 10 and pontos_maquinas <10:
                jogada = input("Jogue entre pedra, papel e tesoura ").lower()
                maqui = random.choice(opções)
                print('Pedra!')
                sleep(1)
                print('Papel!')
                sleep(1)
                print('Tesoura!\n')
                sleep(1)
                print(maqui.upper()+'!')
                #Empate
                if jogada == maqui:
                    print("Vish, deu empate! Vamos de novo!\n")
                #Vitória
                elif jogada == 'pedra' and maqui == 'tesoura':
                    print(f'Droga! Perdi! Vamos de novo {nick}!\n')
                    pontos_player += 1
                elif jogada == 'papel' and maqui == 'pedra':
                    print(f'Droga! Perdi! Vamos de novo {nick}!\n')
                    pontos_player += 1
                elif jogada == 'tesoura' and maqui == 'papel':
                    print(f'Droga! Perdi! Vamos de novo {nick}!\n')
                    pontos_player += 1
                #Derrota
                elif jogada == 'papel' and maqui == 'tesoura':
                    print(f'Isso! Eu venci! Vamos de novo {nick}!\n')
                    pontos_maquinas += 1
                elif jogada == 'tesoura' and maqui == 'pedra':
                    print(f'Isso! Eu venci! Vamos de novo {nick}!\n')
                    pontos_maquinas += 1
                elif jogada == 'pedra' and maqui == 'papel':
                    print(f'Isso! Eu venci! Vamos de novo {nick}!\n')
                    pontos_maquinas += 1
                else:
                    print(f"HAHAHAHAHA! Jogou errado, burrão mané")
            elif pontos_player >= 10 and pontos_maquinas < 10:
                print(f'Parabéns {nick}! Você conseguiu fazer 10 pontos primeiro do que eu')
                print(f'Pontos finais:\
                        \n{nick}: {pontos_player}\
                        \nMaquina: {pontos_maquinas}')
                break
            elif pontos_player < 10 and pontos_maquinas >= 10:
                print(f'EU VENCI! Mais sorte na próxima {nick}')
                print(f'Pontos finais:\
                        \n{nick}: {pontos_player}\
                        \nMaquina: {pontos_maquinas}')
                break

    elif play.lower() == 'não':
        print(f'Adeus {nick}')
        sleep(2)
        break