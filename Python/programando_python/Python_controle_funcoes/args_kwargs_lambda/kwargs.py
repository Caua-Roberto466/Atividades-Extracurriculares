def exibir_ficha(**dados):
    print("-="*20)
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")
    
    print("-="*20)


exibir_ficha(nome="Carlos", cargo="Professor", unidade="ETEC Zona Leste")
exibir_ficha(nome="Amanda", cargo="Diretora", unidade="ETEC Zona Leste", tempo="2 Anos")