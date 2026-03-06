salario = 0
saldo = 1000
contas = []
contasPagas = []
dividas = []
dividasPagas = []

def alterarSalario():
    global salario
    salario = float(input("Digite o novo salário: "))
    return 

def adicionarConta():
    global contas
    nome = input("Qual o nome da conta? ")
    valor = int(input("Digite o valor da conta: "))
    conta = {"Nome": nome, "Valor": valor}
    contas.append(conta)

def pagarConta():
    global contasPagas
    global contas
    global saldo
    nome = input("Qual o nome da conta a ser paga? ")
    valor = int(input("Valor da conta: "))
    if saldo >= valor:
        saldo -= valor
        contaPaga = {"Nome": nome, "Valor": valor}
        contasPagas.append(contaPaga)
        if contaPaga in contas:
            contas.remove(contaPaga)
        else:
            print("Conta não identificada")
    else:
        print("Você não tem dinherio para pagar a conta")

def pagarDivida():
    global dividasPagas
    global dividas
    global saldo
    nome = input("Qual o nome da divida a ser paga? ")
    valor = int(input("Valor da divida: "))
    if saldo >= valor:
        saldo -= valor
        dividaPaga = {"Nome": nome, "Valor": valor}
        dividasPagas.append(dividaPaga)
        if dividaPaga in dividas:
            dividas.remove(dividaPaga)
        else:
            print("Divida não identificada")
    else:
        print("Você não tem dinherio para pagar a divida")

def adicionarDivida():
    global dividas
    nome = input("Digite o nome da divida: ")
    valor = int(input("Digite o valor da divida: "))
    divida = {"Nome": nome, "Valor": valor}
    dividas.append(divida)

while True:
    print("\nO que você deseja consultar no sistema? \
          \n1 - Salário\
          \n2 - Contas\
          \n3 - Dividadas\
          \n4 - Saldo \
          \n0 - Sair")
    
    escolha = int(input("\nEscolha o que você deseja consultar, 1, 2, 3 ou 4: "))
    
    if escolha == 1:
        print("O que você quer fazer com o salário? \
              \n1 - Alterar\
              \n2 - Consultar")
        escolhaSalario = int(input("\nEscolha ente 1 e 2: "))
        if escolhaSalario == 1:
            alterarSalario()
            print(f"Seu salário atual é: {salario}\n")
        elif escolhaSalario == 2:
            print(f'Seu salário é: {salario}')
        else:
            print("[Erro] Digite um número ENTRE 1 OU 2, 1 OU 2")
    
    elif escolha == 2:
        print("O que você quer fazer com suas contas? \
              \n1 - Adicionar conta \
              \n2 - Consultar contas não pagas \
              \n3 - Pagar conta\
              \n4 - Consultar contas pagas")
        escolhaContas = int(input("Escolha entre 1, 2, 3, ou 4: "))
        if escolhaContas == 1:
            adicionarConta()
            print('\n')
            for valores in contas:
                for nome, valor in valores.items():
                    print(f'{nome}: {valor}')
            print('\n')
        elif escolhaContas == 2:
            print("\n")
            for valores in contas:
                for nome, valor in valores.items():
                    print(f'{nome}: {valor}')
        elif escolhaContas == 3:
            print("\n")
            pagarConta()
            print(saldo)
            print("Conta paga com sucesso")
        elif escolhaContas == 4:
            for valores in contasPagas:
                for nome, valor in valores.items():
                    print(f'{nome}: {valor}')
    
    elif escolha == 3:
        print("\n")
        print("O que você quer fazer com suas dvidas? \
              \n1 - Adicionar dividas \
              \n2 - Consultar dividas não pagas \
              \n3 - Pagar divida\
              \n4 - Consultar dividas pagas")
        escolhaDividas = int(input("Escolha entre 1, 2, 3, ou 4: "))
        if escolhaDividas == 1:
            adicionarDivida()
            for valores in dividas:
                for chave, valor in valores.items():
                    print(f"{chave}: {valor}")
        elif escolhaDividas == 2:
            for valores in dividas:
                for chave, valor in valores.items():
                    print(f"{chave}: {valor}")
        
        elif escolhaDividas == 3:
            print("\n")
            pagarDivida()
            print(f'Seu saldo atual é: {saldo}')
            print("Divida paga com sucesso")

        elif escolhaDividas == 4:
            print(f'\n Suas dividas pagas são: ')
            for valores in dividasPagas:
                for chave, valor in valores.items():
                    print(f"{chave}: {valor}")
    
    elif escolha == 4:
        escolhaSaldo = int(input(f'\n Seu saldo é {saldo}, deseja adicionar mais? 1 - Sim 2 Não: '))
        if escolhaSaldo == 1:
            saldoNovo = int(input("Adicione seu novo saldo: "))
            saldo += saldoNovo
            print(f"Seu saldo agora é {saldo}")
        elif escolhaSaldo == 2:
            print(f"Saldo: {saldo}")
        else:
            print("Opção inválida")
    
    elif escolha == 0:
        print("Adeus!")
        break;