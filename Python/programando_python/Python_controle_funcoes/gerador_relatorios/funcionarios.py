from historico import salvar

def cadastrar_funcionario(hst, **funcionarios):
    funcionario = {}
    for chave, valor in funcionarios.items():
        funcionario[chave] = valor
    hst.append(funcionario)
    salvar(hst)

def calcular_bonus(*comissoes):
    soma = sum(comissoes)
    return soma
