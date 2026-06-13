produtos = [
    {'nome': "Notebook", 'preco': 3000},
    {'nome': "Memória RAM", 'preco': 1250},
    {'nome': "NVMe 1TB", 'preco': 1500},
    {'nome': "Case SSD", 'preco': 20}
]

filtrados = list(filter(lambda p: p['preco'] > 100, produtos))

for prod in filtrados:
    print("")
    print("-"*10)
    print(f"{prod['nome']}: R${prod['preco']:.2f}")
    print("-"*10)

ordem = sorted(produtos, key=lambda a: a['preco'], reverse=True)

for prod in ordem:
    print("")
    print("-"*10)
    print(f"{prod['nome']}: R${prod['preco']:.2f}")
    print("-"*10)