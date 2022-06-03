import random

print('JOKENPÔ')

print('Qual você escolhe?\n'
'\033[1;34m[1]Pedra\033[m\n'
'\033[1;35m[2]Papel\033[m\n'
'\033[1;36m[3]Tesoura\033[m')

escolha = int(input('\033[7;40mInsira sua escolha:\033[m'))

lista = [1, 2, 3]
embaralhar = random.choice(lista)

match escolha:
    case 1:
        if embaralhar == 1:
            print('\033[1;37mEMPATE\033[m, a máquina escolheu \033[1;34mpedra.\033[m')
        elif embaralhar == 2:
            print('\033[1;31mPERDEU\033[m, a máquina escolheu \033[1;35mpapel.\033[m')
        else:
            print('\033[1;33mVENCEU\033[m, a máquina escolheu \033[1;36mtesoura.\033[m')
    case 2:
        if embaralhar == 2:
            print('\033[1;37mEMPATE\033[m, a máquina escolheu \033[1;35mpapel.\033[m')
        elif embaralhar == 1:
            print('\033[1;33mVENCEU\033[m, a máquina escolheu \033[1;34mpedra.')
        else:
            print('\033[1;31mPERDEU\033[m, a máquina escolheu \033[1;36mtesoura.')
    case 3:
        if embaralhar == 3:
            print('\033[1;37mEMPATE\033[m, a máquina escolheu \033[1;36mtesoura.')
        elif embaralhar == 2:
            print('\033[1;33mVENCEU\033[m, a máquina escolheu \033[1;35mpapel.')
        else:
            print('\033[1;31mPERDEU\033[m, a máquina escolheu \033[1;34mpedra.')