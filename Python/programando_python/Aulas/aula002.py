#Import _____ -importa tudo/ From ____ import _____ importa algo específico
import math
import random

#biblioteca math
num = int(input('Insira um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.3f}')

#biblioteca random
rand = random.randint(1, 15)
print(f'O valor gerado é {rand}')