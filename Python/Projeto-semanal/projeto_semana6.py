#Adivinhador de número
from random import randint
from time import sleep
numero_tentativas = int(input("Em quantas tentavivas você acha que eu acerto o número que você escolheu? "))
tentativas = 0

numero_escolhido = int(input("Qual é o número escolhido? Escolha entre 1 e 15 "))

while True:
    numero_maquina = randint(1, 15)
    tentativas += 1
    print(f'Seu número é {numero_maquina}?')
    sleep(2)
    if tentativas >= numero_tentativas:
        print(f"Não acertei o número que você escolheu a tempo, droga você venceu")
        break 
    elif numero_maquina == numero_escolhido:
        print(f'Eu acertei o número {numero_escolhido} antes das minhas chances acabarem! Eu venci')
        break