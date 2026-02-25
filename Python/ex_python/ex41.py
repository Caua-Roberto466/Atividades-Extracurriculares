from datetime import date

ano_nasc = int(input("Qual o seu ano de nascimento? "))
ano_atu = date.today().year
idade = ano_atu - ano_nasc
print(f'O atleta tem {idade} anos')

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'junior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'
print(f'Com a idade de {idade} anos, você é da categoria {categoria}')