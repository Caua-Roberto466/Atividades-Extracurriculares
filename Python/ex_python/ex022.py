nome = input('Digite seu nome completo: ')
dividido = nome.split()
primeiro_nome = dividido[0]
nomej = nome.strip()

maiuscula = nome.upper()
minuscula = nome.lower()
letras = len(nome)- nome.count(" ")
letraspn = len(primeiro_nome)

print(f"Seu nome em maiusculo é {maiuscula}")
print(f"Seu nome em minusculo é {minuscula}")
print(f"Seu nome tem {letras} letras")
print(f"Seu primeiro nome é {primeiro_nome} tem {letraspn} letras")