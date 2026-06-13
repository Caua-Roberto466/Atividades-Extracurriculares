from funcionarios import cadastrar_funcionario
from historico import carregar

historico = carregar()

def menu():
    print("")
    print("-="*30)
    print("1 - Cadastrar funcionário")
    print("2 - Calcular bônus do funcionário")
    print("3 - Relatório ordenado por salário")
    print("4 - Relatório filtrado por cargo")
    print("0 - Sair")
    print("-="*30)

while True:
    menu()

    try:
        escolha = int(input("Escolha o que fazer: "))

    except ValueError:
        print("Digite apenas números")