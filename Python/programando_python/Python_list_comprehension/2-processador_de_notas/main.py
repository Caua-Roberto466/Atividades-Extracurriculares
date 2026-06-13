from historico import salvar, carregar

def menu():
    print("")
    print("-="*30)
    print("1 - Cadastrar Aluno")
    print("2 - Listar alunos aprovados")
    print("3 - Listar alunos reprovados")
    print("4 - Ver aluno com maior e menor nota")
    print("5 - Relatório final dos alunos")
    print("-="*30)

def exibir_aluno(alunos):
    for a in alunos:
        print("")
        print("-"*25)
        print(f"Aluno: {a['nome']}")
        print(f"Turma: {a['turma']}")
        print(f"Média: {a['media']}")

        print("-"*25)

historico = carregar()


while True:
    menu()
    try:
        escolha = int(input("Escolha o que fazer: "))

    except ValueError:
        print("Digite apenas números!")

    else:
        if escolha == 1:
            nome = input("\nDigite o nome do aluno: ")
            turma = input("Digite a turma do aluno: " )
            notas = []
            
            for i in range(4):
                while True:
                    try:
                        nota = float(input(f"Digite a {i+1}ª nota: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("A nota deve estar entre 0 e 10")
                    except ValueError:
                        print("Digite um número!")

            aluno = {
                'nome': nome,
                'turma': turma,
                'notas': notas,
                'media': sum(notas) / len(notas)
            }

            historico.append(aluno)
            salvar(historico)

        elif escolha == 2:
            if not historico:
                print("\nNão há alunos cadastrados")

            else:
                try:
                    aprovados = [a for a in historico if a['media'] >= 7]
                except KeyError:
                    print("\nNão foi possível ver a média")
                else:
                    exibir_aluno(aprovados)

        elif escolha == 3:
            if not historico:
                print("Não há alunos cadastrados!")
            else:
                try:
                    reprovados = [a for a in historico if a['media'] <=6]
                except KeyError:
                    print("\nNão foi possível ver a média")
                
                else:
                    exibir_aluno(reprovados)
        
        elif escolha == 4:
            por_media = sorted(historico, key=lambda a: a['media'], reverse=False)
            
            menor = por_media[0]
            maior = por_media[-1]
                
            print(f"\nAluno com maior nota: {maior['nome']} | Média: {maior['media']}")
            print(f"\nAluno com menor nota: {menor['nome']} | Média: {menor['media']}")
        
        elif escolha == 5:
            for i, aluno in enumerate(historico, start=1):
                print(f"{i} - Aluno: {aluno['nome']} | Média: {aluno['media']:.1f}")

        else:
            print("Opção inválida!")
