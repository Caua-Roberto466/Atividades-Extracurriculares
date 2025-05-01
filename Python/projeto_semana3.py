#importa a biblioteca de tempo
from time import sleep
#Recebe o nome completo, e devolve o primeiro nome
nome = input('Qual o seu nome completo? ')
spr = nome.split()
p_nome = spr[0]

while True:
    print('-=-'*25)
    print('Escolha o que deseja fazer:' \
    '\n 1-Adicionar usuário' \
    '\n 2-Ler usuários' \
    '\n 3-Sair')
    print('-=-'*25)

    escolha = int(input("Faça sua escolha: "))
    if escolha == 1:
        with open('usuarios.txt','a')  as arquivo:
            usuario = input("Usuário para ser adicionado: ")
            arquivo.write(f'Usuário: {usuario}\n')
            print("Usuário adicionado com sucesso")
    elif escolha == 2:
        with open('usuarios.txt','r') as arquivo:
            ler = arquivo.read()
            print(f"Os usuários adicionados são: \n{ler}")
    elif escolha == 3:
        print(f'{p_nome} estou desaparecendo!!!!')
        sleep(2)
        print(f'Adeus {p_nome}...')
        sleep(2)
        break
    else:
        print(f'{p_nome}, você sabe o que são números entre 1 e 3? se sabe, POR QUE NÃO ESCOLHEU ENTRE 1, 2 E 3?')