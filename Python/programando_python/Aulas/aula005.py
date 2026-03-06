print('\033[4;30;45mOlá mundo!\033[m')
cores = {'limpa':'\033[m' ,'ciano' : '\033[36m', 'vermelho' : '\033[31m' , 'verde': '\033[32m'}
a = 4
b = 9
print(f'Os valores são {cores['ciano']}{a}{cores['limpa']} e {cores['verde']}{b}{cores['limpa']}')