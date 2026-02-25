preço_produto = float(input("Qual o preço do produto? R$"))
forma_de_pagamento = int(input("Qual a foma de pagamento? (1-dinheiro/cheque | 2-cartão | 3-2x no cartão | 4-3x ou mais)"))
if forma_de_pagamento == 1:
    desconto = preço_produto-(preço_produto*(10/100))
    print(f"com 10% de desconto,o senhor pagará R${desconto:.2f}")
elif forma_de_pagamento == 2:
    desconto = preço_produto-(preço_produto*(5/100))
    print(f'Com 5% de deconto você pagará R${desconto:.2f}')
elif forma_de_pagamento == 3:
    print(f'Você não ganha desconto, e pagará R${preço_produto:.2f} em, duas parcelas de R${preço_produto/2:.2f}')
elif forma_de_pagamento == 4:
    Qparcela = int(input("Quantas parcelas"))
    juros = preço_produto+(preço_produto*(20/100))
    parcela = juros/Qparcela
    print(f'Você pagará com juros R${juros} em {Qparcela} parcelas de R${parcela:.2f}')