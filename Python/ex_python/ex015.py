dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos Km foi rodado com ele? Km: '))
preco_dia = dias * 60
preco_km = km * 0.15
total = preco_dia + preco_km

print(f'O aluguel a ser pago é R${total:.2f};')