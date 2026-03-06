n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print(f'A soma é {a}.')
print(f'A subtração é {s}.')
print(f'A multiplicação é {m}.')
print('A divisão é {}.'.format(d))
print(f'A divisão inteira é {di}.')
print(f'O resto da divisão inteira é {r}.')
print(f'A potência é {e}.')

#Desafio 3-------------------------------------------------------------------
print('Desafio 3')
valor = int(input('Digite um número: '))
print(f'Seu antecessor é {valor-1} e seu sucessor é {valor+1}')

#Desafio 4-------------------------------------------------------------------
print('Desafio 4')

valor2 = int(input('Qual número você quer que eu calcule: '))
print(f'O dobro é {valor2*2}, o triplo é {valor2*3}, a raiz quadrada é {valor2**(1/2)}')

#Desafio 5-------------------------------------------------------------------
nota1 = int(input('Qual é a nota? '))
nota2 = int(input('Qual a segunda nota? '))
print(f'A média das notas foi: {(nota1+nota2)/2}')

#Desafio 6-------------------------------------------------------------------
metros = int(input('Qual o valor em metros? '))
print(f'Valor em centímetros: {metros*100}cm')
print(f'Valor em milímetros: {metros*1000}mm')

#Desafio 7-------------------------------------------------------------------
nt = int(input('Qual número você quer descobrir a tabuada? '))
print(f'1x{nt}={nt*1}')
print(f'2x{nt}={nt*2}')
print(f'3x{nt}={nt*3}')
print(f'4x{nt}={nt*4}')
print(f'5x{nt}={nt*5}')
print(f'6x{nt}={nt*6}')
print(f'7x{nt}={nt*7}')
print(f'8x{nt}={nt*8}')
print(f'9x{nt}={nt*9}')
print(f'10x{nt}={nt*10}')

#Desafio 8-------------------------------------------------------------------
carteira = int(input('Quantos R$ você tem? '))
print(f'Você terá {carteira/5.87:.2f} dólares')

#Desafio 9-------------------------------------------------------------------
altura = int(input('Altura da parede em metros: '))
largura = int(input("Largura da parede em metros: "))
area = altura*largura
print(f'A área da parede é {altura*largura} metros quadrados.')
print(f'A quantidade de litros gastos será: {area/2} litros de tinta.')


#Desafio 10------------------------------------------------------------------
preco = int(input('Qual o preço do produto? '))
desconto = preco/100*5
print(f'O preço inicial é de {preco}, e o preço final com 5% de desconto é de {preco-desconto}')

#Desafio 11------------------------------------------------------------------
salario = int(input('Qual o salário do funcionário? '))
desconto = salario/100*15
print(f'O salário inicial era de R${salario} e foi para R${salario+desconto}')
