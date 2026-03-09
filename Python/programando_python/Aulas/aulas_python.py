#-----------------------------Aula 1-----------------------------------------
#Desafio 1-------------------------------------------------------------------
print("===========Desafio 1===========")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
print(f"A soma entre {n1} e {n2} é {s}")

#Desafio 2-------------------------------------------------------------------
print("===========Desafio 2===========")
n = input("Escreva algo pelo teclado: ")
print(type(n))
print(n.isalpha())
print(n.isupper())
print(n.isnumeric())

#-----------------------------Aula 2-----------------------------------------
#5 + 2 == 7 # + é adição
#5 - 2 == 3 # - é subtração
#5*2 == 10 # * é multiplicação
#5/2 == 2.5 # / é divisão
#5**2 == 25 # ** é potenciação(potência)
#5//2 == 2 # // é uma divisão inteira, sem resultados quebrados
#5%2 == 1 # % é o resto da divisão

#Ordem de Precedência
#1-()
#2-**
#3-*,/,//,%
#4- +,-

#5+3*2 == 11
#3*5+4**2 == 31
#3*(5+4)**2 == 243


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print(f'A soma é {a}, a subtração é {s}, a multiplicação é {m}, a divisão é {d}, a divisão inteira é {di}, o resto da divisão inteira é {r}, e a potência é {e}')

#Desafio 3-------------------------------------------------------------------
carteira = int(input('Quantos R$ você tem? '))
print(f'Você terá {carteira/5.87:.2f} dólares')

#Desafio 4-------------------------------------------------------------------
altura = int(input('Altura da parede em metros: '))
largura = int(input("Largura da parede em metros: "))
area = altura*largura
print(f'A área da parede é {altura*largura} metros quadrados.')
print(f'A quantidade de litros gastos será: {area/2} litros de tinta.')


#Desafio 5------------------------------------------------------------------
preco = int(input('Qual o preço do produto? '))
desconto = preco/100*5
print(f'O preço inicial é de {preco}, e o preço final com 5% de desconto é de {preco-desconto}')

#Desafio 6------------------------------------------------------------------
salario = int(input('Qual o salário do funcionário? '))
desconto = salario/100*15
print(f'O salário inicial era de R${salario} e foi para R${salario+desconto}')

#-----------------------------Aula 2-----------------------------------------
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

#-----------------------------Aula 3-----------------------------------------
frase = "Curso em vídeo Python"
espaco = '   Aprendendo Python  '
print(frase[:5])
print(frase[15:])
print(frase[9::3])

len(frase)
frase.count('o',0,13)
frase.find('deo')
frase.find('Android')
frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
espaco.strip()
frase.split()
'-'.join(frase)

print(len(frase))
print(frase.count("o"))
print(frase.find('deo'))
print(frase.find('Android'))
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(espaco.strip())
print(espaco.rstrip())
print(espaco.lstrip())
print(frase.split())
print('-'.join(frase))
print('Curso' in frase)

#Aula 4
nome = str(input("Qual o seu nome? "))
separador = nome.split()
primeiro_nome = separador[0]

if primeiro_nome == "Cauã":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")
print(f"Bom dia {primeiro_nome}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua média foi {media}, você passou.')
elif media == 10:
    print(f'Você passou com {media}, Parabéns! Temos um gênio entre nós!')
else:
    print(f'Sua média foi {media}, você reprovou. ESTUDE MAIS!!!!')

nome = str(input("Qual o seu nome? "))

if nome == 'Cauã':
    print(f'{nome}, que nome incrível, QI elevado irmão')
elif nome == 'Marinês' or nome == 'Amanda':
    print("Nãooooo...................")
else:
    print(f'{nome}, nomezinho normal o seu em,🥱')

print(f'Tenha um bom dia {nome}!')

n = int(input("Digite um número "))
passo = int(input("Quantas casas "))
for c in range(0, n+1, passo):
    print(c)
s = 0
limite = int(input("Quantos números será somados"))
for c in range(0, 11):
    n = int(input("Digite um número "))
    s += n
print(f"O somatório é {s}")

# for c in range(1, 10):
#     print(c)
# print("Fim")

c = 1

while c < 10:
    print(c)
    c+=1

# print("Fim")
# for c in range(1, 5):
#     n = int(input("Digite um valor: "))
# print("Fim")

r = "S"
par = impar = 0
while r == "S":
    a = int(input("Digite um valor: "))
    r = input("Quer continuar? ").upper()

numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        if numero % 2 == 0:
            par +=1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números impares")