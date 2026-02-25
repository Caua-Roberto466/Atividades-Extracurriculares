from datetime import date

genero = int(input("Qual seu genêro? (1-homem 2-mulher)"))

if genero == 1:
    ano_nascimento = int(input("Qual o ano do seu nascimento? "))
    ano = date.today().year

    idade = ano - ano_nascimento

    if idade < 18:
        print("Você ainda vai se alistar ")
        tempores = 18 - idade
        print(f'Ainda faltam {tempores} ano(s) para você se alistar')
        alist = ano+tempores
        print(f'Seu alistamento será em {alist}')
    elif idade == 18:
        print('Está na hora de se alistar')
    elif idade > 18:
        tempopass = idade - 18
        print(f'Já passou {tempopass} ano(s) do tempo de se alistar')
        alist =ano-tempopass
        print(f'Seu alistamento foi em {alist}')
elif genero ==2:
    print("O alistamneto não é obrigatório")
else:
    print("Opção inválida, tente novamnete")
