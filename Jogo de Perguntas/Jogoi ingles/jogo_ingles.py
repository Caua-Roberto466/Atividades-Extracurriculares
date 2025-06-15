from time import sleep
cores = {'limpa':'\033[m' ,'ciano' : '\033[36m', 'vermelho' : '\033[31m' , 'verde': '\033[32m' , 'amarelo' : '\033[33m'}
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
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhat were you doing at 8 p.m. yesterday?\
        \nQual das opções abaixo é a correta?\
        \nA) I was sleeping\
        \nB) I sleep\
        \nC) I am sleep\
        \nD) I slept\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta1 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta1 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores["amarelo"]}Use was/were + verbo com -ing para ações que estavam acontecendo no passado.{cores["limpa"]}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta1:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta1}{cores['limpa']}, explicação: A pergunta usa past continuous ("What were you doing?"), então a resposta precisa combinar. "Was sleeping" mostra uma ação que estava acontecendo naquele momento. As outras opções estão no tempo verbal errado.')
        else:
            if resposta_pergunta1 == pergunta1:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta1}.{cores["limpa"]}\
                \n Explicação: A pergunta usa past continuous ("What were you doing?"), então a resposta precisa combinar. "Was sleeping" mostra uma ação que estava acontecendo naquele momento. As outras opções estão no tempo verbal errado.')

        #Pergunta 2
        pergunta2 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nWas she watching TV when you called her?\
        \nQual das opções abaixo é a correta?\
        \nA) Yes, she watched.\
        \nB) Yes, she was.\
        \nC) No, she don’t.\
        \nD) She is watching.\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta2 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta2 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores["amarelo"]}Para responder perguntas com "Was/Wasnt", use o mesmo verbo auxiliar na resposta.{cores["limpa"]}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta2:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores["vermelho"]}Resposta errada, a certa era: {pergunta2}{cores["limpa"]}, explicação: A pergunta está no past continuous com "was", então a resposta curta correta é "Yes, she was". "Watched", "don’t" e "is watching" estão em tempos verbais errados.')
        else:
            if resposta_pergunta2 == pergunta2:
                print(f'{cores['verde']}{nick}, você acertou!{cores["limpa"]}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores["vermelho"]}{nick}, você errou a resposta era {pergunta2}.{cores["limpa"]}\
                \n Explicação: A pergunta está no past continuous com "was", então a resposta curta correta é "Yes, she was". "Watched", "don’t" e "is watching" estão em tempos verbais errados.')

        #Pergunta 3
        pergunta3 = 'c'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nThey ____ (cook) dinner when the lights went out.\
        \nQual das opções abaixo é a correta?\
        \nA) cooked\
        \nB) are cooking\
        \nC) were cooking\
        \nD) was cook\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta3 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta3 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores["amarelo"]}Lembre-se: uma ação em progresso foi interrompida.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta3:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores["vermelho"]}Resposta errada, a certa era: {pergunta3}{cores['limpa']}, explicação: A ação de cozinhar estava acontecendo quando as luzes se apagaram (ação que interrompe). Usamos "were cooking" para mostrar que estava em progresso. As outras opções estão gramaticalmente erradas ou estão no tempo errado.')
        else:
            if resposta_pergunta3 == pergunta3:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores["vermelho"]}{nick}, você errou a resposta era {pergunta3}.{cores['limpa']}\
                \n Explicação: A ação de cozinhar estava acontecendo quando as luzes se apagaram (ação que interrompe). Usamos "were cooking" para mostrar que estava em progresso. As outras opções estão gramaticalmente erradas ou estão no tempo errado.')
        
        #Pergunta 4
        pergunta4 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nWere they playing soccer in the park yesterday afternoon?\
        \nQual das opções abaixo é a correta?\
        \nA) Yes, they were.\
        \nB) Yes, they was.\
        \nC) No, they don’t.\
        \nD) They playing soccer.\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta4 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta4 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores["amarelo"]}Combine o tempo verbal da pergunta com o da resposta.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta4:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta4}{cores['limpa']}, explicação: Como a pergunta usa "Were they playing...", a resposta correta curta é "Yes, they were". "As outras formas estão erradas no tempo ou na estrutura da resposta."')
        else:
            if resposta_pergunta4 == pergunta4:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores["vermelho"]}{nick}, você errou a resposta era {pergunta4}.{cores['limpa']}\
                \n Explicação: Como a pergunta usa "Were they playing...", a resposta correta curta é "Yes, they were". "As outras formas estão erradas no tempo ou na estrutura da resposta."')
        
        #Pergunta 5
        pergunta5 = 'd'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nHe ____ (not study) when his mom arrived.\
        \nQual das opções abaixo é a correta?\
        \nA) wasn't study\
        \nB) didn’t studying\
        \nC) was not study\
        \nD) wasn’t studying\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta5 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta5 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores["amarelo"]}Para frases negativas no past continuous, use wasn’t/weren’t + verbo com -ing.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta5:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores["vermelho"]}Resposta errada, a certa era: {pergunta5}{cores['limpa']}, explicação: A forma correta do negativo no past continuous é "wasn''t' '+ verbo com -ing", como em "wasn’t studying". As outras opções combinam errado os verbos e auxiliares.')
        else:
            if resposta_pergunta5 == pergunta5:
                print(f'{cores["verde"]}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores["vermelho"]}{nick}, você errou a resposta era {pergunta5}.{cores['limpa']}\
                \n Explicação: A forma correta do negativo no past continuous é "wasn''t' '+ verbo com -ing", como em "wasn’t studying". As outras opções combinam errado os verbos e auxiliares.')

        #Loja 1
        print(f'\n{cores['ciano']}Parabéns {nick}, você subiu um nível de dificuldade, por isso a loja apareceu!{cores['limpa']}\
              \nEcolha qual item vcoê quer comprar.\
              \n {cores['verde']}1-Energético{cores['limpa']} | {cores['verde']}2-Mochila{cores['limpa']} | {cores['verde']}3- Bola de cristal{cores['limpa']}')
        loja1 = int(input("Qual item você quer? (1, 2 ou 3)"))
        if loja1 == 1:
            if Pontos < 5:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 5
                PontosB = Pontos*3
                print(f"{cores['verde']}Você comprou o energético, todos seus pontos triplicaram{cores['limpa']}")
        elif loja1 == 2:
            if Pontos < 3:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 3
                if Erros >= 2:
                    Erros -= 2
                    PontosB += 4
                else:
                    PontosB -= 2
                print(f"{cores['verde']}Você comprou a mochila, dois de seus erros viraram pontos{cores['limpa']}")
        elif loja1 == 3:
            if Pontos < 2:
                print(f"{cores['vermelho']} não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 2
                print(f"{cores['verde']}Você comprou a bola de cristal, e você ganhou a resposta da próxima pergunta, ela é D{cores['limpa']}")
        else:
            print("Opção inválida, a loja se foi...")
            sleep(2)

        #Pergunta 6
        pergunta6 = 'd'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nYesterday, at six I _____ dinner.\
        \nQual das opções abaixo é a correta?\
        \nA) was prepare\
        \nB) was prepared\
        \nC) did prepare\
        \nD) was preparing\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta6 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta6 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}, a dica é: Começa com "was".{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta6:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta6}{cores['limpa']}, explicação: A frase fala sobre uma ação em um momento específico no passado ("yesterday, at six"). Isso exige o uso do past continuous para mostrar que a ação estava em progresso naquele momento.')
        else:
            if resposta_pergunta6 == pergunta6:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta6}.{cores['limpa']}\
                \n Explicação: A frase fala sobre uma ação em um momento específico no passado ("yesterday, at six"). Isso exige o uso do past continuous para mostrar que a ação estava em progresso naquele momento.')

        #Pergunta 7
        pergunta7 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nMy father ____ a novel while I ___ TV.\
        \nQual das opções abaixo é a correta?\
        \nA) was reading / was watching\
        \nB) was read / was watching\
        \nC) were reading / was watching\
        \nD) read / watched\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta7 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta7 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Termina com "was watching".{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta7:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta7}{cores['limpa']}, explicação: A palavra "while" (enquanto) indica que duas ações estavam acontecendo ao mesmo tempo, ou seja, duas ações contínuas no passado.')
        else:
            if resposta_pergunta7 == pergunta7:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta7}.{cores['limpa']}\
                \n Explicação: A palavra "while" (enquanto) indica que duas ações estavam acontecendo ao mesmo tempo, ou seja, duas ações contínuas no passado. ')

        #Pergunta 8
        pergunta8 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nWe _____ our school when he came in.\
        \nQual das opções abaixo é a correta?\
        \nA) talked\
        \nB) were talking\
        \nC) were talked\
        \nD) talking\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta8 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta8 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Começa com "were".{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta8:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta8}{cores['limpa']}, explicação: A frase mostra que alguém entrou enquanto nós estávamos falando sobre a escola. A ação de "talking" estava em progresso quando outra ação ("he came in") a interrompeu. Isso pede o uso do past continuous: "We were talking"')
        else:
            if resposta_pergunta8 == pergunta8:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta8}.{cores['limpa']}\
                \n Explicação: A frase mostra que alguém entrou enquanto nós estávamos falando sobre a escola. A ação de "talking" estava em progresso quando outra ação ("he came in") a interrompeu. Isso pede o uso do past continuous: "We were talking"')
        
        #Pergunta 9
        pergunta9 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nThe kids _____ in the garden when it suddenly started to rain.\
        \n\nQual das opções abaixo é a correta?\
        \nA) were playing\
        \nB) played\
        \nC) playing\
        \nD) was playing\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta9 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta9 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}A resposta é composta por duas palavras.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta9:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta9}{cores['limpa']}, explicação: A frase mostra uma situação interrompida pela chuva: "The kids were playing in the garden" (ação contínua) "when it suddenly started to rain" (ação que interrompe) "Were playing" está no past continuous e é a forma correta para plural ("kids").')
        else:
            if resposta_pergunta9 == pergunta9:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta9}.{cores['limpa']}\
                \n Explicação: A frase mostra uma situação interrompida pela chuva: "The kids were playing in the garden" (ação contínua) "when it suddenly started to rain" (ação que interrompe) "Were playing" está no past continuous e é a forma correta para plural ("kids").')

        #Pergunta 10
        pergunta10 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nMost of the time we ____ in the park.\
        \nQual das opções abaixo é a correta?\
        \nA) were sat\
        \nB) were sitting\
        \nC) sitting\
        \nD) was sitting\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta10 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta10 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Começa com "were".{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta10:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta10}{cores['limpa']}, explicação: A expressão "Most of the time" mostra uma situação que acontecia com frequência no passado. Apesar de o simple past também funcionar aqui, o past continuous pode ser usado para enfatizar que era uma ação habitual em progresso.')
        else:
            if resposta_pergunta10 == pergunta10:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta10}.{cores['limpa']}\
                \n Explicação: A expressão "Most of the time" mostra uma situação que acontecia com frequência no passado. Apesar de o simple past também funcionar aqui, o past continuous pode ser usado para enfatizar que era uma ação habitual em progresso.')
        
        #Loja 2
        print(f'\n{cores['ciano']}Parabéns {nick}, você subiu um nível de dificuldade, por isso a loja apareceu!{cores['limpa']}\
            \nEcolha qual item vcoê quer comprar.\
            \n {cores['verde']}1-Fazer o Toeic{cores['limpa']} | {cores['verde']}2-Mochila{cores['limpa']} | {cores['verde']}3- Bola de cristal{cores['limpa']}')
        loja2 = int(input("Qual item você quer? (1, 2 ou 3)"))
        if loja2 == 1:
            if Pontos < 5:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 5
                PontosB += 10
                print(f"{cores['verde']}Você fez o Toeic e acertou tudo, você ganhou 10 pontos a mais{cores['limpa']}")
        elif loja2 == 2:
            if Pontos < 3:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 3
                if Erros >= 2:
                    Erros -= 2
                    PontosB += 4
                else:
                    PontosB -= 2
                print(f"{cores['verde']}Você comprou a mochila, dois de seus erros viraram pontos{cores['limpa']}")
        elif loja2 == 3:
            if Pontos < 2:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 2
                print(f"{cores['verde']}Você comprou a bola de cristal, e você ganhou a resposta da próxima pergunta, ela é A{cores['limpa']}")
        else:
            print("Opção inválida, a loja se foi...")
            sleep(2)

        #Pergunta 11
        pergunta11 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nWhat was she doing when the lights suddenly went out?\
        \nQual das opções abaixo é a correta?\
        \nA) She was reading\
        \nB) She reads\
        \nC) She had read\
        \nD) She is reading\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta11 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta11 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}A pergunta já está no passado contínuo; a resposta deve seguir o mesmo tempo verbal.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta11:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta11}{cores['limpa']}, explicação: O passado contínuo ("was reading") indica que a ação estava em andamento quando outra ação (as luzes apagando) ocorreu.')
        else:
            if resposta_pergunta11 == pergunta11:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta11}.{cores['limpa']}\
                \n Explicação: O passado contínuo ("was reading") indica que a ação estava em andamento quando outra ação (as luzes apagando) ocorreu.')
        
        #Pergunta 12
        pergunta12 = 'c'
        print(f"\n{cores['ciano']}{nick}, vamos para a próxima pergunta.{cores['limpa']}\
        \nWhile they were discussing the project, what did the manager say?\
        \nQual das opções abaixo é a correta?\
        \nA) They discussed\
        \nB) They had discussed\
        \nC) They were discussing\
        \nD) They have discussed\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta12 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta12 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é:  {cores['amarelo']}Atenção ao "while" — ele costuma acompanhar ações em progresso.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta12:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta12}{cores['limpa']}, explicação: A forma "were discussing" mostra que a conversa estava em andamento, estabelecendo o contexto para o que o gerente disse.')
        else:
            if resposta_pergunta12 == pergunta12:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta2}.{cores['limpa']}\
                \n Explicação: A forma "were discussing" mostra que a conversa estava em andamento, estabelecendo o contexto para o que o gerente disse.')
        
        #Pergunta 13
        pergunta13 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhat were you thinking about when I called you yesterday?\
        \nQual das opções abaixo é a correta?\
        \nA) You were thinking\
        \nB) You thought\
        \nC) You had thought\
        \nD) You are thinking\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta13 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta13 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Quando algo acontece e interrompe outra ação, a ação anterior costuma estar em andamento.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta13:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta13}{cores['limpa']}, explicação: "Were thinking" indica uma ação contínua que estava ocorrendo no momento em que a chamada foi feita, estabelecendo uma interrupção.')
        else:
            if resposta_pergunta13 == pergunta13:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta13}.{cores['limpa']}\
                \n Explicação: "Were thinking" indica uma ação contínua que estava ocorrendo no momento em que a chamada foi feita, estabelecendo uma interrupção.')
        
        #Pergunta 14
        pergunta14 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nDuring the meeting, what were they discussing when the fire alarm went off?\
        \nQual das opções abaixo é a correta?\
        \nA) They discuss\
        \nB) They were discussing\
        \nC) They had discussed\
        \nD) They were discussed\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta14 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta14 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Palavras como "during" e "when" geralmente indicam que uma ação estava acontecendo e foi interrompida.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta14:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta14}{cores['limpa']}, explicação:  "Were discussing" mostra que a discussão estava em progresso quando a interrupção (o alarme) aconteceu, destacando a continuidade da ação.')
        else:
            if resposta_pergunta14 == pergunta14:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1 
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta14}.{cores['limpa']}\
                \n Explicação: "Were discussing" mostra que a discussão estava em progresso quando a interrupção (o alarme) aconteceu, destacando a continuidade da ação.')
        
        #Pergunta 15
        pergunta15 = 'c'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhat were you doing while the presentation was being prepared?\
        \nQual das opções abaixo é a correta?\
        \nA) You prepared\
        \nB) You have prepared\
        \nC) You were preparing\
        \nD) You were being prepared\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta15 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta15 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpo']}, a dica é: {cores['amarelo']}Duas ações acontecendo ao mesmo tempo no passado? Use o mesmo tempo verbal contínuo nas duas.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta15:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1 
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta15}{cores['limpa']} explicação: A forma "were preparing" indica que a ação estava em andamento simultaneamente à preparação da apresentação, estabelecendo um contexto temporal.')
        else:
            if resposta_pergunta15 == pergunta15:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta15}.{cores['limpa']}\
                \n Explicação:  A forma "were preparing" indica que a ação estava em andamento simultaneamente à preparação da apresentação, estabelecendo um contexto temporal.')
        
        #Loja 3
        print(f'{cores['ciano']}Parabéns {nick}, você subiu um nível de dificuldade, por isso a loja apareceu!{cores['limpa']}\
            \nEcolha qual item vcoê quer comprar.\
            \n {cores['verde']}1-Fazer o Toeic{cores['limpa']} | {cores['verde']}2-Mochila{cores['limpa']} | {cores['verde']}3- Bola de cristal{cores['limpa']}')
        loja2 = int(input("Qual item você quer? (1, 2 ou 3)"))
        if loja2 == 1:
            if Pontos < 5:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 5
                PontosB += 10
                print(f"{cores['verde']}Você fez o Toeic e acertou tudo, você ganhou 10 pontos a mais{cores['limpa']}")
        elif loja2 == 2:
            if Pontos < 3:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 3
                if Erros >= 2:
                    Erros -= 2
                    PontosB += 4
                else:
                    PontosB -= 2
                print(f"{cores['verde']}Você comprou a mochila, dois de seus erros viraram pontos{cores['limpa']}")
        elif loja2 == 3:
            if Pontos < 2:
                print(f"{cores['vermelho']}Você não tem pontos o suficiente para comprar este item.{cores['limpa']}")
            else:
                Pontos -= 2
                print(f"{cores['verde']}Você comprou a bola de cristal, e você ganhou a resposta da próxima pergunta, ela é C{cores['limpa']}")
        else:
            print("Opção inválida, a loja se foi...")
            sleep(2)

        #Pergunta 16
        pergunta16 = 'c'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhat was she doing when the lights suddenly went out?\
        \nQual das opções abaixo é a correta?\
        \nA) She cooks dinner\
        \nB) She cooked dinner\
        \nC) She was cooking dinner\
        \nD) She had cooked dinner\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta16 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta16 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Pense no que estava acontecendo no exato momento em que a luz apagou.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta16:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta16}{cores['limpa']} explicação:  O past continuous descreve uma ação que estava em andamento quando outra ação a interrompeu. A ação "when the lights suddenly went out" (quando as luzes se apagaram) interrompe o que ela estava fazendo. Por isso, usamos "was cooking".')
        else:
            if resposta_pergunta16 == pergunta16:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta16}.{cores['limpa']}\
                \n Explicação: O past continuous descreve uma ação que estava em andamento quando outra ação a interrompeu. A ação "when the lights suddenly went out" (quando as luzes se apagaram) interrompe o que ela estava fazendo. Por isso, usamos "was cooking".')
        
        #Pergunta 17
        pergunta17 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nThey ___________ for hours before the storm finally hit the coast.\
        \nQual das opções abaixo é a correta?\
        \nA) waited\
        \nB) were waiting\
        \nC) had waited\
        \nD) have been waiting\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta17 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta17 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Analise a ideia de "duração contínua antes de um evento".{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta17:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros +=1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta17}{cores['limpa']}, explicação: Apesar de parecer uma frase de past perfect, o foco está na ação contínua (esperar por horas), não na conclusão da ação. "Were waiting" indica que a espera estava acontecendo ao longo do tempo, exatamente o uso do past continuous.')
        else:
            if resposta_pergunta17 == pergunta17:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['ciano']}{nick}, você errou a resposta era {pergunta17}.{cores['limpa']}\
                \n Explicação: Apesar de parecer uma frase de past perfect, o foco está na ação contínua (esperar por horas), não na conclusão da ação. "Were waiting" indica que a espera estava acontecendo ao longo do tempo, exatamente o uso do past continuous.')
        
        #Pergunta 18
        pergunta18 = 'b'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhile he ___________ the report, his boss was preparing the presentation.\
        \nQual das opções abaixo é a correta?\
        \nA) typed\
        \nB) was typing\
        \nC) has typed\
        \nD) would type\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta18 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta18 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Repare na estrutura paralela de duas ações ao mesmo tempo.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta18:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros += 1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta18}{cores['limpa']}, explicação: O uso de "while" mostra que duas ações ocorriam simultaneamente no passado. Ambas precisam estar no past continuous para manter a ideia de ações paralelas: "was typing" e "was preparing".')
        else:
            if resposta_pergunta18 == pergunta18:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta18}.{cores['limpa']}\
                \n Explicação: O uso de "while" mostra que duas ações ocorriam simultaneamente no passado. Ambas precisam estar no past continuous para manter a ideia de ações paralelas: "was typing" e "was preparing".')

        #Pergunta 19
        pergunta19 = 'a'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nI ___________ to the radio when I heard the terrible news.\
        \nQual das opções abaixo é a correta?\
        \nA) was listening\
        \nB) listened\
        \nC) have listened\
        \nD) had been listening\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta19 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta19 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Foque no momento exato em que a notícia foi ouvida.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta19:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros += 1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta19}{cores['limpa']}, explicação: A ação "heard the terrible news" interrompe uma ação em progresso (ouvir o rádio). Portanto, "was listening" mostra que a ação estava em andamento, característica típica do past continuous.')
        else:
            if resposta_pergunta19 == pergunta19:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros +=1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta19}.{cores['limpa']}\
                \n Explicação: A ação "heard the terrible news" interrompe uma ação em progresso (ouvir o rádio). Portanto, "was listening" mostra que a ação estava em andamento, característica típica do past continuous.')

        #Pergunta 20
        pergunta20 = 'd'
        print(f"\n{cores['ciano']}{nick}, vamos para a primeira pergunta.{cores['limpa']}\
        \nWhat ___________ when the alarm went off?\
        \nQual das opções abaixo é a correta?\
        \nA) you were doing\
        \nB) did you do\
        \nC) you did\
        \nD) were you doing\
        \nE) Dica (1 ponto a menos)")
        resposta_pergunta20 = str(input("Qual a opção correta? (a, b, c, d ou e): ")).lower()
        if resposta_pergunta20 == 'e':
            print(f'{cores['ciano']}Muito bem {nick}{cores['limpa']}, a dica é: {cores['amarelo']}Observe a ordem correta da pergunta com verbo auxiliar no passado contínuo.{cores['limpa']}')
            Rdica = str(input('Qual a resposta? (a, b, c ou d)')).lower()
            if Rdica == pergunta20:
                print('Você acertou, mas foi com dica, então você ganhará 1 ponto a menos')
                Acertos += 1
                Pontos += 1
            else:
                Erros += 1
                print(f'{cores['vermelho']}Resposta errada, a certa era: {pergunta20}{cores['limpa']}, explicação: Em perguntas no past continuous, a estrutura correta é: (Wh-word) + was/were + subject + verb-ing "What were you doing" segue essa ordem. As outras alternativas têm erros gramaticais na estrutura.')
        else:
            if resposta_pergunta20 == pergunta20:
                print(f'{cores['verde']}{nick}, você acertou!{cores['limpa']}')
                Acertos += 1
                Pontos +=2
            else:
                Erros += 1
                print(f'{cores['vermelho']}{nick}, você errou a resposta era {pergunta20}.{cores['limpa']}\
                \n Explicação: Em perguntas no past continuous, a estrutura correta é: (Wh-word) + was/were + subject + verb-ing "What were you doing" segue essa ordem. As outras alternativas têm erros gramaticais na estrutura.')

        #Resultados
        print(f'\n{cores['verde']}Parabéns {nick}, você completou o jogo, agora veja sua pontuação:{cores['limpa']}\
              \n\n {cores['ciano']}Nome do jogador: {cores['verde']}{nick}\
              \n {cores['ciano']}Acertos: {cores['verde']}{Acertos}\
              \n {cores['ciano']}Erros: {cores['verde']}{Erros}\
              \n {cores['ciano']}Pontos: {cores['verde']}{Pontos}\
              \n {cores['ciano']}Pontos bonûs: {cores['verde']}{PontosB}\
              \n {cores['ciano']}Pontos totais: {cores['verde']}{Pontos+PontosB}')

        break
    elif vai_jogar == 'não':
        print(f"Adeus {Pnome}...")
        sleep(3)
        break
    else:
        print(f'{Pnome}, opção inválida, escolha entre sim e não.')