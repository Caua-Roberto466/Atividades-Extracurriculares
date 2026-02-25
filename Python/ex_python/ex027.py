nome = input("Insira seu nome completo ")
split = nome.split()
primeiro_nome = split[0]
ultimo_nome = split[:-1]

print(f"Seu primeiro nome é {primeiro_nome} e seu último nome é {ultimo_nome}")