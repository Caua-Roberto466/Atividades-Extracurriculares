#Lista de convidados em arquivo
while True:
    print(f'O que deseja fazer? \
          \n1 - Adicionar convidados \
          \n2 - Ler os convidados \
          \n0 - Sair')
    escolha = int(input("Escolha um número entre 1, 2 ou 0 "))

    if escolha == 1:
        with open('convidados.txt', 'a') as arquivo:
            convidado = input("Adicione o convidado: ")
            arquivo.write(f"Convidado: {convidado}\n")
    elif escolha == 2:
        with open('convidados.txt', 'r') as arquivo:
            ler = arquivo.read()
            print(f"Convidados \n{ler}")
    elif escolha == 0:
        print("Fechando Programa")
        break
    else:
        print("Insira um número válido")