#Falar se é primo o número digitado

n = int(input("Insira um número "))
cores = {'limpa':'\033[m' ,'ciano' : '\033[36m', 'vermelho' : '\033[31m' , 'verde': '\033[32m'}
dividido = 0
    
for i in range(1, n+1):
    if n % i == 0:
        print(f'{cores['verde']}{i}{cores['limpa']}' , end=(' '))
        dividido += 1
    else:
        print(f'{cores['vermelho']}{i}{cores['limpa']}' , end=(' '))

if dividido != 2:
    print(f'\n{n} foi dividido {dividido} logo não é primo')
else:
    print(f'\n{n} é primo')