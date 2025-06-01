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
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta1}.\
                \n Explicação: A pergunta usa past continuous ("What were you doing?"), então a resposta precisa combinar. "Was sleeping" mostra uma ação que estava acontecendo naquele momento. As outras opções estão no tempo verbal errado.')

        #Pergunta 2
        pergunta2 = 'b'
        print(f"{nick}, vamos para a próxima pergunta.\
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
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação: A pergunta está no past continuous com "was", então a resposta curta correta é "Yes, she was". "Watched", "don’t" e "is watching" estão em tempos verbais errados.')

        #Pergunta 3
        pergunta3 = 'c'
        print(f"{nick}, vamos para a próxima pergunta.\
        \nThey ____ (cook) dinner when the lights went out.\
        \nQual das opções abaixo é a correta?\
        \nA) cooked\
        \nB) are cooking\
        \nC) were cooking\
        \nD) was cook\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta3 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta3 == 'e':
            print(f'Muito bem {nick}, a dica é: Lembre-se: uma ação em progresso foi interrompida.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta3:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta3}')
        else:
            if resposta_pergunta3 == pergunta3:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta3}.\
                \n Explicação: A ação de cozinhar estava acontecendo quando as luzes se apagaram (ação que interrompe). Usamos "were cooking" para mostrar que estava em progresso. As outras opções estão gramaticalmente erradas ou estão no tempo errado.')
        
        #Pergunta 4
        pergunta4 = 'a'
        print(f"{nick}, vamos para a próxima pergunta.\
        \nWere they playing soccer in the park yesterday afternoon?\
        \nQual das opções abaixo é a correta?\
        \nA) Yes, they were.\
        \nB) Yes, they were.\
        \nC) No, they don’t.\
        \nD) They playing soccer.\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta4 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta4 == 'e':
            print(f'Muito bem {nick}, a dica é: Combine o tempo verbal da pergunta com o da resposta.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta4:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta4}')
        else:
            if resposta_pergunta4 == pergunta4:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta4}.\
                \n Explicação: Como a pergunta usa "Were they playing...", a resposta correta curta é "Yes, they were". "As outras formas estão erradas no tempo ou na estrutura da resposta."')
        
        #Pergunta 5
        pergunta5 = 'd'
        print(f"{nick}, vamos para a próxima pergunta.\
        \nHe ____ (not study) when his mom arrived.\
        \nQual das opções abaixo é a correta?\
        \nA) wasn't study\
        \nB) didn’t studying\
        \nC) was not study\
        \nD) wasn’t studying\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta5 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta5 == 'e':
            print(f'Muito bem {nick}, a dica é: Para frases negativas no past continuous, use wasn’t/weren’t + verbo com -ing.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta5:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta5}')
        else:
            if resposta_pergunta5 == pergunta5:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta5}.\
                \n Explicação: A forma correta do negativo no past continuous é "wasn''t' '+ verbo com -ing", como em "wasn’t studying". As outras opções combinam errado os verbos e auxiliares.')

        #Loja 1
        print(f'Parabéns {nick}, você subiu um nível de dificuldade, por isso a loja apareceu!\
              \nEcolha qual item vcoê quer comprar.\
              \n 1-Energético | 2-Mochila | 3- Bola de cristal')
        loja1 = int(input("Qual item você quer? (1, 2 ou 3)"))
        if loja1 == 1:
            if Pontos < 5:
                print("Você não tem pontos o suficiente para comprar este item.")
            else:
                Pontos -= 5
                PontosB = Pontos*3
                print("Você comprou o energético, todos seus pontos triplicaram")
        elif loja1 == 2:
            if Pontos < 3:
                print("Você não tem pontos o suficiente para comprar este item.")
            else:
                Pontos -= 3
                if Erros >= 2:
                    Erros -= 2
                    PontosB += 4
                else:
                    PontosB -= 2
                print("Você comprou a mochila, dois de seus erros viraram pontos")
        elif loja1 == 3:
            if Pontos < 2:
                print("Você não tem pontos o suficiente para comprar este item.")
            else:
                Pontos -= 2
                print("Você comprou a bola de cristal, e você ganhou a resposta da próxima pergunta, ela é D")

        #Pergunta 6
        pergunta6 = 'd'
        print(f"{nick}, vamos para a próxia pergunta.\
        \nYesterday, at six I _____ dinner.\
        \nQual das opções abaixo é a correta?\
        \nA) was prepare\
        \nB) was prepared\
        \nC) did prepare\
        \nD) was preparing\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta6 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta6 == 'e':
            print(f'Muito bem {nick}, a dica é: Começa com "was".')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta6:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta6}')
        else:
            if resposta_pergunta6 == pergunta6:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta6}.\
                \n Explicação: A frase fala sobre uma ação em um momento específico no passado ("yesterday, at six"). Isso exige o uso do past continuous para mostrar que a ação estava em progresso naquele momento.')

        #Pergunta 7
        pergunta7 = 'a'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nMy father ____ a novel while I ___ TV.\
        \nQual das opções abaixo é a correta?\
        \nA) was reading / was watching\
        \nB) was read / was watching\
        \nC) were reading / was watching\
        \nD) read / watched\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta7 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta7 == 'e':
            print(f'Muito bem {nick}, a dica é: Termina com "was watching".')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta7:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta7}')
        else:
            if resposta_pergunta7 == pergunta7:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta7}.\
                \n Explicação: A palavra "while" (enquanto) indica que duas ações estavam acontecendo ao mesmo tempo, ou seja, duas ações contínuas no passado. ')

        #Pergunta 8
        pergunta8 = 'b'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nWe _____ our school when he came in.\
        \nQual das opções abaixo é a correta?\
        \nA) talked\
        \nB) were talking\
        \nC) were talked\
        \nD) talking\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta8 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta8 == 'e':
            print(f'Muito bem {nick}, a dica é: Começa com "were".')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta8:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta8}')
        else:
            if resposta_pergunta8 == pergunta8:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta8}.\
                \n Explicação: A frase mostra que alguém entrou enquanto nós estávamos falando sobre a escola. A ação de "talking" estava em progresso quando outra ação ("he came in") a interrompeu. Isso pede o uso do past continuous: "We were talking"')
        
        #Pergunta 9
        pergunta9 = 'a'
        print(f"{nick}, vamos para a primeira pergunta.\
        \nThe kids _____ in the garden when it suddenly started to rain.\
        \n\nQual das opções abaixo é a correta?\
        \nA) were playing\
        \nB) played\
        \nC) playing\
        \nD) was playing\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta9 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta9 == 'e':
            print(f'Muito bem {nick}, a dica é: A resposta é composta por duas palavras.')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta9:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                print(f'Resposta errada, a certa era: {pergunta9}')
        else:
            if resposta_pergunta9 == pergunta9:
                print(f'{nick}, você acertou!')
                Acertos += 1
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta9}.\
                \n Explicação: A frase mostra uma situação interrompida pela chuva: "The kids were playing in the garden" (ação contínua) "when it suddenly started to rain" (ação que interrompe) "Were playing" está no past continuous e é a forma correta para plural ("kids").')

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
                Pontos +=2
            else:
                print(f'{nick}, você errou a resposta era {pergunta2}.\
                \n Explicação:[explicação]')
        
        #Loja 2

        #Pergunta 11
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
        
        #Pergunta 12
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
        
        #Pergunta 13
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
        
        #Pergunta 14
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
        
        #Pergunta 15
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
        
        #Loja 3

        #Pergunta 16
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
        
        #Pergunta 17
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
        
        #Pergunta 18
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

        #Pergunta 19
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

        #Pergunta 20
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

        #Resultados

        break
    elif vai_jogar == 'não':
        print(f"Adeus {Pnome}...")
        sleep(3)
        break
    else:
        print(f'{Pnome}, opção inválida, escolha entre sim e não.')