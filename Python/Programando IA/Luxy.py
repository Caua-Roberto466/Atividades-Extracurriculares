print('🤖Olá, eu sou Luxy, o chatbot em aprendizado, qual a sua dúvida?')
print('Digite "Sair" para encerrar o programa')
while True:
    pergunta = input('Você: ').lower()
    if pergunta == 'sair':
        print("Tchau! Até a próxima")
        break
    elif 'oi' in pergunta or 'olá' in pergunta:
        print("Olá, como eu posso te ajudar?")
    elif 'tudo bem' in pergunta or 'como vai' in pergunta:
        print("EU tô bem, e você? Tudo certo?")