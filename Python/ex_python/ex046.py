# Faça um programa que mostre na tela uma contagem regerrsiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de um segundo entre eles.
from time import sleep

for c in range(10, -1, -1):
    print(f'Faltam {c} segundos para o estouro')
    sleep(1)

print('💥Os fogos estouraram')