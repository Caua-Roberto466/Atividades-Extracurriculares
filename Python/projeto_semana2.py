tarefas_pendentes = []
tarefas_concluidas = []

while True:
    print(f'O que deseja fazer? \
    \n 1- Adicionar tarefas \
    \n 2- Ver tarefas pendentes \
    \n 3- Marcar tarefas como concluída \
    \n 4- Ver tarefas concluídas \
    \n 5- Sair')

    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        tarefa = input("Adicione uma tarefa: ")
        tarefas_pendentes.append(tarefa)
    elif escolha == 2:
        print('Tarefas pendentes')
        for tarefa in tarefas_pendentes:
            print(tarefa)
        
    elif escolha == 3:
        tarefa = input('Marque a tarefa como concluída: ')
        if tarefa in tarefas_pendentes:
            tarefas_pendentes.remove(tarefa)
            tarefas_concluidas.append(tarefa)
            print(f'Tarefa {tarefa} foi concluída!')
        else:
            print(f'A tarefa {tarefa} não está na lista')
        
        
    elif escolha == 4:
        print('Tarefas concluídas')
        for tarefa in tarefas_concluidas:
            print(tarefa)
        
    elif escolha == 5:
        print('Programa encerrado')
        break
    else:
        print(f'A opção {escolha} não existe, tente novamente...')