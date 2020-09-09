#Bibliotecas utilizadas

import random
import time

#Lista para guardar as opções a serem sorteadas
escolhas = ['Tesoura', 'Pedra', 'Papel']

#Escolhe uma das três opções
escolhaDois = random.choice(escolhas)



print('==='*10)
print('Vamos jogar jokenpo?')
print('==='*10)

#Recebe a escolha do usuário
usuario = str(input('Escolha entre pedra, papel ou tesoura:'))
usuario = usuario.upper()

time.sleep(1)
print('\033[0;31m JO \033[m')
time.sleep(1)
print('\033[0;32m KEN \033[m')
time.sleep(1)
print('\033[0;33m PO!!!! \033[m')

print('==='*10)

escolhaDois = escolhaDois.upper()

print('O computador jogou \033[0;35m {} \033[m'.format(escolhaDois))
print('O jogador jogou \033[34m {} \033[m'.format(usuario))

#Mostra na tela alguma das opções que irá cair, e quem irá ganhar.
print('==='*10)
if usuario == escolhaDois:
    print('Empate, ninguém ganhou!')

elif (usuario == 'TESOURA') and (escolhaDois == 'PAPEL'):
    print('Você GANHOU!')

elif (usuario == 'PAPEL') and (escolhaDois == 'TESOURA'):
    print('Você perdeu! Tente novamente')

elif (usuario == 'PEDRA') and (escolhaDois == 'TESOURA'):
    print('Você GANHOU!')

elif (usuario == 'TESOURA') and (escolhaDois == 'PEDRA'):
    print('Voce perdeu. Tente novamente')

elif (usuario == 'PAPEL') and (escolhaDois == 'PEDRA'):
    print('Você GANHOU!')

elif (usuario == 'PEDRA') and (escolhaDois == 'PAPEL'):
    print('Você perdeu! Tente novamente.')
