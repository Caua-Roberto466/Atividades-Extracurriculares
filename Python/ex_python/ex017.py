from math import hypot
c1 = float(input('Insira o valor do cateto 1: '))
c2 = float(input('Insira o valor do cateto 2: '))
h = hypot(c1, c2)
print(f'A hipotenusa entre o cateto {c1} com o cateto {c2} é igual a {h:.2f}')