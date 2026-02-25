valor = input('Digite algo: ')

print(f'O tipo primitivo de {valor} é: ', type(valor))

print(f'{valor} só tem espaços?', valor.isspace())

print(f'{valor} é um número?', valor.isnumeric())

print(f'{valor} é alfabético?', valor.isalpha())

print(f'{valor} é alfanúmerico?', valor.isalnum())

print(f'{valor} é tudo maiúscula?', valor.isupper())

print(f'{valor} é tudo em minúscula?', valor.islower())

print(f'{valor} está capitalizado?', valor.istitle())