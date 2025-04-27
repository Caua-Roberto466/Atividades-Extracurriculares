#Cria a função para saber se o número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

#Inseri o número
n = int(input('Digite o número: '))

contador = 0

#Informa se o número é par ou impar
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é impar')

#Informa se o número é primo ou não
if eh_primo(n):
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')

#Informa quantos e quais os números primos tem até o número escolhido
for n in range(2, n +1):
    if eh_primo(n):
        contador += 1
        print(n, end=", ")

print(f'Até o número {n} tem {contador} números')