import math

angulo = float(input('Insira o ângulo: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo {angulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem a TANGENTE {tangente:.2f}')