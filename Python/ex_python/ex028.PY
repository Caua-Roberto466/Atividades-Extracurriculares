import random
from time import sleep

print('-=-' * 25)
print("Vamos jogar um jogo! Eu escolho um número entre 0 e 5 você adivinha")
print('-=-' * 25)
numero = random.randint(0,5) # O número é sorteado
escolha = int(input("Escolha seu número: ")) # O jogador escolhe o número
print(f'Pensando em um número...')
sleep(2)

if escolha == numero:
    print(f'Acertou!! O número era mesmo {numero}')
else:
    print(f"Errou!!! O número era {numero}")