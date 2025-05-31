from time import sleep
nome = str(input("Qual seu nome completo? "))
spr = nome.split()
Pnome = spr[0]

while True:
    print(f'{Pnome}, você deseja jogar? (sim|não)')
    vai_jogar = str(input("O que você vai fazer? (sim|não) ")).lower()
    if vai_jogar == 'sim':
        Acertos = 0
        Pontos = 0
        Erros = 0
        PontosB = 0
        print(f'{Pnome}, vou te explicar as regras.\
            \n 1-Você responderá perguntas de alternativas, se você acertar você ganha pontos, que podem ser trocados por itens que te beneficiarão.\
            \n 2-Caso você não saiba, pode pedir um dica.\
            \n 3-Acertos feitos com dica dão 2 pontos, com dica é só 1.\
            \n 4-No final, seus erros e acertos serão contabilizados, juntos com seus pontos.')
        nick = str(input("Qual seu nome de Jogador? "))

        pergunta1 = 'a'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nWhat were you doing at 8 p.m. yesterday?\
        \nQual das opções abaixo é a correta?\
        \nA) I was sleeping\
        \nB) I sleep\
        \nC) I am sleep\
        \nD) I slept\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta1 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta1 == 'e':
            print(f'Muito bem {nick}, a dica é: Use was/were + verbo com -ing para ações que estavam acontecendo no passado.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta1:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta1}')
        else:
            if resposta_pergunta1 == pergunta1:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta1}.\
                \n Explicação: A pergunta usa past continuous ("What were you doing?"), então a resposta precisa combinar. "Was sleeping" mostra uma ação que estava acontecendo naquele momento. As outras opções estão no tempo verbal errado.')

        #Pergunta 2
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nWas she watching TV when you called her?\
        \nQual das opções abaixo é a correta?\
        \nA) Yes, she watched.\
        \nB) Yes, she was.\
        \nC) No, she don’t.\
        \nD) She is watching.\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: Para responder perguntas com "Was/Wasnt", use o mesmo verbo auxiliar na resposta.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação: A pergunta está no past continuous com "was", então a resposta curta correta é "Yes, she was". "Watched", "don’t" e "is watching" estão em tempos verbais errados.')

        #Pergunta 3
        pergunta2 = 'c'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nThey ____ (cook) dinner when the lights went out.\
        \nQual das opções abaixo é a correta?\
        \nA) cooked\
        \nB) are cooking\
        \nC) were cooking\
        \nD) was cook\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: Lembre-se: uma ação em progresso foi interrompida.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação: A ação de cozinhar estava acontecendo quando as luzes se apagaram (ação que interrompe). Usamos "were cooking" para mostrar que estava em progresso. As outras opções estão gramaticalmente erradas ou estão no tempo errado.')
        
        #Pergunta 4
        pergunta2 = 'a'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nWere they playing soccer in the park yesterday afternoon?\
        \nQual das opções abaixo é a correta?\
        \nA) Yes, they were.\
        \nB) Yes, they were.\
        \nC) No, they don’t.\
        \nD) They playing soccer.\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: Combine o tempo verbal da pergunta com o da resposta.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação: Como a pergunta usa "Were they playing...", a resposta correta curta é "Yes, they were". "As outras formas estão erradas no tempo ou na estrutura da resposta."')
        
        #Pergunta 5
        pergunta2 = 'd'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nHe ____ (not study) when his mom arrived.\
        \nQual das opções abaixo é a correta?\
        \nA) wasn't study\
        \nB) didn’t studying\
        \nC) was not study\
        \nD) wasn’t studying\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: Para frases negativas no past continuous, use wasn’t/weren’t + verbo com -ing.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação: A forma correta do negativo no past continuous é "wasn''t' '+ verbo com -ing", como em "wasn’t studying". As outras opções combinam errado os verbos e auxiliares.')

        #Loja 1


        #Pergunta 6
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \n[pergunta]\
        \nQual das opções abaixo é a correta?\
        \nA) [resposta]\
        \nB) [alternativa falsa]\
        \nC) [alternativa falsa]\
        \nD) [alternativa falsa]\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: [dica]')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')

        #Pergunta 7
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \n[pergunta]\
        \nQual das opções abaixo é a correta?\
        \nA) [resposta]\
        \nB) [alternativa falsa]\
        \nC) [alternativa falsa]\
        \nD) [alternativa falsa]\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: [dica]')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')

        #Pergunta 8
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \n[pergunta]\
        \nQual das opções abaixo é a correta?\
        \nA) [resposta]\
        \nB) [alternativa falsa]\
        \nC) [alternativa falsa]\
        \nD) [alternativa falsa]\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: [dica]')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')
        
        #Pergunta 9
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \n[pergunta]\
        \nQual das opções abaixo é a correta?\
        \nA) [resposta]\
        \nB) [alternativa falsa]\
        \nC) [alternativa falsa]\
        \nD) [alternativa falsa]\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: [dica]')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')

        #Pergunta 10
        pergunta2 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \n[pergunta]\
        \nQual das opções abaixo é a correta?\
        \nA) [resposta]\
        \nB) [alternativa falsa]\
        \nC) [alternativa falsa]\
        \nD) [alternativa falsa]\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'Muito bem {nick}, a dica é: [dica]')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta2}')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=1
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')


        break
    elif vai_jogar == 'não':
        print(f"Adeus {Pnome}...")
        sleep(3)
        break
    else:
        print(f'{Pnome}, opção inválida, escolha entre sim e não.')