import random 
from time import sleep
var = ['pedra', 'papel', 'tesoura']
print('-=-'*25)
print('Vamos jogar jokenpô')
print('-=-'*25)
escolha = str(input('O que você vai jogar? (pedra, papel ou tesoura) ')).lower()
maqui = random.choice(var)

#Casos de vitória ou empate
if escolha == maqui: #Define a condição: se os dois for igual
    print(f'Eu também escolhi jogar {escolha}! Deu empate') #Mostra a menssagem de empate
elif escolha == 'papel' and maqui == 'pedra': #Define a condição: se o jogador escolheu papel e a nmáquina pedra
    print(f'Dorga! o {escolha} vence da {maqui}, não sei porque eu joguei')
elif escolha == 'pedra' and maqui == 'tesoura':
    print(f'Caramba! Você jogou {escolha}, e ela vence da {maqui}!')
elif escolha == 'tesoura' and maqui == 'papel':
    print(f'Ah não! a sua {escolha} picotou o meu {maqui}!!!')

#Caso de derrota
elif maqui == 'papel' and escolha == 'pedra':
    print(f'Isso! {maqui} vence da {escolha}, eu te esmaguei!!')
elif maqui == 'pedra' and escolha == 'tesoura':
    print(f'Caramba! eu joguei {maqui}, e ela vence da {escolha}!')
elif maqui == 'tesoura' and escolha == 'papel':
    print(f'Aí sim!! a minha {maqui} picotou o seu {escolha}!!!')
else:
    print("Eu queria jogar, mas você conseguiu escolher errado entre duas opções, fazer o que né...")
    sleep(3)